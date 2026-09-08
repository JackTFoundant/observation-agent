---
artifact_id: TPL-01
title: "Template: Meter with Flow and No Deal \u2014 Extend, Issue, or Write Off to\
  \ UAG"
artifact_type: template
opportunity_id: proc_3add3b927d
opportunity_title: 'Meters with flow but no deal: extend, issue, or write off to UAG'
generated_at: '2026-09-08T21:33:08.379017+00:00'
generator: claude -p via .claude/agents/artifact-drafter.md
review_status: draft-unreviewed
evidence:
- cit_12118e5ff76f
- cit_2d4d361dd72a
- cit_2db43e6a6b86
- cit_5a9eef1e4560
- cit_7b0138da70da
- cit_8d089971756a
- cit_8d240e3c0e5b
- cit_abddf46123de
below_threshold_judgment_call: false
---

> **Draft, not reviewed.** Every sentence describing current practice carries a
> citation id that resolves to a verified quote from the archive. Sentences under
> *Recommended change* are proposals and carry no citation. Nobody who does this
> work has read this document.

## Purpose

Give Logistics a single standard mail for the case where a meter shows recorded flow on days that no deal ticket covers. The mail names the meter, the days, the candidate deal, and asks the owning commercial contact for one of three outcomes.

## Scope

Covers retrospective clean-up of measured HPL meter volumes that cannot be booked against a contract. Covers the three outcomes already in use: extend an existing deal (and its purchase contract where one exists), issue a new deal, or write the volume off to Unaccounted for Gas. Does not cover forward nominations or scheduling changes.

## Current practice

The trigger is a meter that has recorded flow for days with no deal against it [cit_8d240e3c0e5b]. Logistics writes to the responsible commercial contact and asks for either a deal to record the volumes that have flowed into HPL's pipeline, or approval to write the volumes off to Unaccounted for Gas [cit_2db43e6a6b86]. Where an existing deal is the candidate, the request is put as a numbered choice: "Logistics needs either (1) Deal #124400 extended, (2) new deal, or (3) approval to write-off these volumes to Unaccounted for Gas." [cit_8d089971756a]. Where a purchase contract is tied to the deal, both are named in option (1) and option (2) asks for a new deal and contract [cit_5a9eef1e4560]. Where more than one deal could cover the gap, both numbers are listed and the months to be covered are stated explicitly [cit_2d4d361dd72a]. Where no deal is a candidate at all, the mail asks only for approval to write the volume off to Unaccounted for Gas [cit_abddf46123de]. Prior-year precedent is cited in the thread when it exists: "We used deal 83388 last January to write off this meter's HPL Strangers balances." [cit_7b0138da70da]. Identification of the right deal is not always settled by the reply — in one thread the contact reported that Daren was not aware of the deal unless it had something to do with ENTEX [cit_12118e5ff76f].

## Template

```
To: {{commercial_contact}}
Cc: {{logistics_owner}}
Subject: Meter {{meter_number}} — flow with no deal, {{flow_month_range}}

Meter {{meter_number}} ({{meter_name}}) has recorded flow for the following
days with no deal:

  {{flow_days_list}}          Total volume: {{volume}} {{volume_units}}

These volumes have flowed into HPL's pipeline and cannot be recorded against
a contract as things stand.

Logistics needs one of the following:

  (1) Deal #{{candidate_deal_number}}{{#purchase_contract}} and Purchase
      Contract #{{purchase_contract_number}} tied to it{{/purchase_contract}}
      extended to cover {{months_to_cover}};
  (2) a new deal{{#purchase_contract}} and contract{{/purchase_contract}} to
      cover {{months_to_cover}}; or
  (3) approval to write off these volumes to Unaccounted for Gas.

Prior history on this meter: {{prior_writeoff_reference}}
Counterparty of record: {{counterparty}}

Please reply with the deal number, or with "(3) approve write-off", by
<to be confirmed>. If the deal above is not yours, tell me whose it is and I
will re-route.

{{sender_name}}
Logistics
```

Variant, no candidate deal — replace the three options with a single line:

```
Logistics needs approval to write off this volume to Unaccounted for Gas.
```

Variant, two candidate deals — replace option (1) with:

```
  (1) Deal #{{candidate_deal_a}} or #{{candidate_deal_b}} extended to cover
      {{months_to_cover}};
```

## Recommended change

Stop sending one hand-written mail per meter. Run a scheduled reconciliation each accounting period that joins measured meter volumes against active deal coverage and emits one exception list: meter, flow days, volume, expired or candidate deal number, tied purchase contract, counterparty of record, and any prior write-off deal used on that meter.

Route the exception list to the owning commercial contact as a single mail per contact, with the three outcomes rendered as selectable responses against each meter line rather than as free prose. Capture the reply back into Sitara as the deal number or the write-off approval, so the decision is attached to the meter rather than living only in the thread.

Carry prior write-off history into the list automatically. The precedent is what unblocks the ambiguous cases, and today it depends on someone remembering it.

Add an explicit "not my deal" response option that re-routes the meter line to another contact without opening a new thread, so misdirected meters do not stall.

Publish a standing owner map — meter to commercial contact — and reconcile it against who actually answers, so ownership questions are resolved before the mail goes out rather than inside it.

## Open questions

- The reply deadline. No cutoff or turnaround expectation appears in the archive; the template carries `<to be confirmed>`.
- Who approves a write-off to Unaccounted for Gas. The mails request approval but the approver's role is not identified.
- Whether the write-off, once approved, is booked in Sitara or in a separate accounting system, and by whom.
- How a meter is assigned to a commercial contact, and where that mapping is held.
- Whether volume units and totals are stated in the outgoing mail or attached separately; the merge fields above assume they are stated.
- Whether the period that surfaces these exceptions is a fixed accounting close or ad hoc.
