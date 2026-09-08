---
artifact_id: RUN-02
title: 'Runbook: Clearing Meter-Level Scheduled-vs-Actual Variances (Unify / Sitara
  / UA4)'
artifact_type: runbook
opportunity_id: proc_8381da9a4e
opportunity_title: Meter-level scheduled-vs-actual variance clearing across Unify,
  Sitara and UA4
generated_at: '2026-09-08T21:38:37.779424+00:00'
generator: claude -p via .claude/agents/artifact-drafter.md
review_status: draft-unreviewed
evidence:
- cit_209530865957
- cit_4f38de347e69
- cit_b4d145322843
- cit_b797721182bf
- cit_c5f04fa8a216
- cit_d669d2b2ccdd
- cit_db35c6ff71bc
- cit_dcfae4792d49
below_threshold_judgment_call: false
---

> **Draft, not reviewed.** Every sentence describing current practice carries a
> citation id that resolves to a verified quote from the archive. Sentences under
> *Recommended change* are proposals and carry no citation. Nobody who does this
> work has read this document.

## Purpose

This runbook describes how a meter-level variance between scheduled or confirmed volume and pipeline-allocated actual volume is currently cleared, and proposes a tracked process to replace the mail thread. It is written for whoever owns the monthly imbalance check on the logistics desk.

## Scope

Covers variances at a single meter for a single production month, surfaced by the UA4 report or a meter exception report, where the fix is a contract, a purchase, a reallocation, or an adjustment to estimated volumes in Unify. Covers interconnect variances between affiliated pipelines. Does not cover trade capture in Sitara, price disputes, or settlement payment mechanics beyond the point where the variance blocks them.

## Current practice

A variance is identified from a report listing meters with differences, and the report holder mails the meters onward for review [cit_b797721182bf]. Some meters appear on the report as new points with flow that cannot be allocated, and the fix requested is a purchase for each meter [cit_d669d2b2ccdd]. Other cases show scheduling confirming one volume at a point while a much smaller volume actually flowed [cit_b4d145322843]. Where the variance cannot be resolved at once, the meter is reallocated as a temporary fix and the total flow is given to one party [cit_dcfae4792d49].

Estimated volumes carried in Unify are corrected by hand, month by month, to match what the pipeline shows was allocated [cit_4f38de347e69]. That correction request arrives by email and is passed on by forwarding the earlier mail into the next one [cit_4f38de347e69]. Supporting figures are obtained from the counterparty pipeline by asking for meter statements to be faxed for the month in question [cit_db35c6ff71bc]. Those statements are then used to work out which meters flowed over what was nominated [cit_db35c6ff71bc].

Requests routinely go unanswered: counterparty numbers were mailed back to the other side with no reply received [cit_209530865957]. The same interconnect recurs: the nomination difference between two affiliated pipelines is described as an ongoing issue every month [cit_c5f04fa8a216].

## Procedure

1. Pull the variance list. Take the meters showing variances from the UA4 report or meter exception report for the production month [cit_b797721182bf].
2. Split the list by fix type. Separate new meters with unallocatable flow, which need a purchase booked per meter [cit_d669d2b2ccdd], from meters where confirmed and flowed volumes disagree [cit_b4d145322843].
3. Get the counterparty numbers. For interconnect and affiliate points, request the meter statements for the month from the other pipeline; today this is a fax request [cit_db35c6ff71bc]. Use them to identify which meters flowed over nomination [cit_db35c6ff71bc].
4. Assign the owner. Route each meter to the person who can supply the contract, purchase or explanation; record that the counterparty numbers were sent and whether a reply came back [cit_209530865957].
5. Apply the interim fix where the item must come off the exception list before it is explained. Reallocate the meter and assign the total flow to one party, and mark the item as temporary [cit_dcfae4792d49].
6. Apply the system-of-record fix. Adjust the estimated volumes in Unify for the month so they match what the pipeline shows was allocated [cit_4f38de347e69]. Sitara-side correction path and the cutoff for the month's adjustment window: `<to be confirmed>`.
7. Flag repeats. Mark points that are known to differ every month, such as the standing nomination difference between the two affiliated pipelines, so the next month's list is not worked from scratch [cit_c5f04fa8a216].

## Recommended change

Run a scheduled comparison that joins nominated and confirmed volumes to pipeline-allocated actuals, keyed on meter and production month, and publish it in place of the mailed exception list.

For each unmatched meter, open a tracked item that carries five fields: meter number, production month, responsible scheduler, required fix (contract, purchase, reallocation, Unify adjustment), and current state. Close the item only when the fix is booked, and close temporary reallocations separately from permanent fixes so an interim allocation is never mistaken for a resolution.

Make ownership visible outside mail. The tracked item should name a single accountable scheduler on creation, and reassignment should be an action on the item rather than a forwarded email.

Set an escalation rule on age. Any item still open into the next production month, or any item where counterparty figures have been sent without a reply, should move to a named escalation owner automatically.

Replace the fax loop for counterparty meter statements with a scheduled file or data exchange with the affiliated pipeline, so the comparison can run without a manual document request.

Maintain a repeat-offender list. Where the same meter, contract or interconnect appears in consecutive months, route it to a standing fix — a contract change or a corrected allocation rule — rather than re-clearing the same exception.

Report back-period items separately from the current month, so items for prior years are not buried under fresh exceptions.

## Open questions

- The monthly cutoff for adjusting estimated volumes in Unify is not stated in the archive.
- The Sitara-side correction path, and whether Sitara or Unify is treated as system of record for the adjusted estimate, is not stated.
- Who owns the recurring imbalance check by role, as opposed to whoever last held the thread, is not established anywhere in the archive.
- The tolerance below which a meter variance is ignored rather than worked is not stated.
- The approval needed to book a purchase for a new meter with unallocatable flow is not stated.
- How a temporary reallocation is subsequently reversed and re-booked to the correct party is not described.
- Whether the UA4 report and the meter exception report are the same list under two names, and who generates each, is not established.
