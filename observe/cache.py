"""Content-addressed cache and run manifest.

"Re-running against an unchanged corpus does not repeat finished work" is a promise about
control flow, so it is kept by deterministic code with an explicit key rather than by a
timestamp comparison.

Two decisions worth defending:

1. **Extractions are cached per message, not per batch.** A changed batch boundary then
   invalidates nothing, and an interrupted run resumes mid-batch. This is what makes the
   promise exactly true rather than approximately true.

2. **`PROMPT_HASH` is the sha256 of the actual `.claude/` bytes a worker loads.** The Claude
   Code configuration is part of the cache key, so editing a rubric correctly invalidates
   every extraction downstream of it. That is demonstrable in ten seconds: touch the skill,
   re-run, watch stage 1 re-execute.

SQLite rather than a JSON manifest because eight concurrent workers writing results into a
JSON file is a lost-update bug waiting to be discovered by whoever reads the report.
"""

from __future__ import annotations

import hashlib
import json
import sqlite3
import threading
import time
from dataclasses import dataclass
from pathlib import Path

CACHE_VERSION = "1.0.0"

_SCHEMA = """
CREATE TABLE IF NOT EXISTS files (
    path TEXT PRIMARY KEY, sha256 TEXT NOT NULL, size INTEGER NOT NULL, seen_at REAL
);
CREATE TABLE IF NOT EXISTS stage_results (
    stage TEXT NOT NULL, key TEXT NOT NULL, unit_id TEXT,
    payload TEXT NOT NULL, model TEXT, duration_ms INTEGER, created_at REAL,
    PRIMARY KEY (stage, key)
);
CREATE INDEX IF NOT EXISTS idx_stage_unit ON stage_results(stage, unit_id);
CREATE TABLE IF NOT EXISTS failures (
    stage TEXT, unit_id TEXT, kind TEXT, detail TEXT, attempt INTEGER, created_at REAL
);
CREATE TABLE IF NOT EXISTS runs (
    run_id TEXT PRIMARY KEY, corpus_digest TEXT, started_at REAL, finished_at REAL,
    status TEXT, notes TEXT
);
"""


def sha256_text(*parts: str) -> str:
    h = hashlib.sha256()
    for p in parts:
        h.update(p.encode())
        h.update(b"\x00")
    return h.hexdigest()


def hash_paths(paths: list[Path]) -> str:
    """Hash a set of files by content, so a rubric edit is detected but a touch is not."""
    h = hashlib.sha256()
    for p in sorted(paths, key=lambda x: str(x)):
        if p.is_file():
            h.update(str(p.name).encode())
            h.update(p.read_bytes())
    return h.hexdigest()


def prompt_hash(claude_dir: Path, *relative: str) -> str:
    """Hash the `.claude/` files one stage's worker actually loads.

    This is what puts the Claude Code configuration into the build graph: edit the
    extractor's rubric and every extraction downstream of it correctly invalidates. You can
    demonstrate it in ten seconds — touch the skill, re-run, watch stage 1 re-execute.

    **Scoped per stage, not globbed.** An earlier version hashed every `agents/*.md`, so
    simply *adding* the artifact-drafter agent invalidated all 2,500 cached extractions and
    the next run paid for them again. Invalidation has to be as precise as the dependency
    actually is: a stage's key covers the files that reach its worker's context window and
    nothing else.
    """
    if not relative:
        raise ValueError("name the files this stage's worker loads; do not glob")
    return hash_paths([claude_dir / r for r in relative])


# What each model stage actually loads. Kept here so the dependency is declared in one
# place rather than implied by whatever a glob happens to match.
EXTRACT_PROMPT_FILES = (
    "agents/message-extractor.md",
    "skills/enron-email-forensics/SKILL.md",
)
CHARACTERIZE_PROMPT_FILES = (
    "agents/process-characterizer.md",
    "skills/enron-email-forensics/SKILL.md",
)
ARTIFACT_PROMPT_FILES = (
    "agents/artifact-drafter.md",
    "skills/enron-email-forensics/SKILL.md",
)


@dataclass
class CacheStats:
    hits: int = 0
    misses: int = 0
    writes: int = 0

    @property
    def total(self) -> int:
        return self.hits + self.misses


class Cache:
    """Thread-safe keyed store. One connection, one lock; the workload is tiny next to the
    subprocess calls it guards."""

    def __init__(self, root: Path):
        self.root = root
        root.mkdir(parents=True, exist_ok=True)
        self.db_path = root / "manifest.sqlite"
        self._lock = threading.Lock()
        self._conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self._conn.execute("PRAGMA journal_mode=WAL")
        self._conn.execute("PRAGMA busy_timeout=5000")
        self._conn.executescript(_SCHEMA)
        self._conn.commit()
        self.stats = CacheStats()

    def close(self) -> None:
        with self._lock:
            self._conn.close()

    # -- corpus fingerprint ------------------------------------------------
    def record_files(self, entries: list[tuple[str, str, int]]) -> str:
        now = time.time()
        with self._lock:
            self._conn.executemany(
                "INSERT OR REPLACE INTO files(path, sha256, size, seen_at) VALUES (?,?,?,?)",
                [(p, s, z, now) for p, s, z in entries],
            )
            self._conn.commit()
        return sha256_text(*[f"{p}:{s}" for p, s, _z in sorted(entries)])

    # -- stage results -----------------------------------------------------
    def get(self, stage: str, key: str):
        with self._lock:
            row = self._conn.execute(
                "SELECT payload FROM stage_results WHERE stage=? AND key=?", (stage, key)
            ).fetchone()
        if row is None:
            self.stats.misses += 1
            return None
        self.stats.hits += 1
        return json.loads(row[0])

    def put(self, stage: str, key: str, payload, *, unit_id: str = "",
            model: str = "", duration_ms: int = 0) -> None:
        with self._lock:
            self._conn.execute(
                "INSERT OR REPLACE INTO stage_results"
                "(stage, key, unit_id, payload, model, duration_ms, created_at)"
                " VALUES (?,?,?,?,?,?,?)",
                (stage, key, unit_id, json.dumps(payload, separators=(",", ":")),
                 model, duration_ms, time.time()),
            )
            self._conn.commit()
        self.stats.writes += 1

    def get_many(self, stage: str, keys: list[str]) -> dict[str, object]:
        """Batch lookup, so a 2,400-message stage does not make 2,400 round trips."""
        out: dict[str, object] = {}
        if not keys:
            return out
        with self._lock:
            for chunk_start in range(0, len(keys), 500):
                chunk = keys[chunk_start:chunk_start + 500]
                q = ",".join("?" * len(chunk))
                rows = self._conn.execute(
                    f"SELECT key, payload FROM stage_results WHERE stage=? AND key IN ({q})",
                    (stage, *chunk),
                ).fetchall()
                for k, payload in rows:
                    out[k] = json.loads(payload)
        self.stats.hits += len(out)
        self.stats.misses += len(keys) - len(out)
        return out

    def record_failure(self, stage: str, unit_id: str, kind: str, detail: str, attempt: int) -> None:
        with self._lock:
            self._conn.execute(
                "INSERT INTO failures(stage, unit_id, kind, detail, attempt, created_at)"
                " VALUES (?,?,?,?,?,?)",
                (stage, unit_id, kind, detail[:2000], attempt, time.time()),
            )
            self._conn.commit()

    def failures(self, stage: str | None = None) -> list[dict]:
        with self._lock:
            if stage:
                rows = self._conn.execute(
                    "SELECT stage, unit_id, kind, detail, attempt, created_at FROM failures"
                    " WHERE stage=? ORDER BY created_at", (stage,)).fetchall()
            else:
                rows = self._conn.execute(
                    "SELECT stage, unit_id, kind, detail, attempt, created_at FROM failures"
                    " ORDER BY created_at").fetchall()
        cols = ("stage", "unit_id", "kind", "detail", "attempt", "created_at")
        return [dict(zip(cols, r)) for r in rows]

    def start_run(self, run_id: str, corpus_digest: str) -> None:
        with self._lock:
            self._conn.execute(
                "INSERT OR REPLACE INTO runs(run_id, corpus_digest, started_at, status)"
                " VALUES (?,?,?,?)", (run_id, corpus_digest, time.time(), "running"))
            self._conn.commit()

    def finish_run(self, run_id: str, status: str, notes: str = "") -> None:
        with self._lock:
            self._conn.execute(
                "UPDATE runs SET finished_at=?, status=?, notes=? WHERE run_id=?",
                (time.time(), status, notes[:4000], run_id))
            self._conn.commit()