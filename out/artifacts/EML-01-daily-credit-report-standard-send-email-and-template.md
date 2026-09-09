---
artifact_id: EML-01
title: 'Daily Credit Report: standard send email and template'
artifact_type: email
opportunity_id: ser_06b1e12574
opportunity_title: '"Credit Report - 1/30/01" produced daily'
generated_at: '2026-09-09T14:58:30.389704+00:00'
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

Give the person who sends the daily credit report a fixed email template, so the subject line, the distribution list, and the attachment reference are the same every day and so a scheduled job can later produce the same message without a human retyping it.

## Scope

Covers the daily "Credit Report" mailed from the trading-support desk to its standing distribution list, February through May 2001 in the archive. Covers the mail message only: the subject line, the body, and the reference to the attached report. Does not cover how the figures inside the report are assembled, which the archive does not show.

## Current practice

The report is mailed by a single sender, `darron.giron@enron.com`, from that account's sent folder [cit_a99a1638e422]. The subject line carries the report date rather than the send date, in the form `Credit Report--M/D/YY` [cit_31f1fd31b136]. The separator is not stable: most days use a double hyphen [cit_07c8f8ec932e], and at least one day uses a space instead [cit_78c3855c5db6]. The day number is usually unpadded [cit_9b4f19be6efa], and is sometimes zero-padded [cit_e6d8a34749a1]. On a normal day the message goes out in the small hours of the morning for that same date [cit_07c8f8ec932e]. Some days the message is sent the following morning for the prior day's report date [cit_24e03b2028aa]. Some days a report date is not mailed until several days later, so a Thursday report date leaves on the following Monday [cit_58a2ebb7bf10], and a mid-month report date leaves later in the month [cit_78c3855c5db6]. Weekend and holiday report dates arrive batched with the next business-day send [cit_e6d8a34749a1].

## Template

Use one message per report date. Do not batch two report dates into one message.

```
To:      {{standing_distribution_list}}
From:    {{report_sender}}
Subject: Credit Report--{{report_date_m_d_yy}}

Attached is the credit report for {{report_date_m_d_yy}}.

Source of figures: {{source_system}}   <to be confirmed>
Prepared by: {{preparer_role}}

Notes for this run (delete if none):
{{exception_note}}

Attachment: {{report_filename}}
```

Field rules:

- `{{report_date_m_d_yy}}` — the business date the report covers, not the date the mail is sent. Unpadded month and day, two-digit year, e.g. `4/20/01`.
- `{{standing_distribution_list}}` — the fixed recipient list, maintained as a mail group rather than typed per message. Current membership `<to be confirmed>`.
- `{{report_filename}}` — name the file with the report date so a recipient can tell two runs apart, e.g. `credit_report_{{report_date_m_d_yy}}`.
- `{{exception_note}}` — used only when a run is late, is a catch-up for an earlier report date, or covers more than one business date.
- `{{source_system}}` — the system the figures come from. Not shown in the archive; fill in before adopting.

## Recommended change

Move the report to a scheduled job. The job pulls the figures from their source, writes the file, and mails it to the standing group on the daily cadence, with the subject line generated from the business date so the separator and padding never vary again.

Normalise the subject to a single form, `Credit Report--M/D/YY`, and generate it rather than type it. This makes the series searchable and makes a missed day visible as a gap rather than something a reader has to notice.

Put the report date in the filename as well as the subject. Recipients who file attachments locally can then identify a run without opening it.

Emit the message even when the figures are unchanged or unavailable, with the reason in the note field. Silence currently cannot be distinguished from a late send.

Add a catch-up rule for weekends, holidays, and missed days: one message per business date, sent in date order, each with its own subject line. Batched sends hide which dates were covered.

Keep the recipient list as a mail group owned by the desk, and review membership on a set date each quarter.

Log each send — report date, send time, recipient group, filename — so the cadence can be audited without reading mailboxes.

## Open questions

- Which system the credit figures are drawn from, and whether the file is assembled in a spreadsheet before mailing. Not determinable from the archive; the message bodies are largely absent and the report itself was an attachment.
- The membership of the standing distribution list, and whether it changed across the four months in scope.
- Whether a cutoff time applies to the send, and who is notified when a report date is missed.
- Whether the several-day gaps between report date and send date are catch-up sends, weekend batching, or reissues of a corrected report.
- The naming convention actually used for the attachment, and whether recipients depend on it.
- Who covers the send when the usual sender is away, since the archive shows only one sending account.
