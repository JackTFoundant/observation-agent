---
artifact_id: EML-02
title: "Weekly California Capacity Report \u2014 standing email template and send\
  \ procedure"
artifact_type: email
opportunity_id: ser_4d4f0b156e
opportunity_title: '"California Capacity Report for Week of 01/14-01/18" produced
  weekly'
generated_at: '2026-09-08T20:58:42.795986+00:00'
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

Give the person who owns the weekly California Capacity Report a fixed email template and a repeatable send procedure, so the report goes to the standing distribution list on the same cadence without being rebuilt from memory each week.

## Scope

Covers the recurring email whose subject is `California Capacity Report for Week of MM/DD-MM/DD`, sent from the Transwestern commercial mailbox to its standing list. Covers the subject-line convention, the send cadence, and the fields the message carries. Does not cover the upstream sources the figures are pulled from, and does not cover ad-hoc capacity questions that arrive as replies.

## Current practice

The report is issued as an email whose subject is `California Capacity Report for Week of` followed by a date range [cit_6e2d9c893a5d]. It is produced and sent by one person from a single mailbox [cit_c955cf19fffb]. The date range in the subject is written as the week's start and end dates separated by a hyphen, in `MM/DD-MM/DD` form [cit_281cdb8ece7c].

The cadence is weekly and the send lands at the end of the work week [cit_e474f470ba47]. Consecutive weeks appear as consecutive subject ranges: `12/10-12/14`, then `12/17-12/21` [cit_c955cf19fffb] [cit_e474f470ba47]. A holiday-shortened week is labelled with the shortened range rather than the full Monday-to-Friday span, as in `12/26-12/28` [cit_7e9d6a9437c9]. A week that crosses a month boundary carries both months in the subject, as in `12/31-01/04` and `01/28-02/01` [cit_73c45be674b7] [cit_e04d7226f87c].

The send time within the day is not fixed; instances appear in the morning and around midday [cit_281cdb8ece7c] [cit_6e2d9c893a5d]. At least one issue of the report also lands back in the sender's own inbox folder, meaning the sender is on the receiving side of the same distribution [cit_97236985661c].

## Template

Use the block below. Replace every `{{merge_field}}`. The subject line format and the weekly cadence match what the archive shows today [cit_6e2d9c893a5d] [cit_e474f470ba47]; the body headings below are a proposal, because the archive preserves the subject lines but not the message bodies.

```
To:      {{standing_distribution_list}}
From:    {{report_owner_mailbox}}
Subject: California Capacity Report for Week of {{week_start_MMDD}}-{{week_end_MMDD}}

Attached / below is the California Capacity Report for the week of
{{week_start_MMDD}}-{{week_end_MMDD}}.

Transwestern deliveries
{{transwestern_deliveries_table}}

El Paso deliveries by point
{{el_paso_deliveries_by_point_table}}

Posted Gas Daily prices
{{gas_daily_posted_prices_table}}

Notes and exceptions this week
{{notes_and_exceptions}}

Source cut-off for the figures above: {{source_cutoff}}   <to be confirmed>
Questions on the numbers: reply to this message.

{{report_owner_name_and_role}}
```

Rules for filling the subject line:

1. Use the first and last working day of the week actually covered, not the calendar Monday and Friday, when the week is shortened by a holiday [cit_7e9d6a9437c9].
2. Keep both months visible when the week spans a month end [cit_73c45be674b7] [cit_e04d7226f87c].
3. Do not add a year, a revision number, or a prefix — the subject is the series key that recipients filter on [cit_6e2d9c893a5d].
4. Send to the standing list unchanged; the owner is also a recipient of the series [cit_97236985661c].
5. Send at the end of the work week [cit_e04d7226f87c].

## Recommended change

Move the assembly to a scheduled job. The job builds the three tables from their sources, writes them into the template above, fills the subject line from the week's working-day range, and sends to the standing list on the same weekly cadence. A human reviews and releases it rather than typing it.

Fix the send slot. Pick one time on the last working day of the week and hold it, so recipients know when to expect the message and can tell "late" from "not coming".

Make the shortened-week and month-crossing rules the job's logic, not the sender's judgement. The job should derive the range from a working-day calendar and flag any week where it had to shorten the range, so the reviewer can confirm the label before release.

Store the standing distribution list in one place the job reads, rather than in the sender's address book. Add a named backup releaser so the report still goes out when the owner is away.

Keep the assembled figures for each week in a file named after the same subject-line range. That gives a week-over-week trail without needing to reopen sent mail.

## Open questions

- The message bodies are not available in the archive, so the exact tables, column headings, units, and order of sections in the current report cannot be read off it. The `## Template` body headings above are a proposal and need to be checked against a real recent issue.
- The seven recipients on the standing list are not identifiable from the material reviewed. The list needs to be confirmed from a recent sent copy before the job is pointed at it.
- Whether the report travels as an attachment, inline text, or both is not established.
- The upstream sources for each table, and the cut-off after which figures are frozen for the week, are not established — marked `<to be confirmed>` in the template.
- Whether anyone acknowledges or replies to the report, and whether replies require follow-up work, cannot be determined from the material reviewed.
- Whether the report was suspended or handed to another owner at any point in the series is not established.
