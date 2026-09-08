---
artifact_id: EML-02
title: "Weekly California Capacity Report \u2014 standing send email template"
artifact_type: email
opportunity_id: ser_4d4f0b156e
opportunity_title: '"California Capacity Report for Week of 10/22-10/26" produced
  weekly'
generated_at: '2026-09-08T19:58:53.820959+00:00'
generator: claude -p via .claude/agents/artifact-drafter.md
review_status: draft-unreviewed
evidence:
- cit_281cdb8ece7c
- cit_6e2d9c893a5d
- cit_73c45be674b7
- cit_7e9d6a9437c9
- cit_97236985661c
- cit_c955cf19fffb
- cit_e04d7226f87c
- cit_e474f470ba47
below_threshold_judgment_call: false
---

> **Draft, not reviewed.** Every sentence describing current practice carries a
> citation id that resolves to a verified quote from the archive. Sentences under
> *Recommended change* are proposals and carry no citation. Nobody who does this
> work has read this document.

## Purpose

Give whoever sends the weekly California Capacity Report a fixed email template and a repeatable send procedure, so the report goes out on the same cadence to the same list regardless of who is covering the desk.

## Scope

Covers the outbound email only: the subject line, the standing distribution list, the send day, and the placeholders that change week to week. It does not cover how the underlying figures are sourced or checked; the report bodies are not available in the archive, so nothing here specifies the report's internal layout.

## Current practice

The report is mailed under the subject line `California Capacity Report for Week of MM/DD-MM/DD`, naming the first and last day of the week covered [cit_97236985661c]. It is sent by a single person on the Transwestern commercial side, from `michelle.lokay@enron.com` [cit_c955cf19fffb]. The send lands on the Friday that closes the reporting week: the 12/17-12/21 report went out on Friday 21 December 2001 [cit_e474f470ba47], and the 12/31-01/04 report went out on Friday 4 January 2002 [cit_73c45be674b7]. The same Friday pattern holds across the 01/14-01/18 report [cit_6e2d9c893a5d] and the 01/28-02/01 report [cit_e04d7226f87c]. Holiday-shortened weeks are still reported, with the subject line naming the shortened span rather than the full week, as in `Week of 12/26-12/28` [cit_7e9d6a9437c9]. At least one week was sent a day early, on Thursday 24 January 2002, for the week labelled 01/21-01/25 [cit_281cdb8ece7c]. Send times vary within the working day, from early morning [cit_7e9d6a9437c9] to late morning [cit_c955cf19fffb].

## Template

```
To:      {{standing_distribution_list}}
From:    {{report_owner}}
Subject: California Capacity Report for Week of {{week_start_mm_dd}}-{{week_end_mm_dd}}

Attached is the California Capacity Report for the week of
{{week_start_mm_dd}}-{{week_end_mm_dd}}.

{{report_body_or_attachment}}

Sections included this week:
  - Transwestern deliveries          <to be confirmed>
  - El Paso deliveries by point      <to be confirmed>
  - Posted Gas Daily prices          <to be confirmed>

Notes / exceptions this week:
{{exception_notes}}

Questions on any figure, come back to me before {{query_cutoff}}
<to be confirmed>.

{{report_owner}}
{{report_owner_title}}
```

Sending notes for the person on the desk:

1. Use the subject form `California Capacity Report for Week of MM/DD-MM/DD` with no other wording, so the series stays sortable in the recipients' mailboxes [cit_97236985661c].
2. Set the week span in the subject to the days actually covered, shortening it for holiday weeks rather than padding to five days [cit_7e9d6a9437c9].
3. Send on the Friday that closes the reporting week [cit_e474f470ba47].
4. If Friday is a holiday or the desk is closed, send on the preceding business day and keep the subject span unchanged [cit_281cdb8ece7c].
5. Send to the standing distribution list unchanged; do not add or drop recipients for a single week without telling the list.

## Recommended change

Move the send to a scheduled job. The job assembles the report from its sources, fills the subject line from the flow week, and mails the standing list on a fixed weekday and hour, with the owner reviewing a draft before release rather than building the mail from scratch.

Hold the distribution list in one place — a mail alias or a distribution group — rather than in the sender's address book, so cover staff inherit the correct list automatically.

Fix a rule for short and holiday weeks in the job configuration: report the days the desk actually covered, and pull the send forward to the last business day of that week. That makes the early Thursday send a configured behaviour instead of a judgement call.

Add a one-line exception field to the template that the owner fills or leaves blank. Recipients then know whether an unusual figure is a data problem or a real market movement, without a follow-up round of mail.

Keep the subject-line format frozen. It is the only thing making this series findable, and any automation should treat it as a contract rather than a formatting choice.

## Open questions

- The report bodies are not in the archive, so the section list in the template above is unverified. The section headings, their order, and the units used all need confirming against a recent copy.
- Whether the report travels as an attachment, as inline text, or both is not determinable from the archive.
- The sources each section is built from — which system, which screen, which posted price sheet — are not identified anywhere in the available messages.
- The identities and roles of the standing recipients are not recorded here; the list needs to be read off a recent send and confirmed as still current.
- No cutoff is documented for recipients to query a figure before it is treated as final.
- The reason the 01/21-01/25 report was sent on the Thursday is not stated; confirm whether that was a holiday rule or a one-off.
- No backup sender is named anywhere in the archive. Confirm who sends the report when the owner is out.
