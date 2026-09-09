---
artifact_id: TPL-01
title: "Book Transfer Request \u2014 standing email template for moving deals between\
  \ trading books"
artifact_type: template
opportunity_id: proc_166c94f829
opportunity_title: Moving deals between trading books by hand-listed request
generated_at: '2026-09-09T14:58:30.386980+00:00'
generator: claude -p via .claude/agents/artifact-drafter.md
review_status: draft-unreviewed
evidence:
- cit_07186744ec2f
- cit_13b77360138d
- cit_2cf730fe5eda
- cit_72224f7dfa69
- cit_7882d24b6e38
- cit_82ca9725c333
- cit_ac1079e9161a
- cit_fc5549a67a69
below_threshold_judgment_call: false
---

> **Draft, not reviewed.** Every sentence describing current practice carries a
> citation id that resolves to a verified quote from the archive. Sentences under
> *Recommended change* are proposals and carry no citation. Nobody who does this
> work has read this document.

## Purpose

Give the person who owns a trading book one fixed form for asking the trading-system side to re-point a named set of deals from one book to another. The form replaces free prose plus an attached or pasted deal list. It is filled in by the requester, sent to the mover, and returned with a completion line so the request and the confirmation live in the same thread.

## Scope

Covers requests to move already-entered deals between books in Sitara: book consolidations, desk reorganisations, and the 2002 bankruptcy-book moves. Covers the follow-up mail that supplies deals missed in the first batch. Does not cover new deal entry, deal cancellation, or after-the-fact revenue reallocation between desks — those follow a different path and are noted under Open questions.

## Current practice

The request is sent as prose naming a source book and a target book, for example moving all deals currently in the INTRA-EMWMEH book into the FT-IM-ENOV book [cit_2cf730fe5eda]. Timing is stated in the same prose rather than as a required effective date, for example that the work is needed within the week if possible [cit_82ca9725c333]. Other requests name a book condition and a target instead of a deal list, such as moving any deals with the FT-TERMIN-GD book to the bankruptcy book from NG-Price [cit_07186744ec2f]. The requester does not always send everything in one message; a second mail follows with more stragglers to move into the bankruptcy books [cit_fc5549a67a69]. The mover cannot finish until the requester answers open questions about scope and target book, and has tied the expected completion of a deals move to getting those answers back [cit_ac1079e9161a]. After a bankruptcy-book move, the same deals are also added by hand to a cumulative deal report held on a shared drive, at `O:\_Dropbox\Global Contracts - Estate Research (CYN'S)\Deals Reported to Risk (Phy) Master Cumulative List.xls` [cit_13b77360138d]. Some of the traffic is a correction rather than a request: it records that deals should have been made under a different desk and acknowledges that this did not happen at entry [cit_7882d24b6e38]. In that case the fix is described in mail as a revenue move between desks after the deals were already booked [cit_72224f7dfa69].

## Template

Send one message per move. Do not mix a move request with a revenue correction.

```
Subject: Book transfer request — {{source_book}} to {{target_book}} — {{effective_date}}

Requester: {{requester_name}}, {{requester_desk}}
System: Sitara

1. SOURCE BOOK
   {{source_book}}

2. TARGET BOOK
   {{target_book}}
   Confirmed correct target? {{yes_no}}

3. WHAT MOVES  (fill in ONE of a or b)
   a) Named deals:
      {{deal_id}} | {{counterparty}} | {{flow_month}}
      {{deal_id}} | {{counterparty}} | {{flow_month}}
      {{deal_id}} | {{counterparty}} | {{flow_month}}
   b) Rule:  move any deals with book {{source_book}} to {{target_book}}
      from {{portfolio_or_desk}}

4. WHAT DOES NOT MOVE
   {{explicit_exclusions}}

5. EFFECTIVE DATE / NEEDED BY
   Effective date: {{effective_date}}
   Needed by: {{needed_by_date}}

6. IS THIS THE COMPLETE LIST?
   {{complete_or_more_to_follow}}
   If more to follow, reply on THIS thread with the additional deal ids.
   Do not open a new subject.

7. OPEN QUESTIONS THE MOVER SHOULD ASK NOW
   {{questions_for_requester}}

8. DOWNSTREAM REPORTING
   Add moved deals to the cumulative deal report on the shared drive?
   {{yes_no}}
   File: O:\_Dropbox\Global Contracts - Estate Research (CYN'S)\
         Deals Reported to Risk (Phy) Master Cumulative List.xls

-- MOVER COMPLETES BELOW AND REPLIES ON THIS THREAD --

Moved by: {{mover_name}}
Method: {{script_or_individual}}
Deals moved: {{count_moved_deal_ids_listed_below}}
   {{deal_id}}
Deals not moved and why: {{exceptions}}
Cumulative deal report updated: {{yes_no}} by {{updater_name}}
Completed: {{completion_timestamp}}
```

Follow-up mail with additional deals reuses section 3 only, quoted under the original subject.

## Recommended change

Make the form the only accepted intake. A request that arrives as prose gets bounced back with the blank form attached, so the mover never starts a move with an unanswered target book.

Move sections 1 through 8 into a small intake form — a shared spreadsheet row or a web form — that validates the target book against the current book list before the request can be submitted. Book structure changes often enough that a free-text book name is the main source of the questions the mover has to ask.

Have the bulk re-book run from the submitted deal ids and write its own completion log: deal id, source book, target book, effective date, timestamp, operator. Publish that log as the cumulative deal report. The shared-drive spreadsheet then stops being a hand-retyped copy and becomes a view of the log, which removes the second place the same list has to be maintained.

Require an explicit "complete list / more to follow" flag at submission. Where more is to follow, keep the request open and append; do not close it and reopen a new one, so stragglers land in the same job rather than a new mail thread.

Separate the correction path from the move path. A deal booked to the wrong desk that has already earned revenue needs an accounting reallocation as well as a book change; route those to the desk that owns revenue restatement with their own form, and reference the original deal ids.

At the next book or desk reorganisation, generate the candidate deal list from the system rather than typing it: query deals whose book is being retired and present them to the book owner for tick-box approval.

## Open questions

- Who is authorised to approve a book transfer, and whether the book owner's request alone is sufficient — `<to be confirmed>`.
- Whether there is a daily cutoff after which a move slips to the next day, and what it is — `<to be confirmed>`.
- Which system the mover's script runs against and whether a downstream system (Unify, TAGG) needs a matching change after the Sitara re-book — `<to be confirmed>`.
- Whether an effective date can be back-dated into a closed month, and who signs that off — `<to be confirmed>`.
- Who owns the cumulative deal report on the shared drive and who is permitted to write to it — `<to be confirmed>`.
- The correct route for an after-the-fact revenue reallocation between desks, and which team performs the split — `<to be confirmed>`.
- Whether any deal types are excluded from bulk re-booking and must be moved individually — `<to be confirmed>`.
