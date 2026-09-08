---
artifact_id: EML-01
title: "Daily Credit Report \u2014 standing distribution email (draft)"
artifact_type: email
opportunity_id: ser_06b1e12574
opportunity_title: '"Credit Report - 1/30/01" produced daily'
generated_at: '2026-09-08T22:19:47.509091+00:00'
generator: claude -p via .claude/agents/artifact-drafter.md
review_status: draft-unreviewed
evidence:
- cit_07c8f8ec932e
- cit_24e03b2028aa
- cit_31f1fd31b136
- cit_58a2ebb7bf10
- cit_78c3855c5db6
- cit_9b4f19be6efa
- cit_a99a1638e422
- cit_e6d8a34749a1
below_threshold_judgment_call: false
---

> **Draft, not reviewed.** Every sentence describing current practice carries a
> citation id that resolves to a verified quote from the archive. Sentences under
> *Recommended change* are proposals and carry no citation. Nobody who does this
> work has read this document.

## Purpose

Give the person who produces the daily Credit Report a fixed email shell to send with it, so the subject line, the report date, and the distribution list are consistent from one send to the next. The same shell is what a scheduled job would emit if the report is later automated.

## Scope

Covers the outbound email that carries the Credit Report to its standing recipients. Covers the subject-line format and the merge fields the send needs. Does not cover how the figures inside the report are assembled, and does not cover credit exceptions raised by reply.

## Current practice

The report is identified only by its subject line, which carries the report date: `Credit Report--2/2/01` [cit_a99a1638e422]. The same subject pattern repeats across consecutive report dates, for example `Credit Report--2/1/01` [cit_58a2ebb7bf10] and `Credit Report--2/15/01` [cit_31f1fd31b136]. The format does not change at month rollover: `Credit Report--3/1/01` [cit_07c8f8ec932e]. Every instance in the archive is sent from the same address, `darron.giron@enron.com` [cit_24e03b2028aa].

The subject format is not applied uniformly. One instance separates the label from the date with a space rather than a double hyphen: `Credit Report 3/15/01` [cit_78c3855c5db6]. Another zero-pads the day: `Credit Report--4/02/01` [cit_e6d8a34749a1].

The send timestamp does not always match the report date in the subject. The report dated 3/15/01 was sent on 2001-03-19 [cit_78c3855c5db6]. The report dated 4/02/01 was sent on 2001-04-06 [cit_e6d8a34749a1]. The report dated 2/1/01 was sent on 2001-02-05 [cit_58a2ebb7bf10]. Sends that do line up with their report date land in the small hours of the morning, before the trading day [cit_31f1fd31b136]. Others go out later in the morning [cit_9b4f19be6efa].

## Template

The block below is the send shell. `{{report_date}}` is the date the report covers, not the date of the send, which is how the subject line is used today [cit_a99a1638e422].

```
To: {{standing_distribution_list}}
From: {{report_owner}}
Subject: Credit Report--{{report_date_m_d_yy}}

Attached is the Credit Report for {{report_date_m_d_yy}}.

Sources as of {{data_as_of_timestamp}}.
Changes from the prior report: {{change_note_or_none}}

Questions on a specific counterparty line: reply to this message.

{{report_owner_name_and_role}}

Attachment: {{report_filename}}
```

Field rules:

- `{{report_date_m_d_yy}}` — single-digit month and day, no leading zero, as in `2/2/01` [cit_a99a1638e422] and `3/1/01` [cit_07c8f8ec932e]. Do not pad the day; one past send did, which breaks sorting by subject [cit_e6d8a34749a1].
- Separator is a double hyphen with no spaces [cit_31f1fd31b136]. The single-space variant is the outlier [cit_78c3855c5db6].
- `{{standing_distribution_list}}` — `<to be confirmed>`; the recipient addresses are not established here.
- `{{data_as_of_timestamp}}` — `<to be confirmed>`; no cutoff or as-of convention is established here.
- `{{report_filename}}` — `<to be confirmed>`.

## Recommended change

Fix the subject line as `Credit Report--M/D/YY` in a saved template or a mail-merge rule, so the label, separator, and date format stop drifting between sends. Sorting a mailbox or a shared folder by subject then groups the whole series.

Replace the standing recipient list with a distribution group, so adding or removing a recipient is one change rather than an edit to the To: line on the next send.

Make the report date and the send date explicit and separate. Put the report date in the subject and the data as-of timestamp in the body, so a reader can tell a normal send from a catch-up send without checking the header.

If the report is scheduled as a job, have the job emit exactly this shell, attach the generated file, and post a one-line note when it cannot run. A silent gap in a daily series is the failure mode worth guarding against, because the series is recognisable only by its subject line.

Add the `{{change_note_or_none}}` line so recipients who only care about movement do not have to open the attachment.

## Open questions

- Who the standing recipients are, and whether the list changed over the period.
- Which systems the figures come from, and whether any step in assembling the attachment is already automated.
- Whether there is a stated cutoff or as-of time for the underlying data.
- Whether the sends whose timestamp is later than their report date were catch-up sends, re-sends, or a different reporting convention [cit_78c3855c5db6].
- What the attachment contains, and whether its layout is stable enough to generate.
- What happens on a day the report is not produced, and who notices.
