---
artifact_id: TPL-03
title: 'Template: Weekly California Interstate Capacity Report'
artifact_type: template
opportunity_id: proc_a58e286bd5
opportunity_title: Weekly California Capacity Report, assembled and mailed by hand
generated_at: '2026-09-09T14:58:30.388462+00:00'
generator: claude -p via .claude/agents/artifact-drafter.md
review_status: draft-unreviewed
evidence:
- cit_271b60ab36fa
- cit_710d7ff06e9b
- cit_7959cb571714
- cit_88fbca232748
- cit_ab9106256865
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

Give the Transwestern commercial analyst who holds the California Interstate Capacity Report a fixed template to fill each week, so the layout stops being rebuilt from memory and the week label stops being typed free-hand.

## Scope

Covers the weekly California Interstate Capacity Report: the subject line, the body blocks, and the merge fields each block needs. Covers the correction mail sent when the week label goes out wrong. Does not cover where the underlying delivery volumes or posted prices are sourced from — that is not visible in the archive and is listed under open questions.

## Current practice

The report is mailed weekly with the week range carried in the subject line [cit_ab9106256865]. Later editions use the same subject form with only the date range changed [cit_710d7ff06e9b]. The body opens with Transwestern's average deliveries to California, a percent-of-capacity figure in parentheses, and San Juan lateral throughput on the same line [cit_7959cb571714]. That opening line keeps the same wording and the same order of figures in later editions [cit_271b60ab36fa]. It is still in the same shape months later [cit_88fbca232748]. El Paso's average deliveries to California follow, with their own percent-of-capacity figure, and a colon introducing a breakout by delivery point [cit_c772a2736ae1]. The week label is set by hand and has gone out wrong, requiring a second mail to the whole distribution list to restate the effective date [cit_feeabdbb4ec3]. The report is a role, not a person: one sender announced a final edition and the cadence continued under another [cit_cd0f539df211].

## Template

Subject line, using the same form as the current editions [cit_ab9106256865]:

```
Subject: California Capacity Report for Week of {{week_start_mm_dd}}-{{week_end_mm_dd}}
To: {{standing_distribution_list}}

Transwestern's average deliveries to California were {{tw_avg_deliveries}} MMBtu/d
({{tw_pct_of_capacity}}), with San Juan lateral throughput at {{san_juan_throughput}} MMBtu/d.

El Paso's average deliveries to California were {{ep_avg_deliveries}} MMBtu/d
({{ep_pct_of_capacity}}):

  {{ep_delivery_point_1}}     {{ep_volume_1}} MMBtu/d
  {{ep_delivery_point_2}}     {{ep_volume_2}} MMBtu/d
  {{ep_delivery_point_n}}     {{ep_volume_n}} MMBtu/d
  <to be confirmed: fixed list and order of El Paso delivery points>

Posted Gas Daily prices:
  <to be confirmed: point names, price field, and layout of this block>

{{sender_name}}
{{sender_role}}
```

Correction mail, to be used only when an edition has already gone out with the wrong week label [cit_feeabdbb4ec3]:

```
Subject: RE: California Capacity Report for Week of {{wrong_week_range}}
To: {{standing_distribution_list}}

Sorry, the effective date for this report is {{correct_week_start_mm_dd}}-{{correct_week_end_mm_dd}}.
```

Handover note, to be used when the role passes to another analyst [cit_cd0f539df211]:

```
Subject: California Capacity Report for Week of {{week_start_mm_dd}}-{{week_end_mm_dd}}
To: {{standing_distribution_list}}

Below is my last California Interstate Capacity Report. From
{{next_edition_week_range}} it will be sent by {{incoming_owner_role}}.

{{report_body}}
```

## Recommended change

Derive the week range in the subject line and the effective-date text from the run date rather than typing it. This is the one error the archive actually shows, and it is the cheapest to remove.

Hold the standing distribution list in one place — a mail alias or a distribution group — so the report body and any correction mail always address the same recipients.

Fix the El Paso delivery-point block as an ordered list in the template, so points appear in the same order every week and a missing point is visible as a blank rather than as a silently shorter list.

Move the report to a scheduled job that reads the Transwestern and El Paso delivery volumes and the posted Gas Daily prices, renders them into this template, and mails the alias. Lift the layout from a recent edition rather than redesigning it; the point is that recipients should not notice a change.

Keep the rendered body inline in the mail. If a spreadsheet is also produced, attach it as a supplement, not as the report itself.

Name a backup owner for the role in the same place the distribution list lives, so a handover is a configuration change rather than a mail announcing one.

## Open questions

- Where each block of figures is sourced from: the system or report behind Transwestern average deliveries, San Juan lateral throughput, El Paso deliveries by point, and posted Gas Daily prices is not visible in the mail.
- How the percent-of-capacity figures are computed, and against which capacity basis.
- The full fixed list of El Paso delivery points and their intended order.
- The exact layout of the posted Gas Daily price block, including which points and which price field are quoted.
- The membership of the standing distribution list, and whether it changed across the handover.
- Which day of the week the edition is sent, and whether the week range in the subject is the week just completed or the week ahead.
- Whether a spreadsheet is a required companion to the mail or an occasional working artefact.
