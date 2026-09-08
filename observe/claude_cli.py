"""Locating and invoking the Claude Code CLI as a headless worker.

This is the only place in the system that shells out to a model. Everything about the
invocation is deliberate:

* `--tools ""` — a worker gets no tools at all. No tool schemas in its context window, no
  filesystem to wander, no way for it to read the corpus and blow its own budget. Text in,
  JSON out. This is the single largest context-budget lever available.
* `--strict-mcp-config --setting-sources ""` — this developer machine has dozens of MCP
  servers configured. Without these flags every worker pays their schemas in tokens and
  their handshakes in latency, for nothing.
* `--system-prompt` (full replacement, not append) — the worker's window is exactly what we
  chose, byte for byte, independent of whatever CLAUDE.md happens to sit in the grader's
  home directory. That is what makes a run reproducible on someone else's laptop.
* `--json-schema` — structured output validated before it reaches us.
* payload on **stdin**, never argv — a multi-kilobyte batch on argv risks `E2BIG` and is
  unreadable in logs.

`--bare` would also isolate the window and would be faster, but its own help states that
auth is then "strictly ANTHROPIC_API_KEY or apiKeyHelper (OAuth and keychain are never
read)". This assignment forbids API spend, so `--bare` is disqualified. Subscription OAuth
requires the normal path.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path

CLI_VERSION_TESTED = "2.1.263"

_RATE_LIMIT = re.compile(r"rate.?limit|429|too many requests|usage limit|overloaded", re.I)
_AUTH_FAIL = re.compile(r"not authenticated|please (run )?(claude )?(auth )?login|invalid api key"
                        r"|unauthorized|401|no credentials", re.I)


class WorkerError(Exception):
    def __init__(self, kind: str, detail: str = "", stderr: str = ""):
        super().__init__(f"{kind}: {detail}")
        self.kind = kind          # "rate_limit" | "auth" | "timeout" | "bad_json" | "nonzero"
        self.detail = detail
        self.stderr = stderr


def resolve_cli() -> Path:
    """Find the CLI. It is frequently *not* on PATH.

    On this machine it lives inside a VS Code extension directory whose name carries a
    version number, so the grader's path will differ from ours; hence a search rather than
    a constant.
    """
    env = os.environ.get("CLAUDE_BIN")
    if env and Path(env).exists():
        return Path(env)

    which = shutil.which("claude")
    if which:
        return Path(which)

    candidates: list[Path] = [
        Path.home() / ".local/bin/claude",
        Path.home() / ".claude/local/claude",
        Path("/opt/homebrew/bin/claude"),
        Path("/usr/local/bin/claude"),
    ]
    ext_root = Path.home() / ".vscode/extensions"
    if ext_root.is_dir():
        matches = sorted(
            ext_root.glob("anthropic.claude-code-*/resources/native-binary/claude"),
            key=lambda p: p.stat().st_mtime,
            reverse=True,
        )
        candidates.extend(matches)
    for c in candidates:
        if c.exists():
            return c

    raise WorkerError(
        "not_found",
        "Claude Code CLI not found. Install it with `claude install` (or set CLAUDE_BIN to "
        "the binary path), then authenticate with `claude auth login`.",
    )


@dataclass
class WorkerResult:
    parsed: dict | list
    raw_stdout: str
    duration_ms: int
    model: str
    attempt: int


def build_argv(
    cli: Path,
    *,
    system_prompt: str,
    model: str,
    json_schema: dict | None,
    effort: str | None = None,
    fallback_model: str | None = None,
) -> list[str]:
    argv = [
        str(cli),
        "-p",
        "--output-format", "json",
        "--model", model,
        "--system-prompt", system_prompt,
        # No tools: the worker is a pure text->JSON function.
        "--tools", "",
        "--strict-mcp-config",
        "--setting-sources", "",
        "--disable-slash-commands",
        "--no-session-persistence",
        "--permission-mode", "dontAsk",
        "--permission-prompts", "none",
        "--exclude-dynamic-system-prompt-sections",
    ]
    if json_schema is not None:
        argv += ["--json-schema", json.dumps(json_schema, separators=(",", ":"))]
    if effort:
        argv += ["--effort", effort]
    if fallback_model:
        argv += ["--fallback-model", fallback_model]
    return argv


def _extract_result_text(stdout: str) -> str:
    """Pull the assistant's answer out of `--output-format json`.

    The envelope has changed shape across CLI versions, so we accept several and fail
    loudly rather than silently returning an empty string.
    """
    stdout = stdout.strip()
    if not stdout:
        raise WorkerError("bad_json", "empty stdout")
    try:
        env = json.loads(stdout)
    except json.JSONDecodeError:
        return stdout
    if isinstance(env, dict):
        for key in ("result", "text", "content", "output"):
            value = env.get(key)
            if isinstance(value, str) and value.strip():
                return value
            if isinstance(value, (dict, list)):
                return json.dumps(value)
        if env.get("is_error"):
            raise WorkerError("nonzero", str(env.get("result") or env.get("error") or env))
    return stdout


def _parse_json_payload(text: str) -> dict | list:
    """Parse the worker's answer, tolerating a fenced code block around it."""
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```[a-zA-Z]*\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # Last resort: the outermost JSON object or array in the text.
        for opener, closer in (("{", "}"), ("[", "]")):
            a, b = text.find(opener), text.rfind(closer)
            if a != -1 and b > a:
                try:
                    return json.loads(text[a:b + 1])
                except json.JSONDecodeError:
                    continue
        raise WorkerError("bad_json", text[:400])


def run_worker(
    payload: str,
    *,
    system_prompt: str,
    model: str = "sonnet",
    json_schema: dict | None = None,
    effort: str | None = None,
    timeout: int = 240,
    cli: Path | None = None,
    attempt: int = 1,
) -> WorkerResult:
    """One headless model call. Raises `WorkerError` with a classified `kind`."""
    cli = cli or resolve_cli()
    argv = build_argv(
        cli, system_prompt=system_prompt, model=model, json_schema=json_schema, effort=effort
    )
    started = time.monotonic()
    try:
        proc = subprocess.run(
            argv,
            input=payload,
            capture_output=True,
            text=True,
            timeout=timeout,
            env={**os.environ, "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"},
        )
    except subprocess.TimeoutExpired:
        raise WorkerError("timeout", f"exceeded {timeout}s")
    duration_ms = int((time.monotonic() - started) * 1000)

    stderr = (proc.stderr or "")[-4000:]
    if proc.returncode != 0:
        if _AUTH_FAIL.search(stderr):
            raise WorkerError("auth", "CLI is not authenticated; run `claude auth login`", stderr)
        if _RATE_LIMIT.search(stderr):
            raise WorkerError("rate_limit", stderr[:200], stderr)
        raise WorkerError("nonzero", f"exit {proc.returncode}: {stderr[:300]}", stderr)

    text = _extract_result_text(proc.stdout)
    if _RATE_LIMIT.search(text[:500]):
        raise WorkerError("rate_limit", text[:200], stderr)
    parsed = _parse_json_payload(text)
    return WorkerResult(parsed=parsed, raw_stdout=proc.stdout, duration_ms=duration_ms,
                        model=model, attempt=attempt)


def doctor(cli: Path | None = None) -> dict:
    """One real call, to fail fast with a specific remedy.

    Run before the extraction stage so a run cannot burn twenty minutes only to discover
    the CLI was never authenticated.
    """
    report: dict = {"ok": False}
    try:
        cli = cli or resolve_cli()
    except WorkerError as e:
        report["error"] = e.detail or str(e)
        report["remedy"] = "Install the CLI (`claude install`) or set CLAUDE_BIN."
        return report
    report["cli_path"] = str(cli)

    try:
        version = subprocess.run([str(cli), "--version"], capture_output=True, text=True, timeout=60)
        report["cli_version"] = (version.stdout or version.stderr).strip()
    except Exception as e:  # noqa: BLE001 - doctor reports, never raises
        report["error"] = f"could not run --version: {e}"
        return report

    schema = {
        "type": "object",
        "properties": {"ok": {"type": "boolean"}, "echo": {"type": "string"}},
        "required": ["ok", "echo"],
        "additionalProperties": False,
    }
    try:
        result = run_worker(
            "Reply with ok=true and echo set to the word SMOKE.",
            system_prompt="You reply with JSON matching the given schema. Nothing else.",
            model="haiku",
            json_schema=schema,
            timeout=120,
            cli=cli,
        )
    except WorkerError as e:
        report["error"] = f"{e.kind}: {e.detail}"
        report["remedy"] = {
            "auth": "Run `claude auth login` (or `claude setup-token` for a headless token). "
                    "Both use your subscription; no API key is involved.",
            "rate_limit": "Subscription rate limit hit. Wait, or lower OBSERVE_CONCURRENCY.",
            "timeout": "The CLI did not answer in 120s. Check network and try again.",
            "bad_json": "The CLI answered but not with JSON. Check the CLI version.",
        }.get(e.kind, "See the error above.")
        report["stderr_tail"] = e.stderr[-500:] if e.stderr else ""
        return report

    report["ok"] = bool(isinstance(result.parsed, dict) and result.parsed.get("ok"))
    report["latency_ms"] = result.duration_ms
    report["response"] = result.parsed
    return report