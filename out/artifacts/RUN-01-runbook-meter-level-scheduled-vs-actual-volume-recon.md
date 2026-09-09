---
artifact_id: RUN-01
title: 'Runbook: Meter-Level Scheduled-vs-Actual Volume Reconciliation'
artifact_type: runbook
opportunity_id: proc_6b088700a9
opportunity_title: Meter-level scheduled-vs-actual volume reconciliation, chased by
  email
generated_at: '2026-09-09T15:14:10.179349+00:00'
generator: claude -p via .claude/agents/artifact-drafter.md
review_status: draft-unreviewed
evidence:
- cit_0c3312966342
- cit_100761050290
- cit_209530865957
- cit_3251de1464be
- cit_6832f6dbe2bd
- cit_787c9faab285
- cit_a0639d71e038
- cit_bcdc65d67989
below_threshold_judgment_call: false
---

> **Draft, not reviewed.** Every sentence describing current practice carries a
> citation id that resolves to a verified quote from the archive. Sentences under
> *Recommended change* are proposals and carry no citation. Nobody who does this
> work has read this document.

## Purpose

This runbook covers what to do when the gas volume recorded at a meter does not match what was nominated, confirmed, or entered as a deal. It documents how the exception is raised, agreed, and corrected today, and where the handling stops. It is written for whoever owns gas logistics and volume reconciliation for the affected meters.

## Scope

In scope: meter-level differences between scheduled or confirmed volumes and actualised or allocated volumes; recorded flow with no matching deal; prior-period adjustments made to match a pipeline or counterparty allocation; related OBA measured-versus-scheduled histories. In scope systems: Unify, POPS, Sitara, spreadsheets, email, and fax. Out of scope: same-day nomination cutoffs, capacity release, and credit reporting.

## Current practice

The exception is usually noticed by a person reading two figures side by side and finding them implausible, for example scheduling showing 8,928 MMBtu confirmed at a point against 646 MMBtu flowed [cit_0c3312966342]. Another form of the same exception is a deal receiving no allocation at all, raised as a commercial problem rather than a data problem: "Why is nothing being allocated to Alpine? This is a good deal we have in place with them and I really need the problem resolved." [cit_3251de1464be]. A third form is a difference between scheduled and actual deliveries on a named contract, stated as both figures at once — scheduled deliveries at Texoma of 374,503 against actuals of 352,568 [cit_bcdc65d67989].

The finder cannot close the exception alone. The request that goes out asks the other party first to agree the figure and then to make the edit: "can you let me know first if you agree with PG&E Texas numbers and if you do, will you please make the necessary changes in unify." [cit_6832f6dbe2bd]. Resolution takes the form of a person going back into a volume system and re-keying prior-period numbers to match an allocation, described in one case as being asked "to go in for the month of October and adjust all of my estimated volumes in Unify to match what HPL shows that we were allocated" [cit_100761050290].

Threads stall when the counterparty does not reply to the numbers sent over: "I sent Jackie Young an email back showing her TETCO's numbers and I haven't received a response." [cit_209530865957].

Bad volumes also reach the downstream system before anyone catches them, as when POPS carried a Saturday identical to the prior day: "We are getting bad numbers in POPS for Sat. Oct. 28th. They are the same as Oct. 27th (27th is correct)." [cit_a0639d71e038]. The control against this is manual vigilance passed on by instruction: "Please watch imbalances very closely. Double check all numbers." [cit_787c9faab285].

## Procedure

1. Identify the exception by comparing the confirmed or scheduled volume against the flowed volume at the meter, as is done today when a confirmed quantity is set against a much smaller flowed quantity [cit_0c3312966342]. Record both figures and the flow dates.
2. Check whether the meter has an allocation at all. Where a deal is receiving nothing, raise it as a commercial issue naming the counterparty and the deal [cit_3251de1464be].
3. State the two numbers explicitly in the request, in the form used today: scheduled deliveries at the point against actuals at the same point [cit_bcdc65d67989]. Include the meter number and the affected dates.
4. Send the request to the party who can agree the figure, asking for agreement first and the system edit second [cit_6832f6dbe2bd]. Name the system the edit is to be made in.
5. Where the correction is against a pipeline or counterparty allocation, apply it to the whole affected month in the volume system, matching the estimated volumes to what the allocating party shows [cit_100761050290]. Record who made the edit and on what date — the log location is `<to be confirmed>`.
6. If no reply arrives after the numbers have been sent, escalate. Today the escalation is a further email reporting the silence [cit_209530865957]. The escalation path and the addressee for it are `<to be confirmed>`.
7. Before relying on downstream volumes, check for repeated or copied days in the volume system, as in the case of a Saturday identical to the prior day [cit_a0639d71e038]. Where a day is suspect, watch the imbalance and double-check the numbers before further work is built on them [cit_787c9faab285].

## Recommended change

Run a scheduled comparison that joins nominated and confirmed volumes to actualised or allocated volumes, per meter per day, and emits an exception list. Each line should carry the meter, the flow dates, both figures, the deal number where one exists, and a missing-deal flag so a meter flowing without a deal appears in the same list. Route the list to a named owner per meter group rather than to a distribution list, so the exception arrives already quantified instead of being found by eye.

Add a duplicate-day check to the same job: flag any meter-day whose volume equals the prior day exactly, and hold it out of downstream reporting until a person clears it.

Replace the email-agreement-then-hand-edit loop with a logged adjustment path. The corrected volume should be entered once, carry the agreeing party and the source allocation, and be visible to both sides without a second re-key. Give each exception a state — raised, agreed, adjusted, disputed — and an owner, so an unanswered request surfaces as an ageing item rather than as a remembered email.

Publish the escalation route for unanswered counterparty requests, and name the system of record for prior-period adjustments so step 5 stops depending on who happens to know.

## Open questions

- Where an adjustment is made by hand, no log location is evident in the archive; it is unclear whether edits are recorded anywhere outside the volume system itself.
- The escalation addressee and the point at which an unanswered request should be escalated are not defined in the material reviewed.
- It is not established which system is authoritative when Unify, POPS, and Sitara disagree on the same meter-day.
- The route by which pipeline and counterparty allocations arrive, and whether any are received only by fax, is not determined.
- No cutoff or deadline for prior-period adjustment is visible; whether a closed month can still be adjusted is unknown.
