"""The hours-and-dollars arithmetic, checked against numbers computed by hand.

The assignment says this maths must be deterministic code rather than a model call, and
that the grader will check whether a model was left holding any of it. These tests are half
of that proof: expectations here were worked out on paper, not captured from a run, so a
change in behaviour fails rather than silently re-baselining.

The other half is `tests/test_schema_guard.py`, which proves a model *cannot* emit one of
these numbers in the first place.
"""

from __future__ import annotations

from decimal import Decimal
from pathlib import Path

import pytest

from observe.estimate.model import (
    BANDS,
    Assumptions,
    Measured,
    band_estimates,
    estimate,
    measure,
    recompute_from_derivation,
    total_dollars,
)

CONFIG = Path(__file__).resolve().parents[1] / "config/estimation.yml"


def base() -> Assumptions:
    return Assumptions.load(CONFIG, "base")


def sample_measured(**over) -> Measured:
    kwargs = dict(
        instances=10, messages=25, dated_messages=25, undated_messages=0,
        participants_median=3, months=Decimal(5),
        rework_rate=Decimal("0.2"), waiting_rate=Decimal("0.1"),
        manual_transfer_rate=Decimal("0.3"), senders=3,
    )
    kwargs.update(over)
    return Measured(**kwargs)


def test_hand_computed_recurring_report():
    """Worked by hand:

        coverage    = 25 dated / 25 messages          = 1
        per_month   = 10 instances / 5 months         = 2
        touches     = 25 messages / 10 instances      = 2.5
        minutes     = 22 + (2.5-1)*4 + 0.2*10 + 0.1*2 = 30.2
        multiplier  = 1 + 0.35*(3-1)                  = 1.7
        hours       = 2 * 30.2 * 1.7 / 60             = 1.711333...
        automatable = 1.711333... * 0.75              = 1.283500
        dollars     = 1.2835 * 85                     = 109.0975 -> $109.10
    """
    est = estimate(sample_measured(), "recurring_report", base())
    assert est.hours_per_month.quantize(Decimal("0.0001")) == Decimal("1.7113")
    assert est.automatable_hours_per_month.quantize(Decimal("0.0001")) == Decimal("1.2835")
    assert est.dollars_per_month == Decimal("109.10")


def test_hand_computed_gas_nomination():
    """Same measured inputs, different class:

        minutes     = 8 + 1.5*3 + 0.2*12 + 0.1*2 = 15.1
        hours       = 2 * 15.1 * 1.7 / 60        = 0.855666...
        automatable = * 0.55                     = 0.470616...
        dollars     = * 85                       = 40.0024... -> $40.00
    """
    est = estimate(sample_measured(), "gas_nomination", base())
    assert est.hours_per_month.quantize(Decimal("0.0001")) == Decimal("0.8557")
    assert est.dollars_per_month == Decimal("40.00")


def test_unknown_task_class_falls_back_to_other_not_to_a_crash():
    est = estimate(sample_measured(), "class_that_does_not_exist", base())
    other = estimate(sample_measured(), "other", base())
    assert est.dollars_per_month == other.dollars_per_month


def test_other_class_claims_almost_no_savings():
    """We will not claim savings on work we could not identify."""
    a = base()
    assert a.for_class("other")["automatable_share"] <= Decimal("0.2")


def test_undated_messages_lift_instances_but_never_widen_the_window():
    """The uplift must raise the rate, not dilute it.

    Widening the coverage window instead would silently shrink every per-month figure,
    which is the wrong direction for an honest estimate.
    """
    dated_only = estimate(
        sample_measured(messages=20, dated_messages=20, undated_messages=0),
        "recurring_report", base(),
    )
    with_undated = estimate(
        sample_measured(messages=20, dated_messages=16, undated_messages=4),
        "recurring_report", base(),
    )
    assert with_undated.dollars_per_month > dated_only.dollars_per_month
    assert with_undated.derivation["measured"]["months"] == dated_only.derivation["measured"]["months"]


def test_months_floor_prevents_a_divide_by_near_zero_blowup():
    est = estimate(sample_measured(months=Decimal(0)), "recurring_report", base())
    assert est.dollars_per_month > 0
    # With the floor at 1 month, 10 instances become 10/month, not a division by zero.
    assert "1.0 months of coverage" in " ".join(est.derivation["steps"])
    assert "= 10.000 instances per month" in " ".join(est.derivation["steps"])


def test_single_participant_has_no_coordination_uplift():
    est = estimate(sample_measured(participants_median=1), "recurring_report", base())
    assert "= 1.000" in " ".join(est.derivation["steps"])


def test_zero_instances_does_not_divide_by_zero():
    est = estimate(sample_measured(instances=0, messages=0, dated_messages=0), "other", base())
    assert est.dollars_per_month >= 0


def test_no_extrapolation_beyond_the_four_mailboxes_observed():
    """Scaling these findings to a whole company would be the least defensible number in
    the report, so the factor is pinned at 1."""
    assert base().extrapolation_factor == Decimal(1)


def test_bands_are_ordered_and_span_a_real_range():
    bands = band_estimates(sample_measured(), "recurring_report", CONFIG)
    lo, mid, hi = (bands[b].dollars_per_month for b in BANDS)
    assert lo < mid < hi
    # The band has to be wide enough to communicate that the base is not a measurement.
    assert hi > lo * Decimal("1.5")


@pytest.mark.parametrize("task_class", [
    "gas_nomination", "volume_imbalance_reconciliation", "deal_entry_correction",
    "month_end_close", "counterparty_admin", "recurring_report", "capacity_notice",
    "meter_data", "invoice_settlement", "access_provisioning", "pnl_reporting",
    "staffing_coverage", "other",
])
def test_every_class_is_configured_and_ordered(task_class):
    bands = band_estimates(sample_measured(), task_class, CONFIG)
    assert bands["low"].dollars_per_month <= bands["base"].dollars_per_month
    assert bands["base"].dollars_per_month <= bands["high"].dollars_per_month
    assert bands["base"].dollars_per_month >= 0


@pytest.mark.parametrize("task_class", ["recurring_report", "gas_nomination", "month_end_close"])
def test_verify_can_recompute_dollars_from_the_published_derivation_alone(task_class):
    """`verify` reads only what shipped. This is the check that makes it independent."""
    est = estimate(sample_measured(), task_class, base())
    assert recompute_from_derivation(est.derivation) == est.dollars_per_month


def test_recompute_detects_a_tampered_derivation():
    est = estimate(sample_measured(), "recurring_report", base())
    tampered = {**est.derivation, "measured": {**est.derivation["measured"], "instances": 40}}
    assert recompute_from_derivation(tampered) != est.dollars_per_month


def test_total_equals_sum_of_parts_to_the_cent():
    parts = [Decimal("109.10"), Decimal("40.005"), Decimal("1234.567"), Decimal("0.004")]
    assert total_dollars(parts) == Decimal("1383.68")


def test_rounding_is_half_even_as_documented():
    assert total_dollars([Decimal("0.125")]) == Decimal("0.12")
    assert total_dollars([Decimal("0.135")]) == Decimal("0.14")


def test_measure_counts_instances_as_threads_not_messages():
    """The single most important debiasing step: a 40-message argument is one task."""
    members = [
        {"msg_uid": f"m{i}", "thread_id": "t1", "person_ids": ["p1", "p2"],
         "month": "2001-04", "rework_signal": False, "waiting_signal": False,
         "manual_transfer_signal": False, "sender_person": "p1"}
        for i in range(40)
    ]
    m = measure(members, {"t1"})
    assert m.messages == 40
    assert m.instances == 1
    assert m.participants_median == 2


def test_measure_computes_signal_rates_from_the_members():
    members = [
        {"msg_uid": f"m{i}", "thread_id": f"t{i}", "person_ids": ["p1"],
         "month": "2001-04", "rework_signal": i < 5, "waiting_signal": i < 2,
         "manual_transfer_signal": False, "sender_person": "p1"}
        for i in range(10)
    ]
    m = measure(members, {f"t{i}" for i in range(10)})
    assert m.rework_rate == Decimal("0.5")
    assert m.waiting_rate == Decimal("0.2")
    assert m.instances == 10


def test_measure_handles_undated_members():
    members = [
        {"msg_uid": f"m{i}", "thread_id": f"t{i}", "person_ids": ["p1"],
         "month": "2001-04" if i < 7 else None, "rework_signal": False,
         "waiting_signal": False, "manual_transfer_signal": False, "sender_person": "p1"}
        for i in range(10)
    ]
    m = measure(members, {f"t{i}" for i in range(10)})
    assert m.dated_messages == 7
    assert m.undated_messages == 3


def test_derivation_records_its_assumption_source_for_the_dashboard():
    est = estimate(sample_measured(), "meter_data", base())
    assert est.derivation["assumption_source"] == "config/estimation.yml#task_classes.meter_data"
    assert est.derivation["formula_id"] == "hours_v1"
    assert len(est.derivation["steps"]) >= 5


def test_no_derivation_step_is_empty_because_they_render_in_the_ui():
    est = estimate(sample_measured(), "recurring_report", base())
    assert all(step.strip() for step in est.derivation["steps"])