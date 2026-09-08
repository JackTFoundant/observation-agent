---
artifact_id: EML-01
title: 'Daily Credit Report: standing distribution email template'
artifact_type: email
opportunity_id: ser_06b1e12574
opportunity_title: '"Credit Report - 1/30/01" produced daily'
generated_at: '2026-09-08T21:33:08.383197+00:00'
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

Give the person who produces the daily Credit Report a fixed subject format and body text, so the report can be sent the same way every day and, later, sent by a scheduled job without the format changing.

## Scope

Covers the daily Credit Report mailed from the trading-support desk to its standing distribution list. Covers the subject line, the send time, and the handling of the attachment. Does not cover how the credit figures themselves are produced, or any other recurring report.

## Current practice

The report is sent as an email whose subject is the words "Credit Report" followed by the report date, for example "Credit Report--2/2/01" [cit_a99a1638e422]. It is sent by one person from the trading-support desk, from that person's own mailbox [cit_31f1fd31b136]. The cadence is daily, including across month boundaries: a report is dated 2/15/01 [cit_31f1fd31b136] and another 3/1/01 [cit_07c8f8ec932e].

The subject format is not stable. Most instances use a double hyphen between the words and the date, as in "Credit Report--3/26/01" [cit_24e03b2028aa]. At least one uses a single space and no hyphen, as in "Credit Report 3/15/01" [cit_78c3855c5db6]. The day number is usually unpadded, as in "Credit Report--4/20/01" [cit_9b4f19be6efa], but is sometimes zero-padded, as in "Credit Report--4/02/01" [cit_e6d8a34749a1].

Send timing is also not stable. Several reports go out in the early hours of the report date itself, such as the 2/2/01 report sent at 02:08 [cit_a99a1638e422], the 2/15/01 report sent at 02:24 [cit_31f1fd31b136], and the 3/1/01 report sent at 02:07 [cit_07c8f8ec932e]. Others are sent after the report date has passed: the 2/1/01 report was sent on 2/5 [cit_58a2ebb7bf10], the 3/15/01 report on 3/19 [cit_78c3855c5db6], and the 4/02/01 report on 4/06 [cit_e6d8a34749a1]. Some are sent the following morning, such as the 3/26/01 report sent on 3/27 at 08:02 [cit_24e03b2028aa].

## Template

Use this text as-is. Fill only the merge fields. Do not change the subject punctuation.

```
Subject: Credit Report--{{report_date_m_d_yy}}

Attached is the credit report for {{report_date_m_d_yy}}.

Source system: {{source_system}}
Positions as of: {{as_of_timestamp}}

Notes for today:
{{exceptions_or_none}}

Attachment: {{attachment_filename}}

Questions on any line item, reply to this message.

{{sender_name}}
{{sender_desk}}
```

If the report is sent later than its report date, add one line above the notes block:

```
This report covers {{report_date_m_d_yy}} and is being sent on {{send_date_m_d_yy}}.
```

If there is no attachment because it did not send, replace the attachment line with:

```
The attachment did not send. Figures are pasted below. <to be confirmed: agreed inline fallback format>
```

## Recommended change

Fix one subject format and use it every day: `Credit Report--M/D/YY`, double hyphen, unpadded month and day. A single format is what lets a downstream filter, rule, or archive search find every instance without a human reading the list.

Move the distribution list out of the sender's personal address book and into a named mail group. The report currently depends on one person's habits; a group alias makes the recipient set visible and editable by someone else.

Schedule the send. The report already goes out on a daily cadence; a scheduled job that pulls the figures from their source system, writes the attachment, and mails it to the group alias on a fixed clock removes the variation in send time and the gap between report date and send date.

Have the job send an explicit line when there is nothing to report, rather than an empty body. An empty message is indistinguishable from a failed one.

Set an alert if the job has not sent by its scheduled time, addressed to the desk rather than to the individual, so a missed day is noticed the same morning.

Keep the human override. The sender should be able to send the same template by hand with the same subject when the job fails, so the series stays unbroken in the archive.

## Open questions

- Who is on the standing distribution list, and whether it is the same set of recipients every day. The archive shows the sender but not a resolved recipient list.
- What system the credit figures are pulled from before the attachment is built. No message body names it.
- Whether a cutoff time was agreed for the send, and what the early-hours sends were timed against.
- What the attachment file was named and what format it used.
- Whether the late sends were deliberate catch-up or a missed day being backfilled.
- Whether the report is expected on weekends and holidays, or only on business days.
