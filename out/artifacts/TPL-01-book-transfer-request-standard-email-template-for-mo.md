---
artifact_id: TPL-01
title: "Book Transfer Request \u2014 standard email template for moving deals between\
  \ trading books"
artifact_type: template
opportunity_id: proc_121d13b6be
opportunity_title: Moving deals between trading books by hand-run script requests
generated_at: '2026-09-08T20:58:42.792599+00:00'
generator: claude -p via .claude/agents/artifact-drafter.md
review_status: draft-unreviewed
evidence:
- cit_2cf730fe5eda
- cit_7ae2224b6a77
- cit_82ca9725c333
- cit_8c1166964272
- cit_9d702ae06db2
- cit_ac1079e9161a
- cit_f1ac3207b624
- cit_fc5549a67a69
below_threshold_judgment_call: false
---

> **Draft, not reviewed.** Every sentence describing current practice carries a
> citation id that resolves to a verified quote from the archive. Sentences under
> *Recommended change* are proposals and carry no citation. Nobody who does this
> work has read this document.

## Purpose

Give the requester one fixed form to use when a set of deals must be moved from one trading book to another, so the operator who runs the transfer script has every parameter on the first mail and does not have to ask for them.

## Scope

Covers requests to reassign existing deals between books in the deal and risk systems — index deals between desk books, intra-month books, and the bankruptcy books — where the move is carried out by an operator running a script rather than by the requester. Does not cover new deal entry, deal amendment of price or volume, or counterparty changes.

## Current practice

The requester writes free-text email naming the source book and the destination book, for example moving all deals in the INTRA-EMWMEH book into the FT-IM-ENOV book [cit_2cf730fe5eda]. A second exemplar states that all index deals are currently in the FT-WEST book and asks that they all be moved to the GD-NEW book [cit_7ae2224b6a77]. Where a deal-type filter applies, it is stated in prose alongside the book names, as in "move any deals with the FT-TERMIN-GD book to the bankruptcy book from NG-Price. Financial deals only." [cit_8c1166964272].

The operator treats the job as a re-run of an existing parameterised script with the book names substituted, described in one thread as "should be the exact same script as yesterday, just substitute FT_TERMIN-GD for the two books" [cit_f1ac3207b624]. Because the book and scope are not fully specified in the opening mail, the operator asks clarifying questions and the move waits on the reply: "If I can have all the answers soon then I think the deals move can be completed around 3:00p.m." [cit_ac1079e9161a]. The requester answers by return mail, confirming the book identity and the outstanding questions in one line — "the book is ENA-FT-WT-SOCAL. Answer to question 2 & 3 - yes" [cit_9d702ae06db2].

Requests frequently carry a target date stated in prose, such as "I need this done this week if possible." [cit_82ca9725c333]. Deals not caught by the first run are sent through afterwards as a follow-up request in the same form: "Here are a few more stragglers to move into the bankruptcy books:" [cit_fc5549a67a69].

## Template

```
To:          {{book_transfer_operator_group}}
Cc:          {{desk_distribution_list}}
Subject:     Book transfer request — {{source_book}} to {{destination_book}} — needed {{required_by_date}}

BOOK TRANSFER REQUEST

1. Source book (exact name):        {{source_book}}
2. Destination book (exact name):   {{destination_book}}
3. Deal types in scope:             {{deal_type_filter}}
   (e.g. financial only / physical only / all)
4. Deal types explicitly excluded:  {{excluded_deal_types}}
5. Counterparty filter:             {{counterparty_name}}
   TAGG short name:                 {{tagg_short_name}}
   (enter ALL if no counterparty filter applies)
6. Effective date / flow dates in scope: {{effective_date_range}}
7. Required by:                     {{required_by_date}} {{required_by_time}}
8. Is this a re-run of a previous request?  {{yes_no}}
   If yes, prior request date/thread:       {{prior_request_reference}}
9. Deals I expect to move (count or list, if known): {{expected_deal_list}}

Before running:
Please return the list of deals the script matched on these
parameters. I will confirm the list back to you, or send additions,
before the run.

Requester:            {{requester_name_and_desk}}
Systems affected:     Sitara / TAGG / {{other_system}}
Approver, if required: <to be confirmed>

---
OPERATOR SECTION (completed on reply)

Matched deals returned to requester on:  {{match_list_sent_datetime}}
Requester confirmation received on:      {{confirmation_datetime}}
Script run completed on:                 {{run_completed_datetime}}
Deals moved:                             {{deals_moved_count}}
Deals not moved and reason:              {{exceptions}}
Confirmation sent to:                    {{desk_distribution_list}}
```

## Recommended change

Require the form above to be complete before the operator picks up the request. Fields 1 through 7 are the parameters the script already takes; supplying them in the opening mail removes the clarification round-trip that currently sits in front of the deadline.

Make the "return the matched list before the run" step mandatory. The requester reviews the matched deals and sends additions in the same thread, so stragglers are caught before the script runs rather than raised as a second request afterwards.

Use a fixed subject line format so that the source book, destination book and required-by date are visible in the mailbox list without opening the message. This also makes the re-run case easy to spot: the operator can find yesterday's thread by book name.

Longer term, put the same field set behind a submission form that validates the book names against the current book list and rejects a request naming a book that does not exist. Book structures change often enough — new desks, reorganisations, bankruptcy books — that a stale book name is a likely cause of a failed or partial run.

Keep the operator section in the same message so the audit trail for a move lives in one thread: parameters in, matched list out, confirmation, run, exceptions.

## Open questions

- Which group or role owns the transfer script, and whether a named backup exists when that person is out. The archive shows the operator replying to the requester but not the owning team name.
- Whether any approval is required before a book transfer is run, and by whom. Marked `<to be confirmed>` in the template.
- The exact list of accepted deal-type filter values in the script, and whether "financial only" is a script parameter or a manual selection by the operator.
- Whether the TAGG short name is a required parameter for every move or only when a counterparty filter is applied.
- Whether the script produces a match list before execution today, or whether that output would have to be added.
- Whether there is a daily cutoff after which a transfer cannot be run for the current day.
- Who should be on the confirmation distribution list at close of the request.
