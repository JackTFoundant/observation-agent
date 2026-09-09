---
artifact_id: EML-02
title: "Weekly California Capacity Report \u2014 transmittal email draft"
artifact_type: email
opportunity_id: ser_4d4f0b156e
opportunity_title: '"California Capacity Report for Week of 01/14-01/18" produced
  weekly'
generated_at: '2026-09-09T15:11:36.824994+00:00'
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

Give the owner of the weekly California Capacity Report a fixed transmittal email, so the same wording, the same subject format, and the same distribution list are used every week without being retyped from the previous send.

## Scope

Covers the transmittal email only: subject line, addressing, and the body that carries or introduces the report. It does not cover how the figures inside the report are gathered or checked. The series is Transwestern commercial reporting sent from the Transwestern commercial mailbox [cit_6e2d9c893a5d].

## Current practice

The report is issued under the subject `California Capacity Report for Week of MM/DD-MM/DD`, naming the week it covers [cit_6e2d9c893a5d]. It is sent by one person from the Transwestern commercial mailbox [cit_281cdb8ece7c]. The subject line carries the week range and nothing else, so the week covered is identifiable from the header alone [cit_e04d7226f87c].

The send follows a weekly cadence. Consecutive weeks appear as separate messages: the week of 12/10-12/14 [cit_c955cf19fffb], then 12/17-12/21 [cit_e474f470ba47], then the short holiday week 12/26-12/28 [cit_7e9d6a9437c9], then the year-boundary week 12/31-01/04 [cit_73c45be674b7]. The week range in the subject shortens when the working week is short, rather than the report being skipped [cit_7e9d6a9437c9].

Sends land at the end of the week they cover, in the morning Pacific time in most weeks [cit_e474f470ba47]. Some weeks are sent later in the day [cit_6e2d9c893a5d]. Some weeks are sent on the Thursday rather than the Friday [cit_281cdb8ece7c].

The report goes to a standing distribution list, and a copy of the same message also appears in the sender's own inbox [cit_97236985661c]. Distribution is by email; no other system appears in the header record for this series [cit_e04d7226f87c].

The message bodies for this series are not available in the archive, so the internal structure of the report, the sources of its figures, and any covering note cannot be read from these messages [cit_6e2d9c893a5d].

## Template

Subject and addressing are fixed. Fill the merge fields, attach or paste the report, send.

```
To:       {{standing_distribution_list}}
Cc:       {{cc_list_if_any}}
Subject:  California Capacity Report for Week of {{week_start_mm_dd}}-{{week_end_mm_dd}}

Attached is the California Capacity Report for the week of
{{week_start_mm_dd}}-{{week_end_mm_dd}}.

Contents:
  - Transwestern deliveries: {{tw_deliveries_section}}
  - El Paso deliveries by point: {{el_paso_by_point_section}}
  - Posted Gas Daily prices: {{gas_daily_prices_section}}

Source as of: {{data_as_of_date}}
Changes from last week: {{notable_changes_or_none}}

Questions on any point, reply to this message.

{{sender_name}}
{{sender_role}}
Transwestern Commercial
```

Notes for whoever fills this in:

- `{{standing_distribution_list}}` — the fixed list this report goes to; the exact addresses are `<to be confirmed>`.
- Section labels above reflect the report's known subject matter, not text read from a body; confirm the real section headings before adopting them as `<to be confirmed>`.
- Short weeks keep the same subject format with the shortened range, e.g. `Week of 12/26-12/28` [cit_7e9d6a9437c9].

## Recommended change

Store the distribution list as a named mail group rather than re-addressing each week, so a leaver or joiner is changed in one place.

Fix a single send slot — one weekday, one clock slot — and put a calendar reminder on it. Weeks currently land on different days and at different times, which makes a missed week hard to notice.

Adopt one dated file name for the attachment matching the subject range, so the archived report and the email that carried it can be matched without opening either.

Once the section list is confirmed, build the report as a scheduled job that pulls Transwestern deliveries, El Paso deliveries by point, and posted Gas Daily prices from their systems of record, renders this template, and sends it to the named mail group on the fixed slot. Keep a human review step before send until two consecutive weeks of generated output match the hand-built version.

Add a short "changes from last week" line so recipients can see movement without comparing two reports side by side.

## Open questions

- The seven addresses on the standing distribution list are not recorded here.
- Whether the report travels as an attachment, inline text, or both.
- The actual section headings and column layout inside the report.
- The systems or reports the figures are copied from, and who owns each source.
- Whether a specific weekday and cutoff time were ever agreed with recipients, or whether the end-of-week send was the sender's own habit.
- Whether anyone acts on the report on a deadline that a late send would break.
- Why some weeks are absent from the archive: not produced, produced and not retained, or filed elsewhere.
