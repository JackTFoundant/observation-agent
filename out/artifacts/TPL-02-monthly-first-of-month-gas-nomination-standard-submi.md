---
artifact_id: TPL-02
title: "Monthly First-of-Month Gas Nomination \u2014 Standard Submission Template"
artifact_type: template
opportunity_id: proc_b568e80cfc
opportunity_title: Monthly first-of-month gas nominations emailed in by counterparties
generated_at: '2026-09-09T19:21:26.110563+00:00'
generator: claude -p via .claude/agents/artifact-drafter.md
review_status: draft-unreviewed
evidence:
- cit_04eb86a692b1
- cit_5ed878358f01
- cit_607989d33ece
- cit_7ad0647816c0
- cit_8ce5472cc445
- cit_d0a4a6dca279
- cit_d7d7daa00d35
- cit_d9554236673a
below_threshold_judgment_call: false
---

> **Draft, not reviewed.** Every sentence describing current practice carries a
> citation id that resolves to a verified quote from the archive. Sentences under
> *Recommended change* are proposals and carry no citation. Nobody who does this
> work has read this document.

## Purpose

Give counterparties and plant schedulers one fixed form for submitting first-of-month natural gas nominations to the logistics desk, so every submission carries the same fields in the same order and can be read without interpretation.

## Scope

Covers monthly nominations emailed to the logistics desk for a named plant or delivery point, including estimates and later revisions. Covers the submission mail only. Does not cover entry of the volumes into any downstream scheduling system, which is not visible in the archive.

## Current practice

Counterparties email the logistics desk a nomination for the coming month, addressed to a named plant and delivery point [cit_7ad0647816c0]. The same wording recurs month after month from the same sender for the same plant [cit_607989d33ece]. The subject line carries the month in short form [cit_d9554236673a]. Other parties submit under their own phrasing for their own points [cit_d7d7daa00d35]. A nomination for a named counterparty and month arrives as free text in the mail body [cit_8ce5472cc445]. Some submissions are explicitly estimates rather than firm volumes [cit_04eb86a692b1]. Revisions arrive later in the same thread and are keyed to a named approver and a date [cit_d0a4a6dca279]. A submission is sometimes incomplete because the sender is waiting on a transport number held by a named person elsewhere [cit_5ed878358f01].

## Template

Send one mail per counterparty per delivery point per month. Do not combine points in one mail. The subject line follows the short-month form already in use [cit_d9554236673a].

```
Subject: NATURAL GAS NOMINATION FOR {{mm_yy}} — {{counterparty}} — {{delivery_point}}

Submission type: {{firm | estimate | revision}}
Counterparty: {{counterparty}}
Plant / delivery point: {{plant_or_point}}
Meter number: {{meter_number}}
Flow month: {{month_year}}
Transport number: {{transport_number}}
  (required; if not yet held, enter PENDING and name the holder below)
Transport number held by: {{name_and_desk_if_pending}}

Volumes:
  Daily quantity: {{daily_quantity}} {{unit}}
  Total month quantity: {{month_quantity}} {{unit}}
  Variance by day (if not flat): {{day_by_day_or_none}}

If this is a revision:
  Supersedes: {{prior_submission_subject_and_date}}
  Authorised by: {{approver_name}}
  Authorised on: {{date_and_time_of_approval}}
  What changed: {{changed_fields}}

If this is an estimate:
  Firm number expected by: {{date_estimate_will_be_replaced}}

Submitted by: {{sender_name}}
Contact for questions: {{phone_or_email}}
```

Sender instructions:

1. Use `Submission type: revision` for any change to a nomination already sent, and fill the `Supersedes` and `Authorised by` lines; the archive shows revisions carrying a named approver and a date [cit_d0a4a6dca279].
2. Use `Submission type: estimate` where the volume is not yet firm, and give the date the firm number will follow [cit_04eb86a692b1].
3. Do not hold the mail because the transport number is outstanding; send with `PENDING` and name the person holding it [cit_5ed878358f01].
4. Send by the monthly submission cutoff `<to be confirmed>`.

## Recommended change

Publish the template above as a saved mail form, one per counterparty and delivery point, with the counterparty, plant, point and meter number pre-filled. Recurring submitters then change only the month and the volumes.

Make the transport number a required field with a `PENDING` value and a named holder, so an incomplete nomination is still submitted on time and the missing field is visible and chaseable rather than sitting with the sender.

Require the `Submission type` line on every mail. Treat `revision` as superseding the referenced prior submission rather than appending to it, and keep the approver name and approval timestamp on the record.

Move parsing off the mail body. A structured web form or a fixed-column attachment writing into a single monthly nomination sheet would remove the re-keying step and let the desk see, per point, which nominations are firm, which are estimates, and which are waiting on a transport number.

Agree an internal escalation for pending transport numbers: if the holder has not supplied the number by an agreed point before flow, the logistics desk raises it rather than the counterparty.

## Open questions

- The submission cutoff date and time for first-of-month nominations is not shown in the archive.
- The unit of volume (MMBtu, Mcf, or other) is not stated in the quoted material and must be fixed before the template is issued.
- Where the numbers go after the mail — which system receives them and who keys them — is not visible in these messages.
- Whether a revision must be authorised by a named approver in all cases, or only in the one instance observed, is not established.
- Whether meter number is required on every submission, or only for some points, is not established.
- Who owns chasing a pending transport number today is not shown.
