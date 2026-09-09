---
artifact_id: TPL-01
title: "Weekly California Capacity Report \u2014 standing email template"
artifact_type: template
opportunity_id: proc_a58e286bd5
opportunity_title: Weekly California Capacity Report, assembled and mailed by hand
generated_at: '2026-09-09T19:21:26.109950+00:00'
generator: claude -p via .claude/agents/artifact-drafter.md
review_status: draft-unreviewed
evidence:
- cit_45a6c764f509
- cit_5f7261c0f77a
- cit_646d6e14a0ad
- cit_7959cb571714
- cit_88fbca232748
- cit_c772a2736ae1
- cit_cd0f539df211
- cit_feeabdbb4ec3
below_threshold_judgment_call: false
---

> **Draft, not reviewed.** Every sentence describing current practice carries a
> citation id that resolves to a verified quote from the archive. Sentences under
> *Recommended change* are proposals and carry no citation. Nobody who does this
> work has read this document.

## Purpose

Give the Transwestern commercial analyst a fixed email template for the weekly California Capacity Report, so the same sections appear in the same order every week and the effective date range is written once rather than retyped from memory.

## Scope

Covers the weekly California Capacity Report mailed from the Transwestern commercial desk to its standing distribution list: Transwestern deliveries to California with San Juan lateral throughput, El Paso deliveries by delivery point, and posted Gas Daily prices. Does not cover the daily credit report, nomination traffic, or OBA imbalance settlement. Does not cover the retired predecessor series.

## Current practice

The report body opens with average Transwestern deliveries to California, stated against capacity, with San Juan lateral throughput on the same line [cit_88fbca232748]. That opening line is rewritten with new figures each week in the same sentence form [cit_7959cb571714]. The wording does not vary between editions, only the numbers [cit_5f7261c0f77a]. The same structure holds across consecutive weeks [cit_45a6c764f509], and again in the following edition [cit_646d6e14a0ad]. El Paso deliveries follow as a second block, stated against capacity and then broken out by delivery point [cit_c772a2736ae1]. The figures reach the reader as prose typed into the mail body, not as an attached or queryable dataset [cit_88fbca232748].

Corrections are issued as a separate follow-up mail that restates the effective date range of a report already distributed [cit_feeabdbb4ec3]. A related series, the California Interstate Capacity Report, was closed out by its sender with a final edition rather than handed over [cit_cd0f539df211].

## Template

Send as plain text. Fill every `{{merge_field}}`. Do not change the section order or the sentence wording — downstream readers scan for the same phrases each week.

```
To:      {{standing_distribution_list}}
Subject: California Capacity Report for Week of {{week_start_mm_dd}}-{{week_end_mm_dd}}

Transwestern's average deliveries to California were {{tw_avg_deliveries}} MMBtu/d
({{tw_pct_of_capacity}}), with San Juan lateral throughput at {{san_juan_throughput}} MMBtu/d.

El Paso's average deliveries to California were {{ep_avg_deliveries}} MMBtu/d
({{ep_pct_of_capacity}}):

  {{ep_delivery_point_1}}    {{ep_volume_1}} MMBtu/d
  {{ep_delivery_point_2}}    {{ep_volume_2}} MMBtu/d
  {{ep_delivery_point_3}}    {{ep_volume_3}} MMBtu/d
  <to be confirmed: full list of El Paso delivery points reported each week>

Posted Gas Daily prices:

  {{price_point_1}}    {{price_1}}
  {{price_point_2}}    {{price_2}}
  <to be confirmed: which Gas Daily price points are standing entries>

{{sender_name}}
{{sender_title}}
```

Correction template, to be used only when a distributed edition carried the wrong effective week:

```
To:      {{standing_distribution_list}}
Subject: RE: California Capacity Report for Week of {{as_sent_mm_dd}}-{{as_sent_mm_dd_end}}

Sorry, the effective date for this new report is {{correct_week_start}}-{{correct_week_end}}.
All figures in the report below are unchanged.
```

Fill rules that apply today:

1. `{{week_start_mm_dd}}` and `{{week_end_mm_dd}}` must match the period the volumes were drawn for; a mismatch here is what forces the correction mail [cit_feeabdbb4ec3].
2. `{{tw_avg_deliveries}}`, `{{tw_pct_of_capacity}}` and `{{san_juan_throughput}}` are the three values on the Transwestern line [cit_88fbca232748].
3. `{{ep_avg_deliveries}}` and `{{ep_pct_of_capacity}}` head the El Paso block, and the delivery-point rows sit under it [cit_c772a2736ae1].
4. Source spreadsheet and cell references for each field: `<to be confirmed>`.
5. Send day and send time: `<to be confirmed>`.

## Recommended change

Move the merge fields off the keyboard and onto a scheduled job. The job should read Transwestern throughput and San Juan lateral throughput from the volume accounting source, read El Paso deliveries by point from the same source, pull posted Gas Daily prices from the price feed, render this template, and mail it to the standing list.

Derive `{{week_start_mm_dd}}` and `{{week_end_mm_dd}}` from the run date rather than from typed input. That removes the only defect class the archive actually shows, and it removes the need for the correction template.

Write the rendered figures to a table as well as to the mail body, keyed by week and delivery point, so a reader who wants a trend does not have to reopen old mail.

Name a second person who can run the job and who is on the standing list, so the series does not depend on one sender continuing to send it. Record the distribution list in the job configuration, not in a mail client's address history.

Until the job exists, keep this template as a saved draft in the mail client and edit only the merge fields.

## Open questions

- The full standing list of El Paso delivery points reported each week is not visible in the archive; the template marks it `<to be confirmed>`.
- Which Gas Daily price points are standing entries, and where they are read from, is not visible.
- The source spreadsheet, its location, and the cells behind each figure are not identified.
- The nominal capacity denominator used for the against-capacity figures on both the Transwestern and El Paso lines is not stated.
- The send day and cutoff time for the weekly edition are not stated anywhere in the archive.
- Membership of the standing distribution list is not enumerated in the messages reviewed.
- Whether the retired California Interstate Capacity Report content was folded into this report or simply dropped is not determinable [cit_cd0f539df211].
