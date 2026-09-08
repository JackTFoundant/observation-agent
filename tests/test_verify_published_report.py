"""Run the independent verifier against the committed report, inside pytest, with no model.

This is the test that makes the shipped run's claims checkable in CI rather than only by
hand. If a citation in `out/` ever stops reproducing from the corpus, or a published figure
stops matching its own derivation, this fails.
"""

from __future__ import annotations

import json
from decimal import Decimal
from pathlib import Path

import pytest

from observe.estimate.model import recompute_from_derivation, total_dollars
from observe.evidence.anchor import STRONG_TIERS
from observe.verify import verify

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "out"
CORPUS = ROOT / "corpus"

pytestmark = pytest.mark.skipif(
    not (OUT / "summary.json").exists(),
    reason="no published report in out/; run `make run` first",
)


@pytest.fixture(scope="module")
def report():
    return verify(OUT, CORPUS, strict=True)


@pytest.fixture(scope="module")
def summary():
    return json.loads((OUT / "summary.json").read_text())


@pytest.fixture(scope="module")
def opportunities(summary):
    out = []
    for row in summary["opportunities"]:
        path = OUT / "opportunities" / f"{row['opportunity_id']}.json"
        if path.exists():
            out.append(json.loads(path.read_text()))
    return out


def test_the_published_report_verifies(report):
    assert report.passed, [f["kind"] + ": " + f["detail"] for f in report.failures[:10]]
    assert report.checks > 50, "suspiciously few checks — is the report populated?"


def test_no_verification_failures_of_any_kind(report):
    assert report.failures == []


def test_every_citation_is_character_identical_or_labelled_weaker(report):
    """Weak-tier citations are allowed but must be a small minority."""
    weak = sum(v for k, v in report.tiers.items() if k not in STRONG_TIERS)
    total = sum(report.tiers.values())
    assert total > 0
    assert weak / total <= 0.4, f"{weak}/{total} citations needed case/punctuation folding"


def test_every_published_dollar_recomputes_from_its_own_derivation(opportunities):
    assert opportunities
    for opp in opportunities:
        published = Decimal(str(opp["dollars_per_month"]["base"]))
        assert recompute_from_derivation(opp["derivation"]) == published, opp["opportunity_id"]


def test_headline_equals_the_sum_of_the_counted_parts(summary, opportunities):
    counted = [Decimal(str(o["dollars_per_month"]["base"]))
               for o in opportunities if o["status"] == "counted"]
    assert total_dollars(counted) == Decimal(str(summary["headline"]["dollars_per_month"]["base"]))


def test_bands_are_ordered_for_every_opportunity(opportunities):
    for o in opportunities:
        d = o["dollars_per_month"]
        assert d["low"] <= d["base"] <= d["high"], o["opportunity_id"]


def test_nothing_counted_lacks_evidence(opportunities):
    from observe.reduce.build import MIN_CITATIONS
    for o in opportunities:
        if o["status"] == "counted":
            assert len(o["citations"]) >= MIN_CITATIONS, o["opportunity_id"]


def test_no_citation_ships_and_is_quarantined(opportunities):
    quarantine = json.loads((OUT / "quarantine.json").read_text())
    shipped = {c["citation_id"] for o in opportunities for c in o["citations"]}
    withheld = {c.get("citation_id") for c in quarantine.get("citations", [])}
    assert not (shipped & (withheld - {None}))


def test_the_generated_table_contributes_no_quantity(summary, opportunities):
    """The 350KB planted message must not be the basis of any figure.

    It is still allowed as evidence — its prose is genuine — so this checks that no
    opportunity is *built* on it, not that it is absent.
    """
    generated = {g["path"] for g in summary["corpus"]["generated_tables"]}
    assert generated, "the generated-table detector found nothing; has it regressed?"
    for o in opportunities:
        if o["status"] != "counted":
            continue
        from_generated = [c for c in o["citations"] if c["source_path"] in generated]
        assert len(from_generated) < len(o["citations"]), (
            f"{o['opportunity_id']} rests entirely on a machine-generated table")


def test_report_markdown_exists_and_names_the_range_not_just_the_base(summary):
    text = (OUT / "report.md").read_text()
    assert "per month" in text
    assert "Range" in text or "range" in text
    assert "floor, not a total" in text, "the attribution caveat must survive into the report"


def test_method_page_publishes_the_assumptions_verbatim():
    method = json.loads((OUT / "method.json").read_text())
    assert "assumptions_source_text" in method
    assert "NOT measured" in method["assumptions_source_text"], (
        "the assumptions file must keep its own honesty note")
    assert method["assumptions"]["global"]["extrapolation_factor"] == 1.0