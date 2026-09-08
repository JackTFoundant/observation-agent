#!/usr/bin/env python3
"""PreToolUse hook: keep a model out of the paths that hold the arithmetic and the evidence.

The assignment says the hours-and-dollars maths, the parsing, the citation validation and
the server must be deterministic code, and that it will be checked whether a model was
left holding any of it. Two mechanisms enforce that:

1. `observe/llm/schema_guard.py` rejects any worker response carrying a duration or an
   amount, and a test proves the rejection with a recorded poisoned response.
2. This hook, which stops an interactive Claude Code session from editing the computed
   outputs or the cache by hand.

The distinction matters. A model may freely edit `observe/estimate/model.py` — writing the
deterministic code is the job. What it may not do is reach past that code and write a
number straight into `out/`, because then the published figure would no longer be one the
code produced, and `make verify` would be checking a fiction.
"""

import json
import sys

PROTECTED_PREFIXES = (
    "out/",              # computed report and dashboard data
    ".observe-cache/",   # the content-addressed store and manifest
    "runs/",             # run logs: the record of what actually happened
)

PROTECTED_SUFFIXES = (
    "verify_result.json",
    "summary.json",
)


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0

    tool = payload.get("tool_name") or payload.get("tool") or ""
    if tool not in ("Write", "Edit", "MultiEdit", "NotebookEdit"):
        return 0

    args = payload.get("tool_input") or payload.get("input") or {}
    path = str(args.get("file_path") or args.get("path") or "")
    if not path:
        return 0

    rel = path.split("observation-agent/", 1)[-1].lstrip("/")
    hit = next((p for p in PROTECTED_PREFIXES if rel.startswith(p)), None) \
        or next((s for s in PROTECTED_SUFFIXES if rel.endswith(s)), None)

    if hit:
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": (
                    f"{rel} is produced by deterministic code, not written by hand. "
                    f"Editing it would mean the published figures are no longer the ones "
                    f"the pipeline computed, and `make verify` would be validating a "
                    f"fiction. Change the code in observe/ or the assumptions in "
                    f"config/estimation.yml and re-run `make run` instead."
                ),
            }
        }))
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
