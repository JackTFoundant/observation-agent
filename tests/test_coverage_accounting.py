"""Coverage must be derived from ground truth, not from the error path.

A cold run dropped one batch of 32 messages when the extraction stage hit its deadline, and
reported `messages_not_extracted: 0` and `complete: true` while its own `coverage_share`
said 0.9874. The cause: a unit abandoned at the deadline returns early and is never added
to `outcome.failed`, and the accounting walked `failed`.

Comparing the eligible set against the extracted set cannot miss a message however it went
astray — failure, deadline, call budget, or a lost bisection half.
"""

from __future__ import annotations

import pytest


def _cards(n: int):
    """(uid, card, key) triples, matching what `message_cards` returns."""
    return [(f"m{i}", object(), f"k{i}") for i in range(n)]


def _coverage(cards, extractions: dict, failed: list[dict]) -> dict:
    """The accounting under test, isolated from the pipeline's I/O."""
    reason_by_uid: dict[str, dict] = {}
    for f in failed:
        for uid in f.get("expected_ids") or []:
            reason_by_uid[uid] = {"batch": f.get("unit_id"), "reason": f.get("kind")}

    lost = []
    for uid, _card, _key in cards:
        if uid in extractions:
            continue
        lost.append({"msg_uid": uid, **reason_by_uid.get(
            uid, {"batch": None, "reason": "stage_deadline"})})
    return {
        "eligible": len(cards),
        "extracted": len(extractions),
        "not_extracted": len(lost),
        "share": round(len(extractions) / max(len(cards), 1), 4),
        "complete": not lost,
        "lost": lost,
    }


def test_a_deadline_abandoned_batch_is_counted_even_though_it_never_failed():
    """The exact bug. 32 of 2531 missing, nothing in `failed`."""
    cards = _cards(2531)
    extractions = {f"m{i}": {} for i in range(2499)}      # last 32 never returned
    cov = _coverage(cards, extractions, failed=[])        # deadline units are not "failed"

    assert cov["not_extracted"] == 32
    assert cov["complete"] is False
    assert cov["share"] == 0.9874
    assert len(cov["lost"]) == 32
    assert all(x["reason"] == "stage_deadline" for x in cov["lost"])


def test_share_and_not_extracted_can_never_disagree():
    """The two numbers are now derived from the same comparison, so they cannot contradict
    each other the way they did in the shipped cold run."""
    for missing in (0, 1, 32, 500, 2531):
        cards = _cards(2531)
        extractions = {f"m{i}": {} for i in range(2531 - missing)}
        cov = _coverage(cards, extractions, failed=[])
        assert cov["not_extracted"] == missing
        assert (cov["share"] == 1.0) == (missing == 0)
        assert cov["complete"] == (missing == 0)


def test_a_known_failure_keeps_its_specific_reason():
    cards = _cards(10)
    extractions = {f"m{i}": {} for i in range(8)}
    cov = _coverage(cards, extractions, failed=[
        {"unit_id": "extract_0000", "kind": "throttled_out", "expected_ids": ["m8"]},
    ])
    reasons = {x["msg_uid"]: x["reason"] for x in cov["lost"]}
    assert reasons["m8"] == "throttled_out", "a diagnosed failure keeps its reason"
    assert reasons["m9"] == "stage_deadline", "an undiagnosed gap still gets counted"


def test_a_complete_run_reports_complete():
    cards = _cards(100)
    cov = _coverage(cards, {f"m{i}": {} for i in range(100)}, failed=[])
    assert cov["complete"] is True
    assert cov["not_extracted"] == 0
    assert cov["lost"] == []


def test_a_lost_bisection_half_is_also_caught():
    """Bisection can drop a half without either half being recorded as failed."""
    cards = _cards(24)
    extractions = {f"m{i}": {} for i in range(12)}   # only one half came back
    cov = _coverage(cards, extractions, failed=[])
    assert cov["not_extracted"] == 12
    assert cov["complete"] is False
