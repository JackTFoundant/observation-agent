"""The conductor. One command runs this; every stage is deterministic except three.

The shape of the whole system, and the answer to the assignment's central tension: the
README says Claude Code is the runtime, and also demands one command, unattended, under
thirty minutes, skipping finished work, with exact arithmetic and tests that never invoke a
model. Those are two different kinds of requirement.

*Promises about control flow* — finishes unattended, inside a time budget, resumable,
arithmetic exact — cannot be delegated to a model, because a model cannot promise its own
control flow. *Judgments* — what is this message about, where does this work stall, what
should the SOP say — cannot be delegated to code.

So: a deterministic conductor whose entire workforce is Claude Code.

    stage 0  parse, resolve identity, dedupe, thread, triage   deterministic
    stage 1  per-message extraction                            model, ~100 calls
    stage 2  block, cluster, gate, label                       deterministic
    stage 3  characterize each promoted cluster                model, ~1 per cluster
    stage 4  measure, estimate hours and dollars, rank         deterministic
    stage 5  anchor every quote to raw bytes, gate claims      deterministic
    stage 6  draft artifacts above threshold                   model, ~6 calls
    stage 7  render report and dashboard data                  deterministic
"""

from __future__ import annotations

import json
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

import yaml

from observe import cluster as cluster_mod
from observe import extract as extract_mod
from observe.cache import (
    ARTIFACT_PROMPT_FILES, CHARACTERIZE_PROMPT_FILES, EXTRACT_PROMPT_FILES,
    Cache, prompt_hash, sha256_text)
from observe.classify import classify, detect_table
from observe.dedupe import build_threads, find_duplicates
from observe.dispatch import RunLog, Unit, dispatch
from observe.estimate.model import BANDS, Assumptions, band_estimates, estimate, measure
from observe.evidence.anchor import AnchorError, build_citation
from observe.identity import resolve
from observe.llm.schema_guard import check
from observe.parse import iter_corpus, parse_file, read_raw

PIPELINE_VERSION = "1.0.0"

MIN_CITATIONS_PROCESS = 3
MIN_THREADS_PROCESS = 2
MIN_SENDERS_PROCESS = 2


@dataclass
class Context:
    root: Path
    corpus: Path
    run_id: str
    run_dir: Path
    cache: Cache
    log: RunLog
    started: float = field(default_factory=time.monotonic)
    deadline_s: float = 25 * 60
    concurrency: int = 8
    stats: dict = field(default_factory=dict)

    @property
    def deadline_at(self) -> float:
        return self.started + self.deadline_s

    def elapsed(self) -> float:
        return time.monotonic() - self.started


def new_context(root: Path, *, run_id: str | None = None, concurrency: int = 8,
                deadline_s: float = 25 * 60) -> Context:
    run_id = run_id or datetime.now(timezone.utc).strftime("run_%Y%m%dT%H%M%SZ")
    run_dir = root / "runs" / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    return Context(
        root=root, corpus=root / "corpus", run_id=run_id, run_dir=run_dir,
        cache=Cache(root / ".observe-cache"), log=RunLog(run_dir / "run.jsonl"),
        concurrency=concurrency, deadline_s=deadline_s,
    )


# ---------------------------------------------------------------------------
# Stage 0 - deterministic reduction
# ---------------------------------------------------------------------------

@dataclass
class Corpus:
    messages: list
    survivors: list
    by_uid: dict
    duplicates: dict
    dup_groups: list
    people: dict
    address_to_person: dict
    threads: dict
    uid_to_thread: dict
    classifications: dict
    corpus_digest: str
    generated_tables: dict


def stage0(ctx: Context) -> Corpus:
    t0 = time.monotonic()
    paths = iter_corpus(ctx.corpus)
    messages = [parse_file(p, ctx.corpus) for p in paths]
    digest = ctx.cache.record_files([(m.path, m.file_sha256, m.file_size) for m in messages])

    address_to_person, people = resolve(messages)
    duplicates, dup_groups = find_duplicates(messages)
    survivors = [m for m in messages if m.msg_uid not in duplicates]
    uid_to_thread, threads = build_threads(survivors, address_to_person)
    classifications = {m.msg_uid: classify(m) for m in survivors}

    # Find and prove machine-generated tables once, so no later stage has to re-decide.
    generated: dict[str, dict] = {}
    for m in survivors:
        if m.file_size > 60_000:
            table = detect_table(m.body_decoded)
            if table is not None:
                generated[m.msg_uid] = {
                    "path": m.path, "rows": table.row_count, "columns": table.column_count,
                    "chars": table.char_span, "generated": table.generated,
                    "proof": table.proof,
                }

    ctx.log.event(stage="parse", event="done", files=len(messages),
                  duplicates=len(duplicates), survivors=len(survivors),
                  threads=len(threads), people=len(people),
                  duration_ms=int((time.monotonic() - t0) * 1000))
    ctx.stats["stage0"] = {
        "files": len(messages), "duplicates_removed": len(duplicates),
        "duplicate_groups": len(dup_groups), "survivors": len(survivors),
        "task_instances": len(threads), "people": len(people),
        "generated_tables": sum(1 for v in generated.values() if v["generated"]),
        "seconds": round(time.monotonic() - t0, 2),
    }
    return Corpus(
        messages=messages, survivors=survivors,
        by_uid={m.msg_uid: m for m in messages},
        duplicates=duplicates, dup_groups=dup_groups, people=people,
        address_to_person=address_to_person, threads=threads,
        uid_to_thread=uid_to_thread, classifications=classifications,
        corpus_digest=digest, generated_tables=generated,
    )


# ---------------------------------------------------------------------------
# Stage 1 - extraction
# ---------------------------------------------------------------------------

def stage1(ctx: Context, corpus: Corpus, *, model: str = "sonnet") -> dict:
    schema, schema_hash = extract_mod.load_schema(ctx.root)
    system_prompt = extract_mod.load_system_prompt(ctx.root)
    ph = prompt_hash(ctx.root / ".claude", *EXTRACT_PROMPT_FILES)

    cards = extract_mod.message_cards(
        corpus.survivors, corpus.classifications,
        prompt_hash=ph, model=model, schema_hash=schema_hash,
    )

    # The unit of cached work is one message. Batching is only how they travel.
    key_by_uid = {uid: key for uid, _card, key in cards}
    cached = ctx.cache.get_many(extract_mod.MESSAGE_STAGE, [k for _u, _c, k in cards])
    extractions: dict[str, dict] = {}
    todo: list[tuple[str, object, str]] = []
    for uid, card, key in cards:
        if key in cached:
            extractions[uid] = cached[key]
        else:
            todo.append((uid, card, key))

    ctx.log.event(stage="extract", event="message_cache_pass",
                  total=len(cards), cached=len(extractions), todo=len(todo))

    units = extract_mod.build_units(todo)
    outcome = dispatch(
        units, stage="extract_batch", system_prompt=system_prompt, json_schema=schema,
        validate=extract_mod.validate, cache=ctx.cache, log=ctx.log, model=model,
        effort="low", concurrency=ctx.concurrency, timeout=300,
        deadline_at=ctx.deadline_at, max_model_calls=300, split=extract_mod.split_unit,
    )

    for result in outcome.results.values():
        for item in result.get("messages", []):
            uid = item.get("msg_uid")
            if uid not in key_by_uid:
                continue
            extractions[uid] = item
            # Store per message, so the next run skips it whatever batch it lands in.
            ctx.cache.put(extract_mod.MESSAGE_STAGE, key_by_uid[uid], item, unit_id=uid,
                          model=model)

    ctx.stats["stage1"] = {
        "messages_eligible": len(cards),
        "cache_hits_messages": len(cards) - len(todo),
        "messages_extracted_now": len(todo),
        "batches": len(units), "batches_ok": len(outcome.results),
        "model_calls": outcome.model_calls,
        "extractions": len(extractions), "failed_batches": len(outcome.failed),
    }
    ctx.log.event(stage="extract", event="stage_done", **ctx.stats["stage1"])
    return extractions


# ---------------------------------------------------------------------------
# Stage 2 - clustering
# ---------------------------------------------------------------------------

def _iso_week(dt) -> str:
    y, w, _ = dt.isocalendar()
    return f"{y}-W{w:02d}"


def stage2(ctx: Context, corpus: Corpus, extractions: dict, *, method: str = "tfidf"):
    t0 = time.monotonic()
    class_labels = {
        name: spec["label"]
        for name, spec in yaml.safe_load(
            (ctx.root / "config/task_classes.yml").read_text())["classes"].items()
    }

    records: list[dict] = []
    for uid, item in extractions.items():
        msg = corpus.by_uid.get(uid)
        if msg is None or not item.get("is_operational"):
            continue
        people = sorted({corpus.address_to_person.get(a, a) for a in msg.all_participants})
        records.append({
            "msg_uid": uid,
            "task_class": item.get("task_class") or "other",
            "process_phrase": item.get("process_phrase") or "",
            "role": item.get("role") or "fyi",
            "systems_referenced": item.get("systems_referenced") or [],
            "rework_signal": bool(item.get("rework_signal")),
            "waiting_signal": bool(item.get("waiting_signal")),
            "manual_transfer_signal": bool(item.get("manual_transfer_signal")),
            "deadline_signal": bool(item.get("deadline_signal")),
            "evidence": item.get("evidence") or [],
            "confidence": item.get("confidence") or "medium",
            "subject_key": msg.subject_key,
            "novel_hash": msg.novel_hash,
            "sender_person": corpus.address_to_person.get(msg.sender or "", msg.sender),
            "person_ids": people,
            "person_pairs": tuple(sorted(people))[:2],
            "thread_id": corpus.uid_to_thread.get(uid, uid),
            "month": msg.sent_at.strftime("%Y-%m") if msg.sent_at else None,
            "week": _iso_week(msg.sent_at) if msg.sent_at else None,
            "folder": msg.path.rsplit("/", 1)[0],
        })

    clusters = cluster_mod.build_clusters(records, class_labels, method=method)
    promoted = [c for c in clusters if c.gate.passed]
    ctx.stats["stage2"] = {
        "records": len(records), "clusters": len(clusters), "promoted": len(promoted),
        "residual": len(clusters) - len(promoted),
        "seconds": round(time.monotonic() - t0, 2),
    }
    ctx.log.event(stage="cluster", event="done", **ctx.stats["stage2"])
    return clusters, {r["msg_uid"]: r for r in records}


# ---------------------------------------------------------------------------
# Stage 3 - characterization
# ---------------------------------------------------------------------------

def stage3(ctx: Context, clusters, records: dict, *, model: str = "opus") -> dict:
    promoted = [c for c in clusters if c.gate.passed]
    if not promoted:
        ctx.stats["stage3"] = {"clusters": 0, "model_calls": 0}
        return {}

    schema = json.loads((ctx.root / "schemas/characterization.schema.json").read_text())
    schema.pop("$schema", None)
    schema_hash = sha256_text(json.dumps(schema, sort_keys=True))
    system_prompt = _characterizer_prompt(ctx.root)
    ph = prompt_hash(ctx.root / ".claude", *CHARACTERIZE_PROMPT_FILES)

    units: list[Unit] = []
    for c in promoted:
        payload = _render_cluster(c, records)
        units.append(Unit(
            unit_id=c.cluster_id,
            payload=payload,
            cache_key=sha256_text("characterize", payload, ph, model, schema_hash),
            expected_ids=set(c.exemplar_uids),
            meta={"cluster_id": c.cluster_id},
        ))

    def validate(parsed, unit: Unit) -> list[str]:
        problems = list(check(parsed).violations)
        if not isinstance(parsed, dict):
            return problems + ["$: expected an object"]
        for key in ("title", "what_happens", "where_it_stalls", "automation_opportunity",
                    "artifact_recommendation", "coherence"):
            if not parsed.get(key):
                problems.append(f"$.{key}: missing")
        bad = [u for u in (parsed.get("key_evidence_uids") or []) if u not in unit.expected_ids]
        if bad:
            problems.append(f"$.key_evidence_uids: {bad[:3]} were not offered for this cluster")
        return problems

    outcome = dispatch(
        units, stage="characterize", system_prompt=system_prompt, json_schema=schema,
        validate=validate, cache=ctx.cache, log=ctx.log, model=model, effort="medium",
        concurrency=min(6, ctx.concurrency), timeout=300, deadline_at=ctx.deadline_at,
        max_model_calls=120,
    )
    ctx.stats["stage3"] = {
        "clusters": len(units), "characterized": len(outcome.results),
        "model_calls": outcome.model_calls, "cache_hits": outcome.cache_hits,
        "failed": len(outcome.failed),
    }
    ctx.log.event(stage="characterize", event="stage_done", **ctx.stats["stage3"])
    return outcome.results


def _characterizer_prompt(root: Path) -> str:
    agent = extract_mod._strip_frontmatter(
        (root / ".claude/agents/process-characterizer.md").read_text())
    skill = extract_mod._strip_frontmatter(
        (root / ".claude/skills/enron-email-forensics/SKILL.md").read_text())
    return ("You describe one already-discovered process cluster. You return JSON only.\n\n"
            + agent + "\n\n---\n\n# Domain reference\n\n" + skill)


def _render_cluster(c, records: dict) -> str:
    m = c.gate.metrics
    lines = [
        f"CLUSTER {c.cluster_id}",
        f"mechanical label: {c.label}",
        f"task class: {c.task_class}",
        "",
        "MEASURED (deterministic; do not contradict these):",
        f"  messages: {m['messages']}",
        f"  distinct task instances (threads): {m['threads']}",
        f"  distinct senders: {m['senders']}",
        f"  distinct people involved: {m['people']}",
        f"  months spanned: {m['months']}  (distinct weeks: {m['weeks']})",
        f"  mailbox folders: {m['folders']}",
        "  signal rates: " + ", ".join(f"{k.replace('_signal','')}={v:.0%}"
                                       for k, v in c.signal_rates.items()),
        "  roles: " + ", ".join(f"{k}={v}" for k, v in c.roles.items()),
        "  systems mentioned: " + (", ".join(f"{k}={v}" for k, v in c.systems.items()) or "none"),
        f"  months present: {', '.join(c.months[:14])}",
        "",
        f"EXEMPLAR MESSAGES ({len(c.exemplar_uids)} of {c.size}, spread across senders and months):",
    ]
    for uid in c.exemplar_uids:
        r = records.get(uid)
        if not r:
            continue
        sig = [k.replace("_signal", "") for k in
               ("rework_signal", "waiting_signal", "manual_transfer_signal", "deadline_signal")
               if r.get(k)]
        lines.append(f"\n  [{uid}] {r['month'] or 'undated'} | role={r['role']}"
                     f" | signals={','.join(sig) or 'none'}")
        lines.append(f"    activity: {r['process_phrase']}")
        for ev in (r.get("evidence") or [])[:2]:
            quote = (ev.get("quote_proposal") or "").replace("\n", " ")[:240]
            lines.append(f'    quote: "{quote}"')
    return "\n".join(lines)

# ---------------------------------------------------------------------------
# Stage 4-5 - measure, cite, gate, cost, rank
# ---------------------------------------------------------------------------

def stage45(ctx: Context, corpus: Corpus, clusters, records: dict,
            characterizations: dict, series):
    """Everything here is deterministic. No model is consulted about any number."""
    from observe.recurring import promote as promote_series
    from observe.reduce import build as build_mod

    t0 = time.monotonic()
    config = ctx.root / "config/estimation.yml"
    get_raw = build_mod._raw_cache(ctx.corpus)

    promoted_series, rejected_series = promote_series(series)
    opportunities = build_mod.build_from_clusters(
        clusters, characterizations, records, corpus, config, get_raw)
    opportunities += build_mod.build_from_series(
        promoted_series, corpus, config, get_raw, characterizations)
    opportunities = build_mod.rank(opportunities)

    counted = [o for o in opportunities if o.status == "counted"]
    cited = sum(len(o.citations) for o in opportunities)
    quarantined_cits = sum(len(o.quarantined_citations) for o in opportunities)

    ctx.stats["stage45"] = {
        "opportunities": len(opportunities),
        "counted": len(counted),
        "low_confidence": sum(1 for o in opportunities if o.status == "low_confidence"),
        "quarantined": sum(1 for o in opportunities if o.status == "quarantined"),
        "citations_verified": cited,
        "citations_quarantined": quarantined_cits,
        "series_promoted": len(promoted_series),
        "series_rejected": len(rejected_series),
        "seconds": round(time.monotonic() - t0, 2),
    }
    ctx.log.event(stage="build", event="done", **ctx.stats["stage45"])
    return opportunities, rejected_series


# ---------------------------------------------------------------------------
# Stage 7 - render
# ---------------------------------------------------------------------------

def stage7(ctx: Context, corpus: Corpus, opportunities, clusters, rejected_series,
           artifacts: list[dict] | None = None) -> dict:
    from observe.reduce import render as render_mod
    t0 = time.monotonic()
    summary = render_mod.write_all(
        ctx, corpus, opportunities, clusters, rejected_series, artifacts or [])
    ctx.stats["stage7"] = {"seconds": round(time.monotonic() - t0, 2)}
    ctx.log.event(stage="render", event="done", **ctx.stats["stage7"])
    return summary


# ---------------------------------------------------------------------------
# Stage 6 - act
# ---------------------------------------------------------------------------

def stage6(ctx: Context, opportunities, *, model: str = "opus") -> tuple[list[dict], list[dict]]:
    """Draft a usable document for each opportunity above the defended threshold."""
    from observe.reduce import artifacts as art

    thresholds = art.Thresholds.load(ctx.root / "config/thresholds.yml")
    selected, skipped = art.select(opportunities, thresholds)
    if not selected:
        ctx.stats["stage6"] = {"selected": 0, "written": 0, "skipped": len(skipped)}
        return [], skipped

    schema = json.loads((ctx.root / "schemas/artifact.schema.json").read_text())
    schema.pop("$schema", None)
    schema_hash = sha256_text(json.dumps(schema, sort_keys=True))
    agent = extract_mod._strip_frontmatter(
        (ctx.root / ".claude/agents/artifact-drafter.md").read_text())
    skill = extract_mod._strip_frontmatter(
        (ctx.root / ".claude/skills/enron-email-forensics/SKILL.md").read_text())
    system_prompt = ("You draft one working document. You return JSON only.\n\n"
                     + agent + "\n\n---\n\n# Domain reference\n\n" + skill)
    ph = prompt_hash(ctx.root / ".claude", *ARTIFACT_PROMPT_FILES)

    units = art.build_units(selected, prompt_hash=ph, model=model, schema_hash=schema_hash)
    outcome = dispatch(
        units, stage="artifact", system_prompt=system_prompt, json_schema=schema,
        validate=art.validate, cache=ctx.cache, log=ctx.log, model=model, effort="high",
        concurrency=min(4, ctx.concurrency), timeout=360, deadline_at=ctx.deadline_at,
        max_model_calls=40,
    )
    written = art.write_files(outcome.results, selected, ctx.root / "out" / "artifacts")
    for f in outcome.failed:
        skipped.append({"opportunity_id": f["unit_id"].replace("artifact_", ""),
                        "title": "", "reasons": [f"drafting failed: {f['detail'][:160]}"]})

    ctx.stats["stage6"] = {
        "selected": len(selected), "written": len(written),
        "skipped": len(skipped), "model_calls": outcome.model_calls,
        "cache_hits": outcome.cache_hits, "failed": len(outcome.failed),
        "threshold_dollars": thresholds.min_dollars,
        "cap": thresholds.max_artifacts,
    }
    ctx.log.event(stage="artifact", event="stage_done", **ctx.stats["stage6"])
    return written, skipped
