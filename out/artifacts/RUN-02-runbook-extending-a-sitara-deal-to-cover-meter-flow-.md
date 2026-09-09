---
artifact_id: RUN-02
title: 'Runbook: Extending a Sitara deal to cover meter flow outside the deal term'
artifact_type: runbook
opportunity_id: proc_f416357f1e
opportunity_title: Extending Sitara deals by request to cover unallocated meter flow
generated_at: '2026-09-09T15:14:10.181354+00:00'
generator: claude -p via .claude/agents/artifact-drafter.md
review_status: draft-unreviewed
evidence:
- cit_23ba30ad80ce
- cit_4bfbff6103a8
- cit_6a0022ab9d63
- cit_9f0498ab829a
- cit_d1512f9b2bae
- cit_d73baaf8565e
- cit_da672f3158ef
- cit_f79c9932ff41
below_threshold_judgment_call: false
---

> **Draft, not reviewed.** Every sentence describing current practice carries a
> citation id that resolves to a verified quote from the archive. Sentences under
> *Recommended change* are proposals and carry no citation. Nobody who does this
> work has read this document.

## Purpose

Give the deal owner and the requester one agreed path for the case where gas allocated at a meter falls outside the term of the deal that should cover it. The request is made so that Volume Management can create an accounting arrangement against the deal [cit_d73baaf8565e]. Without the extension the requester's stated fallback is to allocate the gas off to strangers [cit_4bfbff6103a8].

## Scope

Covers single meter-days and short tail-flow periods found during allocation, where the fix is either extending the existing deal or putting a different deal in place [cit_d1512f9b2bae]. Covers requests raised by Volume Management, Logistics and schedulers to the deal owner by email [cit_f79c9932ff41]. Does not cover pathing held outside Unify in legacy systems; one thread found June 1999 pathing sitting in Autonoms, which was not Y2K compatible, and that is a separate remediation [cit_9f0498ab829a].

## Current practice

The requester finds volume allocated at a meter on a date the deal does not cover and emails the deal owner with the meter, the deal, the dates and the volume, asking that the deal be extended so Volume Management can create an accounting arrangement [cit_f79c9932ff41]. Where the exposure runs to the end of a month the ask is phrased as extending the deal through that date, again so Volume Management can build the arrangement [cit_d73baaf8565e]. The cause is often physical: a scheduler reports that the deal needs extending because the valve was not completely shut [cit_da672f3158ef].

The requester cannot make the change and the item waits on the deal owner, so Logistics states in writing that it is waiting to hear from the deal owner, and that he will either need to extend the deal or another deal should be put in place [cit_d1512f9b2bae]. Urgency is added by naming a manager who has asked that the issue be resolved that day [cit_6a0022ab9d63]. The same deal is reopened repeatedly; one request asks the owner to extend the deal "one more time for me" for a prior month-end date [cit_23ba30ad80ce]. Where the requester sees no other option the mail puts the two outcomes side by side: extend the deal, or allocate off to strangers [cit_4bfbff6103a8].

Discovery is late rather than continuous, and old flow dates surface long after the fact, including flow whose pathing was never in Unify [cit_9f0498ab829a].

## Procedure

1. **Requester (Volume Management, Logistics or scheduler)** — identify the meter, the flow date or dates, the allocated volume and the deal number that should cover them [cit_f79c9932ff41].
2. **Requester** — email the deal owner with those four items and state the reason for the ask, which is that Volume Management needs the deal term to cover the flow before it can create an accounting arrangement [cit_d73baaf8565e].
3. **Requester** — where the cause is known, say so in the same mail, for example tail flow because a valve was not completely shut [cit_da672f3158ef].
4. **Deal owner** — decide between extending the existing deal and putting a different deal in place, and reply with the decision [cit_d1512f9b2bae].
5. **Deal owner** — make the change in Sitara and confirm it is reflected in Unify; the screen and the field used for the deal end date are `<to be confirmed>`.
6. **Requester** — on receiving the reply, ask Volume Management to create the accounting arrangement against the extended deal [cit_d73baaf8565e].
7. **Requester** — if no reply arrives, escalate by restating that the item is waiting on the deal owner and naming the manager who wants it resolved [cit_6a0022ab9d63]. The escalation path and the wait before escalating are `<to be confirmed>`.
8. **Requester** — if the deal is not extended, record the alternative disposition, which today is allocating the volume off to strangers [cit_4bfbff6103a8].
9. **Requester** — if the flow date predates the deal's presence in Unify, raise it as a legacy pathing item rather than a deal extension [cit_9f0498ab829a].

## Recommended change

Build an exception report that joins allocated meter volumes to deal start and end dates and lists every meter-day with flow outside its deal term. Route each exception to the deal owner as a queue item with deal number, meter, flow dates and allocated volume already populated, so the requester is not composing free-text mail.

Give the queue an in-system extend action, plus a second action for "different deal required" that routes back to the requester. Log both outcomes against the deal so repeat extensions on the same deal are visible without searching mail.

Run the report every allocation cycle so tail flow is found in the cycle it occurs rather than months later. Add a rule that flags meters with repeat exceptions to the scheduler who operates the valve, so the physical cause is fixed and not just the deal term.

Route the queue to a role, not a named individual, with a backup holder, so no item sits in one inbox. Set an explicit service target for the deal owner's response and an automatic escalation when it is missed, replacing the current practice of restating the ask by mail.

Exclude flow whose pathing never reached Unify from the extension queue and send it to a separate legacy remediation list.

## Open questions

- Which Sitara screen and field the deal end date is changed on, and whether the change propagates to Unify automatically or needs a manual step.
- Who is authorised to extend a deal besides the named deal owner, and whether a backup exists.
- The agreed escalation path and the point at which a waiting item is escalated.
- What "allocate off to strangers" resolves to downstream, and what has to be unwound if the deal is extended after that allocation is made.
- Whether any tolerance exists below which a deal is not extended at all, and who sets it.
- Whether Volume Management's accounting arrangement can be created before the deal term is corrected, or only after.
- The current status of legacy pathing held outside Unify, and who owns it.
