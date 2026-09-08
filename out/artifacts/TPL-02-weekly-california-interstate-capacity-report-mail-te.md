---
artifact_id: TPL-02
title: "Weekly California Interstate Capacity Report \u2014 mail template"
artifact_type: template
opportunity_id: proc_a58e286bd5
opportunity_title: Weekly California Capacity Report, assembled and mailed by hand
generated_at: '2026-09-08T21:34:50.319125+00:00'
generator: claude -p via .claude/agents/artifact-drafter.md
review_status: draft-unreviewed
evidence:
- cit_45a6c764f509
- cit_646d6e14a0ad
- cit_7959cb571714
- cit_a7a837f366fb
- cit_c772a2736ae1
- cit_cd0f539df211
- cit_e142f4dedf42
- cit_feeabdbb4ec3
below_threshold_judgment_call: false
---

> **Draft, not reviewed.** Every sentence describing current practice carries a
> citation id that resolves to a verified quote from the archive. Sentences under
> *Recommended change* are proposals and carry no citation. Nobody who does this
> work has read this document.

## Purpose

Give whoever holds the weekly California Interstate Capacity Report a fixed mail template, so the wording and section order do not have to be rebuilt from the previous week's message each time, and so the reporting period is filled from a field rather than retyped.

## Scope

Covers the weekly capacity report mailed from the Transwestern commercial desk to its standing distribution list: Transwestern average deliveries to California, San Juan lateral throughput, and El Paso deliveries broken out by delivery point. Covers the correction mail sent when the reporting period in the header is wrong. Does not cover where the underlying delivery and throughput figures are produced, or the capacity numbers the utilisation figures are measured against.

## Current practice

The report is delivered as text in the body of an email, not as an attachment [cit_45a6c764f509]. The Transwestern section is a single sentence giving average deliveries to California, the utilisation figure in parentheses, and San Juan lateral throughput [cit_45a6c764f509]. That sentence keeps the same wording and order from week to week, with only the figures and the period changing [cit_7959cb571714]. The same structure holds across consecutive weeks in the same month [cit_a7a837f366fb]. It also holds across a month boundary [cit_e142f4dedf42]. It holds again in later issues [cit_646d6e14a0ad]. The El Paso section follows the same pattern: average deliveries to California with a utilisation figure, then a breakout by delivery point introduced with a colon [cit_c772a2736ae1]. The reporting period is stated by hand in each issue, and when it is stated wrongly the fix is a second mail to the same list carrying the corrected effective dates [cit_feeabdbb4ec3]. The duty is handed from one person to the next while the report format stays unchanged, described by the outgoing owner as their last California Interstate Capacity Report [cit_cd0f539df211].

## Template

Weekly issue. Subject line and period come from the reporting week, not from the previous message.

```
To:      {{standing_distribution_list}}
Subject: California Capacity Report for Week of {{period_start_mm_dd}}-{{period_end_mm_dd}}

Transwestern's average deliveries to California were {{tw_avg_deliveries}} MMBtu/d
({{tw_utilisation}}), with San Juan lateral throughput at {{san_juan_throughput}} MMBtu/d.

El Paso's average deliveries to California were {{ep_avg_deliveries}} MMBtu/d
({{ep_utilisation}}):

  {{ep_delivery_point_1}}   {{ep_volume_1}} MMBtu/d
  {{ep_delivery_point_2}}   {{ep_volume_2}} MMBtu/d
  {{ep_delivery_point_3}}   {{ep_volume_3}} MMBtu/d
  ...

Posted Gas Daily prices:
  {{price_point_1}}   {{price_1}}
  {{price_point_2}}   {{price_2}}

{{sender_name}}
{{sender_role}}
```

Correction issue. Send only when the period in the header of an already-sent issue is wrong. Keep the body of the original report unchanged below the correction line so recipients can see which issue is being amended.

```
To:      {{standing_distribution_list}}
Subject: Corrected - California Capacity Report for Week of {{period_start_mm_dd}}-{{period_end_mm_dd}}

Sorry, the effective date for this report is {{period_start_mm_dd}}-{{period_end_mm_dd}}.

{{original_report_body}}
```

Handover issue. Send when the duty passes to another person.

```
To:      {{standing_distribution_list}}
Subject: California Capacity Report for Week of {{period_start_mm_dd}}-{{period_end_mm_dd}}

Below is my last California Interstate Capacity Report. Going forward it will be sent by
{{incoming_owner_name}}, {{incoming_owner_role}}.

{{report_body}}
```

Fields to fill before sending: `{{period_start_mm_dd}}`, `{{period_end_mm_dd}}`, `{{tw_avg_deliveries}}`, `{{tw_utilisation}}`, `{{san_juan_throughput}}`, `{{ep_avg_deliveries}}`, `{{ep_utilisation}}`, and one line per El Paso delivery point. Source of the delivery and throughput figures: `<to be confirmed>`. Full membership of the standing distribution list: `<to be confirmed>`. Day of week and time the issue is expected: `<to be confirmed>`.

## Recommended change

Derive the two period fields from the run date instead of typing them. If the report is generated on a fixed weekday, the period start and end are a function of that date, and the header error that triggers a correction mail to the whole list stops being possible.

Keep the distribution list in one place — a mail group or a named list in the sending tool — rather than copying recipients forward from last week's message. Handover then changes the sender, not the addressees.

Move the figures out of the mail body and into a small spreadsheet or query that holds one row per reporting week, with columns matching the merge fields above. Render the mail from that row. This gives a week-over-week series for free and removes the re-keying step that the current body-text format forces.

Once the render step exists, schedule it and leave the owner a review-and-release action: the draft is built with the period and figures already in place, and the owner sends it. Keep the sentence wording exactly as it stands now; recipients read this report by shape, and changing the phrasing costs more than it gains.

## Open questions

- Where the Transwestern delivery, San Juan lateral throughput, and El Paso delivery-point figures originate. The messages state the numbers but not the source system or report they are read from.
- What capacity denominator the utilisation figures are measured against, and whether it changes with season or with a rate case.
- The full standing distribution list, and whether it is a mail group or a list of individual addresses copied forward each week.
- The expected send day and time, if there is one. Nothing in these messages sets a deadline or shows anyone being chased.
- Whether the El Paso delivery points are a fixed set or vary by week.
- Whether any review or approval happens before the mail goes out, and if so by whom.
