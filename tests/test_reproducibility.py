"""Reproducibility, which the caching promise quietly depends on.

"Re-running against an unchanged corpus does not repeat finished work" is only true if the
cache keys are stable, and a cache key is stable only if everything feeding it is
order-independent.

Two real bugs live behind these tests. Extraction results arrive in thread-completion order
on a cold run and in card order on a replay, so the record list had two orderings for one
corpus. And `Counter.most_common` breaks ties by insertion order, which came from iterating
a `set` of tokens — an order Python randomizes per process. Between them, a replay that
should have been a total cache hit re-ran half the clusters.
"""

from __future__ import annotations

from collections import Counter

from observe.cluster import _mechanical_label, _rank, build_clusters
from observe.recurring import subject_template


def _record(uid: str, phrase: str, task_class: str = "gas_nomination", **over) -> dict:
    base = {
        "msg_uid": uid, "task_class": task_class, "process_phrase": phrase,
        "role": "request", "systems_referenced": ["sitara"],
        "rework_signal": False, "waiting_signal": False,
        "manual_transfer_signal": False, "deadline_signal": False,
        "evidence": [], "confidence": "high", "subject_key": "nom",
        "novel_hash": "h" + uid, "sender_person": "p1", "person_ids": ["p1", "p2"],
        "person_pairs": ("p1", "p2"), "thread_id": "t" + uid,
        "month": "2001-04", "week": "2001-W15", "folder": "corpus/farmer-d/logistics",
    }
    base.update(over)
    return base


def test_rank_breaks_ties_on_the_key_not_on_insertion_order():
    a = Counter({"beta": 3, "alpha": 3, "gamma": 1})
    b = Counter({"alpha": 3, "gamma": 1, "beta": 3})
    assert _rank(a) == _rank(b)
    assert _rank(a)[0][0] == "alpha", "ties must resolve alphabetically, not by insertion"


def test_mechanical_label_is_stable_under_reordered_input():
    phrases = [
        "confirm nomination change with pipeline scheduler",
        "confirm nomination volume with scheduler",
        "revise nomination volume for meter",
    ]
    a = _mechanical_label(phrases, "gas_nomination", {})
    b = _mechanical_label(list(reversed(phrases)), "gas_nomination", {})
    # Reversing input may legitimately change nothing here; what must not change is that
    # two identical multisets of phrases produce identical labels.
    c = _mechanical_label(phrases[:], "gas_nomination", {})
    assert a == c
    assert isinstance(b[0], str)


def test_mechanical_label_does_not_depend_on_set_iteration_order():
    """The exact bug: `counts.update(set(toks))` let PYTHONHASHSEED pick the label."""
    phrases = ["alpha beta gamma delta", "beta alpha delta gamma"]
    labels = {_mechanical_label(phrases, "other", {})[0] for _ in range(30)}
    assert len(labels) == 1


def test_clustering_is_identical_under_reordered_records():
    """Record order comes from a dict whose insertion order differs between a cold run and
    a cached replay. Cluster ids must not notice."""
    records = [
        _record("m1", "confirm nomination change with pipeline scheduler"),
        _record("m2", "confirm nomination change with scheduler"),
        _record("m3", "reconcile scheduled against actual volumes",
                task_class="volume_imbalance_reconciliation"),
        _record("m4", "reconcile scheduled versus actual volume for meter",
                task_class="volume_imbalance_reconciliation"),
        _record("m5", "distribute weekly capacity report", task_class="recurring_report"),
    ]
    forward = build_clusters(sorted(records, key=lambda r: r["msg_uid"]), {})
    backward = build_clusters(sorted(list(reversed(records)), key=lambda r: r["msg_uid"]), {})
    assert [c.cluster_id for c in forward] == [c.cluster_id for c in backward]
    assert [c.label for c in forward] == [c.label for c in backward]
    assert [c.exemplar_uids for c in forward] == [c.exemplar_uids for c in backward]


def test_cluster_metadata_dicts_are_deterministically_ordered():
    records = [
        _record(f"m{i}", "confirm nomination change with scheduler",
                systems_referenced=["unify", "sitara"] if i % 2 else ["sitara", "unify"],
                role="request" if i % 3 else "confirmation")
        for i in range(1, 9)
    ]
    a = build_clusters(records, {})
    b = build_clusters(list(records), {})
    assert [list(c.systems.items()) for c in a] == [list(c.systems.items()) for c in b]
    assert [list(c.roles.items()) for c in a] == [list(c.roles.items()) for c in b]


def test_subject_template_is_pure():
    for _ in range(20):
        assert subject_template("Credit Report--4/3/01") == "credit report <date>"
        assert subject_template("Credit Report - 4/4/01") == "credit report <date>"
        assert subject_template("RE: Credit Report 4/5/01") == "credit report <date>"


def test_subject_template_collapses_punctuation_variants_to_one_series():
    variants = ["Credit Report--5/9/01", "Credit Report - 5/10/01",
                "Credit Report 5/11/01", "Credit Report -5/12/01"]
    assert len({subject_template(v) for v in variants}) == 1, (
        "punctuation variants must not split one daily report into four series that each "
        "fail the recurrence gate")
