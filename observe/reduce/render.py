"""Stage 7: write the report and every file the dashboard reads.

Deterministic and dependency-free. The server that later serves these files does no
computation at all — it reads them off disk — which is what makes "the server is
deterministic code" true by construction rather than by argument.

Totals are summed unrounded and quantized once, so the headline always equals the sum of
its parts under the documented rule. Only `counted` opportunities reach the headline;
`low_confidence` and `quarantined` ones are published with their own visible subtotals so
nothing is silently removed.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path

from observe.estimate.model import BANDS, total_dollars

RENDER_VERSION = "1.0.0"


def _write(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, default=str) + "\n")


def write_all(ctx, corpus, opportunities, clusters, rejected_series, artifacts) -> dict:
    out = ctx.root / "out"
    out.mkdir(parents=True, exist_ok=True)

    counted = [o for o in opportunities if o.status == "counted"]
    low = [o for o in opportunities if o.status == "low_confidence"]
    quarantined = [o for o in opportunities if o.status == "quarantined"]

    totals = {
        band: float(total_dollars([o.bands[band].dollars_per_month for o in counted]))
        for band in BANDS
    }
    hours_total = {
        band: round(sum(float(o.bands[band].automatable_hours_per_month) for o in counted), 1)
        for band in BANDS
    }
    low_subtotal = float(total_dollars([o.bands["base"].dollars_per_month for o in low]))
    quarantined_subtotal = float(
        total_dollars([o.bands["base"].dollars_per_month for o in quarantined]))

    dated = [m for m in corpus.survivors if m.sent_at]
    span = (min(m.sent_at for m in dated), max(m.sent_at for m in dated)) if dated else (None, None)
    months = sorted({m.sent_at.strftime("%Y-%m") for m in dated})

    all_citations = [c for o in opportunities for c in o.citations]
    tiers: dict[str, int] = {}
    for c in all_citations:
        tiers[c.match_tier] = tiers.get(c.match_tier, 0) + 1

    generated = {k: v for k, v in corpus.generated_tables.items() if v["generated"]}

    corpus_stats = {
        "files": len(corpus.messages),
        "duplicates_removed": len(corpus.duplicates),
        "duplicate_groups": len(corpus.dup_groups),
        "unique_messages": len(corpus.survivors),
        "task_instances": len(corpus.threads),
        "distinct_people": len(corpus.people),
        "mailboxes": sorted({m.path.split("/")[1] for m in corpus.messages}),
        "folders": sorted({m.path.rsplit("/", 1)[0] for m in corpus.messages}),
        "date_span": {
            "from": span[0].date().isoformat() if span[0] else None,
            "to": span[1].date().isoformat() if span[1] else None,
            "months": len(months),
        },
        "undated_messages": sum(1 for m in corpus.survivors if not m.sent_at),
        "categories": _count(corpus.classifications.values(), lambda c: c.category),
        "messages_sent_to_a_model": sum(
            1 for c in corpus.classifications.values() if c.send_to_model),
        "ack_only_messages": sum(
            1 for c in corpus.classifications.values() if c.category == "ack"),
        "generated_tables": [
            {"path": v["path"], "rows": v["rows"], "columns": v["columns"],
             "chars": v["chars"], "proof": v["proof"]}
            for v in generated.values()
        ],
    }

    # How much of the observed operational work these figures actually account for.
    #
    # This is the most important caveat on the headline and it belongs in the data, not
    # only in the notes. The promotion gate is strict on purpose, so most operational
    # messages sit in a long tail of work that recurred too few times, over too short a
    # window, or from too few people to be called a recurring process. That tail is real
    # work and it is *not* costed here. The headline is therefore a floor: the portion of
    # the observed workload we could attribute to an identified, evidenced process.
    operational_uids = {
        uid for uid, c in corpus.classifications.items() if c.send_to_model
    }
    attributed: set[str] = set()
    for o in counted:
        attributed |= set(o.member_uids)
    attribution = {
        "operational_messages": len(operational_uids),
        "attributed_to_counted_opportunities": len(attributed & operational_uids),
        "share_attributed": round(
            len(attributed & operational_uids) / max(len(operational_uids), 1), 4),
        "unattributed_long_tail": len(operational_uids - attributed),
        "note": (
            "The headline counts only work attributed to an identified recurring process. "
            "The remaining operational messages are a long tail that failed the promotion "
            "gate - too few repetitions, too short a window, or too few people to call it "
            "a process. That work is real and is deliberately not costed, which makes the "
            "headline a floor rather than an estimate of total waste."
        ),
    }

    summary = {
        "run_id": ctx.run_id,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "corpus_digest": corpus.corpus_digest,
        "scope_line": _scope_line(corpus_stats),
        "attribution": attribution,
        "blended_rate_usd_per_hour": 85,
        "headline": {
            "dollars_per_month": totals,
            "automatable_hours_per_month": hours_total,
            "counted_opportunities": len(counted),
        },
        "not_counted": {
            "low_confidence": {"count": len(low), "dollars_per_month_base": low_subtotal},
            "quarantined": {"count": len(quarantined),
                            "dollars_per_month_base": quarantined_subtotal},
        },
        "evidence": {
            "citations_verified": len(all_citations),
            "citations_quarantined": sum(len(o.quarantined_citations) for o in opportunities),
            "tiers": tiers,
            "repaired": sum(1 for c in all_citations if c.repaired),
        },
        "corpus": corpus_stats,
        "opportunities": [_row(o) for o in opportunities],
        "artifacts": [
            {k: a[k] for k in ("artifact_id", "title", "artifact_type", "opportunity_id",
                               "filename", "review_status") if k in a}
            for a in artifacts
        ],
        "stages": ctx.stats,
        "residual": {
            "content_clusters_not_promoted": sum(1 for c in clusters if not c.gate.passed),
            "series_not_promoted": len(rejected_series),
        },
    }
    _write(out / "summary.json", summary)

    for o in opportunities:
        _write(out / "opportunities" / f"{o.opportunity_id}.json", o.as_dict())

    _write(out / "residual.json", {
        "explanation": (
            "Candidate processes the pipeline found and declined to promote. Published "
            "because what a system rejects is as informative as what it reports: a tidy "
            "list with no residual would mean the gate was not doing anything."
        ),
        "gates": _gate_doc(),
        "content_clusters": [
            {
                "cluster_id": c.cluster_id, "label": c.label, "task_class": c.task_class,
                "messages": c.size, "metrics": c.gate.metrics,
                "failed_gates": c.gate.failed_gates,
            }
            for c in clusters if not c.gate.passed and c.size >= 3
        ],
        "recurring_series": rejected_series,
    })

    _write(out / "quarantine.json", {
        "explanation": (
            "Claims and citations excluded from the report. Nothing here is counted in any "
            "dollar total. Published rather than deleted: a report with no visible "
            "exclusions is one whose exclusions you cannot check."
        ),
        "opportunities": [
            {"opportunity_id": o.opportunity_id, "title": o.title, "status": o.status,
             "reason": o.status_reason, "flags": sorted(o.flags),
             "would_have_been_dollars_per_month": float(o.bands["base"].dollars_per_month),
             "verified_citations": len(o.citations)}
            for o in opportunities if o.status != "counted"
        ],
        "citations": [
            {**q, "opportunity_id": o.opportunity_id}
            for o in opportunities for q in o.quarantined_citations
        ],
    })

    _write(out / "method.json", _method(ctx, corpus_stats))
    (out / "report.md").write_text(_report_md(summary, opportunities, artifacts))
    _write(ctx.run_dir / "summary.json", summary)
    return summary


def _count(items, key) -> dict:
    counts: dict[str, int] = {}
    for i in items:
        k = key(i)
        counts[k] = counts.get(k, 0) + 1
    return dict(sorted(counts.items(), key=lambda kv: -kv[1]))


def _scope_line(stats: dict) -> str:
    span = stats["date_span"]
    return (
        f"Observed across {len(stats['mailboxes'])} mailboxes and "
        f"{stats['files']:,} messages, {span['from']} to {span['to']} "
        f"({span['months']} months). Not extrapolated beyond what was observed."
    )


def _row(o) -> dict:
    return {
        "opportunity_id": o.opportunity_id,
        "title": o.title,
        "task_class": o.task_class,
        "source": o.source,
        "status": o.status,
        "status_reason": o.status_reason,
        "confidence": o.confidence,
        "dollars_per_month": {b: float(o.bands[b].dollars_per_month) for b in BANDS},
        "automatable_hours_per_month": {
            b: float(o.bands[b].automatable_hours_per_month.quantize(Decimal("0.1")))
            for b in BANDS
        },
        "messages": o.measured.messages,
        "instances": o.measured.instances,
        "months": len(o.months),
        "people": len(o.person_ids),
        "citations": len(o.citations),
        "artifact_shape": o.artifact_shape,
        "flags": sorted(o.flags),
    }


def _gate_doc() -> dict:
    from observe.cluster import GATES
    from observe.recurring import _MIN_INSTANCES, _MIN_MONTHS, _MIN_WEEKS
    from observe.reduce.build import (
        MIN_CITATION_SENDERS, MIN_CITATION_THREADS, MIN_CITATIONS, MAX_NORMALIZED_SHARE)
    return {
        "content_cluster": {
            **GATES,
            "_note": "A cluster becomes a recurring process only if the corpus insists. "
                     "The single-sender escape exists because one person doing something "
                     "sixty times is a process, and requiring two senders would delete the "
                     "recurring reports.",
        },
        "recurring_series": {
            "min_instances": _MIN_INSTANCES,
            "min_months": _MIN_MONTHS,
            "min_weeks": _MIN_WEEKS,
            "_note": "Replies are excluded from a series rather than disqualifying it.",
        },
        "claim": {
            "min_verified_citations": MIN_CITATIONS,
            "min_distinct_messages": MIN_CITATION_THREADS,
            "min_distinct_senders": MIN_CITATION_SENDERS,
            "max_normalized_citation_share": MAX_NORMALIZED_SHARE,
            "_note": "Failing a claim gate quarantines the whole opportunity and removes "
                     "it from every dollar total.",
        },
    }


def _method(ctx, corpus_stats: dict) -> dict:
    import yaml
    config_text = (ctx.root / "config/estimation.yml").read_text()
    return {
        "the_evidence_invariant": (
            "Every quote published by this system is produced by slicing bytes out of a "
            "corpus file. It is never copied from model output; a model's proposed quote "
            "is used only as a search key. If no anchor is found there is no quote, and "
            "the claim that depended on it does not ship. A hallucinated quote therefore "
            "cannot reach the report."
        ),
        "the_arithmetic_invariant": (
            "No model produces any duration or amount. Every response is passed through a "
            "guard that rejects a key or value naming one, and a test feeds that guard a "
            "recorded poisoned response to prove the rejection. Hours and dollars are "
            "computed in Decimal from counts measured by deterministic code, and every "
            "published number carries the derivation that produced it."
        ),
        "formula": (
            "hours_per_month = (instances / coverage / months) x minutes_per_instance x "
            "coordination_multiplier / 60;  "
            "minutes_per_instance = handle + (touches-1) x per_touch + rework_rate x "
            "rework + waiting_rate x waiting_admin;  "
            "coordination_multiplier = 1 + alpha x (median_participants - 1);  "
            "dollars = automatable_hours x $85"
        ),
        "what_is_measured": [
            "task instances (threads, not messages)", "touches per instance",
            "median participants per instance", "months and weeks of coverage",
            "rework / waiting / manual-transfer signal rates", "distinct senders",
        ],
        "what_is_assumed": [
            "minutes per touch, per task class", "minutes added by rework and waiting",
            "the automatable share of each task class", "the coordination alpha",
        ],
        "largest_uncertainty": (
            "The per-class handling-minute assumptions. Nobody timed this work and nobody "
            "could: the people left in 2002 and the systems no longer exist. The dollar "
            "total moves close to linearly with these values, which is why every figure "
            "ships a low-base-high band rather than a point estimate."
        ),
        "assumptions_file": "config/estimation.yml",
        "assumptions": yaml.safe_load(config_text),
        "assumptions_source_text": config_text,
        "gates": _gate_doc(),
        "how_to_check_it_yourself": [
            "make verify - re-anchors every citation from scratch and recomputes every "
            "number from its published derivation",
            "make test - the full suite, with zero model calls",
            "docs/AUDIT.md - 25 random citations with paste-able dd and sed commands",
            "Every citation in the dashboard shows its byte range and line range, and the "
            "raw message view highlights the span by slicing the file the server just read",
        ],
        "corpus": corpus_stats,
        "stages": ctx.stats,
    }


def _money(v: float) -> str:
    return f"${v:,.0f}"


def _report_md(summary: dict, opportunities, artifacts) -> str:
    h = summary["headline"]
    L = []
    A = L.append
    A("# Where this company is losing time")
    A("")
    A(f"*Run `{summary['run_id']}` · generated {summary['generated_at'][:19]}Z · "
      f"corpus digest `{summary['corpus_digest'][:12]}`*")
    A("")
    A(f"## {_money(h['dollars_per_month']['base'])} per month")
    A("")
    A(f"Range {_money(h['dollars_per_month']['low'])} – "
      f"{_money(h['dollars_per_month']['high'])}. "
      f"{h['automatable_hours_per_month']['base']:.0f} automatable hours per month at a "
      f"blended $85/hour, across {h['counted_opportunities']} opportunities.")
    A("")
    A(summary["scope_line"])
    A("")
    A("The range is not decoration. The counts behind these figures are measured from the "
      "corpus; the minutes-per-task are estimates nobody was able to verify, so the base "
      "number should be read as the middle of a band, not as a measurement.")
    A("")
    att = summary["attribution"]
    A(f"**This is a floor, not a total.** "
      f"{att['attributed_to_counted_opportunities']:,} of {att['operational_messages']:,} "
      f"operational messages ({att['share_attributed']:.0%}) could be attributed to an "
      f"identified recurring process. The other {att['unattributed_long_tail']:,} are a "
      f"long tail that failed the promotion gate - too few repetitions, too short a "
      f"window, or too few people to call it a process. That work is real and is "
      f"deliberately left uncosted rather than estimated. Every rejected candidate is "
      f"published in `out/residual.json` with the gate it failed.")
    A("")

    c = summary["corpus"]
    A("### What was read")
    A("")
    A(f"- **{c['files']:,} files**, every one of them, {c['unique_messages']:,} unique after "
      f"removing {c['duplicates_removed']} duplicates in {c['duplicate_groups']} groups")
    A(f"- grouped into **{c['task_instances']:,} task instances**, because a forty-message "
      f"argument about one nomination is one task")
    A(f"- **{c['messages_sent_to_a_model']:,} messages** were shown to a model; "
      f"{c['ack_only_messages']:,} were acknowledgements with no new text and were counted "
      f"deterministically instead")
    A(f"- **{summary['evidence']['citations_verified']} citations** verified against raw "
      f"bytes, {summary['evidence']['citations_quarantined']} rejected and published in "
      f"`out/quarantine.json`")
    A("")

    for g in c["generated_tables"]:
        A(f"> **A note on `{g['path']}`.** This message is 5% of the corpus in one file. Its "
          f"{g['rows']:,}-row table is machine-generated placeholder content, not business "
          f"data, and **no quantity in this report is derived from it**. The proof is "
          f"arithmetic:")
        A(">")
        for p in g["proof"][1:]:
            A(f"> - {p}")
        A(">")
        A("> The prose above the table is genuine and is cited where relevant.")
        A("")

    A("## Ranked opportunities")
    A("")
    A("| # | Opportunity | $/month | Range | Hours/mo | Instances | Months | Cites | Conf |")
    A("|---:|---|---:|---|---:|---:|---:|---:|---|")
    counted = [o for o in opportunities if o.status == "counted"]
    for i, o in enumerate(counted, 1):
        d = o.bands
        A(f"| {i} | {o.title} | {_money(float(d['base'].dollars_per_month))} | "
          f"{_money(float(d['low'].dollars_per_month))}–"
          f"{_money(float(d['high'].dollars_per_month))} | "
          f"{float(d['base'].automatable_hours_per_month):.1f} | "
          f"{o.measured.instances} | {len(o.months)} | {len(o.citations)} | "
          f"{o.confidence} |")
    A("")

    nc = summary["not_counted"]
    if nc["low_confidence"]["count"] or nc["quarantined"]["count"]:
        A("### Not counted")
        A("")
        A(f"{nc['low_confidence']['count']} opportunities were demoted to low confidence "
          f"({_money(nc['low_confidence']['dollars_per_month_base'])}/month not included "
          f"in the headline) and {nc['quarantined']['count']} were quarantined for "
          f"insufficient evidence "
          f"({_money(nc['quarantined']['dollars_per_month_base'])}/month excluded). "
          f"See `out/quarantine.json`.")
        A("")

    A("---")
    A("")
    for i, o in enumerate(counted, 1):
        A(f"## {i}. {o.title}")
        A("")
        A(f"**{_money(float(o.bands['base'].dollars_per_month))}/month** "
          f"(range {_money(float(o.bands['low'].dollars_per_month))}–"
          f"{_money(float(o.bands['high'].dollars_per_month))}) · "
          f"{float(o.bands['base'].automatable_hours_per_month):.1f} automatable hours/month · "
          f"confidence {o.confidence}")
        A("")
        A(f"*Measured:* {o.measured.messages} messages in {o.measured.instances} task "
          f"instances, {o.measured.senders} sender(s), {len(o.person_ids)} people, "
          f"{len(o.months)} months. "
          + ", ".join(f"{k.replace('_signal','')} {v:.0%}"
                      for k, v in o.signal_rates.items() if v) + ".")
        A("")
        if o.narrative.get("what_happens"):
            A(f"**What happens.** {o.narrative['what_happens']}")
            A("")
        if o.narrative.get("where_it_stalls"):
            A(f"**Where it stalls.** {o.narrative['where_it_stalls']}")
            A("")
        if o.narrative.get("why_it_recurs"):
            A(f"**Why it recurs.** {o.narrative['why_it_recurs']}")
            A("")
        if o.narrative.get("automation_opportunity"):
            A(f"**What could absorb it.** {o.narrative['automation_opportunity']}")
            A("")
        if o.narrative.get("discovery_note"):
            A(f"*{o.narrative['discovery_note']}*")
            A("")

        A("**How the number was reached.**")
        A("")
        A("```")
        for step in o.bands["base"].derivation["steps"]:
            A(step)
        A("```")
        A("")
        A(f"Assumptions from `{o.bands['base'].derivation['assumption_source']}`.")
        A("")
        A("**Evidence.**")
        A("")
        for cit in o.citations:
            tier = "" if cit.match_tier == "raw_exact" else f" · {cit.match_tier}"
            A(f"- \"{cit.quote.strip()}\"")
            A(f"  — `{cit.source_path}` bytes {cit.raw_start}–{cit.raw_end}, "
              f"lines {cit.line_start}–{cit.line_end}{tier}")
            A(f"    ```")
            A(f"    {cit.to_dict()['check_commands']['sed']}")
            A(f"    ```")
        A("")

    if artifacts:
        A("---")
        A("")
        A("## Drafted artifacts")
        A("")
        A("Ready to use on Monday morning. Every sentence asserting current practice "
          "carries a citation marker that resolves to verified evidence; recommendations "
          "carry no marker and sit under their own heading, so observation and proposal "
          "never blur.")
        A("")
        for a in artifacts:
            A(f"- **{a.get('title')}** (`{a.get('filename')}`) — {a.get('artifact_type')}, "
              f"for *{a.get('opportunity_title', a.get('opportunity_id'))}*")
        A("")

    A("---")
    A("")
    A("## How to check any of this")
    A("")
    A("```")
    A("make verify     # re-anchor every citation from scratch; recompute every number")
    A("make test       # full suite, zero model calls")
    A("make serve      # dashboard with click-through to the highlighted bytes")
    A("```")
    A("")
    A("Every citation above prints the `sed` command that reproduces it. `docs/AUDIT.md` "
      "holds 25 randomly sampled citations with both `dd` and `sed` commands.")
    A("")
    A("Where this is most likely wrong, and what it took on faith, is in `NOTES.md`.")
    A("")
    return "\n".join(L)