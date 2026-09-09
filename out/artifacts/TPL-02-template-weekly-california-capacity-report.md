---
artifact_id: TPL-02
title: 'Template: Weekly California Capacity Report'
artifact_type: template
opportunity_id: proc_a58e286bd5
opportunity_title: Weekly California Capacity Report, assembled and mailed by hand
generated_at: '2026-09-09T15:14:10.180743+00:00'
generator: claude -p via .claude/agents/artifact-drafter.md
review_status: draft-unreviewed
evidence:
- cit_45a6c764f509
- cit_5f7261c0f77a
- cit_88fbca232748
- cit_c772a2736ae1
- cit_d6681d88e310
- cit_e2066f723f8d
- cit_f22673c230de
- cit_feeabdbb4ec3
below_threshold_judgment_call: false
---

> **Draft, not reviewed.** Every sentence describing current practice carries a
> citation id that resolves to a verified quote from the archive. Sentences under
> *Recommended change* are proposals and carry no citation. Nobody who does this
> work has read this document.

## Purpose

Give the Transwestern commercial analyst a fixed, fill-in template for the weekly California Capacity Report, so the wording and the effective-date line stop being retyped from scratch each cycle.

## Scope

Covers the weekly capacity summary mailed to the standing distribution list: Transwestern average deliveries to California against capacity, San Juan lateral throughput, El Paso deliveries by delivery point, and posted Gas Daily prices. Covers the effective-date line and the handoff copy sent when the author changes. Does not cover OBA imbalance work, capacity release, or any other Transwestern reporting.

## Current practice

The report is prose in the body of an email, not an attachment [cit_88fbca232748]. The opening sentence states Transwestern's average deliveries to California against capacity, followed by San Juan lateral throughput [cit_88fbca232748]. That sentence recurs week to week with only the figures changed [cit_5f7261c0f77a]. The same wording appears again in later weeks with new figures [cit_45a6c764f509]. In some weeks the sentence carries the delivery figure and capacity percentage without a lateral throughput clause [cit_f22673c230de]. El Paso deliveries are stated the same way — an average against capacity — and the sentence ends in a colon introducing a breakout by delivery point [cit_c772a2736ae1]. The delivery and throughput figures are keyed into the sentence itself rather than carried in a linked table [cit_d6681d88e310].

The report week is stated as an effective date range in the mail [cit_feeabdbb4ec3]. Because that line is written by hand alongside the figures, it can be wrong: a separate follow-up mail was sent to restate the effective date for a report already distributed [cit_feeabdbb4ec3]. When the series changes hands, the outgoing author pastes their last California Interstate Capacity Report into the body of a mail to the incoming author [cit_e2066f723f8d].

## Template

Fill only the `{{merge_field}}` values. Do not reword the sentences — the recipients read the same structure every week.

```
Subject: California Capacity Report for Week of {{week_start}}-{{week_end}}

To: {{standing_distribution_list}}

The effective date for this report is {{week_start}}-{{week_end}}.

Transwestern's average deliveries to California were {{tw_avg_deliveries}} MMBtu/d
({{tw_pct_of_capacity}}), with San Juan lateral throughput at
{{san_juan_lateral_throughput}} MMBtu/d.

El Paso's average deliveries to California were {{ep_avg_deliveries}} MMBtu/d
({{ep_pct_of_capacity}}):

  {{ep_delivery_point_name}}      {{ep_delivery_point_volume}} MMBtu/d
  (repeat one line per delivery point, in the order used last week)

Posted Gas Daily prices:

  {{gas_daily_point_name}}        {{gas_daily_price}} {{price_unit}}
  (repeat one line per posted point)

{{analyst_name}}
{{analyst_title}}
```

Notes for the person filling it in:

1. Set `{{week_start}}` and `{{week_end}}` first, and copy the same two values into the subject line and the effective-date sentence so the two cannot disagree [cit_feeabdbb4ec3].
2. If a week has no San Juan lateral figure, drop the clause after the comma and end the sentence at the capacity percentage [cit_f22673c230de].
3. Keep the colon at the end of the El Paso sentence; the point-by-point lines follow it [cit_c772a2736ae1].
4. Source table or spreadsheet for each figure: `<to be confirmed>`.
5. Send day and send time: `<to be confirmed>`.
6. On handoff, send the last issued report in the body of a mail to the incoming author so the series wording carries over [cit_e2066f723f8d].

## Recommended change

Derive the effective-date range from the data window used to compute the figures, and write it into both the subject line and the effective-date sentence from that single value. The date-only correction disappears once the label is a function of the data rather than a separate keystroke.

Move the four figure groups — Transwestern deliveries and capacity, San Juan lateral throughput, El Paso deliveries by point, Gas Daily postings — into named cells or a query in one source, then have a scheduled job render this template from those values and mail it to the standing list. The analyst reviews a generated draft instead of retyping sentences.

Hold the El Paso delivery-point list and its order in the source, not in the analyst's memory of last week's mail. Store the standing distribution list with the job, so a change of author does not change the recipients.

Keep the report as body text. Recipients read it inline today, and an attachment would change how they consume it.

## Open questions

- The standing distribution list is not established from the messages cited here; confirm the exact addresses and who owns changes to it.
- The source of each figure — which spreadsheet, table, or system produces Transwestern deliveries, capacity, San Juan lateral throughput, El Paso point volumes, and the Gas Daily postings — is not identified in the cited messages.
- The full list of El Paso delivery points and their intended order is not fixed by the citations available.
- The exact format and unit of the posted Gas Daily price block is not shown; `{{price_unit}}` is marked `<to be confirmed>`.
- Whether the capacity percentage is against firm, design, or available capacity is not stated.
- The intended send day and cutoff for the week's figures are not visible.
- The relationship between the "California Capacity Report" title and the "California Interstate Capacity Report" name used in the handoff message is unclear [cit_e2066f723f8d]; confirm whether these are the same series.
