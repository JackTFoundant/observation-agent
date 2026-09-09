---
artifact_id: RUN-01
title: 'Runbook: Scheduled-versus-Actual Volume Exceptions'
artifact_type: runbook
opportunity_id: proc_4a1bc6bb6f
opportunity_title: Scheduled-versus-actual volume exceptions, reconciled by hand in
  Unify
generated_at: '2026-09-09T19:21:26.109287+00:00'
generator: claude -p via .claude/agents/artifact-drafter.md
review_status: draft-unreviewed
evidence:
- cit_0c3312966342
- cit_100761050290
- cit_2bf3be959cdb
- cit_30fedd9d1441
- cit_3251de1464be
- cit_7650ee9d60f9
- cit_96657bd2123f
- cit_dcc1e1ea7478
below_threshold_judgment_call: false
---

> **Draft, not reviewed.** Every sentence describing current practice carries a
> citation id that resolves to a verified quote from the archive. Sentences under
> *Recommended change* are proposals and carry no citation. Nobody who does this
> work has read this document.

## Purpose

This runbook covers the handling of a single volume exception: a meter, contract or deal where the actual measured volume does not agree with what was scheduled, nominated or confirmed. It describes how the exception is worked today, and proposes a change to how breaks are found and routed.

## Scope

In scope: scheduled-versus-actual and scheduled-versus-allocated breaks on gas deals and meters, including breaks found after month-end allocations arrive from a pipeline counterparty. Systems in scope are the ones named in the mail: Unify, Sitara, MOPS, and the ENA books. Out of scope: nomination changes made before flow date, and pipeline OFO handling.

## Current practice

A break is raised in plain text by whoever notices it, naming the contract and stating that the actuals did not arrive as scheduled [cit_30fedd9d1441]. Some breaks are total rather than partial: a deal is scheduled at volume and then actualized at zero, and the finder records only that the person who spotted it thinks the result is incorrect [cit_2bf3be959cdb]. Others are partial and are framed as a comparison between what scheduling confirmed and what actually flowed [cit_0c3312966342].

The finder is usually not the person who can fix the record. The mail therefore asks a named colleague to make the change in the system of record — "will you please make the necessary changes in unify" [cit_7650ee9d60f9]. Corrections are also driven the other way, by a counterparty's allocation: a request comes in to go back into a closed month and adjust estimated volumes in Unify to match what the pipeline shows was allocated [cit_100761050290]. Where the record lives in MOPS, the owner reports back that the volumes have been corrected there [cit_96657bd2123f].

Threads stall on two things. First, on counterparty or internal response: the numbers are sent back to the other side and nothing comes back [cit_dcc1e1ea7478]. Second, on ownership of the underlying problem, which is escalated in the mail as an open question rather than assigned — "Why is nothing being allocated to Alpine? This is a good deal we have in place with them and I really need the problem resolved" [cit_3251de1464be].

## Procedure

1. **Identify the break.** Record the contract, deal number or meter, and both sides of the volume: what was scheduled or confirmed, and what was actualized or allocated [cit_0c3312966342].
2. **State the direction of the error.** Note whether actuals failed to arrive as scheduled [cit_30fedd9d1441], or arrived at zero against a scheduled volume [cit_2bf3be959cdb].
3. **Name the system of record for this deal.** The correction is made in Unify [cit_7650ee9d60f9], in MOPS [cit_96657bd2123f], or against the estimated volumes held for the affected month [cit_100761050290]. Where the deal spans systems, the owning system is `<to be confirmed>`.
4. **Send the correction request to a named person, not a group.** Ask explicitly for the change to be made in the named system [cit_7650ee9d60f9].
5. **If the break depends on a counterparty allocation, send that side your numbers and record the date sent.** Chase if no reply is received, because unanswered allocation mail is where these threads sit [cit_dcc1e1ea7478].
6. **Make the adjustment in the prior period.** Where the counterparty's allocation governs, adjust the month's estimated volumes to match what the pipeline allocated [cit_100761050290].
7. **Close the thread with a status note naming the system and confirming the volumes were corrected** [cit_96657bd2123f].
8. **Escalate when the break is structural rather than clerical** — for example when nothing at all is being allocated to a counterparty on a live deal [cit_3251de1464be]. The escalation path and the arbiter between scheduling and allocation are `<to be confirmed>`.

## Recommended change

Run a scheduled comparison, per meter and per deal, that pulls scheduled, confirmed and actualized volumes from Unify, Sitara and MOPS alongside the counterparty's allocation file. Flag only the breaks above an agreed tolerance; set the tolerance jointly with allocations and scheduling before the first run, and publish it.

Route each flagged break to a single named owner derived from the deal record, with the counterparty allocation attached. The mail should then carry a decision to be made, not a discovery to be investigated.

Maintain a break log keyed on deal number. Each entry should hold: the break as found, the system corrected, the adjusted volume, the person who made the adjustment, and the date. This removes the need to re-key the same volumes into a second system and gives month-end close a single list to work from.

Add a chase rule for allocation disputes: if a counterparty has not replied to a numbers-back mail by an agreed offset, the log escalates it automatically rather than relying on the sender to remember.

Name an arbiter for scheduling-versus-allocation disagreements and record that role in this runbook, so a break like the Alpine case has a defined destination rather than an open question in a thread.

## Open questions

- Which system is authoritative when Unify, Sitara, MOPS and the ENA books hold different volumes for the same deal. The archive shows corrections made in each, but no rule for choosing.
- Whether there is any tolerance below which a break is not worked. None is stated in the mail.
- Who owns the final adjustment for a closed month, and who authorises reopening it.
- The cutoff, if any, after which a prior month can no longer be re-posted.
- The escalation path when a counterparty does not respond to an allocation query.
- Whether the meter exception report that surfaces these breaks is generated on a fixed schedule, and by whom.
