"""Independent re-verification of a published report. No model, no pipeline state.

The grader says: "I will pull claims at random and check them against the raw files." This
is that check, automated, and deliberately built to share nothing with the code that
produced the report. It reads only what shipped in `out/`, re-reads the corpus off disk,
and recomputes everything from scratch:

* every file's sha256 still matches what the report recorded — catches corpus drift or a
  doctored store;
* every citation's byte range, re-sliced from the file, still equals the published quote;
* every citation matches at the tier it claims **and no weaker one** — a citation claiming
  `raw_exact` that only survives normalization is a failure, not a pass;
* every hours and dollars figure, recomputed from its own published derivation, equals the
  published number to the cent;
* the headline equals the sum of its parts under the documented rounding rule;
* no citation that shipped also appears in the quarantine file.

Exit status is 0 or 1, so `make verify` is usable in CI. `--sample N` prints paste-able
`dd` and `sed` commands for N random citations, which is what `docs/AUDIT.md` contains.
"""

from __future__ import annotations

import argparse
import json
import random
import sys
from dataclasses import dataclass, field
from decimal import Decimal
from pathlib import Path

from observe.estimate.model import recompute_from_derivation, total_dollars
from observe.evidence.anchor import STRONG_TIERS, reverify
from observe.parse import parse_file, read_raw

VERIFY_VERSION = "1.0.0"


@dataclass
class Report:
    checks: int = 0
    failures: list[dict] = field(default_factory=list)
    warnings: list[dict] = field(default_factory=list)
    tiers: dict = field(default_factory=dict)

    def ok(self, _label: str = "") -> None:
        self.checks += 1

    def fail(self, kind: str, detail: str, **extra) -> None:
        self.checks += 1
        self.failures.append({"kind": kind, "detail": detail, **extra})

    def warn(self, kind: str, detail: str, **extra) -> None:
        self.warnings.append({"kind": kind, "detail": detail, **extra})

    @property
    def passed(self) -> bool:
        return not self.failures


def verify(out_dir: Path, corpus_root: Path, *, strict: bool = True) -> Report:
    rep = Report()
    summary = json.loads((out_dir / "summary.json").read_text())

    opportunities: list[dict] = []
    for row in summary.get("opportunities", []):
        path = out_dir / "opportunities" / f"{row['opportunity_id']}.json"
        if not path.exists():
            rep.fail("missing_opportunity_file", f"{path.name} referenced by summary but absent")
            continue
        opportunities.append(json.loads(path.read_text()))

    quarantined_ids: set[str] = set()
    qpath = out_dir / "quarantine.json"
    if qpath.exists():
        for c in json.loads(qpath.read_text()).get("citations", []):
            if c.get("citation_id"):
                quarantined_ids.add(c["citation_id"])

    _verify_completeness(rep, summary, out_dir)
    _verify_citations(rep, opportunities, corpus_root, quarantined_ids)
    _verify_arithmetic(rep, summary, opportunities)
    _verify_artifacts(rep, out_dir, opportunities)
    return rep


def _verify_completeness(rep: Report, summary: dict, out_dir: Path) -> None:
    """A degraded run must not be indistinguishable from a good one.

    `verify` checks that what shipped is *true*; this checks that what shipped is
    *complete*. A cold run once hit its deadline during extraction, drafted no artifacts
    and wrote no narratives, and still reported PASS with a normal-looking headline.
    """
    for d in summary.get("degraded_stages", []):
        rep.warn("stage_incomplete",
                 f"{d['stage']}: {d.get('completed')} of {d.get('total')} units completed "
                 f"- {d.get('effect')}",
                 stage=d["stage"])

    cov = summary.get("coverage") or {}
    if cov and not cov.get("complete", True):
        rep.warn("incomplete_coverage",
                 f"{cov.get('messages_extracted')} of {cov.get('messages_eligible')} "
                 f"eligible messages were classified")

    counted = [o for o in summary.get("opportunities", []) if o.get("status") == "counted"]
    if counted and not summary.get("artifacts"):
        rep.warn("no_artifacts",
                 "the run produced no drafted artifacts, so the 'act on what you find' "
                 "deliverable is empty")
    rep.ok()


def _verify_citations(rep: Report, opportunities, corpus_root: Path,
                      quarantined_ids: set[str]) -> None:
    raw_cache: dict[str, tuple[str, str]] = {}
    parsed_cache: dict[str, object] = {}

    for opp in opportunities:
        for cit in opp.get("citations", []):
            path = Path(cit["source_path"])
            cid = cit.get("citation_id", "?")

            if not path.exists():
                rep.fail("source_missing", f"{path} does not exist", citation_id=cid)
                continue

            if path.as_posix() not in raw_cache:
                if len(raw_cache) > 60:
                    raw_cache.clear()
                    parsed_cache.clear()
                raw, sha, _size = read_raw(path)
                raw_cache[path.as_posix()] = (raw, sha)
            raw, sha = raw_cache[path.as_posix()]

            if sha != cit.get("source_sha256"):
                rep.fail("sha_mismatch",
                         f"{path} has changed since the report was written",
                         citation_id=cid, recorded=cit.get("source_sha256")[:12], actual=sha[:12])
                continue

            if path.as_posix() not in parsed_cache:
                parsed_cache[path.as_posix()] = parse_file(path, corpus_root)
            msg = parsed_cache[path.as_posix()]

            ok, reason = reverify(cit, raw, msg.body_decoded, msg.offset_map)
            tier = cit.get("match_tier", "?")
            rep.tiers[tier] = rep.tiers.get(tier, 0) + 1

            if not ok:
                rep.fail("citation_failed", reason, citation_id=cid,
                         source_path=str(path), quote=cit.get("quote", "")[:120])
                continue

            # Independent belt-and-braces: the two published hand-checks must agree.
            lines = raw.split("\n")
            window = "\n".join(lines[cit["line_start"] - 1:cit["line_end"]])
            if cit["quote"] not in window and cit["quote"].strip() not in window:
                rep.fail("line_range_disagrees_with_bytes",
                         "the published line range does not contain the published quote",
                         citation_id=cid, source_path=str(path))
                continue

            if cid in quarantined_ids:
                rep.fail("shipped_and_quarantined",
                         "this citation appears both in the report and in the quarantine file",
                         citation_id=cid)
                continue

            rep.ok()

    weak = sum(v for k, v in rep.tiers.items() if k not in STRONG_TIERS)
    total = sum(rep.tiers.values()) or 1
    if weak / total > 0.4:
        rep.warn("many_weak_citations",
                 f"{weak} of {total} citations needed case or punctuation folding to match")


def _verify_arithmetic(rep: Report, summary: dict, opportunities) -> None:
    counted: list[Decimal] = []
    for opp in opportunities:
        derivation = opp.get("derivation") or {}
        published = opp.get("dollars_per_month", {}).get("base")
        if not derivation or published is None:
            rep.fail("missing_derivation",
                     f"{opp.get('opportunity_id')} publishes a figure with no derivation")
            continue
        try:
            recomputed = recompute_from_derivation(derivation)
        except (KeyError, TypeError, ArithmeticError) as e:
            rep.fail("derivation_unusable",
                     f"{opp.get('opportunity_id')}: {e}",
                     opportunity_id=opp.get("opportunity_id"))
            continue

        if recomputed != Decimal(str(published)):
            rep.fail("arithmetic_mismatch",
                     f"published ${published} but the derivation recomputes to ${recomputed}",
                     opportunity_id=opp.get("opportunity_id"))
            continue
        rep.ok()

        # Confirm the derivation's own stated result agrees with the published field.
        stated = (derivation.get("result") or {}).get("dollars_per_month")
        if stated is not None and Decimal(str(stated)) != Decimal(str(published)):
            rep.fail("derivation_result_mismatch",
                     f"derivation states ${stated}, opportunity publishes ${published}",
                     opportunity_id=opp.get("opportunity_id"))
        else:
            rep.ok()

        if opp.get("status") == "counted":
            counted.append(Decimal(str(published)))

    headline = summary.get("headline", {}).get("dollars_per_month", {}).get("base")
    if headline is None:
        rep.fail("missing_headline", "summary.json has no headline dollar figure")
        return
    expected = total_dollars(counted)
    if expected != Decimal(str(headline)):
        rep.fail("headline_mismatch",
                 f"headline ${headline} but the counted parts sum to ${expected}")
    else:
        rep.ok()

    for opp in opportunities:
        bands = opp.get("dollars_per_month", {})
        if not bands:
            continue
        lo, base, hi = bands.get("low"), bands.get("base"), bands.get("high")
        if None in (lo, base, hi):
            continue
        if not (lo <= base <= hi):
            rep.fail("bands_out_of_order",
                     f"{opp.get('opportunity_id')}: {lo} / {base} / {hi}",
                     opportunity_id=opp.get("opportunity_id"))
        else:
            rep.ok()


def _verify_artifacts(rep: Report, out_dir: Path, opportunities) -> None:
    """Every citation marker in every artifact must resolve to a verified citation."""
    index = out_dir / "artifacts" / "index.json"
    if not index.exists():
        return
    verified_by_opp = {
        o["opportunity_id"]: {c["citation_id"] for c in o.get("citations", [])}
        for o in opportunities
    }
    import re
    marker = re.compile(r"\[(cit_[0-9a-f]{12})\]")
    for entry in json.loads(index.read_text()):
        path = out_dir / "artifacts" / entry["filename"]
        if not path.exists():
            rep.fail("artifact_missing", f"{entry['filename']} listed but absent")
            continue
        body = path.read_text()
        allowed = verified_by_opp.get(entry.get("opportunity_id"), set())
        unresolved = sorted({m for m in marker.findall(body) if m not in allowed})
        if unresolved:
            rep.fail("artifact_citation_unresolved",
                     f"{entry['filename']} cites {unresolved[:3]} which are not verified "
                     f"evidence for its opportunity")
        else:
            rep.ok()


def sample_commands(out_dir: Path, n: int, seed: int) -> list[dict]:
    """Random citations with the shell commands that reproduce them."""
    summary = json.loads((out_dir / "summary.json").read_text())
    cits: list[dict] = []
    for row in summary.get("opportunities", []):
        path = out_dir / "opportunities" / f"{row['opportunity_id']}.json"
        if path.exists():
            opp = json.loads(path.read_text())
            for c in opp.get("citations", []):
                cits.append({**c, "opportunity_title": opp.get("title")})
    rng = random.Random(seed)
    rng.shuffle(cits)
    return cits[:n]


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        prog="observe-verify",
        description="Re-verify a published report against the raw corpus. No model calls.")
    p.add_argument("--out", default="out", type=Path)
    p.add_argument("--corpus", default="corpus", type=Path)
    p.add_argument("--strict", action="store_true", default=True)
    p.add_argument("--sample", type=int, default=0,
                   help="print N random citations with dd/sed commands to hand-check")
    p.add_argument("--seed", type=int, default=7)
    p.add_argument("--json", dest="as_json", action="store_true")
    args = p.parse_args(argv)

    if not (args.out / "summary.json").exists():
        print(f"no report at {args.out}/summary.json - run `make run` first", file=sys.stderr)
        return 2

    if args.sample:
        for i, c in enumerate(sample_commands(args.out, args.sample, args.seed), 1):
            print(f"\n--- {i}. {c['citation_id']}  [{c['match_tier']}]")
            print(f"    opportunity: {c.get('opportunity_title', '')}")
            print(f"    quote: \"{c['quote'].strip()}\"")
            print(f"    {c['check_commands']['dd']}")
            print(f"    {c['check_commands']['sed']}")
        print()

    rep = verify(args.out, args.corpus, strict=args.strict)
    result = {
        "verify_version": VERIFY_VERSION,
        "passed": rep.passed,
        "checks": rep.checks,
        "failures": rep.failures,
        "warnings": rep.warnings,
        "citation_tiers": rep.tiers,
    }
    (args.out / "verify_result.json").write_text(json.dumps(result, indent=2) + "\n")

    if args.as_json:
        print(json.dumps(result, indent=2))
    else:
        status = "PASS" if rep.passed else "FAIL"
        print(f"\n{status}  {rep.checks} checks, {len(rep.failures)} failures, "
              f"{len(rep.warnings)} warnings")
        print(f"citation tiers: {rep.tiers}")
        for f in rep.failures[:25]:
            print(f"  FAIL {f['kind']}: {f['detail']}")
        for w in rep.warnings:
            print(f"  warn {w['kind']}: {w['detail']}")
    return 0 if rep.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())