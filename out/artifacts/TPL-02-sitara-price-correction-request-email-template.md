---
artifact_id: TPL-02
title: "Sitara Price Correction Request \u2014 Email Template"
artifact_type: template
opportunity_id: proc_66cb726f71
opportunity_title: Sitara deal price corrections requested by email before invoicing
generated_at: '2026-09-09T14:58:30.387818+00:00'
generator: claude -p via .claude/agents/artifact-drafter.md
review_status: draft-unreviewed
evidence:
- cit_05d84f659acb
- cit_0f8385967b03
- cit_228d2225d561
- cit_8679afac67b0
- cit_b317a748a55a
- cit_ced3d96c78eb
- cit_ecee0749008d
- cit_f9e449cf00c4
below_threshold_judgment_call: true
---

> **Draft, not reviewed.** Every sentence describing current practice carries a
> citation id that resolves to a verified quote from the archive. Sentences under
> *Recommended change* are proposals and carry no citation. Nobody who does this
> work has read this document.

## Purpose

Give anyone who finds a wrong price or volume on a Sitara deal one standard email to send, so the person holding Sitara edit rights receives every field needed to make the change on first read, and the requester gets a confirmation back instead of chasing one.

## Scope

Covers corrections to price on an existing Sitara deal or ticket — flat price, index-plus-differential, and corrections limited to specific production days — raised by a requester who does not hold Sitara write access. Covers the confirmation the requester needs before invoicing or reconciling. Does not cover new deal capture, deal cancellation, or volume-only amendments.

## Current practice

The requester emails the change to the person with Sitara write access, naming the deal and the corrected commodity price [cit_ced3d96c78eb]. The corrected figure is sometimes stated as an index plus a differential rather than a flat number [cit_ecee0749008d]. Some requests are scoped to particular production days within a month [cit_05d84f659acb]. The request states what Sitara currently shows so the two figures can be compared [cit_0f8385967b03]. The requester frequently cannot send the change directly and asks a third party to pass it on: "pls forward this to Daren so that he can change the price in Sitara" [cit_ecee0749008d]. After sending, the requester waits and asks to be told when the edit lands [cit_228d2225d561]. The trigger is often an imminent invoice — "I need to send out my invoice this afternoon" [cit_8679afac67b0]. Where the requester attempts the edit themselves, the attempt is on a specific ticket number [cit_b317a748a55a], and access can be refused outright, turning the data fix into an escalation [cit_f9e449cf00c4].

## Template

Send to the holder of Sitara edit rights. One deal per mail where possible; use the table for a batch.

```
Subject: Sitara price correction — deal {{deal_or_ticket_number}} — {{production_month}}

Sitara edit request. Please change and confirm back.

Deal / ticket number:      {{deal_or_ticket_number}}
Counterparty:              {{counterparty}}
Production month:          {{production_month}}
Days affected:             {{production_days_or_ALL}}
Price currently in Sitara: {{current_sitara_price}}
Correct price:             {{corrected_price_or_index_formula}}
Basis for the correction:  {{contract_confirm_or_customer_price_source}}

Batch (delete if single deal):
| Deal #       | Days   | Sitara price | Correct price |
|--------------|--------|--------------|---------------|
| {{deal_1}}   | {{d1}} | {{old_1}}    | {{new_1}}     |
| {{deal_2}}   | {{d2}} | {{old_2}}    | {{new_2}}     |

Reason this is needed by a date:
{{invoice_or_settlement_deadline}} — {{what_is_blocked}}

Please reply to this mail once the deal record shows the corrected price.
I will check that the change comes across before I {{invoice_or_reconcile}}.

Requester: {{requester_name}}, {{requester_role}}
Sitara write access held by: {{editor_name}}
```

Access-refusal variant. Use when the requester tried the ticket and was blocked [cit_b317a748a55a][cit_f9e449cf00c4].

```
Subject: Sitara access — cannot edit ticket {{deal_or_ticket_number}} — escalation

I attempted to correct the pricing on Sitara ticket {{deal_or_ticket_number}}
and was refused access. Reason shown: {{access_error_text}}.

The correction still needs to be made:
  Days affected:  {{production_days_or_ALL}}
  Correct price:  {{corrected_price_or_index_formula}}

Please either make the change and confirm, or route this to the person
who holds edit rights on deals of this vintage.

Blocking: {{invoice_or_settlement_deadline}}
```

## Recommended change

Route price corrections through a logged request rather than free-text mail, so the deal number, affected production days, old price and new price or index formula are always present and the request has an owner from the moment it is raised.

Have the request routed automatically to whoever currently holds Sitara edit rights for that deal, rather than to a named individual who may then forward it on. Forwarding is where the request loses its owner.

Return an automatic confirmation to the requester when the Sitara deal record changes, keyed to the deal number. The requester should not have to ask to be notified, and should not have to re-open the deal to see whether the edit landed.

Run a comparison of Sitara price against the contracted or customer price ahead of the invoice run, and surface the mismatches as a list before the invoice date. Corrections found on that list are handled with time in hand rather than on the afternoon the invoice goes out.

Treat an access refusal as an escalation with a named target from the start. A request that cannot be actioned by its recipient should not sit as an unanswered mail.

## Open questions

- Who currently holds Sitara edit rights, and whether rights differ by deal vintage or by book. The archive shows access being refused on one ticket but not who grants it.
- Whether a cutoff exists for price changes relative to the invoice run or month-end settlement. Mark this `<to be confirmed>` in the template until established.
- Whether an audit record of the pre-change price is kept anywhere other than the request email.
- Whether the same request path applies to volume corrections, or only to price.
- How index-based corrections are entered — as a formula on the deal or as a resolved flat price — and who resolves the index.
