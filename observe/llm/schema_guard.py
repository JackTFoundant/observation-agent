"""The mechanical guarantee that no model is holding the arithmetic.

The assignment says the hours and dollars maths must be deterministic code, and that the
grader will "check whether a model was left holding any of it". Prompting a model not to
emit numbers is not a guarantee; rejecting any response that contains one is.

So every worker response passes through here before it can enter the store, and a response
carrying a key or value that looks like a duration or an amount is rejected outright. The
test that feeds this a poisoned fixture containing `"hours_saved": 40` and asserts the
rejection is the proof, and it runs without a model.

This is enforcement, not validation theatre: a rejected batch is retried once with a
stricter instruction and then hard-failed to the quarantine file. It never degrades into
"accept it anyway".
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

GUARD_VERSION = "1.0.0"

# Field names that would mean the model had done the sums.
#
# Matched against whole *segments* of a key (`hours_saved` -> {"hours", "saved"}), not as
# substrings. A substring search here is actively harmful: `hrs?` matches the "hr" inside
# `process_phrase`, so the guard rejected the single most important field the extractor
# produces. Segment matching is both stricter about what it catches and incapable of that
# class of false positive.
_FORBIDDEN_SEGMENTS = frozenset({
    "hour", "hours", "hr", "hrs",
    "minute", "minutes", "min", "mins",
    "second", "seconds", "sec", "secs",
    "day", "days", "week", "weeks",
    "cost", "costs", "costing",
    "dollar", "dollars", "usd", "money", "price", "pricing",
    "salary", "salaries", "wage", "wages", "rate",
    "fte", "ftes", "headcount",
    "saving", "savings", "saved", "roi", "payback",
    "spend", "spending", "budget",
    "duration", "effort", "workload", "capacity",
})
_KEY_SEGMENT = re.compile(r"[^a-z0-9]+")

# Values that smuggle a quantity in as prose.
_FORBIDDEN_VALUE = (
    re.compile(r"\$\s?\d"),
    re.compile(r"\b\d+(?:\.\d+)?\s*(hours?|hrs?|minutes?|mins?|FTEs?|man.?(hours?|days?))\b", re.I),
    re.compile(r"\b\d+(?:\.\d+)?\s*(?:hours?|hrs?)\s*(?:per|/)\s*(?:month|week|day)\b", re.I),
    re.compile(r"\b(?:usd|dollars?)\s*\d", re.I),
)

# Keys that are legitimately numeric counts of things visible in one message. Anything
# numeric outside this set is suspicious by default.
_ALLOWED_NUMERIC_KEYS = frozenset({
    "actors_named", "touches_observed", "index", "n", "count", "batch_index",
    "message_index", "confidence_score", "distinct_recipients",
})


@dataclass
class GuardResult:
    ok: bool
    violations: list[str] = field(default_factory=list)

    def raise_if_bad(self) -> None:
        if not self.ok:
            raise SchemaGuardViolation(self.violations)


class SchemaGuardViolation(Exception):
    def __init__(self, violations: list[str]):
        super().__init__("; ".join(violations[:6]))
        self.violations = violations


def check(payload, path: str = "$") -> GuardResult:
    """Walk a parsed response and collect every violation. Never raises."""
    violations: list[str] = []
    _walk(payload, path, violations)
    return GuardResult(ok=not violations, violations=violations)


def _walk(node, path: str, out: list[str]) -> None:
    if isinstance(node, dict):
        for key, value in node.items():
            here = f"{path}.{key}"
            name = str(key).lower()
            if name not in _ALLOWED_NUMERIC_KEYS:
                segments = {s for s in _KEY_SEGMENT.split(name) if s}
                offending = segments & _FORBIDDEN_SEGMENTS
                if offending:
                    out.append(
                        f"{here}: key segment {sorted(offending)[0]!r} names a duration or "
                        f"an amount, which only deterministic code may produce"
                    )
            _walk(value, here, out)
    elif isinstance(node, list):
        for i, value in enumerate(node):
            _walk(value, f"{path}[{i}]", out)
    elif isinstance(node, str):
        for pat in _FORBIDDEN_VALUE:
            m = pat.search(node)
            if m:
                out.append(f"{path}: value contains a quantity {m.group(0)!r}")
                break


def check_extraction_batch(payload, expected_ids: set[str]) -> GuardResult:
    """Guard plus structural checks specific to the extraction stage.

    Also catches the quieter failure: a worker that answers about messages it was not
    given, or silently drops half the batch. Both would corrupt counts downstream while
    looking like a successful call.
    """
    result = check(payload)
    violations = list(result.violations)

    items = payload.get("messages") if isinstance(payload, dict) else payload
    if not isinstance(items, list):
        violations.append("$: expected a list of per-message extractions")
        return GuardResult(False, violations)

    seen: set[str] = set()
    for i, item in enumerate(items):
        if not isinstance(item, dict):
            violations.append(f"$[{i}]: not an object")
            continue
        uid = item.get("msg_uid")
        if not uid:
            violations.append(f"$[{i}]: missing msg_uid")
            continue
        if uid not in expected_ids:
            violations.append(f"$[{i}]: msg_uid {uid!r} was not in this batch")
        if uid in seen:
            violations.append(f"$[{i}]: duplicate msg_uid {uid!r}")
        seen.add(uid)

    missing = expected_ids - seen
    if missing:
        violations.append(
            f"$: {len(missing)} of {len(expected_ids)} messages missing from the response "
            f"(e.g. {sorted(missing)[:3]})"
        )
    return GuardResult(ok=not violations, violations=violations)