# Where this company is losing time

*Run `resume4` · generated 2026-09-09T14:58:30Z · corpus digest `c94acc4b08cb`*

## $1,556 per month

Range $357 – $5,043. 18 automatable hours per month at a blended $85/hour, across 12 opportunities.

Observed across 4 mailboxes and 3,240 messages, 1999-12-13 to 2002-03-25 (28 months). Not extrapolated beyond what was observed.

The range is not decoration. The counts behind these figures are measured from the corpus; the minutes-per-task are estimates nobody was able to verify, so the base number should be read as the middle of a band, not as a measurement.

**This is a floor, not a total.** 172 of 2,531 operational messages (7%) could be attributed to an identified recurring process. The other 2,359 are a long tail that failed the promotion gate - too few repetitions, too short a window, or too few people to call it a process. That work is real and is deliberately left uncosted rather than estimated. Every rejected candidate is published in `out/residual.json` with the gate it failed.

### What was read

- **3,240 files**, every one of them, 3,224 unique after removing 16 duplicates in 16 groups
- grouped into **2,823 task instances**, because a forty-message argument about one nomination is one task
- **2,531 messages** were shown to a model; 596 were acknowledgements with no new text and were counted deterministically instead
- **98 citations** verified against raw bytes, 0 rejected and published in `out/quarantine.json`

> **A note on `corpus/farmer-d/logistics/3221.`.** This message is 5% of the corpus in one file. Its 3,600-row table is machine-generated placeholder content, not business data, and **no quantity in this report is derived from it**. The proof is arithmetic:
>
> - column 0: exactly arithmetic across all 3600 rows — value = 1000000 + 1*n, zero deviation
> - column 1: constant 'HPL' for all 3600 rows
> - column 2: modular arithmetic — value = 1*n mod 400 across all 3600 rows (8 wraps, and only 2 distinct first differences where real data would have thousands)
> - column 3: repeats with period 60 across 3600 rows (60 identical cycles)
> - column 4: modular arithmetic — value = 911*n mod 45000 across all 3600 rows (72 wraps, and only 2 distinct first differences where real data would have thousands)
> - column 5: modular arithmetic — value = 331*n mod 45000 across all 3600 rows (26 wraps, and only 2 distinct first differences where real data would have thousands)
> - column 7: repeats with period 3 across 3600 rows (1200 identical cycles)
> - column 8: exactly arithmetic across all 3600 rows — value = 0 + 7*n, zero deviation
>
> The prose above the table is genuine and is cited where relevant.

## Ranked opportunities

| # | Opportunity | $/month | Range | Hours/mo | Instances | Months | Cites | Conf |
|---:|---|---:|---|---:|---:|---:|---:|---|
| 1 | "Credit Report - 1/30/01" produced daily | $544 | $155–$1,534 | 6.4 | 69 | 4 | 8 | medium |
| 2 | "California Capacity Report for Week of 01/14-01/18" produced weekly | $266 | $51–$929 | 3.1 | 15 | 5 | 8 | medium |
| 3 | Weekly California Capacity Report, assembled and mailed by hand | $248 | $48–$865 | 2.9 | 16 | 6 | 8 | high |
| 4 | "Calpine Daily Gas Nomination" produced monthly | $87 | $19–$284 | 1.0 | 17 | 11 | 8 | medium |
| 5 | Scheduled-versus-actual meter volume reconciliation across Unify, Sitara and HPL | $83 | $19–$284 | 1.0 | 33 | 18 | 8 | high |
| 6 | Moving deals between trading books by hand-listed request | $70 | $14–$268 | 0.8 | 10 | 3 | 8 | medium |
| 7 | Extending expired deals so unallocated meter flow can be allocated | $64 | $14–$213 | 0.8 | 10 | 4 | 8 | high |
| 8 | Monthly gas nomination letters for Morgan's Point MTBE plant, typed by hand | $58 | $8–$221 | 0.7 | 11 | 8 | 8 | high |
| 9 | Sitara deal price corrections requested by email before invoicing | $47 | $11–$158 | 0.6 | 7 | 4 | 8 | high |
| 10 | Nomination changes confirmed by hand with pipeline and counterparty schedulers | $34 | $7–$114 | 0.4 | 10 | 5 | 8 | medium |
| 11 | Daily Calpine gas nomination, mailed as an attached document | $31 | $6–$106 | 0.4 | 26 | 13 | 8 | high |
| 12 | Monthly estimated nomination volumes agreed by email (Josey Ranch, Calpine, Midcon) | $22 | $5–$66 | 0.3 | 8 | 3 | 8 | medium |

### Not counted

0 opportunities were demoted to low confidence ($0/month not included in the headline) and 2 were quarantined for insufficient evidence ($59/month excluded). See `out/quarantine.json`.

---

## 1. "Credit Report - 1/30/01" produced daily

**$544/month** (range $155–$1,534) · 6.4 automatable hours/month · confidence medium

*Measured:* 69 messages in 69 task instances, 1 sender(s), 4 people, 4 months. manual_transfer 100%.

**What happens.** The same message, "Credit Report - 1/30/01", is produced and sent daily by one person to 3 recipient(s). 69 instances span 4 months and 14 distinct weeks, with a median gap of 1.0 days. 58% of them carry no message body at all, meaning the content was an attachment assembled outside the mail system. 

**Where it stalls.** This series was discovered from headers alone, so the corpus shows that it happened on a cadence but not what it cost to produce. The bodies are unavailable.

**Why it recurs.** A fixed daily reporting obligation to a standing distribution list.

**What could absorb it.** A scheduled job that assembles the same figures from their sources and sends them to the standing list on the same cadence.

*Discovered deterministically from subject lines, with no model involved. Content clustering could not see this process because the bodies are empty in 58% of instances.*

**How the number was reached.**

```
69.00 task instances / 4 months of coverage = 17.250 instances per month
minutes per instance = 22 handle + (1.00 touches - 1) x 4 + 0.00 rework rate x 10 + 0.00 waiting rate x 2 = 22.00 min
coordination multiplier = 1 + 0.35 x (2 median participants - 1) = 1.350
hours per month = 17.250 x 22.00 x 1.350 / 60 = 8.539
automatable hours = 8.539 x 0.75 automatable share = 6.404
dollars per month = 6.404 h x $85/h = $544.35
```

Assumptions from `config/estimation.yml#task_classes.recurring_report`.

**Evidence.**

- "Subject: Credit Report--2/2/01"
  — `corpus/giron-d/sent/267.` bytes 161–191, lines 5–5
    ```
    sed -n '5,5p' corpus/giron-d/sent/267.
    ```
- "Subject: Credit Report--2/1/01"
  — `corpus/giron-d/sent/255.` bytes 161–191, lines 5–5
    ```
    sed -n '5,5p' corpus/giron-d/sent/255.
    ```
- "Subject: Credit Report--2/15/01"
  — `corpus/giron-d/sent/220.` bytes 162–193, lines 5–5
    ```
    sed -n '5,5p' corpus/giron-d/sent/220.
    ```
- "Subject: Credit Report--3/1/01"
  — `corpus/giron-d/sent/174.` bytes 161–191, lines 5–5
    ```
    sed -n '5,5p' corpus/giron-d/sent/174.
    ```
- "Subject: Credit Report 3/15/01"
  — `corpus/giron-d/sent/151.` bytes 162–192, lines 5–5
    ```
    sed -n '5,5p' corpus/giron-d/sent/151.
    ```
- "Subject: Credit Report--3/26/01"
  — `corpus/giron-d/sent/121.` bytes 160–191, lines 5–5
    ```
    sed -n '5,5p' corpus/giron-d/sent/121.
    ```
- "Subject: Credit Report--4/02/01"
  — `corpus/giron-d/sent/85.` bytes 161–192, lines 5–5
    ```
    sed -n '5,5p' corpus/giron-d/sent/85.
    ```
- "Subject: Credit Report--4/20/01"
  — `corpus/giron-d/sent/53.` bytes 163–194, lines 5–5
    ```
    sed -n '5,5p' corpus/giron-d/sent/53.
    ```

## 2. "California Capacity Report for Week of 01/14-01/18" produced weekly

**$266/month** (range $51–$929) · 3.1 automatable hours/month · confidence medium

*Measured:* 15 messages in 15 task instances, 1 sender(s), 9 people, 5 months. .

**What happens.** The same message, "California Capacity Report for Week of 01/14-01/18", is produced and sent weekly by one person to 7 recipient(s). 15 instances span 5 months and 15 distinct weeks, with a median gap of 7.01 days. 

**Where it stalls.** This series was discovered from headers alone, so the corpus shows that it happened on a cadence but not what it cost to produce. The bodies are unavailable.

**Why it recurs.** A fixed weekly reporting obligation to a standing distribution list.

**What could absorb it.** A scheduled job that assembles the same figures from their sources and sends them to the standing list on the same cadence.

*Discovered deterministically from subject lines, with no model involved. Content clustering could not see this process because the bodies are empty in 0% of instances.*

**How the number was reached.**

```
15.00 task instances / 5 months of coverage = 3.000 instances per month
minutes per instance = 22 handle + (1.00 touches - 1) x 4 + 0.00 rework rate x 10 + 0.00 waiting rate x 2 = 22.00 min
coordination multiplier = 1 + 0.35 x (9 median participants - 1) = 3.800
hours per month = 3.000 x 22.00 x 3.800 / 60 = 4.180
automatable hours = 4.180 x 0.75 automatable share = 3.135
dollars per month = 3.135 h x $85/h = $266.48
```

Assumptions from `config/estimation.yml#task_classes.recurring_report`.

**Evidence.**

- "Subject: California Capacity Report for Week of 10/22-10/26"
  — `corpus/lokay-m/inbox/10.` bytes 325–384, lines 8–8
    ```
    sed -n '8,8p' corpus/lokay-m/inbox/10.
    ```
- "Subject: California Capacity Report for Week of 12/10-12/14"
  — `corpus/lokay-m/sent_items/18.` bytes 325–384, lines 8–8
    ```
    sed -n '8,8p' corpus/lokay-m/sent_items/18.
    ```
- "Subject: California Capacity Report for Week of 12/17-12/21"
  — `corpus/lokay-m/sent_items/67.` bytes 325–384, lines 8–8
    ```
    sed -n '8,8p' corpus/lokay-m/sent_items/67.
    ```
- "Subject: California Capacity Report for Week of 12/26-12/28"
  — `corpus/lokay-m/sent_items/63.` bytes 324–383, lines 8–8
    ```
    sed -n '8,8p' corpus/lokay-m/sent_items/63.
    ```
- "Subject: California Capacity Report for Week of 12/31-01/04"
  — `corpus/lokay-m/sent_items/55.` bytes 322–381, lines 8–8
    ```
    sed -n '8,8p' corpus/lokay-m/sent_items/55.
    ```
- "Subject: California Capacity Report for Week of 01/14-01/18"
  — `corpus/lokay-m/sent_items/40.` bytes 325–384, lines 8–8
    ```
    sed -n '8,8p' corpus/lokay-m/sent_items/40.
    ```
- "Subject: California Capacity Report for Week of 01/21-01/25"
  — `corpus/lokay-m/sent_items/30.` bytes 323–382, lines 8–8
    ```
    sed -n '8,8p' corpus/lokay-m/sent_items/30.
    ```
- "Subject: California Capacity Report for Week of 01/28-02/01"
  — `corpus/lokay-m/sent_items/79.` bytes 323–382, lines 8–8
    ```
    sed -n '8,8p' corpus/lokay-m/sent_items/79.
    ```

## 3. Weekly California Capacity Report, assembled and mailed by hand

**$248/month** (range $48–$865) · 2.9 automatable hours/month · confidence high

*Measured:* 18 messages in 16 task instances, 2 sender(s), 10 people, 6 months. rework 6%, manual_transfer 89%.

**What happens.** Each week a Transwestern commercial analyst compiles a California Interstate Capacity Report and mails it to a fixed distribution list. The body follows a near-identical template every week: Transwestern's average deliveries to California with a percent-of-capacity figure, San Juan lateral throughput, El Paso deliveries broken out by delivery point, and posted Gas Daily prices. The figures are pulled together from separate sources and pasted into the mail body rather than generated by a reporting system; a spreadsheet appears alongside the mail in a couple of instances. The message is titled with the week range ("California Capacity Report for Week of 01/21-01/25") and the cycle ends when it is sent — the exemplars show no replies, questions or follow-up work. One message closes the series ("Below is my last California Interstate Capacity Report"), and the work later resumes under a second sender.

**Where it stalls.** There is no waiting or deadline pressure visible here at all — nothing stalls waiting on a counterparty. The friction is in assembly: nearly every message carries a manual-transfer signal, meaning the numbers are re-keyed into an email body week after week in the same shape. The one failure that does surface is the header rather than the data: a correction message ("Sorry, the effective date for this new report is 01/07-01/11") shows the week label being set by hand and mailed wrong, forcing a second send to the whole list. Who sources each block of figures is not visible in the mail.

**Why it recurs.** A fixed weekly reporting cadence with a standing distribution list. The report has no owner-system behind it, so each week's edition must be rebuilt from source data by whoever holds the role — the handover between two senders shows the cadence outlives the individual.

**What could absorb it.** A scheduled job that reads Transwestern and El Paso delivery volumes and the posted Gas Daily prices, renders them into the existing template with the week range derived from the run date, and mails the standing list — removing both the re-keying and the hand-typed effective-date errors. Because the layout is already stable week to week, the template can be lifted directly from a recent edition.

**How the number was reached.**

```
16.00 task instances / 6 months of coverage = 2.667 instances per month
minutes per instance = 22 handle + (1.12 touches - 1) x 4 + 0.06 rework rate x 10 + 0.00 waiting rate x 2 = 23.06 min
coordination multiplier = 1 + 0.35 x (9 median participants - 1) = 3.800
hours per month = 2.667 x 23.06 x 3.800 / 60 = 3.894
automatable hours = 3.894 x 0.75 automatable share = 2.920
dollars per month = 2.920 h x $85/h = $248.23
```

Assumptions from `config/estimation.yml#task_classes.recurring_report`.

**Evidence.**

- "California Capacity Report for Week of 12/10-12/14"
  — `corpus/lokay-m/sent_items/18.` bytes 334–384, lines 8–8
    ```
    sed -n '8,8p' corpus/lokay-m/sent_items/18.
    ```
- "Transwestern's average deliveries to California were 1122 MMBtu/d (103%), with San Juan lateral throughput at 844 MMBtu/d."
  — `corpus/lokay-m/sent_items/18.` bytes 1339–1461, lines 23–23
    ```
    sed -n '23,23p' corpus/lokay-m/sent_items/18.
    ```
- "Sorry, the effective date for this new report is 01/07-01/11."
  — `corpus/lokay-m/sent_items/46.` bytes 1231–1292, lines 23–23
    ```
    sed -n '23,23p' corpus/lokay-m/sent_items/46.
    ```
- "El Paso's average deliveries to California were 1782 MMBtu/d (66%):"
  — `corpus/lokay-m/inbox/10.` bytes 1487–1554, lines 24–24
    ```
    sed -n '24,24p' corpus/lokay-m/inbox/10.
    ```
- "Below is my last California Interstate Capacity Report."
  — `corpus/lokay-m/inbox/20.` bytes 728–783, lines 19–19
    ```
    sed -n '19,19p' corpus/lokay-m/inbox/20.
    ```
- "California Capacity Report for Week of 01/21-01/25"
  — `corpus/lokay-m/sent_items/30.` bytes 332–382, lines 8–8
    ```
    sed -n '8,8p' corpus/lokay-m/sent_items/30.
    ```
- "Transwestern's average deliveries to California were 933 MMBtu/d (86%), with San Juan lateral throughput at 864 MMBtu/d."
  — `corpus/lokay-m/sent_items/30.` bytes 1337–1457, lines 23–23
    ```
    sed -n '23,23p' corpus/lokay-m/sent_items/30.
    ```
- "Transwestern's average deliveries to California were 884 MMBtu/d (81%), with San Juan lateral throughput at 773 MMBtu/d."
  — `corpus/lokay-m/inbox/32.` bytes 1333–1453, lines 23–23
    ```
    sed -n '23,23p' corpus/lokay-m/inbox/32.
    ```

## 4. "Calpine Daily Gas Nomination" produced monthly

**$87/month** (range $19–$284) · 1.0 automatable hours/month · confidence medium

*Measured:* 17 messages in 17 task instances, 1 sender(s), 14 people, 11 months. .

**What happens.** The same message, "Calpine Daily Gas Nomination", is produced and sent monthly by one person to 5 recipient(s). 17 instances span 11 months and 15 distinct weeks, with a median gap of 24.55 days. 

**Where it stalls.** This series was discovered from headers alone, so the corpus shows that it happened on a cadence but not what it cost to produce. The bodies are unavailable.

**Why it recurs.** A fixed monthly reporting obligation to a standing distribution list.

**What could absorb it.** A scheduled job that assembles the same figures from their sources and sends them to the standing list on the same cadence.

*Discovered deterministically from subject lines, with no model involved. Content clustering could not see this process because the bodies are empty in 0% of instances.*

**How the number was reached.**

```
17.00 task instances / 11 months of coverage = 1.545 instances per month
minutes per instance = 22 handle + (1.00 touches - 1) x 4 + 0.00 rework rate x 10 + 0.00 waiting rate x 2 = 22.00 min
coordination multiplier = 1 + 0.35 x (5 median participants - 1) = 2.400
hours per month = 1.545 x 22.00 x 2.400 / 60 = 1.360
automatable hours = 1.360 x 0.75 automatable share = 1.020
dollars per month = 1.020 h x $85/h = $86.70
```

Assumptions from `config/estimation.yml#task_classes.recurring_report`.

**Evidence.**

- "Subject: Calpine Daily Gas Nomination"
  — `corpus/farmer-d/logistics/579.` bytes 158–195, lines 5–5
    ```
    sed -n '5,5p' corpus/farmer-d/logistics/579.
    ```
- "Subject: Calpine Daily Gas Nomination"
  — `corpus/farmer-d/logistics/1027.` bytes 152–189, lines 5–5
    ```
    sed -n '5,5p' corpus/farmer-d/logistics/1027.
    ```
- "Subject: Calpine Daily Gas Nomination"
  — `corpus/farmer-d/logistics/1229.` bytes 152–189, lines 5–5
    ```
    sed -n '5,5p' corpus/farmer-d/logistics/1229.
    ```
- "Subject: Calpine Daily Gas Nomination"
  — `corpus/farmer-d/logistics/1312.` bytes 152–189, lines 5–5
    ```
    sed -n '5,5p' corpus/farmer-d/logistics/1312.
    ```
- "Subject: Calpine Daily Gas Nomination"
  — `corpus/farmer-d/logistics/1318.` bytes 150–187, lines 5–5
    ```
    sed -n '5,5p' corpus/farmer-d/logistics/1318.
    ```
- "Subject: Calpine Daily Gas Nomination"
  — `corpus/farmer-d/logistics/1336.` bytes 151–188, lines 5–5
    ```
    sed -n '5,5p' corpus/farmer-d/logistics/1336.
    ```
- "Subject: Calpine Daily Gas Nomination"
  — `corpus/farmer-d/logistics/1411.` bytes 156–193, lines 5–5
    ```
    sed -n '5,5p' corpus/farmer-d/logistics/1411.
    ```
- "Subject: Calpine Daily Gas Nomination"
  — `corpus/farmer-d/logistics/1561.` bytes 158–195, lines 5–5
    ```
    sed -n '5,5p' corpus/farmer-d/logistics/1561.
    ```

## 5. Scheduled-versus-actual meter volume reconciliation across Unify, Sitara and HPL

**$83/month** (range $19–$284) · 1.0 automatable hours/month · confidence high

*Measured:* 39 messages in 33 task instances, 23 sender(s), 76 people, 18 months. rework 46%, waiting 21%, manual_transfer 28%, deadline 5%.

**What happens.** An exception surfaces on a meter — a nomination that does not match what flowed, an interconnect variance, a missing allocation, or numbers that a downstream system shows differently from the pipeline's own statement. Whoever spots it (a scheduler, a volume-management or accounting contact, or a counterparty) mails the logistics desk with the meter number, the flow days and the two figures that disagree, and asks how it should be handled. The desk then chases the source data — meter statements, daily volume statements, sometimes by fax — and either explains the difference (a measurement or pressure-base adjustment, a liquidation booked on the wrong side) or asks someone to go back into Unify or Sitara and restate the estimated volumes so they agree with what was allocated. Threads close with a correction being entered by hand, a handoff to another person, or a note that the prior month has been revised and re-posted. Many run for weeks and get re-opened when the next month shows the same gap at the same meter.

**Where it stalls.** The desk cannot close a variance from its own records: it needs the counterparty's or the pipeline's statement to say which side is wrong, and those arrive by mail or fax after the month has already been actualized. That produces the pattern visible in the roles — escalations restating an unanswered question ("I sent Jackie Young an email back showing her TETCO's numbers and I haven't received a response", "We need to revisit this issue again") alongside requests to retro-adjust a whole month of estimated volumes in Unify by hand to match what HPL shows. Where two systems hold the same volume (ENA and ENA Upstream, CPR versus OSS, POPS feeds), no reconciliation runs between them, so the mismatch is only found when a person reads an exception report.

**Why it recurs.** Volumes are actualized every month against meters whose measured figures arrive later and from a different party, and the deal and volume systems are not reconciled to each other automatically, so each month's close reproduces the same class of exception at the same meters.

**What could absorb it.** A scheduled comparison that pulls scheduled/confirmed volumes and posted actuals per meter from Sitara, Unify and the pipeline statements, and emits a dated exception list naming the meter, the flow days and the disagreeing figures — so the desk starts from a variance record rather than an inbound mail. Pair it with a standing request for counterparty daily volume statements in a fixed electronic format instead of fax, and a logged adjustment path so month-end restatements in Unify are entered once and traceable.

**How the number was reached.**

```
33.00 task instances / 18 months of coverage = 1.833 instances per month
minutes per instance = 20 handle + (1.18 touches - 1) x 7 + 0.46 rework rate x 20 + 0.21 waiting rate x 4 = 31.32 min
coordination multiplier = 1 + 0.35 x (3 median participants - 1) = 1.700
hours per month = 1.833 x 31.32 x 1.700 / 60 = 1.627
automatable hours = 1.627 x 0.6 automatable share = 0.976
dollars per month = 0.976 h x $85/h = $82.98
```

Assumptions from `config/estimation.yml#task_classes.volume_imbalance_reconciliation`.

**Evidence.**

- "asking me to go in for the 
month of October and adjust all of my estimated volumes in Unify to match 
what HPL shows that we were allocated"
  — `corpus/farmer-d/logistics/1972.` bytes 2913–3053, lines 56–58 · rewrapped
    ```
    sed -n '56,58p' corpus/farmer-d/logistics/1972.
    ```
- "I sent Jackie Young an email 
back showing her TETCO's numbers and I haven't received a response."
  — `corpus/farmer-d/logistics/1972.` bytes 3360–3457, lines 62–63 · rewrapped
    ```
    sed -n '62,63p' corpus/farmer-d/logistics/1972.
    ```
- "it seems odd to me that scheduling had 8,928 
MMBtu confirmed at this point and only 646 MMBtu flowed."
  — `corpus/farmer-d/logistics/2100.` bytes 1436–1538, lines 36–37 · rewrapped
    ```
    sed -n '36,37p' corpus/farmer-d/logistics/2100.
    ```
- "Why is nothing being allocated to Alpine?  This is a good deal we have in 
place with them and I really need the problem resolved."
  — `corpus/farmer-d/logistics/2100.` bytes 3046–3176, lines 78–79 · rewrapped
    ```
    sed -n '78,79p' corpus/farmer-d/logistics/2100.
    ```
- "We have an ongoing issue every month between what we nominate from GEPL into HGPL and on to King Ranch (flows into HGPL at meter 8284) and what is in the system as purchase gas upstream of the meter."
  — `corpus/farmer-d/logistics/160.` bytes 1277–1476, lines 23–23
    ```
    sed -n '23,23p' corpus/farmer-d/logistics/160.
    ```
- "Would you please fax the meter statements from GEPL for February so that I can try to determine which meters are flowing over what is nominated"
  — `corpus/farmer-d/logistics/160.` bytes 1587–1730, lines 23–23
    ```
    sed -n '23,23p' corpus/farmer-d/logistics/160.
    ```
- "There is an interconnect variance at meter 980071 for 2/99."
  — `corpus/farmer-d/logistics/1105.` bytes 1166–1225, lines 51–51
    ```
    sed -n '51,51p' corpus/farmer-d/logistics/1105.
    ```
- "but HPL does not show a receipt of this volume."
  — `corpus/farmer-d/logistics/1105.` bytes 1428–1475, lines 54–54
    ```
    sed -n '54,54p' corpus/farmer-d/logistics/1105.
    ```

## 6. Moving deals between trading books by hand-listed request

**$70/month** (range $14–$268) · 0.8 automatable hours/month · confidence medium

*Measured:* 11 messages in 10 task instances, 6 sender(s), 18 people, 3 months. rework 18%, waiting 9%, manual_transfer 27%, deadline 18%.

**What happens.** Someone who owns a book emails whoever can edit the trading system asking that a named set of deals be re-pointed from one book to another — INTRA-EMWMEH into FT-IM-ENOV, everything to GD-NEW, FT-TERMIN-GD deals into the bankruptcy book. The request arrives as prose plus a list of deals rather than a structured job, and the receiving side either runs a script or moves them individually. Follow-up mail supplies stragglers, answers questions about which book is correct ("the book is ENA-FT-WT-SOCAL"), and confirms when the move is done. In the 2002 bankruptcy-book instances the moved deals are also copied by hand into a cumulative spreadsheet on a shared drive so the list stays current. A minority of the traffic is not a request at all but a correction after the fact, restating revenue that ended up in the wrong desk and describing how it was split back.

**Where it stalls.** Two distinct stalls show up. First, the mover cannot start until the requester answers which target book applies and whether particular deals are in scope — one message ties completion to getting answers back ("If I can have all the answers soon then I think the deals move can be completed around 3:00p.m."), and requests arrive in waves with "a few more stragglers" after the first batch. Second, when the book was wrong at entry the fix is a manual revenue reallocation after the fact: "All deals should have been made under the ST-NW desk... (I recognize this did not happen" and a 70/30 revenue re-split between books. The same lists are then retyped into a master spreadsheet, so the system of record and the tracking file are maintained separately.

**Why it recurs.** Book structure keeps changing — new books, desk reorganisations, and bankruptcy books in 2002 — while deals are booked one at a time, so each change creates a fresh batch of deals sitting in the wrong place and a fresh round of list-and-move mail.

**What could absorb it.** A standing request form that captures deal ids, source book, target book and effective date, feeding a scripted bulk re-book that writes its own completion log; the log then becomes the cumulative deal report instead of someone retyping moved deals into a shared spreadsheet.

**How the number was reached.**

```
10.00 task instances / 3 months of coverage = 3.333 instances per month
minutes per instance = 12 handle + (1.10 touches - 1) x 5 + 0.18 rework rate x 18 + 0.09 waiting rate x 3 = 16.05 min
coordination multiplier = 1 + 0.35 x (4 median participants - 1) = 2.050
hours per month = 3.333 x 16.05 x 2.050 / 60 = 1.827
automatable hours = 1.827 x 0.45 automatable share = 0.822
dollars per month = 0.822 h x $85/h = $69.90
```

Assumptions from `config/estimation.yml#task_classes.deal_entry_correction`.

**Evidence.**

- "I want to move all deals currently in the INTRA-EMWMEH book into the 
FT-IM-ENOV book."
  — `corpus/giron-d/sent/619.` bytes 445–531, lines 19–20 · rewrapped
    ```
    sed -n '19,20p' corpus/giron-d/sent/619.
    ```
- "I need this done 
this week if possible."
  — `corpus/giron-d/sent/619.` bytes 647–687, lines 21–22 · rewrapped
    ```
    sed -n '21,22p' corpus/giron-d/sent/619.
    ```
- "These deals have also been added to the cumulative deal report saved on the O:\_Dropbox\Global Contracts - Estate Research (CYN'S)\Deals Reported to Risk (Phy) Master Cumulative List.xls."
  — `corpus/giron-d/inbox/72.` bytes 1367–1554, lines 24–24
    ```
    sed -n '24,24p' corpus/giron-d/inbox/72.
    ```
- "If I can have all the answers soon then I think the deals move can be completed around 3:00p.m."
  — `corpus/giron-d/inbox/67.` bytes 1166–1261, lines 29–29
    ```
    sed -n '29,29p' corpus/giron-d/inbox/67.
    ```
- "All deals should have been made under the ST-NW desk to route with the PGE =
deal-buy tranny-etc. (I recognize this did not happen"
  — `corpus/williams-w3/sent_items/272.` bytes 627–758, lines 19–20 · decoded_exact
    ```
    sed -n '19,20p' corpus/williams-w3/sent_items/272.
    ```
- "Revenue was moved from ST-NW to ST-Whourly for 70/30 split between LP and ST-Whourly"
  — `corpus/williams-w3/sent_items/271.` bytes 581–665, lines 19–19
    ```
    sed -n '19,19p' corpus/williams-w3/sent_items/271.
    ```
- "Here are a few more stragglers to move into the bankruptcy books:"
  — `corpus/giron-d/inbox/57.` bytes 1171–1236, lines 23–23
    ```
    sed -n '23,23p' corpus/giron-d/inbox/57.
    ```
- "move any deals with the FT-TERMIN-GD book to the bankruptcy book from NG-Price"
  — `corpus/giron-d/inbox/44.` bytes 1057–1135, lines 22–22
    ```
    sed -n '22,22p' corpus/giron-d/inbox/44.
    ```

## 7. Extending expired deals so unallocated meter flow can be allocated

**$64/month** (range $14–$213) · 0.8 automatable hours/month · confidence high

*Measured:* 12 messages in 10 task instances, 5 sender(s), 16 people, 4 months. rework 92%, waiting 8%, deadline 8%.

**What happens.** Gas is found flowing at a meter with no live deal behind it — the deal has expired, was never rolled, or carries no evergreen flag — usually surfacing when Volume Management cannot build an accounting arrangement and the meter lands on an unallocated ("ua4") list. The scheduler emails whoever can touch the deal in the deal-capture systems, gives the meter number, the last deal number and the exact flow dates and volumes, and asks that the deal be rolled or extended to cover those days. The recipient checks whether the flow actually occurred and whether the deal can legitimately be extended, then amends it; Volume Management can then create the accounting arrangement and the flow is allocated. Some requests reach back months, and in those cases the answer is that the desk was not on Unify at the time and the request cannot be processed at all. The thread ends when the deal is extended or when the requester is told to find another route.

**Where it stalls.** The work is corrective by construction — nearly every message is a rework signal, because a deal that should have been rolled at expiry is being patched after the gas has already moved. Two messages escalate, and the blocking answer is systemic rather than clerical: the deal predates the desk being live on Unify, so no extension can be recorded and the flow stays unallocated. Requesters also have to verify flow occurred before they can even ask, and one request carries a same-day deadline pushed down from a manager, so the fix competes with the daily schedule.

**Why it recurs.** Deals expire on fixed end dates while physical flow at the meter continues, and nothing links the two. Volume Management's unallocated list re-surfaces the same gap every allocation cycle, so the same meter-by-meter patching request is written again by hand.

**What could absorb it.** A scheduled comparison of measured meter flow against deal end dates that flags meters flowing past their last deal before the allocation cycle closes, and raises the roll/extend request pre-filled with meter, last deal number and flow dates. Pairing that with an evergreen-flag audit at deal entry would stop most of these from arising.

**How the number was reached.**

```
10.00 task instances / 4 months of coverage = 2.500 instances per month
minutes per instance = 12 handle + (1.20 touches - 1) x 5 + 0.92 rework rate x 18 + 0.08 waiting rate x 3 = 29.75 min
coordination multiplier = 1 + 0.35 x (2 median participants - 1) = 1.350
hours per month = 2.500 x 29.75 x 1.350 / 60 = 1.673
automatable hours = 1.673 x 0.45 automatable share = 0.753
dollars per month = 0.753 h x $85/h = $64.01
```

Assumptions from `config/estimation.yml#task_classes.deal_entry_correction`.

**Evidence.**

- "Can the deal be extended 
for 6/4 (548 dec.) and 6/9 (40 dec.) to cover this flow so that Volume 
Management can create an accounting arrangement"
  — `corpus/farmer-d/logistics/1486.` bytes 759–904, lines 23–25 · rewrapped
    ```
    sed -n '23,25p' corpus/farmer-d/logistics/1486.
    ```
- "I don't think we can even process this request.  The East Desk was not up and 
running on Unify in June of 1999."
  — `corpus/farmer-d/logistics/1492.` bytes 1443–1555, lines 41–42 · rewrapped
    ```
    sed -n '41,42p' corpus/farmer-d/logistics/1492.
    ```
- "I have some flow at the above referenced meter without a deal."
  — `corpus/farmer-d/logistics/1479.` bytes 516–578, lines 21–21
    ```
    sed -n '21,21p' corpus/farmer-d/logistics/1479.
    ```
- "I am now on the dreaded ua4 list from Vol. Mgmt."
  — `corpus/farmer-d/logistics/1520.` bytes 886–934, lines 24–24
    ```
    sed -n '24,24p' corpus/farmer-d/logistics/1520.
    ```
- "No new deal # referenced and no evergreen flag."
  — `corpus/farmer-d/logistics/896.` bytes 868–915, lines 27–27
    ```
    sed -n '27,27p' corpus/farmer-d/logistics/896.
    ```
- "Can you please check into whether or not the below deals for the above meters 
can be rolled and extended?"
  — `corpus/farmer-d/logistics/896.` bytes 530–636, lines 21–22 · rewrapped
    ```
    sed -n '21,22p' corpus/farmer-d/logistics/896.
    ```
- "Pat has asked that this issue be resolved 
today, so, your assistance would be greatly appreciated."
  — `corpus/farmer-d/logistics/1502.` bytes 804–903, lines 23–24 · rewrapped
    ```
    sed -n '23,24p' corpus/farmer-d/logistics/1502.
    ```
- "I need to verify that flow occured so that I can have a deal(s) 
extended to allocate the flow to."
  — `corpus/farmer-d/logistics/1483.` bytes 912–1010, lines 24–25 · rewrapped
    ```
    sed -n '24,25p' corpus/farmer-d/logistics/1483.
    ```

## 8. Monthly gas nomination letters for Morgan's Point MTBE plant, typed by hand

**$58/month** (range $8–$221) · 0.7 automatable hours/month · confidence high

*Measured:* 11 messages in 11 task instances, 4 sender(s), 31 people, 8 months. waiting 9%.

**What happens.** Each month, ahead of the next flow month, a counterparty contact mails Daren Farmer's logistics mailbox a nomination for the coming month. The recurring form is an EGPFC letter — "EGPFC nominates the following natural gas requirements for the MTBE Plant at Morgan's Point for [month]" — followed by the daily volumes and, in some messages, the price basis (for example volumes at "Gas Daily HSC mid flat"). The same slot also carries nominations arriving as attachments rather than body text, such as a Calpine monthly nomination document and an `egmnom-Jan.xls` spreadsheet. The messages are almost entirely requests: the sender states the volumes, and the scheduling side is expected to take them into the nomination process. The archive shows the inbound submission; what happens to the numbers after receipt is not visible in these messages.

**Where it stalls.** The volumes arrive as free prose or as an attached file rather than in a fixed field layout, so each month the same figures are re-read and re-keyed from a differently shaped message. Waiting appears in a minority of instances and is concrete when it does: one sender is held up because "I am still waiting on a transport number from lori Allen in your shop", i.e. the nomination cannot be completed until a detail owned by the other side comes back. No correction or rework roles appear here, so the visible friction is intake format and missing reference data, not repeated fixing.

**Why it recurs.** The nomination is per flow month for a standing delivery point, so the same letter is retyped for each successive month across the period covered.

**What could absorb it.** Give the recurring counterparties a fixed submission template (or a small form) with point, month and per-day volumes in named fields, so the monthly letter lands in a structure that can be parsed and loaded rather than read and re-keyed. Pair it with a required transport/reference number field so an incomplete nomination is rejected at submission instead of stalling in mail.

**How the number was reached.**

```
11.00 task instances / 8 months of coverage = 1.375 instances per month
minutes per instance = 8 handle + (1.00 touches - 1) x 3 + 0.00 rework rate x 12 + 0.09 waiting rate x 2 = 8.18 min
coordination multiplier = 1 + 0.35 x (17 median participants - 1) = 6.600
hours per month = 1.375 x 8.18 x 6.600 / 60 = 1.238
automatable hours = 1.238 x 0.55 automatable share = 0.681
dollars per month = 0.681 h x $85/h = $57.85
```

Assumptions from `config/estimation.yml#task_classes.gas_nomination`.

**Evidence.**

- "EGPFC nominates the following requirements for the MTBE Plant at Morgan's 
Point for January 2000"
  — `corpus/farmer-d/logistics/607.` bytes 1180–1277, lines 28–29 · rewrapped
    ```
    sed -n '28,29p' corpus/farmer-d/logistics/607.
    ```
- "EGPFC nominates the following natural gas requirements for the MTBE Plant at 
Morgan's Point for September 2000"
  — `corpus/farmer-d/logistics/1367.` bytes 1194–1305, lines 28–29 · rewrapped
    ```
    sed -n '28,29p' corpus/farmer-d/logistics/1367.
    ```
- "I am still waiting on a transport number from lori Allen in your
shop"
  — `corpus/farmer-d/logistics/1539.` bytes 823–892, lines 21–22 · rewrapped
    ```
    sed -n '21,22p' corpus/farmer-d/logistics/1539.
    ```
- "For March 11 to 31, they will take 33,000/d at a price of Gas Daily HSC mid 
flat."
  — `corpus/farmer-d/logistics/830.` bytes 812–894, lines 25–26 · rewrapped
    ```
    sed -n '25,26p' corpus/farmer-d/logistics/830.
    ```
- "CALPINE MONTHLY GAS NOMINATION___.doc"
  — `corpus/farmer-d/logistics/619.` bytes 556–593, lines 19–19
    ```
    sed -n '19,19p' corpus/farmer-d/logistics/619.
    ```
- "See attached file: egmnom-Jan.xls"
  — `corpus/farmer-d/logistics/620.` bytes 830–863, lines 32–32
    ```
    sed -n '32,32p' corpus/farmer-d/logistics/620.
    ```
- "EGPFC nominates the following natural gas requirements for the MTBE Plant at 
Morgan's Point for October 2000:"
  — `corpus/farmer-d/logistics/1423.` bytes 1192–1302, lines 28–29 · rewrapped
    ```
    sed -n '28,29p' corpus/farmer-d/logistics/1423.
    ```
- "EGPFC nominates the following requirements for the MTBE Plant at Morgan's 
Point for February 2000"
  — `corpus/farmer-d/logistics/719.` bytes 1172–1270, lines 28–29 · rewrapped
    ```
    sed -n '28,29p' corpus/farmer-d/logistics/719.
    ```

## 9. Sitara deal price corrections requested by email before invoicing

**$47/month** (range $11–$158) · 0.6 automatable hours/month · confidence high

*Measured:* 8 messages in 7 task instances, 5 sender(s), 10 people, 4 months. rework 100%, waiting 25%, manual_transfer 50%, deadline 25%.

**What happens.** Someone reviewing a deal — usually ahead of invoicing or a month-end settlement — finds that the price or volume recorded in Sitara does not match what was agreed, and emails the person with Sitara write access to change it. The mail names the deal or ticket number and states the corrected figure, sometimes as an index formula (for example an NGI monthly index less a differential) rather than a flat price, and sometimes covering only particular production days. The requester then waits for the change to be made and asks to be notified, or checks that the corrected price has flowed through. In one instance the requester compiled a side-by-side list of Sitara price versus customer price to show which deals were wrong. The work ends when the person with access edits the deal and the requester can invoice or reconcile against it.

**Where it stalls.** The requester cannot make the change themselves, so every correction becomes a hand-off: half of these messages pass the figure onward to someone else ("pls forward this to Daren so that he can change the price in Sitara"), and the requester is left waiting for confirmation that the edit landed. One message shows the hand-off failing outright on permissions — "I tried to get into the Sitara ticket # 373590 to correct the swing pricing... I am not allowed to access it" — which turns a data fix into an escalation. Because the trigger is frequently an imminent invoice ("I need to send out my invoice this afternoon"), the wait sits directly in front of a deadline the requester does not control.

**Why it recurs.** Prices are entered once at deal capture but verified later against the invoice or the customer's own price, so the mismatch is only discovered on a billing cycle, and correcting it always requires a person with Sitara edit rights.

**What could absorb it.** A structured price-change request — deal number, affected production days, old price, new price or index formula — that is logged, routed to whoever holds Sitara edit rights, and returns an automatic confirmation once the deal record changes, so the requester stops chasing. A pre-invoice comparison of Sitara price against the contracted or customer price would surface the same mismatches before the invoice date rather than after.

**How the number was reached.**

```
7.00 task instances / 4 months of coverage = 1.750 instances per month
minutes per instance = 12 handle + (1.14 touches - 1) x 5 + 1.00 rework rate x 18 + 0.25 waiting rate x 3 = 31.46 min
coordination multiplier = 1 + 0.35 x (2 median participants - 1) = 1.350
hours per month = 1.750 x 31.46 x 1.350 / 60 = 1.239
automatable hours = 1.239 x 0.45 automatable share = 0.558
dollars per month = 0.558 h x $85/h = $47.39
```

Assumptions from `config/estimation.yml#task_classes.deal_entry_correction`.

**Evidence.**

- "For June, I need a couple of things changed in Sitara: 
Deal 819592 - the commodity price needs to be 3.6318"
  — `corpus/farmer-d/logistics/74.` bytes 652–760, lines 21–22
    ```
    sed -n '21,22p' corpus/farmer-d/logistics/74.
    ```
- "I'll wait to see how these changes come across. Please notify me when these changes have been made."
  — `corpus/farmer-d/logistics/74.` bytes 1338–1437, lines 32–32
    ```
    sed -n '32,32p' corpus/farmer-d/logistics/74.
    ```
- "Currently, Sitara is showing a price of  HSC GDP +.05."
  — `corpus/farmer-d/logistics/179.` bytes 791–845, lines 18–18
    ```
    sed -n '18,18p' corpus/farmer-d/logistics/179.
    ```
- "pls forward this to Daren so that he can change the price in Sitara to $ 5.235 +.05"
  — `corpus/farmer-d/logistics/179.` bytes 889–972, lines 20–20
    ```
    sed -n '20,20p' corpus/farmer-d/logistics/179.
    ```
- "I tried to get into the Sitara ticket # 373590 to correct the swing pricing"
  — `corpus/farmer-d/logistics/106.` bytes 1341–1416, lines 39–39
    ```
    sed -n '39,39p' corpus/farmer-d/logistics/106.
    ```
- "I am not allowed to access it beacuse it is a deal from when we
were at Enron"
  — `corpus/farmer-d/logistics/106.` bytes 1425–1502, lines 40–41 · rewrapped
    ```
    sed -n '40,41p' corpus/farmer-d/logistics/106.
    ```
- "Could you pls the pricing on this deal for March 2001 Production for days 25 & 26 to  $ 5.285?"
  — `corpus/farmer-d/logistics/177.` bytes 900–994, lines 24–24
    ```
    sed -n '24,24p' corpus/farmer-d/logistics/177.
    ```
- "I need to send out my invoice this afternoon."
  — `corpus/farmer-d/logistics/177.` bytes 1050–1095, lines 26–26
    ```
    sed -n '26,26p' corpus/farmer-d/logistics/177.
    ```

## 10. Nomination changes confirmed by hand with pipeline and counterparty schedulers

**$34/month** (range $7–$114) · 0.4 automatable hours/month · confidence medium

*Measured:* 10 messages in 10 task instances, 8 sender(s), 21 people, 5 months. rework 40%, waiting 10%, manual_transfer 20%, deadline 20%.

**What happens.** A volume change on a gas nomination arises — a counterparty revises its nom, a meter volume needs cutting, or a discrepancy is spotted between what was nominated and what flowed. A scheduler in the logistics mailbox mails the pipeline or counterparty scheduler with the meter, the old and new volumes and the effective cycle, then asks the other side to agree ("Is this correct?", "Please advise"). Once the other side agrees, the change is written back into the deal systems — Sitara or Unify — by hand, and the agreement itself is recorded only as a line in the mail ("This change was confirmed with Patsy Shimek @ Kinder Morgan"). The thread ends when the confirming reply arrives; there is no visible system record of the confirmation other than the message.

**Where it stalls.** The confirmation is a person-to-person message, not a system state, so the change and the record of the change drift apart. Two of the ten messages are corrections re-opening a volume already set — one because gas flowed after the volume was cut ("Lorraine says she flowed this gas even though I cut the volume"), another because the nom figure and Sitara disagree and Sitara must be edited to match. Where a cycle deadline or an IT-agreement cut is involved, the sender has no unilateral authority and must ask whether they can act at all if the counterparty does not cut voluntarily, which leaves the nomination unresolved while the cutoff approaches.

**Why it recurs.** Nominations are changed against daily flow cycles, and every change needs bilateral agreement plus a manual re-key into Sitara or Unify, so each revision generates its own confirm-and-transcribe loop.

**What could absorb it.** A single nomination-change record that captures meter, old and new volume, effective cycle and the counterparty contact who agreed, then writes the agreed volume into Sitara and Unify from that one entry rather than by re-keying — with an unconfirmed-changes list surfaced before each cycle cutoff.

**How the number was reached.**

```
10.00 task instances / 5 months of coverage = 2.000 instances per month
minutes per instance = 8 handle + (1.00 touches - 1) x 3 + 0.40 rework rate x 12 + 0.10 waiting rate x 2 = 13.00 min
coordination multiplier = 1 + 0.35 x (3 median participants - 1) = 1.700
hours per month = 2.000 x 13.00 x 1.700 / 60 = 0.737
automatable hours = 0.737 x 0.55 automatable share = 0.405
dollars per month = 0.405 h x $85/h = $34.44
```

Assumptions from `config/estimation.yml#task_classes.gas_nomination`.

**Evidence.**

- "This change was 
confirmed with Patsy Shimek @ Kinder Morgan."
  — `corpus/farmer-d/logistics/2029.` bytes 783–844, lines 24–25 · rewrapped
    ```
    sed -n '24,25p' corpus/farmer-d/logistics/2029.
    ```
- "Will you approve revising the volume in Unify down to 2,300?  Please advise."
  — `corpus/farmer-d/logistics/1163.` bytes 715–791, lines 27–27
    ```
    sed -n '27,27p' corpus/farmer-d/logistics/1163.
    ```
- "the San Jac. nom  should be 29,209.  
Is this correct?  We'll need to change sitara."
  — `corpus/farmer-d/logistics/603.` bytes 827–911, lines 30–31 · rewrapped
    ```
    sed -n '30,31p' corpus/farmer-d/logistics/603.
    ```
- "We did not nominate 
this for the days you are referring to, but Lorraine says she flowed this gas 
even though I cut the volume."
  — `corpus/farmer-d/logistics/1126.` bytes 1349–1478, lines 35–37 · rewrapped
    ```
    sed -n '35,37p' corpus/farmer-d/logistics/1126.
    ```
- "does the fact that this is an IT agreement give me enough 
leverage to cut this nom if TGLO does not do so voluntarily?"
  — `corpus/farmer-d/logistics/1549.` bytes 1743–1862, lines 36–37 · rewrapped
    ```
    sed -n '36,37p' corpus/farmer-d/logistics/1549.
    ```
- "a nom change from
3,300 to 2,400 mmbtu/d at HPL Meter 98-6296 delivery @ HPL Thompsonville"
  — `corpus/farmer-d/logistics/1151.` bytes 880–970, lines 29–30 · rewrapped
    ```
    sed -n '29,30p' corpus/farmer-d/logistics/1151.
    ```
- "nom change for champions"
  — `corpus/farmer-d/logistics/955.` bytes 296–320, lines 7–7
    ```
    sed -n '7,7p' corpus/farmer-d/logistics/955.
    ```
- "Here's REVISED March 2000 (effective 3/21/00 9:00am cycle) setup for Josey"
  — `corpus/farmer-d/logistics/921.` bytes 936–1010, lines 29–29
    ```
    sed -n '29,29p' corpus/farmer-d/logistics/921.
    ```

## 11. Daily Calpine gas nomination, mailed as an attached document

**$31/month** (range $6–$106) · 0.4 automatable hours/month · confidence high

*Measured:* 26 messages in 26 task instances, 4 sender(s), 31 people, 13 months. deadline 4%.

**What happens.** Each gas day a nomination is prepared for a counterparty — most often Calpine, with the same pattern used for Hidalgo and HPL — and sent by email as an attached Word document or spreadsheet (`CALPINE DAILY GAS NOMINATION 1.doc`, `egmnom-Feb.xls`). The body of the message is usually little more than a pointer to the attachment; the volumes and path live inside the file rather than in the mail. A small group of senders repeats this across many months, and the same attachment filename recurs unchanged, indicating a fixed form that is edited and re-sent for each flow date. The cycle closes when the counterparty replies to confirm, as in one exemplar stating that volumes are unchanged from the prior day. Fax appears alongside email in some instances, so the same nomination is evidently delivered by more than one channel.

**Where it stalls.** The measured signals here are near-flat: no rework, no waiting, no manual-transfer markers, and deadline language in only one message. So the visible friction is not chasing or correction but the shape of the handoff — the nomination content sits in an attached file that must be opened, edited and re-attached daily, and confirmations come back as free-text mail ("Confirmed on my end. Same volumes as yesterday") rather than into any system. Who reconciles the confirmed volumes against a scheduling system is not visible in these messages.

**Why it recurs.** Nominations are per-flow-date, so the same form is filled and mailed again every gas day to the same counterparties; the recurrence is driven by the daily cycle, not by anything going wrong.

**What could absorb it.** Replace the hand-edited attachment with a generated nomination: pull the day's path and volumes from the scheduling record, render the counterparty's standard form, and mail or fax it on the daily cycle, defaulting to the previous day's volumes so an unchanged day needs only an approval click. Counterparty confirmations could be captured against the same record instead of living only in reply text.

**How the number was reached.**

```
coverage = 25 dated / 26 messages = 0.962; instances 26 / 0.962 = 27.04 adjusted
27.04 task instances / 13 months of coverage = 2.080 instances per month
minutes per instance = 8 handle + (1.00 touches - 1) x 3 + 0.00 rework rate x 12 + 0.00 waiting rate x 2 = 8.00 min
coordination multiplier = 1 + 0.35 x (5 median participants - 1) = 2.400
hours per month = 2.080 x 8.00 x 2.400 / 60 = 0.666
automatable hours = 0.666 x 0.55 automatable share = 0.366
dollars per month = 0.366 h x $85/h = $31.12
```

Assumptions from `config/estimation.yml#task_classes.gas_nomination`.

**Evidence.**

- "Calpine Daily Gas Nomination"
  — `corpus/farmer-d/logistics/1561.` bytes 167–195, lines 5–5
    ```
    sed -n '5,5p' corpus/farmer-d/logistics/1561.
    ```
- "Confirmed on my end. Same volumes as yesterday, no changes to the path."
  — `corpus/giron-d/sent/795.` bytes 452–523, lines 16–16
    ```
    sed -n '16,16p' corpus/giron-d/sent/795.
    ```
- "(See attached file: egmnom-Feb.xls)"
  — `corpus/farmer-d/logistics/764.` bytes 858–893, lines 32–32
    ```
    sed -n '32,32p' corpus/farmer-d/logistics/764.
    ```
- "HPL Nom for January 4, 2001"
  — `corpus/farmer-d/logistics/2025.` bytes 313–340, lines 7–7
    ```
    sed -n '7,7p' corpus/farmer-d/logistics/2025.
    ```
- "HIDALGO DAILY GAS NOMINATION.doc"
  — `corpus/farmer-d/logistics/1229.` bytes 667–699, lines 19–19
    ```
    sed -n '19,19p' corpus/farmer-d/logistics/1229.
    ```
- "CALPINE DAILY GAS NOMINATION 1.doc"
  — `corpus/farmer-d/logistics/579.` bytes 554–588, lines 19–19
    ```
    sed -n '19,19p' corpus/farmer-d/logistics/579.
    ```
- "CALPINE DAILY GAS NOMINATION 1.doc"
  — `corpus/farmer-d/logistics/1537.` bytes 765–799, lines 19–19
    ```
    sed -n '19,19p' corpus/farmer-d/logistics/1537.
    ```
- "(See attached file: egmnom-Feb.xls)"
  — `corpus/farmer-d/logistics/767.` bytes 840–875, lines 31–31
    ```
    sed -n '31,31p' corpus/farmer-d/logistics/767.
    ```

## 12. Monthly estimated nomination volumes agreed by email (Josey Ranch, Calpine, Midcon)

**$22/month** (range $5–$66) · 0.3 automatable hours/month · confidence medium

*Measured:* 8 messages in 8 task instances, 2 sender(s), 6 people, 3 months. .

**What happens.** Ahead of a new flow month, someone circulates an estimate of how much gas is expected to be nominated at a given point or for a given counterparty. In two instances this is a standing note stating "the estimated Josey Ranch nomination" for the following month. In the remainder, a question is asked about whether an average is a reasonable basis for next month's number ("Does this average represent a good estimate of the Calpine May nom?") and colleagues reply with per-counterparty figures — Midcon, Southern Union, a Tville point, an IFERC daily rate and a monthly total. The output is an agreed number carried in the body of an email rather than in a system; the thread ends once someone states the assumption plainly, e.g. "So, 5000 total is a safe assumption."

**Where it stalls.** No waiting, rework or deadline signals were measured here, so the evidence does not show chasing or redoing. The visible weakness is different: the monthly estimate is derived by judgment ("I would assume 40000 for Midcon") and settled in free-text mail, with no artefact showing what source the average came from or where the agreed figure is recorded afterwards. Who owns the number once the thread closes is not visible in these messages.

**Why it recurs.** Nominations are set per flow month, so a fresh estimate is needed for each upcoming month and for each point or counterparty on the list.

**What could absorb it.** A scheduled pre-month query that pulls recent actual volumes per meter and counterparty, computes the trailing average, and mails a pre-filled estimate sheet for confirmation would replace the ad-hoc "does this average look right" exchange and leave the agreed figure written down in one place.

**How the number was reached.**

```
8.00 task instances / 3 months of coverage = 2.667 instances per month
minutes per instance = 8 handle + (1.00 touches - 1) x 3 + 0.00 rework rate x 12 + 0.00 waiting rate x 2 = 8.00 min
coordination multiplier = 1 + 0.35 x (2 median participants - 1) = 1.350
hours per month = 2.667 x 8.00 x 1.350 / 60 = 0.480
automatable hours = 0.480 x 0.55 automatable share = 0.264
dollars per month = 0.264 h x $85/h = $22.44
```

Assumptions from `config/estimation.yml#task_classes.gas_nomination`.

**Evidence.**

- "Does this average represent a good estimate of the Calpine May nom?"
  — `corpus/farmer-d/logistics/1063.` bytes 498–565, lines 23–23
    ```
    sed -n '23,23p' corpus/farmer-d/logistics/1063.
    ```
- "So, 5000 total is a safe assumption."
  — `corpus/farmer-d/logistics/1053.` bytes 631–667, lines 23–23
    ```
    sed -n '23,23p' corpus/farmer-d/logistics/1053.
    ```
- "I would assume 40000 for Midcon."
  — `corpus/farmer-d/logistics/1051.` bytes 444–476, lines 17–17
    ```
    sed -n '17,17p' corpus/farmer-d/logistics/1051.
    ```
- "This is the estimated Josey Ranch nomination for the month of
February 2000."
  — `corpus/farmer-d/logistics/724.` bytes 1009–1085, lines 34–35 · rewrapped
    ```
    sed -n '34,35p' corpus/farmer-d/logistics/724.
    ```
- "This is the estimated Josey Ranch nomination for the month of March
2000."
  — `corpus/farmer-d/logistics/850.` bytes 980–1053, lines 31–32 · rewrapped
    ```
    sed -n '31,32p' corpus/farmer-d/logistics/850.
    ```
- "IFERC  40000/d  Total of 1,240,000"
  — `corpus/farmer-d/logistics/1054.` bytes 495–529, lines 19–19
    ```
    sed -n '19,19p' corpus/farmer-d/logistics/1054.
    ```
- "5031 at TVille I-.02 for May"
  — `corpus/farmer-d/logistics/1057.` bytes 787–815, lines 35–35
    ```
    sed -n '35,35p' corpus/farmer-d/logistics/1057.
    ```
- "Southern Union for May
2100 83 st
2100 Port Arthur"
  — `corpus/farmer-d/logistics/1056.` bytes 770–820, lines 37–39
    ```
    sed -n '37,39p' corpus/farmer-d/logistics/1056.
    ```

---

## Drafted artifacts

Ready to use on Monday morning. Every sentence asserting current practice carries a citation marker that resolves to verified evidence; recommendations carry no marker and sit under their own heading, so observation and proposal never blur.

- **Book Transfer Request — standing email template for moving deals between trading books** (`TPL-01-book-transfer-request-standing-email-template-for-mo.md`) — template, for *Moving deals between trading books by hand-listed request*
- **Sitara Price Correction Request — Email Template** (`TPL-02-sitara-price-correction-request-email-template.md`) — template, for *Sitara deal price corrections requested by email before invoicing*
- **Template: Weekly California Interstate Capacity Report** (`TPL-03-template-weekly-california-interstate-capacity-repor.md`) — template, for *Weekly California Capacity Report, assembled and mailed by hand*
- **Runbook: Meter Volume Variance Reconciliation (Sitara / Unify / Pipeline Statements)** (`RUN-01-runbook-meter-volume-variance-reconciliation-sitara-.md`) — runbook, for *Scheduled-versus-actual meter volume reconciliation across Unify, Sitara and HPL*
- **Daily Credit Report: standard send email and template** (`EML-01-daily-credit-report-standard-send-email-and-template.md`) — email, for *"Credit Report - 1/30/01" produced daily*
- **Weekly California Capacity Report — standing email template and handover notes** (`EML-02-weekly-california-capacity-report-standing-email-tem.md`) — email, for *"California Capacity Report for Week of 01/14-01/18" produced weekly*
- **Calpine Daily Gas Nomination — standing email template (draft)** (`EML-03-calpine-daily-gas-nomination-standing-email-template.md`) — email, for *"Calpine Daily Gas Nomination" produced monthly*

---

## How to check any of this

```
make verify     # re-anchor every citation from scratch; recompute every number
make test       # full suite, zero model calls
make serve      # dashboard with click-through to the highlighted bytes
```

Every citation above prints the `sed` command that reproduces it. `docs/AUDIT.md` holds 25 randomly sampled citations with both `dd` and `sed` commands.

Where this is most likely wrong, and what it took on faith, is in `NOTES.md`.
