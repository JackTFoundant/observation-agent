---
artifact_id: RUN-01
title: 'Runbook: Extending an existing deal ticket to cover unbooked meter flow'
artifact_type: runbook
opportunity_id: proc_7dd2a1eead
opportunity_title: Extending existing deal tickets in Sitara/Unify to cover unbooked
  meter flow
generated_at: '2026-09-08T20:58:42.793430+00:00'
generator: claude -p via .claude/agents/artifact-drafter.md
review_status: draft-unreviewed
evidence:
- cit_4f3610f710eb
- cit_79ccf0623d7f
- cit_969179cf132d
- cit_9e9ab1d61248
- cit_9f0498ab829a
- cit_d239579d3927
- cit_d73baaf8565e
- cit_e82f53b88502
below_threshold_judgment_call: true
---

> **Draft, not reviewed.** Every sentence describing current practice carries a
> citation id that resolves to a verified quote from the archive. Sentences under
> *Recommended change* are proposals and carry no citation. Nobody who does this
> work has read this document.

## Purpose

This runbook covers uncovered meter flow: gas measured at a meter with no deal or nomination behind it. It describes how the gap is closed today by extending an existing deal ticket rather than writing a new deal, and what to check before the thread is closed.

## Scope

Applies to gas logistics and volume reconciliation staff who find unbooked flow at a meter and need coverage in Sitara so the record reaches Unify and Volume Management can create an accounting arrangement [cit_79ccf0623d7f]. Covers single flow days, part months, and multi-month gaps [cit_969179cf132d] [cit_e82f53b88502]. Does not cover new deal creation, and does not cover flow periods predating the desk's move onto Unify, where no clean record exists to extend against [cit_9f0498ab829a].

## Current practice

When uncovered flow is found, the reconciler identifies the last deal used on that meter and mails the deal owner asking for it to be extended [cit_d239579d3927]. The request states the coverage needed, either a date range through a month end [cit_d73baaf8565e], a named set of flow months [cit_e82f53b88502], or a single flow date with the volume [cit_969179cf132d]. The stated reason for the extension is to let Volume Management create the accounting arrangement against it [cit_d73baaf8565e]. Volume Management holds the accounting arrangements until the requester reports back on deal status [cit_79ccf0623d7f].

After the request, the requester checks Unify and often finds nothing there, and re-opens the same thread to ask whether the edit was made against the same deal ticket [cit_4f3610f710eb]. The deal system and Unify do not confirm the extension back to the requester, so this check is made by hand and chased by mail [cit_4f3610f710eb]. Where the flow date is old, the thread escalates on the age of the discovery itself [cit_9e9ab1d61248]. In one such case the answer was that the desk was not on Unify for that flow month and its pathing sat in Autonoms, which is not Y2K compatible [cit_9f0498ab829a].

## Procedure

1. Identify the meter and the uncovered flow dates from the reconciliation pass, and record the last deal used on that meter [cit_d239579d3927].
2. Mail the owner of that deal. Give the deal number and the exact coverage required: a through-date [cit_d73baaf8565e], the flow months [cit_e82f53b88502], or the single flow date and volume [cit_969179cf132d].
3. State in the same message that the extension is needed so Volume Management can create the accounting arrangement [cit_d73baaf8565e].
4. Wait for the deal owner to confirm the extension, and tell Volume Management the deal status so the arrangements can be raised and the item cleared [cit_79ccf0623d7f].
5. Check the downstream system. If the deal has not appeared, reply on the same thread and ask explicitly whether the same deal ticket was used [cit_4f3610f710eb]. Retry interval and number of chases: `<to be confirmed>`.
6. If the flow period predates the desk's move onto Unify, stop the extension route and escalate, because the pathing for that period is held in Autonoms and there is no Unify record to extend [cit_9f0498ab829a]. Escalation owner for aged flow: `<to be confirmed>`.
7. If the flow date is materially older than the current reconciliation period, flag the age of discovery when you raise the request, since that question is asked of the requester anyway [cit_9e9ab1d61248].

## Recommended change

Build a standing exception report that matches measured meter volumes against booked deal coverage. For each uncovered flow date it should list the meter, the dates, the volume, and the last deal used on that meter — the three facts the requester currently reconstructs by hand before writing the mail. The report should be the source of the request, so the mail becomes a pre-filled ticket rather than a fresh piece of research.

Add a propagation notice. When an extended deal lands in Unify, send an automatic message to the original requester and to Volume Management. That removes the "has this shown up yet" round trip and the follow-up question about which ticket was edited, because the notice names the ticket.

Include the deal ticket number as a required field on the extension request, and echo it back in the confirmation. The recurring failure is not the edit, it is the uncertainty about which ticket the edit hit.

Add an age flag to the exception report. Any uncovered flow date older than the current reconciliation cycle should route to a named escalation owner rather than to the deal owner, and should carry a check for whether the period sits in a superseded pathing system where extension is not possible.

Give Volume Management a status view of open extension requests instead of waiting to be told the deal status by mail.

## Open questions

- Which team or role owns the deal ticket in Sitara for a given meter, and how the requester currently identifies that owner.
- The expected lag between a Sitara extension and its appearance in Unify, and therefore when a chase is justified.
- How many chases are sent before the request is escalated, and to whom.
- The named escalation owner for flow periods held in a superseded pathing system.
- Whether a new deal is ever written instead of an extension, and what decides between the two.
- Where the uncovered-flow list comes from today, and on what cycle the reconciliation pass runs.
