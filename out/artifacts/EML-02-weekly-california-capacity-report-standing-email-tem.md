---
artifact_id: EML-02
title: "Weekly California Capacity Report \u2014 standing email template and handover\
  \ notes"
artifact_type: email
opportunity_id: ser_4d4f0b156e
opportunity_title: '"California Capacity Report for Week of 01/14-01/18" produced
  weekly'
generated_at: '2026-09-09T14:58:30.390307+00:00'
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

Give the owner of the weekly California Capacity Report a reusable email template and a written record of how the report is currently issued, so the send can be handed to another person or to a scheduled job without reconstructing it from the mailbox.

## Scope

Covers the weekly email whose subject is `California Capacity Report for Week of MM/DD-MM/DD`, as sent from the Transwestern commercial mailbox. Covers the subject convention, the send cadence, and the standing distribution. Does not cover the OBA imbalance and capacity-release traffic handled by the same mailbox, and does not cover the internal sources the figures are drawn from, because the archive does not show them.

## Current practice

The report goes out as an email whose subject carries the covered week as a date range, in the form `California Capacity Report for Week of MM/DD-MM/DD` [cit_6e2d9c893a5d]. One sender issues it; the same mailbox appears on every instance in the archive [cit_c955cf19fffb]. The distribution is a standing list of seven recipients rather than a list rebuilt each week [cit_281cdb8ece7c].

The send repeats on a weekly cadence, with consecutive week ranges following one another without a gap: `12/10-12/14` [cit_c955cf19fffb], then `12/17-12/21` [cit_e474f470ba47], then `12/26-12/28` [cit_7e9d6a9437c9], then `12/31-01/04` [cit_73c45be674b7]. The range in the subject is trimmed to the working days actually covered when a holiday shortens the week, as in `12/26-12/28` [cit_7e9d6a9437c9]. Ranges that cross a month or a year boundary are written across the boundary rather than split, as in `12/31-01/04` [cit_73c45be674b7] and `01/28-02/01` [cit_e04d7226f87c].

The send lands at the end of the week it reports on, and the send time within that day is not fixed: one instance is timestamped in the morning [cit_281cdb8ece7c] and another the same week of the month in the afternoon [cit_6e2d9c893a5d]. At least one instance is also present in the sender's own inbox, indicating the sender is on the distribution as well as originating it [cit_97236985661c].

The archive holds the headers for these sends but not the message bodies, so the figures the report carries and the sources they were assembled from cannot be read out of the corpus [cit_e04d7226f87c].

## Template

Use this as the standing weekly send. Merge fields are filled from the report source sheet. Sections marked `<to be confirmed>` need the current body format checked against a recent live send before this template is used unedited.

```
To: {{standing_distribution_list}}
From: {{report_owner_mailbox}}
Subject: California Capacity Report for Week of {{week_start_MM/DD}}-{{week_end_MM/DD}}

Attached / below is the California Capacity Report for the week of
{{week_start_MM/DD}}-{{week_end_MM/DD}}.

Transwestern deliveries:
{{transwestern_deliveries}}

El Paso deliveries by point:
{{el_paso_deliveries_by_point}}

Posted Gas Daily prices:
{{gas_daily_posted_prices}}

Notes and exceptions this week:
{{notes_and_exceptions}}

Source and as-of stamp: {{source_system_or_sheet}} as of {{as_of_date}}
<to be confirmed: whether the figures are pasted inline or attached, and the
column layout used in the live report>

{{report_owner_name_block}}
```

Filling rules that the archive supports:

1. Set `{{week_start_MM/DD}}` and `{{week_end_MM/DD}}` to the first and last working day covered, trimming the range when a holiday shortens the week [cit_7e9d6a9437c9].
2. Write ranges that cross a month or year boundary straight across the boundary; do not split them into two sends [cit_73c45be674b7].
3. Send to the standing list of seven; do not rebuild the recipient list each week [cit_281cdb8ece7c].
4. Send at the close of the week the report covers [cit_e04d7226f87c].

## Recommended change

Move the send to a scheduled job. The job runs once a week on the last working day of the covered week, builds the subject line from the covered date range using the trimming and boundary rules above, pulls the Transwestern delivery, El Paso delivery-by-point, and posted Gas Daily figures from their sources, and mails the result to the standing list.

Hold the distribution list in one named place — a mail distribution group or a config entry the job reads — rather than in the sender's habit. That is what makes the send survive a handover.

Add two lines to the body that the current send does not appear to carry: the source and the as-of stamp for each block of figures. A recipient who spots a number they do not believe should be able to see which source and which vintage it came from without replying to ask.

Fix the send window. Pick one time on the last working day of the week, publish it to the seven recipients, and have the job miss loudly — an alert to the owner — rather than silently sliding to the next day.

Keep a human approval gate before the first automated sends. The job assembles and stages the draft; the owner reviews and releases. Once several consecutive weeks pass review unchanged, drop the gate for the standard case and keep it for weeks with entries in `{{notes_and_exceptions}}`.

Retain each sent report body somewhere durable — a shared folder or a report archive keyed by week — so a later reader can reconstruct a week's figures without the mailbox.

## Open questions

- The body format is unknown. The archive preserves the headers of these sends but not the bodies, so the column layout, the ordering of the delivery blocks, and whether the figures were pasted inline or attached all need confirming against a recent live send [cit_e04d7226f87c].
- The sources of the figures are not identified. Which system or sheet the Transwestern deliveries, the El Paso deliveries by point, and the posted Gas Daily prices are read from is not visible in the archive [cit_c955cf19fffb].
- The seven recipients are a count, not a named list, in what is recorded here; the actual addresses and their roles need pulling from a live send before the list is moved into a distribution group [cit_281cdb8ece7c].
- There is no stated deadline for the send. The instances land at the end of the covered week but at different times of day, so whether a published cutoff exists is unresolved [cit_6e2d9c893a5d].
- The handling of a week with no data or a missed source is not shown. Whether the report is skipped, sent empty, or sent late is unknown [cit_7e9d6a9437c9].
