---
artifact_id: RUN-01
title: 'Runbook: Meter Volume Variance Reconciliation (Sitara / Unify / Pipeline Statements)'
artifact_type: runbook
opportunity_id: proc_df90b91705
opportunity_title: Scheduled-versus-actual meter volume reconciliation across Unify,
  Sitara and HPL
generated_at: '2026-09-09T14:58:30.389120+00:00'
generator: claude -p via .claude/agents/artifact-drafter.md
review_status: draft-unreviewed
evidence:
- cit_0c3312966342
- cit_100761050290
- cit_209530865957
- cit_3251de1464be
- cit_410f90f80c03
- cit_6798dfc1be32
- cit_8083160ef7e3
- cit_db35c6ff71bc
below_threshold_judgment_call: false
---

> **Draft, not reviewed.** Every sentence describing current practice carries a
> citation id that resolves to a verified quote from the archive. Sentences under
> *Recommended change* are proposals and carry no citation. Nobody who does this
> work has read this document.

## Purpose

Give the logistics desk a single working procedure for handling a scheduled-versus-actual volume exception on a meter, from the moment the variance is raised to the moment the corrected volume is entered and the requester is told it is done.

## Scope

Covers meter-level variances between nominated, confirmed, scheduled and allocated volumes where the disagreeing figures sit in Sitara, in Unify, or on a pipeline or counterparty meter statement. Covers exceptions raised by a scheduler, a volume-management or accounting contact, or a counterparty. Covers month-end restatement of estimated volumes. Does not cover price or invoice disputes, and does not cover physical measurement equipment faults beyond identifying them as the cause.

## Current practice

An exception is raised by mail naming the meter and the period, in the form "There is an interconnect variance at meter 980071 for 2/99." [cit_8083160ef7e3]. The two disagreeing figures are stated in the same message, for example that scheduling "had 8,928 MMBtu confirmed at this point and only 646 MMBtu flowed" [cit_0c3312966342], or that one side sent a volume "but HPL does not show a receipt of this volume." [cit_410f90f80c03].

Some exceptions are not one-off: the desk carries a known repeat, described as "an ongoing issue every month between what we nominate from GEPL into HGPL and on to King Ranch (flows into HGPL at meter 8284) and what is in the system as purchase gas upstream of the meter." [cit_6798dfc1be32].

The desk cannot settle the variance from its own records and asks the other party for the source document, by fax: "Would you please fax the meter statements from GEPL for February so that I can try to determine which meters are flowing over what is nominated" [cit_db35c6ff71bc].

Resolution can require restating a whole month by hand, described as being asked "to go in for the month of October and adjust all of my estimated volumes in Unify to match what HPL shows that we were allocated" [cit_100761050290].

Threads stall when the other party does not reply, and are re-opened by restating the unanswered question: "I sent Jackie Young an email back showing her TETCO's numbers and I haven't received a response." [cit_209530865957]. Escalation is also raised on commercial grounds when nothing is being allocated at all: "Why is nothing being allocated to Alpine? This is a good deal we have in place with them and I really need the problem resolved." [cit_3251de1464be].

## Procedure

1. **Log the exception.** Record the meter number and the affected period exactly as raised, in the form used today: meter id plus month [cit_8083160ef7e3]. If the raiser gave only a narrative, get the meter id before doing anything else.

2. **Capture both figures.** Write down the two numbers that disagree and which side each came from — confirmed/scheduled against flowed [cit_0c3312966342], or delivered against received where the downstream pipeline shows no receipt [cit_410f90f80c03].

3. **Check whether this meter is a known repeat.** Some meters produce the same gap every month between what is nominated across the interconnect and what the system holds as purchase gas upstream [cit_6798dfc1be32]. If it is a repeat, attach the prior month's thread rather than starting a fresh investigation.

4. **Request the source statement from the party that holds it.** Ask for the meter statements for the specific month so you can determine which meters are flowing over what was nominated [cit_db35c6ff71bc]. Record the request date; the acknowledged delivery channel today is fax [cit_db35c6ff71bc].

5. **Chase on a fixed interval.** Where no response has come back, the current escalation is to restate the position and say plainly that no answer has been received [cit_209530865957]. Chase interval: `<to be confirmed>`.

6. **Determine the side that is wrong.** Compare the received statement against the internal figures. If nothing at all is allocating to a counterparty, treat it as a commercial escalation, not a rounding difference [cit_3251de1464be].

7. **Enter the correction.** Where the internal estimate is the wrong side, adjust the estimated volumes in Unify for the affected month so they match the allocated volumes shown by the pipeline [cit_100761050290]. Approver for a month-level restatement: `<to be confirmed>`.

8. **Close the loop.** Reply to the person who raised the exception with the meter, the period, the cause, and the figure now standing. Attach the statement you relied on.

## Recommended change

- Run a scheduled comparison per meter that pulls confirmed and scheduled volumes from Sitara, posted volumes from Unify, and allocated volumes from the pipeline statement, and emits a dated exception list naming the meter, the flow days and the disagreeing figures. The desk should start each day from that list rather than from an inbound mail.
- Flag on the exception list any meter that appeared on the previous month's list, so known repeats are visibly separated from new breaks and can be worked as a standing item.
- Replace the fax request for meter statements with a standing arrangement for a fixed electronic file from each counterparty and pipeline, delivered on a set day of the month, loaded automatically.
- Create a logged adjustment path for month-end restatements in Unify: one entry per adjustment, carrying the meter, the period, the source document and the person who entered it, so a restatement can be re-traced without reading the mail thread.
- Set a written chase interval and an escalation owner for unanswered statement requests, so a stalled thread escalates on a schedule instead of when someone remembers.
- Route "nothing is allocating" cases down a separate path from quantity variances. A total absence of allocation is a deal or setup fault and should be triaged by whoever owns the deal record, not investigated as a measurement difference.

## Open questions

- The chase interval for an unanswered statement request is not stated in the archive.
- Who approves a month-level restatement of estimated volumes in Unify, and whether any approval is required at all, is not stated.
- Whether the corrected volume must also be restated in Sitara once Unify is adjusted, or whether Unify alone is authoritative for the actualized figure, is not determined.
- The cutoff after which a month is considered closed and can no longer be restated is not stated.
- Which meters carry a standing known variance, beyond the GEPL/HGPL/King Ranch interconnect at meter 8284, is not enumerated anywhere in the archive.
- Whether an exception report already exists that lists these breaks, and who reads it, could not be determined.
