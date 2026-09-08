---
artifact_id: TPL-03
title: "Sitara deal ticket correction request \u2014 mail template"
artifact_type: template
opportunity_id: proc_7b2079ed91
opportunity_title: Sitara deal price corrections chased by hand before invoicing
generated_at: '2026-09-08T21:33:08.381491+00:00'
generator: claude -p via .claude/agents/artifact-drafter.md
review_status: draft-unreviewed
evidence:
- cit_2214793e2b80
- cit_2718f1a7a56c
- cit_84a4eb86fd30
- cit_8851bb718668
- cit_a1667ea29fa2
- cit_b317a748a55a
- cit_edd529a6d3b4
- cit_f9e449cf00c4
below_threshold_judgment_call: true
---

> **Draft, not reviewed.** Every sentence describing current practice carries a
> citation id that resolves to a verified quote from the archive. Sentences under
> *Recommended change* are proposals and carry no citation. Nobody who does this
> work has read this document.

## Purpose

Give a fixed format for asking that a Sitara deal ticket price or volume be corrected, so the request carries the ticket number, the current value, the requested value, and the downstream deadline in one mail.

## Scope

Covers corrections to price or volume on an existing Sitara deal ticket found by comparing the ticket against a counterparty invoice, a confirmation, or a settlement statement. Covers both the first request and the follow-up chase. Does not cover new deal entry, deal cancellation, or imbalance and OBA settlement.

## Current practice

The discrepancy is found by comparing what the counterparty paid or invoiced against what the deal ticket in Sitara shows, and both figures are stated side by side in the mail [cit_2214793e2b80]. The counterparty figure is named as the basis for the comparison [cit_2718f1a7a56c]. The requester names the counterparty, the flow date, the point, and the deal ticket number, then asks the recipient to confirm the price [cit_8851bb718668]. Some requests state only the deal number and the price the commodity needs to be [cit_a1667ea29fa2]. Follow-ups are sent as free-text mail restating the adjustment and noting that Sitara still shows the old figure [cit_84a4eb86fd30]. The reason for the chase is a downstream deadline, in one case an invoice going out the next day [cit_edd529a6d3b4]. Where the requester tries to make the change directly, they go into the Sitara ticket by number to correct the pricing themselves [cit_b317a748a55a]. That route can fail on access rather than on data, and the request then has to proceed through someone else [cit_f9e449cf00c4].

## Template

Send as plain text. One deal ticket per mail. Keep the subject line exactly as below so follow-ups thread.

```
Subject: Sitara correction - deal {{deal_ticket_number}} - {{counterparty}} {{flow_date}}

Deal ticket:        {{deal_ticket_number}}
Counterparty:       {{counterparty}}
Point:              {{point}}
Flow date(s):       {{flow_date_range}}

Sitara currently shows:
  Volume:           {{sitara_volume}}
  Price:            {{sitara_price}}

Source document says ({{source_type}}: invoice / confirmation / settlement statement,
dated {{source_date}}):
  Volume:           {{source_volume}}
  Price:            {{source_price}}

Requested change:   {{field_to_change}} on ticket {{deal_ticket_number}}
                    from {{current_value}} to {{requested_value}}

Why it is needed:   {{downstream_action}} (invoice / path the volume / settle)
Needed by:          {{needed_by_date}}

Can you confirm the price and volume, or make the change and confirm back on this
thread?

I have / have not been able to open the ticket myself: {{access_status}}
If edit rights sit elsewhere, the owner of record is: <to be confirmed>

Requester:          {{requester_name}}, {{requester_desk}}
```

Chase mail, sent on the same thread:

```
Subject: RE: Sitara correction - deal {{deal_ticket_number}} - {{counterparty}} {{flow_date}}

Following up. Sitara still shows {{sitara_price}} / {{sitara_volume}} on ticket
{{deal_ticket_number}}. The requested value is {{requested_value}}.

{{downstream_action}} is due {{needed_by_date}} and is held on this correction.

Please either make the change or tell me who holds edit rights on this ticket.
```

## Recommended change

Run a recurring exception report that matches Sitara ticket price and volume against counterparty invoice and confirmation data and lists only the mismatches, timed to run before the monthly invoicing cycle rather than after.

Replace the free-text mail with a structured correction request carrying five required fields: ticket number, field, current value, requested value, requester. Route it automatically to whoever holds edit rights on that ticket, so the requester does not have to discover the owner by trial.

Keep an open-items list of submitted corrections with their downstream deadline, so a chase is a status change on a record rather than a second mail.

Record edit rights per ticket, including tickets inherited from a predecessor entity, so an access refusal is known before the requester tries.

## Open questions

- Who owns edit rights on a Sitara ticket, and whether that is the deal owner or a support desk, is not determinable from the archive.
- The cutoff by which a correction must be in Sitara to make a given invoice run is not stated.
- Whether corrected tickets need any matching change in a downstream system before settlement is not shown.
- The route for tickets the requester is barred from opening is not documented; the archive shows only that the request had to go elsewhere.
- Whether volume-only corrections follow the same path as price corrections is unclear.
