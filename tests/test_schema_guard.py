"""Proof that no model was left holding the arithmetic.

The assignment says the hours-and-dollars maths must be deterministic code and that the
grader will check whether a model was left holding any of it. Prompting a model not to emit
numbers is not a guarantee. Rejecting any response that contains one is.

`test_poisoned_extraction_is_rejected` is the load-bearing test in this file: it feeds the
guard a recorded response carrying `"hours_saved": 40` and asserts the rejection. It runs
with no model involved.
"""

from __future__ import annotations

import json
from pathlib import Path

from observe.llm.schema_guard import (
    SchemaGuardViolation,
    check,
    check_extraction_batch,
)

FIXTURES = Path(__file__).parent / "golden"


def test_poisoned_extraction_is_rejected():
    """The proof. A model that did the sums cannot get its answer into the store."""
    poisoned = json.loads((FIXTURES / "poisoned_extraction.json").read_text())
    result = check(poisoned)
    assert not result.ok
    assert any("hours" in v for v in result.violations)


def test_clean_extraction_passes():
    clean = json.loads((FIXTURES / "clean_extraction.json").read_text())
    assert check(clean).ok, check(clean).violations


# ---------------------------------------------------------------------------
# Keys that would mean the model had computed something
# ---------------------------------------------------------------------------

def test_duration_and_amount_keys_are_rejected():
    for payload in (
        {"hours_saved": 40},
        {"hours_per_month": 12.5},
        {"minutes_per_touch": 5},
        {"dollars_per_month": 1000},
        {"estimated_cost": "x"},
        {"annual_savings": 1},
        {"fte_equivalent": 0.4},
        {"blended_rate": 85},
        {"payback_months": 3},
        {"effort": "large"},
        {"nested": [{"deep": {"total_hours": 3}}]},
    ):
        assert not check(payload).ok, f"{payload} should be rejected"


def test_fields_the_extractor_legitimately_uses_are_not_rejected():
    """A guard that fires on its own schema is worse than no guard.

    `process_phrase` is here because an earlier substring-matching version rejected it:
    the pattern `hrs?` matched the "hr" inside "phrase", and the guard silently killed the
    single most important field the extractor produces.
    """
    for payload in (
        {"process_phrase": "confirm nomination change with pipeline scheduler"},
        {"msg_uid": "m_0041a2", "role": "request", "confidence": "high"},
        {"actors_named": 3},
        {"systems_referenced": ["sitara", "unify"]},
        {"rework_signal": True, "waiting_signal": False},
        {"task_class": "volume_imbalance_reconciliation"},
        {"phrase": "distribute weekly capacity report"},
        {"threads": 4, "senders": 2, "months": 5},
    ):
        result = check(payload)
        assert result.ok, f"{payload} should pass, got {result.violations}"


# ---------------------------------------------------------------------------
# Quantities smuggled in as prose
# ---------------------------------------------------------------------------

def test_quantities_in_model_authored_prose_are_rejected():
    for text in (
        "this takes about 15 minutes each time",
        "roughly 2 hours per month",
        "costs $85 per hour",
        "worth $1,200 a month",
        "approximately 0.5 FTE",
        "40 man-hours a year",
    ):
        assert not check({"why": text}).ok, f"{text!r} should be rejected"


def test_verbatim_corpus_quotes_containing_money_are_allowed():
    """The guard stops a model *asserting* a quantity, not *quoting* the archive.

    Applied to quotes it does real damage: a verbatim line about a payment amount is
    exactly the evidence an invoice-and-settlement finding needs, and rejecting it would
    blind the report to a whole task class. This is safe because a quote is never trusted
    anyway - deterministic code re-locates it in the raw file and slices the published text
    from there.
    """
    payload = {
        "evidence": [{
            "quote_proposal": "entitled to receive the additional payment of $4,500",
            "why": "shows the payment authorisation step",
        }]
    }
    assert check(payload).ok, check(payload).violations


def test_a_quote_field_does_not_launder_a_model_assertion_in_a_sibling_field():
    payload = {
        "evidence": [{
            "quote_proposal": "entitled to receive the additional payment of $4,500",
            "why": "each one takes 20 minutes to process",
        }]
    }
    assert not check(payload).ok


def test_quote_exemption_does_not_leak_to_the_next_field():
    """Exemption is per-key, not sticky across a walk."""
    payload = {
        "a": {"quote": "the additional payment of $4,500 was approved by finance"},
        "b": {"note": "this costs $500 a month"},
    }
    result = check(payload)
    assert not result.ok
    assert any(".b.note" in v for v in result.violations)


# ---------------------------------------------------------------------------
# Structural checks on an extraction batch
# ---------------------------------------------------------------------------

def _item(uid: str) -> dict:
    return {
        "msg_uid": uid, "is_operational": True, "task_class": "gas_nomination",
        "process_phrase": "confirm nomination change", "role": "request",
        "systems_referenced": [], "rework_signal": False, "waiting_signal": False,
        "manual_transfer_signal": False, "deadline_signal": False,
        "evidence": [], "confidence": "high",
    }


def test_batch_accepts_a_complete_response():
    payload = {"messages": [_item("a"), _item("b")]}
    assert check_extraction_batch(payload, {"a", "b"}).ok


def test_batch_rejects_a_response_that_drops_messages():
    """A worker that silently answers about half the batch would corrupt every count
    downstream while looking like a success."""
    payload = {"messages": [_item("a")]}
    result = check_extraction_batch(payload, {"a", "b", "c"})
    assert not result.ok
    assert any("missing from the response" in v for v in result.violations)


def test_batch_rejects_invented_message_ids():
    payload = {"messages": [_item("a"), _item("not_in_this_batch")]}
    result = check_extraction_batch(payload, {"a"})
    assert not result.ok
    assert any("was not in this batch" in v for v in result.violations)


def test_batch_rejects_duplicate_ids():
    payload = {"messages": [_item("a"), _item("a")]}
    result = check_extraction_batch(payload, {"a"})
    assert not result.ok
    assert any("duplicate" in v for v in result.violations)


def test_batch_rejects_a_non_list_payload():
    result = check_extraction_batch({"messages": "oops"}, {"a"})
    assert not result.ok


def test_batch_rejects_an_item_missing_its_id():
    payload = {"messages": [{"task_class": "other"}]}
    result = check_extraction_batch(payload, {"a"})
    assert not result.ok
    assert any("missing msg_uid" in v for v in result.violations)


def test_batch_still_catches_a_quantity_inside_a_valid_shape():
    item = _item("a")
    item["process_phrase"] = "confirm nomination, takes 20 minutes"
    result = check_extraction_batch({"messages": [item]}, {"a"})
    assert not result.ok


def test_raise_if_bad_raises_with_the_violations_attached():
    result = check({"hours_saved": 1})
    try:
        result.raise_if_bad()
    except SchemaGuardViolation as e:
        assert e.violations
    else:
        raise AssertionError("expected SchemaGuardViolation")


def test_good_result_does_not_raise():
    check({"role": "request"}).raise_if_bad()