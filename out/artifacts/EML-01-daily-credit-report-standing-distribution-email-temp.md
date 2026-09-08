---
artifact_id: EML-01
title: "Daily Credit Report \u2014 standing distribution email template"
artifact_type: email
opportunity_id: ser_06b1e12574
opportunity_title: '"Credit Report--5/9/01" produced daily'
generated_at: '2026-09-08T19:58:53.820243+00:00'
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

Give the desk one standard email for the daily Credit Report, so the subject line, the distribution list and the attachment name are the same every day. The template below is a draft to be adopted by whoever owns the Credit Report today, and to be reused unchanged by a scheduled job if the send is ever automated.

## Scope

Covers the daily Credit Report series sent from the trading-support desk (giron-d) to its standing distribution list [cit_a99a1638e422]. The archive window for this series runs from early February 2001 [cit_58a2ebb7bf10] through late April 2001 [cit_9b4f19be6efa]. Out of scope: the contents of the report itself, and the systems the figures are pulled from.

## Current practice

One sender produces and mails the report; every instance in the archive is sent from the same address [cit_a99a1638e422]. The subject line carries the report date in `M/D/YY` form, for example `Credit Report--2/15/01` [cit_31f1fd31b136]. The cadence is daily and the subject rolls to the next date each business day, as with `Credit Report--3/1/01` [cit_07c8f8ec932e].

The subject format is not stable. One instance drops the double hyphen and reads `Credit Report 3/15/01` [cit_78c3855c5db6]. Another zero-pads the day as `Credit Report--4/02/01` [cit_e6d8a34749a1].

Send dates do not always match report dates. The report for 2/1/01 was sent on 2/5/01 [cit_58a2ebb7bf10]. The report for 3/15/01 was sent on 3/19/01 [cit_78c3855c5db6]. The report for 4/02/01 was sent on 4/06/01 [cit_e6d8a34749a1]. Other instances go out on the morning after the report date, such as the 3/26/01 report sent on 3/27/01 [cit_24e03b2028aa].

What the archive preserves for each instance is the header — subject, sender, timestamp — and not the figures [cit_9b4f19be6efa]. The report content travelled as an attachment assembled outside the mail system [cit_a99a1638e422].

## Template

```
To:       {{standing_distribution_list}}
Cc:       {{desk_backup}}
Subject:  Credit Report--{{report_date_m/d/yy}}

Credit Report for {{report_date_m/d/yy}} is attached.

Figures are as of {{as_of_timestamp}}, sourced from {{source_system}} <to be confirmed>.

Exceptions or changes since the prior report:
{{exception_notes_or_"none"}}

Questions on this report: {{owner_role}}, {{owner_contact}}.

Attachment: {{credit_report_filename}}
```

Filling rules for the sender:

1. `{{report_date_m/d/yy}}` is the date the figures describe, not the date the mail goes out. Use the `Credit Report--M/D/YY` form with the double hyphen and no zero padding on the day [cit_31f1fd31b136].
2. `{{standing_distribution_list}}` is a fixed group. Do not retype addresses per send; keep the list as a named mail group so the recipients stay identical day to day [cit_07c8f8ec932e].
3. `{{credit_report_filename}}` should embed the same date string as the subject, so an attachment can be matched to its mail without opening it [cit_e6d8a34749a1].
4. If a report is sent later than the day after its report date, state the reason in `{{exception_notes_or_"none"}}`; late sends occur today with no note in the header record [cit_78c3855c5db6].
5. If no figures changed, still send. The obligation is the cadence, and gaps in the series are indistinguishable from a missed send [cit_24e03b2028aa].

## Recommended change

Freeze the subject line to a single machine-generated form: `Credit Report--M/D/YY`, produced from the report date by the sending job rather than typed. That alone makes the series findable, sortable and auditable, and removes the hyphen and zero-padding variants.

Move the distribution list out of the sender's mail client and into a named group owned by the desk. The list should be reviewed on a fixed date each quarter by the report owner.

Put the report body in the mail as well as in the attachment. A short plain-text summary block — as-of timestamp, source, exceptions — means a recipient can read the headline on a phone and the record survives without the file.

Have the assembly job write the report to a shared location first and mail a link plus the attachment. Then a late or failed send does not block anyone who knows where to look.

Name a backup sender and a documented fallback: if the scheduled job does not deliver by the agreed cutoff, the backup sends the prior day's file with an explicit "no update" note rather than sending nothing.

Once the source of each figure is confirmed, replace the manual assembly with a scheduled job that pulls from those sources and sends on the same cadence to the same group. Keep a human sign-off step until the job has run clean for a full month of business days.

## Open questions

- What the report contains. The archive holds headers only for this series, so the fields, layout and figures are unknown [cit_9b4f19be6efa].
- Which systems the figures come from. `{{source_system}}` is marked `<to be confirmed>` in the template for that reason.
- The daily cutoff time by which recipients need the report. Send timestamps vary and no stated deadline appears in the archive [cit_e6d8a34749a1].
- Who the recipients are by role, and whether the list changed during the archive window [cit_a99a1638e422].
- Whether the gaps in the daily series are weekends, holidays, genuine misses, or reports sent from another mailbox [cit_58a2ebb7bf10].
- Who covers the send when the usual sender is out; every instance in the archive comes from one address [cit_07c8f8ec932e].
- Whether the late sends were the report arriving late or the mail being resent [cit_78c3855c5db6].
