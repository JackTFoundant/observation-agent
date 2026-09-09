---
artifact_id: EML-02
title: "Weekly California Capacity Report \u2014 standing cover email (draft)"
artifact_type: email
opportunity_id: ser_4d4f0b156e
opportunity_title: '"California Capacity Report for Week of 01/14-01/18" produced
  weekly'
generated_at: '2026-09-09T19:21:26.111827+00:00'
generator: claude -p via .claude/agents/artifact-drafter.md
review_status: draft-unreviewed
evidence:
- cit_281cdb8ece7c
- cit_6e2d9c893a5d
- cit_73c45be674b7
- cit_7e9d6a9437c9
- cit_97236985661c
- cit_c955cf19fffb
- cit_e04d7226f87c
- cit_e474f470ba47
below_threshold_judgment_call: false
---

> **Draft, not reviewed.** Every sentence describing current practice carries a
> citation id that resolves to a verified quote from the archive. Sentences under
> *Recommended change* are proposals and carry no citation. Nobody who does this
> work has read this document.

## Purpose

Give the Transwestern commercial desk a fixed cover email for the weekly California Capacity Report, so the subject line, the distribution list, and the send day stay the same from week to week and the report can later be assembled and sent by a scheduled job.

## Scope

Covers the weekly California Capacity Report only: the subject line format, the standing recipients, and the send timing. Does not cover the underlying deliveries and price data, how it is sourced, or any other Transwestern report.

## Current practice

The report is issued as an email whose subject is `California Capacity Report for Week of MM/DD-MM/DD`, naming the first and last day of the week being reported [cit_6e2d9c893a5d]. It is sent from one sender, michelle.lokay@enron.com [cit_97236985661c]. It repeats week after week without a break in the numbering of weeks: `12/10-12/14` [cit_c955cf19fffb], then `12/17-12/21` [cit_e474f470ba47], then `12/26-12/28` [cit_7e9d6a9437c9], then `12/31-01/04` [cit_73c45be674b7]. Holiday weeks keep the same subject format but carry the shortened date range of the working week, as in `12/26-12/28` [cit_7e9d6a9437c9]. The report normally goes out on the last working day of the week it covers; the `01/28-02/01` report was sent on 2002-02-01 [cit_e04d7226f87c] and the `01/14-01/18` report on 2002-01-18 [cit_6e2d9c893a5d]. The send can move earlier in the week when needed: the `01/21-01/25` report was sent on 2002-01-24 [cit_281cdb8ece7c]. The series is visible in both the sender's `sent_items` folder [cit_c955cf19fffb] and in her `inbox` [cit_97236985661c], which indicates she is on the distribution list herself.

## Template

Use this as the standing cover email. The subject line follows the format already in use [cit_6e2d9c893a5d]. The body content below is a placeholder skeleton: the archive preserved the subject lines of this series but not the bodies [cit_e04d7226f87c], so every content block is marked for confirmation against a recent live copy before this template is adopted.

```
To:      {{standing_distribution_list}}
From:    {{report_owner}}
Subject: California Capacity Report for Week of {{week_start_mm_dd}}-{{week_end_mm_dd}}

Attached is the California Capacity Report for the week of
{{week_start_mm_dd}}-{{week_end_mm_dd}}.

Transwestern deliveries:            <to be confirmed — section order and units>
{{transwestern_deliveries}}

El Paso deliveries by point:        <to be confirmed — point list>
{{el_paso_deliveries_by_point}}

Posted Gas Daily prices:            <to be confirmed — which postings, which day>
{{gas_daily_prices}}

Notes for the week:
{{weekly_notes}}

{{report_owner}}
{{report_owner_phone}}
```

Merge fields to be populated per week: `{{week_start_mm_dd}}`, `{{week_end_mm_dd}}`, `{{transwestern_deliveries}}`, `{{el_paso_deliveries_by_point}}`, `{{gas_daily_prices}}`, `{{weekly_notes}}`. Fields populated once and then held constant: `{{standing_distribution_list}}`, `{{report_owner}}`, `{{report_owner_phone}}`.

## Recommended change

1. Freeze the distribution list in one place — a mail group or a distribution list object — rather than re-addressing the message each week. Name the group after the report so a change of owner does not change who receives it.
2. Name a standing backup sender. Today the series depends on a single mailbox; the backup should have the same list, the same template, and access to the source data.
3. Set the default send for the last working day of the reported week, and treat an earlier send as an exception the owner chooses, not as a variation in the template.
4. Define the holiday-week rule explicitly: the subject carries the actual working-day range of that week, so short weeks need no separate approval or naming decision.
5. Once the section list is confirmed against a live copy, build a scheduled job that pulls the Transwestern delivery figures, the El Paso delivery figures by point, and the posted Gas Daily prices into this template, and queues the message for the owner to review and release. Keep a human release step until the assembled figures have matched the hand-built report for several consecutive weeks.
6. Archive each sent report to a shared folder rather than relying on the sender's mailbox, so the prior week's figures are available to whoever covers.

## Open questions

- The report bodies are not in the archive, so the actual section headings, the order of sections, the units, and the wording of the covering sentence are unknown. Confirm against the most recent sent copy before adopting this template.
- The exact membership of the standing distribution list is not established here; `{{standing_distribution_list}}` must be filled from a live copy.
- Whether the report travels as an attachment or inline in the body is not established.
- The sources feeding the Transwestern and El Paso delivery figures, and which Gas Daily posting is quoted, are not identified in the archive.
- Whether any recipient acknowledges or acts on the report on a deadline is not visible from the headers alone.
- The named backup sender and the escalation path when the owner is out are not recorded.
