---
artifact_id: EML-03
title: 'Standing email template: Calpine Daily Gas Nomination notice'
artifact_type: email
opportunity_id: ser_c103eb437b
opportunity_title: '"Calpine Daily Gas Nomination" produced monthly'
generated_at: '2026-09-08T22:28:23.132655+00:00'
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

Give the gas logistics desk a fixed template for the recurring "Calpine Daily Gas Nomination" message, so the same fields arrive in the same order every time and the recipient list does not have to be rebuilt by hand.

## Scope

Covers the single recurring message titled "Calpine Daily Gas Nomination" as it arrives in the `farmer-d/logistics` folder from the Calpine side, and the standing distribution list that receives it. Does not cover the downstream nomination entry into Sitara, meter corrections, or imbalance and OBA settlement; those are separate processes with their own mail.

## Current practice

The message carries the fixed subject line "Calpine Daily Gas Nomination" with no date, cycle, or version marker in the subject [cit_61f81d3ab9f5]. It is sent by a single originator at the counterparty, `rickya@calpine.com`, rather than by an Enron-side scheduler [cit_b843b41c8654]. The same subject line recurs unchanged across months, so successive instances are indistinguishable from each other in a mailbox search [cit_ba466aea576b]. Consecutive instances arrive with the identical subject even when they land days apart, as on 31 July and 3 August 2000 [cit_4cccefa9b11b] [cit_afa39320fe4b]. The message reaches the logistics folder in the early morning hours, before the working day on the receiving desk [cit_8eaeeb47890d]. It arrives as ordinary mail to a standing list of recipients, not as a posting in a scheduling system [cit_4e2ac2d3f0d4]. The pattern continues across the turn of the year with the same subject and the same originator [cit_70d1c123124d].

## Template

Send as plain text. Keep the field order fixed so a reader can diff one instance against the previous one.

```
To: {{standing_distribution_list}}
From: {{originator_email}}
Subject: Calpine Daily Gas Nomination - flow date {{flow_date}} - cycle {{nomination_cycle}} - rev {{revision_number}}

Flow date:            {{flow_date}}
Nomination cycle:     {{nomination_cycle}}          <to be confirmed>
Revision:             {{revision_number}} (0 = original)
Pipeline:             {{pipeline}}
Contract / deal ref:  {{contract_ref}}

Receipt points
  Meter {{receipt_meter_id}}  {{receipt_meter_name}}   {{receipt_volume}}

Delivery points
  Meter {{delivery_meter_id}} {{delivery_meter_name}}  {{delivery_volume}}

Total nominated:      {{total_volume}}
Change from prior nomination: {{delta_from_prior}}

Confirmation requested by: {{confirmation_deadline}}   <to be confirmed>
Reply to this message with your confirmation, or state the cut and the reason.

Prepared by: {{originator_name}}, {{originator_role}}
Contact:     {{originator_phone}}
```

Notes for whoever sends it:

1. Do not change the leading words of the subject. Downstream mail rules and folder searches key on "Calpine Daily Gas Nomination" [cit_61f81d3ab9f5].
2. Add the flow date, cycle, and revision number to the subject so two instances can be told apart without opening them [cit_ba466aea576b].
3. Send from the same address every time; the series is already identified in the archive by its single originator [cit_b843b41c8654].
4. Send to the standing list, not to individually retyped addresses [cit_4e2ac2d3f0d4].
5. If a nomination is superseded within the same flow day, send a new message with the revision number incremented rather than replying inside the prior thread [cit_4cccefa9b11b] [cit_afa39320fe4b].

## Recommended change

Move the series to a scheduled job. The job pulls receipt and delivery volumes by meter from the source of record, renders the template above, and mails it to the standing list on the agreed cadence. The subject line becomes machine-composed, so the flow date, cycle, and revision are always present and always formatted the same way.

Put the volume table in an attached CSV as well as inline. Inline text survives the gateway; the CSV lets the receiving desk filter its own meters instead of reading past everyone else's rows.

Give each instance a stable identifier — flow date plus cycle plus revision — and echo it in both the subject and the body. Confirmations then reference the identifier rather than "your last nomination".

Hold the distribution list in one place and have the job read it. When someone joins or leaves the desk, the list changes once.

Let confirmations reply to a monitored address that files them against the identifier, so an unconfirmed nomination is visible without a mailbox search.

Ask the counterparty whether they will send a structured file rather than a mail body. If they will, the mail becomes a notification and the figures stop being retyped on the receiving end.

## Open questions

- The message bodies are not available in the archive, so the actual field list, units, and meter-level layout are unknown. The template above is a proposal and needs to be checked against a real instance before use.
- The nomination cycle referenced by each message is not recorded in the subject or otherwise visible, so `{{nomination_cycle}}` is marked `<to be confirmed>`.
- The confirmation deadline is not visible in the archive. `{{confirmation_deadline}}` is marked `<to be confirmed>`.
- The composition of the standing distribution list, and who owns adding or removing a recipient, is not determinable from the headers alone.
- Which system the figures are drawn from — Sitara, TAGG, or a Calpine-side system — is not shown, so the source of record for a scheduled job is undetermined.
- Whether an Enron-side acknowledgement was expected for every instance, or only when a volume was cut, is not shown.
