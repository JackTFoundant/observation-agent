---
artifact_id: CHK-01
title: 'Checklist: Correcting a Wrong Deal Price in Sitara'
artifact_type: checklist
opportunity_id: proc_04f796a5b2
opportunity_title: Fixing wrong deal prices in Sitara after the fact
generated_at: '2026-09-09T19:21:26.108509+00:00'
generator: claude -p via .claude/agents/artifact-drafter.md
review_status: draft-unreviewed
evidence:
- cit_2874902d6601
- cit_2d3930fbcf82
- cit_5160f9a064ab
- cit_52db8ac62baa
- cit_5a1f86c95a68
- cit_9fed7efcaa12
- cit_d3a8d3df7638
- cit_f7716817d54d
below_threshold_judgment_call: true
---

> **Draft, not reviewed.** Every sentence describing current practice carries a
> citation id that resolves to a verified quote from the archive. Sentences under
> *Recommended change* are proposals and carry no citation. Nobody who does this
> work has read this document.

## Purpose

Give the desk and the Sitara editor one shared checklist for handling a deal whose recorded price is wrong after entry, so the request, the edit and the confirmation follow the same path every time.

## Scope

Covers price corrections on an existing deal in Sitara, raised for a named deal number and flow month, where the wrong price was found downstream by billing, settlement, or someone reading a deal summary. Covers the workaround used when the deal itself cannot be amended. Does not cover new deal entry, volume corrections, or counterparty changes.

## Current practice

The person who spots the error is not the person who fixes it: they mail the Sitara editor and ask for the price on a specific deal number and flow month to be updated [cit_5a1f86c95a68]. Requests name the flow month explicitly, for example asking that the deal in Sitara be updated to reflect the correct price for a stated month [cit_2874902d6601]. A carried-forward deal keeps the prior month's rate until someone edits it, and the request says so [cit_5a1f86c95a68]. Some deals are found sitting at a zero price, and the request asks for the change and for the requester to be advised when it is complete [cit_f7716817d54d]. The Sitara editor makes the change and reports back that the price was adjusted in Sitara [cit_d3a8d3df7638]. Where the deal cannot be fixed, the group instead agrees a fixed price to be written onto both lines of the affected month's deal [cit_9fed7efcaa12]. Billing holds its own view of the price and states what the counterparty was billed at from Deal Manager-Sitara [cit_2d3930fbcf82]. In one instance the error was found from a new deal summary and the sender named both the old and the corrected price when reporting the change [cit_52db8ac62baa]. That same correction was chased so the revenue figure would be right, with a request to recalculate or zero it out prior to the morning flash [cit_5160f9a064ab].

## Procedure

- [ ] **Requester (billing, settlement, or desk reviewing the deal summary): record the deal number and the flow month before mailing.** Both are named in every request today [cit_2874902d6601].
- [ ] **Requester: state the price now on the deal and the price it should be, and say where the correct price came from** — quote, bill, or counterparty's own record [cit_52db8ac62baa].
- [ ] **Requester: if billing has already invoiced, say what price the counterparty was billed at from Deal Manager-Sitara** [cit_2d3930fbcf82].
- [ ] **Requester: mail the Sitara editor and ask to be advised when the change is complete** [cit_f7716817d54d].
- [ ] **Requester: if the figure feeds the morning flash, flag that in the request** and say whether a recalculation or a zero-out is wanted before the flash runs [cit_5160f9a064ab].
- [ ] **Sitara editor: open the deal for the stated flow month and correct the price** [cit_d3a8d3df7638].
- [ ] **Sitara editor: if the deal cannot be reopened, get agreement on a fixed price and apply it to both lines of the affected month's deal** [cit_9fed7efcaa12].
- [ ] **Sitara editor: reply to the requester confirming the deal number, the flow month and that the price was adjusted in Sitara** [cit_d3a8d3df7638].
- [ ] **Requester: re-read the deal summary after the edit and confirm the revenue figure now matches** [cit_52db8ac62baa].
- [ ] **Requester: escalate to <to be confirmed> if no confirmation is received by <to be confirmed>.** The archive shows escalation happening but not the owner or the timing.

## Recommended change

Add a validation at deal entry that blocks or warns on a price of zero and on a price identical to the prior flow month's rate for the same deal. Prices are re-set per flow month, so an unchanged rate is the single most common failure mode this checklist exists to clean up.

Run a nightly exception query over deals for the current flow month that flags three conditions: price of zero, price unchanged from the prior month, and price divergent from the quoted or billed value. Mail the exception list to the deal owner before the morning flash report is produced, so the correction happens ahead of the revenue figure rather than behind it.

Move the price-change request out of mail and onto the deal. Log the requested price, the requester, the flow month, the editor and the completion timestamp as a record attached to the deal, so the audit trail does not depend on someone keeping the thread.

Where a deal genuinely cannot be reopened, record the fixed-price workaround as an explicit annotation on the original deal, naming who agreed it. Today the source record stays wrong and only the workaround is correct.

Publish one owner for Sitara price edits and one escalation path with a stated response window, so requesters know who to chase and when.

## Open questions

- Who is the named owner for Sitara price edits, and is it one person or a rota? The archive shows several people making the edit but no assigned role.
- What is the cutoff, if any, for getting a price correction in before the morning flash report is produced? A correction was chased against the flash, but no time was stated [cit_5160f9a064ab].
- Which deals can be reopened and which cannot, and what rule decides? The archive shows the fixed-price workaround used only when the deal could not be fixed, without stating the constraint [cit_9fed7efcaa12].
- Whether a corrected price in Sitara triggers a re-bill automatically or whether billing must be told separately.
- Whether any approval is needed before a price is edited, and by whom.
