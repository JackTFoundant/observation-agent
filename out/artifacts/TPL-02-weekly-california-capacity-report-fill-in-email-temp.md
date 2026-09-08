---
artifact_id: TPL-02
title: "Weekly California Capacity Report \u2014 fill-in email template"
artifact_type: template
opportunity_id: proc_697cde74c9
opportunity_title: Weekly California Capacity Report, assembled and mailed by hand
generated_at: '2026-09-08T21:33:08.380662+00:00'
generator: claude -p via .claude/agents/artifact-drafter.md
review_status: draft-unreviewed
evidence:
- cit_3104fe6a8620
- cit_5413519d0047
- cit_778703228f63
- cit_848a234a06fb
- cit_88fbca232748
- cit_c772a2736ae1
- cit_e142f4dedf42
- cit_feeabdbb4ec3
below_threshold_judgment_call: false
---

> **Draft, not reviewed.** Every sentence describing current practice carries a
> citation id that resolves to a verified quote from the archive. Sentences under
> *Recommended change* are proposals and carry no citation. Nobody who does this
> work has read this document.

## Purpose

Give the Transwestern commercial desk a fixed, fill-in template for the weekly California Capacity Report, so the same numbers land in the same places every week and the effective-week header is derived rather than retyped.

## Scope

Covers the weekly California capacity email sent from the Transwestern commercial side to the standing distribution list: average Transwestern deliveries to California, San Juan lateral throughput, El Paso deliveries by delivery point, and posted Gas Daily prices. Does not cover nomination cutoffs, OBA imbalance settlement, or capacity release notices.

## Current practice

The report is a plain email body, not an attachment, and its first line states average Transwestern deliveries to California together with San Juan lateral throughput in a single sentence [cit_778703228f63]. That opening sentence repeats week to week with only the figures changing [cit_e142f4dedf42]. The same opening appears again months later in the same form [cit_88fbca232748]. In some weeks the deliveries figure is given without the San Juan lateral throughput on the same line [cit_848a234a06fb]. Other weeks follow that shorter form as well [cit_5413519d0047]. The pattern holds into March [cit_3104fe6a8620]. El Paso deliveries follow, introduced by their own averaged line and then broken out by delivery point [cit_c772a2736ae1]. The figures are typed into the mail body as literal text, so a header field that is wrong goes out wrong and is corrected by a follow-up mail: "Sorry, the effective date for this new report is 01/07-01/11" [cit_feeabdbb4ec3].

## Template

Fill every `{{merge_field}}`. The parenthesised comparison figure carried after each deliveries volume is part of the existing wording [cit_778703228f63]; supply it with its sign included in the merge value. Where a week has no San Juan lateral figure, use the short variant of line 1, which is also existing practice [cit_848a234a06fb].

```
To: {{standing_distribution_list}}
Subject: California Capacity Report for Week of {{week_start_mm_dd}}-{{week_end_mm_dd}}

Transwestern's average deliveries to California were {{tw_avg_deliveries}} MMBtu/d
({{tw_comparison_figure}}), with San Juan lateral throughput at
{{san_juan_lateral_throughput}} MMBtu/d.

[short variant, weeks with no lateral figure:]
Transwestern's average deliveries to California were {{tw_avg_deliveries}} MMBtu/d
({{tw_comparison_figure}}).

El Paso's average deliveries to California were {{ep_avg_deliveries}} MMBtu/d
({{ep_comparison_figure}}):

    {{ep_point_1_name}}          {{ep_point_1_volume}} MMBtu/d
    {{ep_point_2_name}}          {{ep_point_2_volume}} MMBtu/d
    {{ep_point_3_name}}          {{ep_point_3_volume}} MMBtu/d
    ({{repeat_per_delivery_point}})

Posted Gas Daily prices:

    {{price_point_1_name}}       {{price_point_1_value}}
    {{price_point_2_name}}       {{price_point_2_value}}
    ({{repeat_per_price_point}})

Source: {{source_spreadsheet_reference}} <to be confirmed>
Pipeline postings as of {{posting_date}} <to be confirmed>
```

Fill order, matching the order the figures appear in the sent body:

1. Set `{{week_start_mm_dd}}` and `{{week_end_mm_dd}}` from the run date, not from the previous week's mail; the effective week is the field that has been corrected after the fact [cit_feeabdbb4ec3].
2. Enter Transwestern average deliveries and, where available, San Juan lateral throughput [cit_778703228f63].
3. Enter El Paso average deliveries, then the per-point breakout beneath it [cit_c772a2736ae1].
4. Enter posted Gas Daily prices from the pipeline posting source `<to be confirmed>`.
5. Re-read the subject line against the body dates before sending, then send to the standing list [cit_feeabdbb4ec3].

## Recommended change

Build a scheduled job that renders this template. It should read the Transwestern deliveries and San Juan lateral throughput, the El Paso per-point deliveries, and the posted Gas Daily prices from their existing sources, derive `week_start` and `week_end` from the run date, and produce a draft addressed to the standing list. The sender then reviews and releases it rather than assembling it.

Make the week range a computed field everywhere it appears — subject line and body — so a single wrong entry cannot survive into a sent mail and force a correction.

Keep the two line-1 variants in the renderer: emit the long form when a San Juan lateral figure is present and the short form when it is not, so the job never invents a number to fill the slot.

Name a second person on the desk who can run the job and release the draft, and record the source locations in the job configuration rather than in one person's habit.

Store each week's rendered body so the following week's figures can be diffed against the last send before release.

## Open questions

- Which spreadsheet, and which sheet or cell range, supplies the Transwestern and El Paso delivery figures.
- Which pipeline website page the posted Gas Daily prices are taken from, and at what point in the week that page is considered final.
- The full membership of the standing distribution list.
- The day of the week and the time the report is expected to go out.
- What the parenthesised comparison figure after each deliveries volume is measured against — design capacity, the prior week, or something else.
- The complete, fixed list of El Paso delivery points and price points, and whether that list ever changes between weeks.
- Whether a correction is expected to restate the whole report or only the corrected field.
