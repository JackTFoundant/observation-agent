---
artifact_id: EML-03
title: 'Standing email template: Calpine Daily Gas Nomination'
artifact_type: email
opportunity_id: ser_c103eb437b
opportunity_title: '"Calpine Daily Gas Nomination" produced monthly'
generated_at: '2026-09-09T19:21:26.112473+00:00'
generator: claude -p via .claude/agents/artifact-drafter.md
review_status: draft-unreviewed
evidence:
- cit_4cccefa9b11b
- cit_4e2ac2d3f0d4
- cit_61f81d3ab9f5
- cit_70d1c123124d
- cit_8eaeeb47890d
- cit_afa39320fe4b
- cit_b843b41c8654
- cit_ba466aea576b
below_threshold_judgment_call: false
---

> **Draft, not reviewed.** Every sentence describing current practice carries a
> citation id that resolves to a verified quote from the archive. Sentences under
> *Recommended change* are proposals and carry no citation. Nobody who does this
> work has read this document.

## Purpose

Give the owner of the Calpine gas nomination series a standing email template and a record of what the archive actually proves about it, so the send can be reissued consistently or handed to a scheduled job.

## Scope

Covers the recurring message with the subject line "Calpine Daily Gas Nomination" sent to Daren Farmer's logistics folder between December 1999 and December 2000. Covers the header pattern, the sender, and the fixed subject line only. Does not cover the nomination figures themselves, the contract they sit under, or the downstream confirmation step in Sitara or on the pipeline's own system — the archive does not carry the message bodies for this series.

## Current practice

The message carries an unchanging subject line, "Calpine Daily Gas Nomination" [cit_61f81d3ab9f5]. Every instance in the archive comes from the same external address, rickya@calpine.com [cit_b843b41c8654]. Every instance lands in the same destination folder, farmer-d/logistics [cit_ba466aea576b]. The earliest instance in the archive is dated 1999-12-14 [cit_61f81d3ab9f5]. Instances continue through 2000-04-10 [cit_b843b41c8654], 2000-06-22 [cit_ba466aea576b], 2000-07-31 [cit_4cccefa9b11b], 2000-08-03 [cit_afa39320fe4b], 2000-08-15 [cit_8eaeeb47890d], 2000-09-18 [cit_4e2ac2d3f0d4], and 2000-12-12 [cit_70d1c123124d]. The subject line is reused unchanged rather than carrying the flow date or the nomination cycle it applies to [cit_4cccefa9b11b]. Two instances fall in consecutive business days at the turn of July into August, both under the same undifferentiated subject [cit_4cccefa9b11b] [cit_afa39320fe4b]. The message is delivered as email; the archive shows no other system in the series [cit_8eaeeb47890d]. Several instances are timestamped in the small hours of the sender's day, ahead of the recipient's working morning [cit_70d1c123124d] [cit_4e2ac2d3f0d4].

## Template

Draft standing form for the send. Fields in `{{ }}` are merged per instance. Fields marked `<to be confirmed>` are not evidenced in the archive and must be fixed by the process owner before first use.

```
To: {{scheduling_distribution_list}}
From: {{nominating_party_scheduler}}
Subject: Calpine Daily Gas Nomination - flow date {{flow_date}} - {{nomination_cycle}}

Flow date: {{flow_date}}
Nomination cycle: {{nomination_cycle}}
Contract / agreement reference: {{contract_reference}}
Pipeline: {{pipeline}}

Nomination detail:

  Receipt meter    {{receipt_meter_id}}   {{receipt_meter_name}}   {{receipt_volume}}
  Delivery meter   {{delivery_meter_id}}  {{delivery_meter_name}}  {{delivery_volume}}
  Total nominated                                                  {{total_volume}}

Change from prior day: {{change_note}}

Please confirm receipt and scheduled volumes to {{confirmation_address}}
by <to be confirmed - nomination cutoff for this cycle>.

Questions on this nomination: {{sender_name}}, {{sender_phone}}.
```

Send rule for the template: one message per flow date and cycle, subject line carrying both, so a reply can be matched to the nomination it answers.

## Recommended change

1. Put the flow date and the nomination cycle in the subject line of every send. A single reused subject line cannot be threaded, searched, or reconciled against a confirmation, and two sends on consecutive days become indistinguishable in a mailbox.
2. Replace the free-text body with the fixed field block above, so the same fields appear in the same order every time and a downstream parser can read them.
3. Move the recurring send to a scheduled job that pulls the meter list, the contract reference and the nominated volumes from their systems of record and mails the assembled block to a named standing distribution list on the agreed cadence. Keep the email as the delivery channel until the counterparty can accept a machine-readable feed.
4. Name the distribution list explicitly rather than addressing individuals, so the list survives staff changes on either side.
5. Require an explicit confirmation reply against the subject line, and have the job flag any flow date and cycle for which no confirmation arrived before the cutoff.
6. Log each send and each confirmation against the flow date, so scheduled-versus-confirmed gaps can be reviewed without re-reading the mailbox.

## Open questions

- The message bodies for this series are not in the archive, so the actual field list, meter set and volume detail carried by the nomination are unknown. The template's field block is a proposal, not a reconstruction.
- The nomination cutoff time and the cycle names used by the receiving pipeline are not evidenced. Marked `<to be confirmed>` in the template.
- The full recipient list is not visible in these citations; only the destination folder is. The standing list must be confirmed with the process owner before the template is used.
- Whether a confirmation was returned for each nomination, and by what route, cannot be determined from the archive.
- Whether the nomination was also entered into Sitara or another deal-capture or scheduling system, and by whom, is not shown.
- The gap in the archive between the December 1999 instance and the April 2000 instance is unexplained: it may be a real pause in the arrangement or a gap in the export.
