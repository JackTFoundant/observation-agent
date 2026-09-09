---
artifact_id: TPL-01
title: 'Deal price correction in Sitara: request and confirmation mail template'
artifact_type: template
opportunity_id: proc_7039a92ef2
opportunity_title: Correcting mispriced deals by hand in Sitara after the fact
generated_at: '2026-09-09T15:14:10.180110+00:00'
generator: claude -p via .claude/agents/artifact-drafter.md
review_status: draft-unreviewed
evidence:
- cit_228d2225d561
- cit_34b923ccd566
- cit_5160f9a064ab
- cit_52db8ac62baa
- cit_a1667ea29fa2
- cit_b72a6d852e79
- cit_d2ac21d4fc0f
- cit_f7716817d54d
below_threshold_judgment_call: true
---

> **Draft, not reviewed.** Every sentence describing current practice carries a
> citation id that resolves to a verified quote from the archive. Sentences under
> *Recommended change* are proposals and carry no citation. Nobody who does this
> work has read this document.

## Purpose

Give the desk one standard mail for correcting a commodity price already booked on a deal, and one standard reply for the person who makes the edit. The aim is that a price correction leaves a written record of the deal, the old price, the new price, where it was changed, and who verified it downstream.

## Scope

Covers corrections to the commodity price field on an already-captured deal in Sitara, including prices left at a placeholder of zero, prices carried over from the prior month, prices superseded before booking, and second corrections where an earlier price change was not final. Covers the follow-through when a report has already been produced from the wrong price. Does not cover new deal entry, volume or meter corrections, or deal cancellation.

## Current practice

The requester identifies the deal by number and states the commodity price the deal should carry [cit_a1667ea29fa2]. The request is mailed to whoever can edit the record and asks for the price on a named deal and flow month to be updated in Sitara, setting the rate currently booked against the rate the customer was invoiced [cit_d2ac21d4fc0f]. Some requests concern a price left at zero and ask the editor to change or review the change and advise when it is complete [cit_f7716817d54d]. The editor replies in free text that the price was adjusted in Sitara [cit_b72a6d852e79]. The requester cannot check the record and asks to be notified once the change has been made, then watches the downstream report to see how the change comes across [cit_228d2225d561]. Where a deal summary has already been produced from the wrong price, the requester flags the deal, the old and new price, and the revenue the summary is wrongly showing [cit_52db8ac62baa]. The fix then races a fixed publication point, and the requester asks for the entry to be recalculated or simply zeroed out before the morning flash [cit_5160f9a064ab]. At least one thread is a correction to a correction, where the earlier changed price was not final and a further price applies to named hours [cit_34b923ccd566].

## Template

Use Block A to raise the correction. The editor replies with Block B. The requester closes the thread with Block C after the downstream report is checked.

```
--- BLOCK A: price correction request (requester -> deal editor) ---

Subject: Price correction - deal {{deal_number}} - {{flow_date}} - Sitara

Deal number:            {{deal_number}}
Counterparty:           {{counterparty}}
Flow date / month:      {{flow_date}}
Hours affected:         {{hours_or_all_day}}
Price currently booked: {{booked_price}}
Price it should be:     {{correct_price}}
Source of correct price:{{invoice_confirm_or_ticket}}
Reason:                 {{prior_month_rate | zero_placeholder | superseded_price |
                         correction_to_earlier_correction}}

Please change the commodity price in Sitara and advise when complete.

Also to be updated in: {{other_system_or_report}}   <to be confirmed - see Open questions>

Downstream report I will check: {{report_name}}
Publication point this must beat: {{publication_point}}   <to be confirmed>

If the corrected figure cannot be recalculated before that point, reply and say so;
I will ask for the entry to be zeroed out instead.

{{requester_name_and_role}}


--- BLOCK B: editor confirmation (deal editor -> requester) ---

Subject: RE: Price correction - deal {{deal_number}} - {{flow_date}} - Sitara

Changed in Sitara: deal {{deal_number}}, {{flow_date}}.
Price was {{booked_price}}, now {{correct_price}}.
Hours applied: {{hours_or_all_day}}
Changed by:    {{editor_name}}
Changed at:    {{timestamp}}
Other systems updated: {{other_system_or_report | none}}
Not done / blocked:    {{blocker | none}}


--- BLOCK C: requester verification close (requester -> editor, copy originators) ---

Subject: RE: Price correction - deal {{deal_number}} - {{flow_date}} - VERIFIED

Checked {{report_name}} dated {{report_date}}.
Corrected price is showing:      {{yes_no}}
Revenue / value now showing:     {{value_shown}}
Matches expected:                {{yes_no}}
Outstanding:                     {{outstanding_or_none}}

Closing this thread. If the figure moves again, raise a new request quoting
deal {{deal_number}} and this thread.
```

## Recommended change

Make the deal number, the old price and the new price mandatory fields in the request. A correction mail that names only the new price cannot be audited later, and it cannot be told apart from a second correction to the same deal.

Put a validation step at deal capture that blocks or flags a commodity price of zero, and one that flags a price identical to the prior month's booked rate for the same counterparty and deal. Both are the two failure modes the request mails describe.

Have Sitara fire the confirmation automatically when the price field on a named deal changes, addressed to the person who raised the request. That removes the editor's free-text reply from the critical path and gives the requester a system record instead of a promise.

Run a periodic reconciliation query comparing invoiced rate to booked rate by deal and flow month, and circulate the exceptions before the morning flash rather than after a report disagrees.

Record which secondary places a price also lives in — the deal summary, any reconciliation spreadsheet, any other system — as a named list on the request, so the editor is not deciding case by case what else to touch.

Give the requester read access to the price field on deals they raise. Verification by the person who spotted the error is the step currently missing.

## Open questions

- Who holds edit rights on the price field in Sitara, and whether that is a named role or whoever is available. Not determinable from the archive.
- The clock time of the morning flash, and whether a correction landing after it is republished or waits for the next cycle.
- Which secondary systems and reports must be updated alongside Sitara, and whether that is fixed or varies by desk. The archive names more than one place but not a rule.
- Whether zeroing out an entry needs approval, and from whom.
- What form the corrected-price evidence takes — invoice, confirm, or ticket — and whether it is attached to the request.
- Whether a correction to an earlier correction follows the same route or is escalated.
