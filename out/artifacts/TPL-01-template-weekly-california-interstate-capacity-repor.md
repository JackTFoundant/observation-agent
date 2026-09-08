---
artifact_id: TPL-01
title: 'Template: Weekly California Interstate Capacity Report'
artifact_type: template
opportunity_id: proc_a58e286bd5
opportunity_title: Weekly California Capacity Report, assembled and mailed by hand
generated_at: '2026-09-08T19:58:53.819184+00:00'
generator: claude -p via .claude/agents/artifact-drafter.md
review_status: draft-unreviewed
evidence:
- cit_45a6c764f509
- cit_646d6e14a0ad
- cit_7959cb571714
- cit_88fbca232748
- cit_c772a2736ae1
- cit_cd0f539df211
- cit_e142f4dedf42
- cit_feeabdbb4ec3
below_threshold_judgment_call: true
---

> **Draft, not reviewed.** Every sentence describing current practice carries a
> citation id that resolves to a verified quote from the archive. Sentences under
> *Recommended change* are proposals and carry no citation. Nobody who does this
> work has read this document.

## Purpose

Give the Transwestern commercial desk a fixed, fill-in template for the weekly California Interstate Capacity Report, so the mail body is assembled the same way every issue and the effective-date line is derived rather than typed from memory.

## Scope

Covers the weekly capacity report mailed from the Transwestern commercial side to its standing distribution list: Transwestern deliveries to California against capacity, San Juan lateral throughput, El Paso deliveries by delivery point, and posted Gas Daily prices. Does not cover nominations, OBA imbalance settlement, or capacity release.

## Current practice

The report is issued as text in the mail body, opening with a single line giving average Transwestern deliveries to California against capacity together with San Juan lateral throughput [cit_45a6c764f509]. That same line appears with the same wording and the same two figures in issue after issue, with only the values changing [cit_7959cb571714]. It recurs unchanged across later issues as well [cit_e142f4dedf42], [cit_646d6e14a0ad]. It continues in the same form in the most recent issues in the archive [cit_88fbca232748]. El Paso deliveries to California are stated on their own line, against capacity, and introduced with a colon that opens the breakout by delivery point [cit_c772a2736ae1]. The reporting period is stated in the mail as an effective date range, and at least one issue went out with the wrong range and was corrected by a follow-up mail [cit_feeabdbb4ec3]. Ownership of the report has changed hands at least once, announced by the outgoing sender as their last California Interstate Capacity Report, after which the report continued from a new sender [cit_cd0f539df211].

## Template

Fill every `{{merge_field}}`. Fields marked `<to be confirmed>` are structural gaps listed under Open questions.

```
To: {{standing_distribution_list}}
Subject: California Capacity Report for Week of {{week_start_mmdd}}-{{week_end_mmdd}}

Effective date for this report is {{week_start_mmdd}}-{{week_end_mmdd}}.

Transwestern's average deliveries to California were {{tw_avg_deliveries}} MMBtu/d
({{tw_percent_of_capacity}}), with San Juan lateral throughput at
{{san_juan_lateral_throughput}} MMBtu/d.

El Paso's average deliveries to California were {{ep_avg_deliveries}} MMBtu/d
({{ep_percent_of_capacity}}):

    {{ep_point_1_name}}          {{ep_point_1_volume}} MMBtu/d
    {{ep_point_2_name}}          {{ep_point_2_volume}} MMBtu/d
    {{ep_point_3_name}}          {{ep_point_3_volume}} MMBtu/d
    {{additional_ep_points}}

Posted Gas Daily prices:

    {{price_point_1_name}}       {{price_point_1_posted}}
    {{price_point_2_name}}       {{price_point_2_posted}}
    {{additional_price_points}}

{{sender_name_and_role}}
```

Fill order and source per field:

1. Set `{{week_start_mmdd}}` and `{{week_end_mmdd}}` from the reporting week, then copy the same values into the subject line and the effective-date line so the two cannot disagree; a mismatch here is the error the archive shows being corrected after issue [cit_feeabdbb4ec3].
2. Enter `{{tw_avg_deliveries}}`, `{{tw_percent_of_capacity}}` and `{{san_juan_lateral_throughput}}` into the single Transwestern line, keeping the wording as issued [cit_45a6c764f509].
3. Enter `{{ep_avg_deliveries}}` and `{{ep_percent_of_capacity}}`, then list each El Paso delivery point under the colon [cit_c772a2736ae1].
4. Enter the posted Gas Daily price rows from `<to be confirmed: source of record for posted prices>`.
5. Mail to the standing distribution list held at `<to be confirmed: where the list is maintained>`; the issue closes when the mail goes out, and no approval step is visible in the archive [cit_45a6c764f509].

## Recommended change

Move the figures out of manual transcription and into a scheduled job. The job should read Transwestern average deliveries and capacity, San Juan lateral throughput, El Paso deliveries by delivery point, and posted Gas Daily prices from their systems of record, render them into the template above, and hold the result as a draft for the desk to review before release.

Derive the week's date range from the run date and write it once into both the subject and the effective-date line. This removes the only error class the archive shows for this report.

Keep the wording of the Transwestern and El Paso lines exactly as issued today. Recipients read this report by shape; changing the sentence structure costs more than it gains.

Store the distribution list in one place referenced by the job, not in a mail client's autocomplete. Record the report owner alongside it, so a handover changes one field rather than relying on the outgoing sender to announce it.

Where a source of record does not exist for a field, flag that field in the draft rather than leaving it blank, so the reviewer knows the difference between a zero and an unavailable figure.

## Open questions

- Which system or spreadsheet is the source of record for Transwestern average deliveries, the capacity denominator, and San Juan lateral throughput. Not determinable from the archive.
- Which source supplies El Paso deliveries by delivery point, and whether the point list is fixed or varies by week.
- Where posted Gas Daily prices are taken from, and which price points belong in the report.
- The day of week and time the report is expected to go out. No deadline signal appears in the archive.
- The membership of the standing distribution list and who maintains it.
- Whether any review or approval was ever expected before issue, and who performs it now that ownership has changed [cit_cd0f539df211].
