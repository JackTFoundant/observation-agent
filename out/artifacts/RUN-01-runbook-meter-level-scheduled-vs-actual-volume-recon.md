---
artifact_id: RUN-01
title: 'Runbook: Meter-Level Scheduled-vs-Actual Volume Reconciliation'
artifact_type: runbook
opportunity_id: proc_b166bd1e99
opportunity_title: Meter-level scheduled-versus-actual volume reconciliation, chased
  by email
generated_at: '2026-09-08T21:33:08.382442+00:00'
generator: claude -p via .claude/agents/artifact-drafter.md
review_status: draft-unreviewed
evidence:
- cit_09fc9ddbd230
- cit_209530865957
- cit_24690dcd052f
- cit_351a8b5f945e
- cit_4909514b81ad
- cit_87ffd855b230
- cit_b3c317b28b19
- cit_dcfae4792d49
below_threshold_judgment_call: false
---

> **Draft, not reviewed.** Every sentence describing current practice carries a
> citation id that resolves to a verified quote from the archive. Sentences under
> *Recommended change* are proposals and carry no citation. Nobody who does this
> work has read this document.

## Purpose

This runbook covers the handling of a single meter-level volume variance: the case where the volume scheduling nominated or confirmed does not agree with the volume the measurement or allocation source reports as flowed. It describes how the variance is worked today, gives the step order, and separates that from proposed changes. The end state of a variance is a corrected volume in the affected system so that the month's allocations and invoices can close.

## Scope

In scope: variances at a named meter for named days, chased between Enron scheduling, logistics, gas accounting, and an external counterparty or pipeline. Systems in scope are Sitara, Unify, POPS, and counterparty-supplied reports. Out of scope: nomination entry itself, capacity release, and OFO handling.

## Current practice

A variance is raised by naming the meter, the period, and the two figures that disagree — for example, a PG&E Service Summary Report showing a flow of 50,000 mmbtus on the 24th against Swamp Rat Fuel Allocations (HPL) indicating 53,000 mmbtus [cit_351a8b5f945e]. The raiser mails the party believed able to explain the gap and asks them to get the counterparty to confirm which volume is correct, so that the month's allocations can be finalised [cit_b3c317b28b19]. Variances are also raised from the scheduling side, where a confirmed quantity is compared against measured flow and the mismatch is called out in the mail body — "it seems odd to me that scheduling had 8,928 MMBtu confirmed at this point and only 646 MMBtu flowed" [cit_09fc9ddbd230].

Resolution is a manual keying job in the downstream system: one party is asked to go into Unify for the month of October and adjust the estimated volumes to match what HPL shows [cit_4909514b81ad]. Where the correct split cannot be agreed, the meter is adjusted as a workaround instead — "As a temporary fix I reallocated the meter and gave the total flow to Alpine Resources" [cit_dcfae4792d49].

Threads stall waiting on the second party's confirmation, and the wait is recorded in the mail itself: "I sent Jackie Young an email back showing her TETCO's numbers and I haven't received a response." [cit_209530865957]. Open items are tracked as a list held by the person chasing, who asks for resolution "as soon as possible so that we could clear this off our list" [cit_24690dcd052f]. Items stay on that list across accounting periods; an exception at meter 4045 for 2/99 was still being worked, and clearing it required an ECT transport delivery [cit_87ffd855b230].

## Procedure

1. **Identify the variance.** Compare the confirmed scheduled quantity against the measured or allocated quantity for the meter and day, and state both figures explicitly in the mail [cit_09fc9ddbd230].
2. **Name the two sources.** Record which report each figure came from — for example the counterparty's Service Summary Report versus the internal fuel allocation report — so the disagreement is between two identified sources, not two numbers [cit_351a8b5f945e].
3. **Send the confirmation request.** Mail the party who can reach the counterparty, ask them to confirm which volume is correct, and state the allocation deadline that depends on the answer [cit_b3c317b28b19]. Copy the internal owner of the meter `<to be confirmed>`.
4. **Log the item on the open exception list.** Carry the meter number and the period on the list, and reference the list when chasing so the recipient knows the item is outstanding [cit_24690dcd052f].
5. **Chase if no confirmation returns.** Re-send the figures and record in the thread that the earlier mail went unanswered [cit_209530865957]. Chase interval: `<to be confirmed>`.
6. **Apply the agreed correction.** Once the correct figure is agreed, adjust the volumes by hand in the downstream system for the affected month so they match the source of record [cit_4909514b81ad].
7. **If no agreement is reached, apply a documented workaround.** Reallocate the meter and assign the flow to a party, and state in the thread that the reallocation is a temporary fix [cit_dcfae4792d49].
8. **Close the item.** An exception is only cleared when the supporting document exists — for meter 4045 for 2/99, an ECT transport delivery was required before the exception could be cleared [cit_87ffd855b230].

## Recommended change

- Build a scheduled comparison that pulls confirmed nomination volumes and measured or allocated volumes per meter per day from Sitara, Unify, POPS, and loaded counterparty reports, and posts only the rows that disagree beyond a tolerance. Set the tolerance per meter class and review it each quarter.
- Attach two fields to every posted exception row: the responsible party and the date the exception first appeared. Age, not volume, should drive the chase order.
- Replace the personal open-items list with one logged exception list, one row per meter-month, carrying a status (raised / awaiting counterparty / agreed / corrected / workaround applied / cleared). Chase mails should link to the row rather than restate the figures.
- Require that a workaround such as a manual meter reallocation sets the row status to "workaround applied" and leaves the row open, so the underlying variance is not lost when the month closes.
- When a correction is keyed in one system, raise a linked task in the others rather than assuming propagation. Until the systems reconcile automatically, the linked task is the only record that the same discrepancy will not resurface from a different source.
- Set an escalation rule: an exception with no counterparty confirmation after a fixed number of chases is routed to a named owner rather than re-chased by the raiser.

## Open questions

- Which system is the source of record when Sitara, Unify, POPS, and a counterparty report disagree. The archive shows corrections keyed into Unify to match an external figure, but not a general rule.
- What tolerance, if any, is applied before a variance is chased at all.
- The chase interval and the escalation path when a counterparty does not respond.
- Who owns the open exception list, and whether it is a shared artefact or held per person.
- The cutoff date within the monthly allocation cycle after which an unresolved variance must be worked as a prior-period adjustment.
- Whether the ECT transport delivery required to clear an exception is a standing mechanism for aged items or was specific to that meter and period.
