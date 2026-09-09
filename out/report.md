# Where this company is losing time

*Run `replay` · generated 2026-09-09T19:20:27Z · corpus digest `c94acc4b08cb`*

## $1,501 per month

Range $346 – $4,850. 18 automatable hours per month at a blended $85/hour, across 11 opportunities.

Observed across 4 mailboxes and 3,240 messages, 1999-12-13 to 2002-03-25 (28 months). Not extrapolated beyond what was observed.

The range is not decoration. The counts behind these figures are measured from the corpus; the minutes-per-task are estimates nobody was able to verify, so the base number should be read as the middle of a band, not as a measurement.

**This is a floor, not a total.** 172 of 2,531 operational messages (7%) could be attributed to an identified recurring process. The other 2,359 are a long tail that failed the promotion gate - too few repetitions, too short a window, or too few people to call it a process. That work is real and is deliberately left uncosted rather than estimated. Every rejected candidate is published in `out/residual.json` with the gate it failed.

### What was read

- **3,240 files**, every one of them, 3,224 unique after removing 16 duplicates in 16 groups
- grouped into **2,823 task instances**, because a forty-message argument about one nomination is one task
- **2,531 messages** were shown to a model; 596 were acknowledgements with no new text and were counted deterministically instead
- **88 citations** verified against raw bytes, 0 rejected and published in `out/quarantine.json`

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
| 4 | Scheduled-versus-actual volume exceptions, reconciled by hand in Unify | $91 | $20–$314 | 1.1 | 33 | 18 | 8 | high |
| 5 | "Calpine Daily Gas Nomination" produced monthly | $87 | $19–$284 | 1.0 | 17 | 11 | 8 | medium |
| 6 | Monthly first-of-month gas nominations emailed in by counterparties | $67 | $9–$260 | 0.8 | 13 | 9 | 8 | high |
| 7 | Extending deal tickets by hand to cover unallocated meter flow | $58 | $13–$194 | 0.7 | 15 | 6 | 8 | high |
| 8 | Fixing wrong deal prices in Sitara after the fact | $46 | $10–$153 | 0.5 | 7 | 4 | 8 | high |
| 9 | Fixing deal prices in Sitara by hand before invoices go out | $41 | $8–$150 | 0.5 | 7 | 5 | 8 | high |
| 10 | Daily gas nominations mailed as Word and Excel attachments | $31 | $6–$106 | 0.4 | 28 | 14 | 8 | high |
| 11 | Nomination changes confirmed by hand across Sitara, Unify and counterparties | $20 | $5–$60 | 0.2 | 8 | 6 | 8 | high |

### Not counted

0 opportunities were demoted to low confidence ($0/month not included in the headline) and 1 were quarantined for insufficient evidence ($32/month excluded). See `out/quarantine.json`.

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

**What happens.** Each week a Transwestern commercial analyst compiles a California capacity summary and mails it to a fixed distribution list. The body follows the same structure every time: average Transwestern deliveries to California with San Juan lateral throughput, El Paso deliveries broken out by delivery point, and posted Gas Daily prices. The figures are pulled together from separate sources — spreadsheets are referenced on about half the messages — and then retyped into the mail body rather than generated by a system. The report is sent as a plain status message with no reply expected; the cycle closes when the next week's edition goes out. One message in the set is a correction issuing the right effective week for a report already sent, and one marks the end of a related "California Interstate Capacity Report" series.

**Where it stalls.** The failure mode is not chasing — there are no waiting signals and no deadline language. It is manual transfer: nearly every message carries the signal of numbers being moved by hand from a spreadsheet into an email body, so the report exists only as prose in a mailbox and never as data anyone can query. That hand-keying is what produced the observed correction, where the effective date range on a distributed report had to be restated after the fact. Production also rests on a very small number of senders, so the series simply stops when that person stops sending.

**Why it recurs.** A fixed weekly cadence and a standing distribution list: the same figures for the same delivery points must be restated every week regardless of whether anything changed.

**What could absorb it.** A scheduled job that reads throughput by delivery point and the posted Gas Daily prices from their source systems, renders the standing template including the effective week, and mails it to the fixed list — with the header dates derived from the run date so the effective range cannot be mistyped.

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

- "Transwestern's average deliveries to California were 884 MMBtu/d (81%), with San Juan lateral throughput at 773 MMBtu/d."
  — `corpus/lokay-m/inbox/32.` bytes 1333–1453, lines 23–23
    ```
    sed -n '23,23p' corpus/lokay-m/inbox/32.
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
- "Transwestern's average deliveries to California were 1122 MMBtu/d (103%), with San Juan lateral throughput at 844 MMBtu/d."
  — `corpus/lokay-m/sent_items/18.` bytes 1339–1461, lines 23–23
    ```
    sed -n '23,23p' corpus/lokay-m/sent_items/18.
    ```
- "Transwestern's average deliveries to California were 1058 MMBtu/d (97%), with San Juan lateral throughput at 864 MMBtu/d."
  — `corpus/lokay-m/sent_items/79.` bytes 1337–1458, lines 23–23
    ```
    sed -n '23,23p' corpus/lokay-m/sent_items/79.
    ```
- "Transwestern's average deliveries to California were 1015 MMBtu/d (93%), with San Juan lateral throughput at 873 MMBtu/d."
  — `corpus/lokay-m/sent_items/110.` bytes 1339–1460, lines 23–23
    ```
    sed -n '23,23p' corpus/lokay-m/sent_items/110.
    ```
- "Transwestern's average deliveries to California were 815 MMBtu/d (75%), with San Juan lateral throughput at 879 MMBtu/d."
  — `corpus/lokay-m/sent_items/117.` bytes 1338–1458, lines 23–23
    ```
    sed -n '23,23p' corpus/lokay-m/sent_items/117.
    ```

## 4. Scheduled-versus-actual volume exceptions, reconciled by hand in Unify

**$91/month** (range $20–$314) · 1.1 automatable hours/month · confidence high

*Measured:* 38 messages in 33 task instances, 26 sender(s), 67 people, 18 months. rework 61%, waiting 29%, manual_transfer 32%, deadline 3%.

**What happens.** A meter, contract or deal shows actual measured volume that does not match what was scheduled or nominated, and someone flags it by mail — often off a meter exception report or after month-end allocations arrive from a pipeline counterparty. The finder describes the discrepancy in plain text, naming the meter, deal number or contract and the volumes on each side, and asks a named colleague to decide what to do: cut or extend a deal, insert a path, adjust estimated volumes, or re-actualize. Whoever owns the record then goes back into the system of record — Unify, Sitara, MOPS or the ENA books are all named in these messages — and edits the prior period's numbers to match. The thread closes with a status note that the volumes were corrected or the month re-posted, or it simply stops. Volumes already booked in an earlier month are frequently reopened and revised.

**Where it stalls.** The discrepancy is visible to the person reading the exception report but the correction must be made by someone else, in a different system, for a month that is already closed — so most messages are requests or escalations rather than completions. Nearly two thirds carry rework signals: the same volumes are entered, then re-entered to match what the pipeline says it allocated. Chasing is visible where a counterparty or internal group does not answer ("I sent Jackie Young an email back showing her TETCO's numbers and I haven't received a response"), and where scheduling and allocation disagree with no arbiter named ("scheduling had 8,928 MMBtu confirmed... and only 646 MMBtu flowed"). Who owns the final adjustment is not visible in the mail; it is negotiated thread by thread.

**Why it recurs.** Measured volumes never equal scheduled volumes, and allocations arrive after the fact, so every month's close produces a fresh exception list. Systems that hold the same volume — Unify, Sitara, MOPS, the ENA books, and the counterparty's own allocation — do not agree with each other automatically, so agreement is reached by mail.

**What could absorb it.** A scheduled comparison that pulls scheduled, confirmed and actualized volumes per meter and deal from each system, flags the breaks above a tolerance, and routes each break to a named owner with the counterparty's allocation attached — so the mail carries a decision rather than a discovery. Logging the resulting adjustment against the deal number would remove the re-keying that shows up as rework here.

**How the number was reached.**

```
33.00 task instances / 18 months of coverage = 1.833 instances per month
minutes per instance = 20 handle + (1.15 touches - 1) x 7 + 0.61 rework rate x 20 + 0.29 waiting rate x 4 = 34.32 min
coordination multiplier = 1 + 0.35 x (3 median participants - 1) = 1.700
hours per month = 1.833 x 34.32 x 1.700 / 60 = 1.783
automatable hours = 1.783 x 0.6 automatable share = 1.070
dollars per month = 1.070 h x $85/h = $90.93
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
back showing her TETCO's numbers and I haven't received a response"
  — `corpus/farmer-d/logistics/1972.` bytes 3360–3456, lines 62–63 · rewrapped
    ```
    sed -n '62,63p' corpus/farmer-d/logistics/1972.
    ```
- "The actuals on this contract did not come in as scheduled."
  — `corpus/farmer-d/logistics/972.` bytes 1522–1580, lines 44–44
    ```
    sed -n '44,44p' corpus/farmer-d/logistics/972.
    ```
- "will you please make the 
necessary changes in unify"
  — `corpus/farmer-d/logistics/972.` bytes 1884–1936, lines 48–49 · rewrapped
    ```
    sed -n '48,49p' corpus/farmer-d/logistics/972.
    ```
- "it seems odd to me that scheduling had 8,928 
MMBtu confirmed at this point and only 646 MMBtu flowed."
  — `corpus/farmer-d/logistics/2100.` bytes 1436–1538, lines 36–37
    ```
    sed -n '36,37p' corpus/farmer-d/logistics/2100.
    ```
- "Why is nothing being allocated to Alpine?  This is a good deal we have in 
place with them and I really need the problem resolved."
  — `corpus/farmer-d/logistics/2100.` bytes 3046–3176, lines 78–79
    ```
    sed -n '78,79p' corpus/farmer-d/logistics/2100.
    ```
- "there was around 20,000 MMBTU scheduled, but when it was actualized, it was actualized at 0.  He thinks this is incorrect."
  — `corpus/farmer-d/logistics/77.` bytes 736–858, lines 19–19
    ```
    sed -n '19,19p' corpus/farmer-d/logistics/77.
    ```
- "I have gone back into MOPS and 
corrected these volumes."
  — `corpus/farmer-d/logistics/1141.` bytes 1026–1082, lines 32–33 · rewrapped
    ```
    sed -n '32,33p' corpus/farmer-d/logistics/1141.
    ```

## 5. "Calpine Daily Gas Nomination" produced monthly

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

## 6. Monthly first-of-month gas nominations emailed in by counterparties

**$67/month** (range $9–$260) · 0.8 automatable hours/month · confidence high

*Measured:* 13 messages in 13 task instances, 6 sender(s), 33 people, 9 months. rework 8%, waiting 8%.

**What happens.** Each month, counterparties and plant schedulers email the logistics desk their gas volumes for the coming month. The dominant form is a recurring note from EGPFC nominating natural gas requirements for the MTBE Plant at Morgan's Point, sent with near-identical wording month after month ("EGPFC nominates the following natural gas requirements for the MTBE Plant at Morgan's Point for October 2000"). The same pattern appears for other parties and points — a Calpine January 2000 nomination, an estimated Josey Ranch nomination, and Forest's "first of the month noms". The volumes arrive as free text in the mail body rather than through a system, and the recipient is expected to pick them up and carry them into scheduling; occasionally a revision follows, keyed to a named approver ("revision PER JOHN KJELMYR, 12/26 am"). Nothing in these messages shows the downstream entry step, so where the numbers go after the mail is not visible here.

**Where it stalls.** Two failure modes are visible, both in a minority of the messages. First, the nomination is sometimes an estimate rather than a firm number ("This is the estimated Josey Ranch nomination"), so it must be revisited and superseded — the one correction-role message is an explicit month-end revision authorised verbally by a named person. Second, a nomination cannot be completed because a required input is held by someone else: "I am still waiting on a transport number from lori Allen in your shop." That leaves the desk holding an incomplete nomination and chasing an internal colleague for the missing field.

**Why it recurs.** The monthly nomination cycle: every counterparty must restate volumes for the coming month before it begins, so the same near-identical mail is composed and re-keyed each month for each plant and delivery point.

**What could absorb it.** A fixed submission form or structured template per counterparty and delivery point — same fields every month, with the transport number as a required field — feeding a monthly nomination sheet automatically, so volumes arrive parseable rather than as prose and revisions supersede rather than append.

**How the number was reached.**

```
13.00 task instances / 9 months of coverage = 1.444 instances per month
minutes per instance = 8 handle + (1.00 touches - 1) x 3 + 0.08 rework rate x 12 + 0.08 waiting rate x 2 = 9.08 min
coordination multiplier = 1 + 0.35 x (17 median participants - 1) = 6.600
hours per month = 1.444 x 9.08 x 6.600 / 60 = 1.442
automatable hours = 1.442 x 0.55 automatable share = 0.793
dollars per month = 0.793 h x $85/h = $67.42
```

Assumptions from `config/estimation.yml#task_classes.gas_nomination`.

**Evidence.**

- "EGPFC nominates the following natural gas requirements for the MTBE Plant at 
Morgan's Point for October 2000"
  — `corpus/farmer-d/logistics/1423.` bytes 1192–1301, lines 28–29 · rewrapped
    ```
    sed -n '28,29p' corpus/farmer-d/logistics/1423.
    ```
- "Below are Forest's first of the month noms:"
  — `corpus/farmer-d/logistics/2008.` bytes 815–858, lines 27–27
    ```
    sed -n '27,27p' corpus/farmer-d/logistics/2008.
    ```
- "revision PER JOHN KJELMYR, 12/26 am."
  — `corpus/farmer-d/logistics/2008.` bytes 964–1000, lines 34–34
    ```
    sed -n '34,34p' corpus/farmer-d/logistics/2008.
    ```
- "I am still waiting on a transport number from lori Allen in your
shop"
  — `corpus/farmer-d/logistics/1539.` bytes 823–892, lines 21–22 · rewrapped
    ```
    sed -n '21,22p' corpus/farmer-d/logistics/1539.
    ```
- "This is the estimated Josey Ranch nomination for the month of April
2000."
  — `corpus/farmer-d/logistics/993.` bytes 1013–1086, lines 30–31 · rewrapped
    ```
    sed -n '30,31p' corpus/farmer-d/logistics/993.
    ```
- "NATURAL GAS NOMINATION FOR 03/00"
  — `corpus/farmer-d/logistics/834.` bytes 547–579, lines 11–11
    ```
    sed -n '11,11p' corpus/farmer-d/logistics/834.
    ```
- "EGPFC nominates the following for the MTBE Plant at Morgan's Point for March 
2000"
  — `corpus/farmer-d/logistics/834.` bytes 1468–1550, lines 33–34 · rewrapped
    ```
    sed -n '33,34p' corpus/farmer-d/logistics/834.
    ```
- "Calpine January 2000 Nomination"
  — `corpus/farmer-d/logistics/619.` bytes 166–197, lines 5–5
    ```
    sed -n '5,5p' corpus/farmer-d/logistics/619.
    ```

## 7. Extending deal tickets by hand to cover unallocated meter flow

**$58/month** (range $13–$194) · 0.7 automatable hours/month · confidence high

*Measured:* 22 messages in 15 task instances, 8 sender(s), 18 people, 6 months. rework 68%, waiting 14%, manual_transfer 5%, deadline 5%.

**What happens.** Gas flows at a meter for days that no live deal ticket covers, so the volume cannot be allocated or booked. Whoever spots the gap — usually someone reconciling allocations or chasing volumes that Volume Management cannot arrange accounting for — emails the deal owner with the meter number, the prior deal number and the specific flow dates, asking that the existing deal be extended rather than a new one written. The deal owner amends the ticket, and the requester checks whether the change has appeared downstream in Unify before the volume can be allocated; if it has not, they ask whether the same deal ticket was used. Where no extension is possible, the fallback is to allocate the gas off to "Strangers" until someone decides what to do.

**Where it stalls.** The request is a one-off email naming a deal number and dates, so nothing tracks it: the requester must come back later and confirm the amendment surfaced in Unify ("This has not yet shown up in Unify. Did you use the same deal ticket?"). Some requests cannot be honoured at all — one thread stalls on the East Desk not having been on Unify for the flow period in question — and those messages escalate rather than resolve. Two-thirds of the messages carry rework signals: the same meters and deals come back for repeated extension, including one request explicitly asking "one more time".

**Why it recurs.** Physical flow keeps running past the end date of the deal that covers it (valves not shut, months rolling over), and nothing reconciles deal end dates against measured meter volumes, so each gap is discovered after the fact and fixed by hand.

**What could absorb it.** A scheduled reconciliation that compares measured meter volumes against deal coverage dates and raises a ticketed extension request naming the meter, last deal number and uncovered dates, then confirms automatically when the amendment appears in Unify — removing both the discovery step and the manual follow-up chase.

**How the number was reached.**

```
15.00 task instances / 6 months of coverage = 2.500 instances per month
minutes per instance = 12 handle + (1.47 touches - 1) x 5 + 0.68 rework rate x 18 + 0.14 waiting rate x 3 = 27.02 min
coordination multiplier = 1 + 0.35 x (2 median participants - 1) = 1.350
hours per month = 2.500 x 27.02 x 1.350 / 60 = 1.520
automatable hours = 1.520 x 0.45 automatable share = 0.684
dollars per month = 0.684 h x $85/h = $58.12
```

Assumptions from `config/estimation.yml#task_classes.deal_entry_correction`.

**Evidence.**

- "This has not yet shown up in Unify.  Did you use the same deal ticket?"
  — `corpus/farmer-d/logistics/221.` bytes 536–606, lines 19–19
    ```
    sed -n '19,19p' corpus/farmer-d/logistics/221.
    ```
- "I think that the deal needs to be extended, it looks like the valve 
was not completely shut by 9 am."
  — `corpus/farmer-d/logistics/1502.` bytes 701–802, lines 22–23 · rewrapped
    ```
    sed -n '22,23p' corpus/farmer-d/logistics/1502.
    ```
- "Pat has asked that this issue be resolved 
today, so, your assistance would be greatly appreciated."
  — `corpus/farmer-d/logistics/1502.` bytes 804–903, lines 23–24 · rewrapped
    ```
    sed -n '23,24p' corpus/farmer-d/logistics/1502.
    ```
- "Please let me know if we want to extend this deal (85% 
of hsc - lg, etc) or if I should put this gas on Strangers until we determine 
what to do."
  — `corpus/farmer-d/logistics/1520.` bytes 738–884, lines 22–24 · rewrapped
    ```
    sed -n '22,24p' corpus/farmer-d/logistics/1520.
    ```
- "I am now on the dreaded ua4 list from Vol. Mgmt."
  — `corpus/farmer-d/logistics/1520.` bytes 886–934, lines 24–24
    ```
    sed -n '24,24p' corpus/farmer-d/logistics/1520.
    ```
- "Can the deal be extended 
for 6/4 (548 dec.) and 6/9 (40 dec.) to cover this flow so that Volume 
Management can create an accounting arrangement for these two days?"
  — `corpus/farmer-d/logistics/1486.` bytes 759–924, lines 23–25 · rewrapped
    ```
    sed -n '23,25p' corpus/farmer-d/logistics/1486.
    ```
- "I don't think we can even process this request.  The East Desk was not up and 
running on Unify in June of 1999."
  — `corpus/farmer-d/logistics/1492.` bytes 1443–1555, lines 41–42 · rewrapped
    ```
    sed -n '41,42p' corpus/farmer-d/logistics/1492.
    ```
- ".16 decatherms allocated at this meter for 5/31/2000.  Can you please extend 
deal (one more time for me) for 5/31/2000."
  — `corpus/farmer-d/logistics/1174.` bytes 524–644, lines 21–22 · rewrapped
    ```
    sed -n '21,22p' corpus/farmer-d/logistics/1174.
    ```

## 8. Fixing wrong deal prices in Sitara after the fact

**$46/month** (range $10–$153) · 0.5 automatable hours/month · confidence high

*Measured:* 8 messages in 7 task instances, 5 sender(s), 12 people, 4 months. rework 100%, manual_transfer 12%, deadline 12%.

**What happens.** Someone downstream — billing, settlement or a desk reviewing a deal summary — notices that the price recorded on a deal in Sitara is wrong: a stale prior-month rate, a zero, or a figure that does not match what was quoted or billed. They mail the person who can edit the deal and ask for the price to be changed for a specific deal number and flow month, sometimes naming both the wrong and the correct value. That person edits the price in Sitara, or, when the deal cannot be reopened, applies an agreed fixed price to the affected lines as a workaround. The thread closes with a confirmation that the change was made or a request to advise when complete. In one instance the correction was chased so the revenue figure would be right before the morning flash report.

**Where it stalls.** Every message in this cluster carries a rework signal: the deal is priced once, discovered to be wrong later, and priced again by a second person. The correction is not made by whoever spotted it — requests, handoffs and one escalation show the fix travelling to a Sitara editor, so the error's discovery and its remedy sit in different hands. Where the deal cannot be amended at all, the group resorts to writing a fixed price onto both lines rather than fixing the source, which leaves the original record wrong. Nothing here shows a check that would catch a stale price at entry.

**Why it recurs.** Prices are re-set per flow month, so a deal carried forward keeps last month's rate until someone edits it; the error only surfaces when billing or a deal summary is read, which is after the fact.

**What could absorb it.** A validation at deal entry or a nightly exception query that flags deals whose price is zero, unchanged from the prior month, or divergent from the quoted/billed price, mailed to the deal owner before the flash report is produced. Pair it with a logged price-change request so the edit, the requester and the confirmation live on the deal rather than in mail.

**How the number was reached.**

```
7.00 task instances / 4 months of coverage = 1.750 instances per month
minutes per instance = 12 handle + (1.14 touches - 1) x 5 + 1.00 rework rate x 18 + 0.00 waiting rate x 3 = 30.71 min
coordination multiplier = 1 + 0.35 x (2 median participants - 1) = 1.350
hours per month = 1.750 x 30.71 x 1.350 / 60 = 1.209
automatable hours = 1.209 x 0.45 automatable share = 0.544
dollars per month = 0.544 h x $85/h = $46.26
```

Assumptions from `config/estimation.yml#task_classes.deal_entry_correction`.

**Evidence.**

- "Can you please update the 04/01 price for deal # 27253 in Sitara? It 
currently has a rate of $2.3043 (last month's price)."
  — `corpus/giron-d/sent/12.` bytes 677–800, lines 29–30
    ```
    sed -n '29,30p' corpus/giron-d/sent/12.
    ```
- "I changed the El Paso Electric deal #697528 price from $4 to $68. I should not receive the $25524.54 as revenue shown in the new deal summary."
  — `corpus/williams-w3/sent_items/366.` bytes 579–721, lines 18–18
    ```
    sed -n '18,18p' corpus/williams-w3/sent_items/366.
    ```
- "Is there any way to recalculate this (or simply zero it out) prior to the morning flash?"
  — `corpus/williams-w3/sent_items/366.` bytes 723–811, lines 18–18
    ```
    sed -n '18,18p' corpus/williams-w3/sent_items/366.
    ```
- "Since we cannot fix the deal, go ahead and put a fixed price of $2.81359 on 
both lines of the May 2000 deal."
  — `corpus/farmer-d/logistics/1285.` bytes 721–830, lines 30–31 · rewrapped
    ```
    sed -n '30,31p' corpus/farmer-d/logistics/1285.
    ```
- "please change and/or review a 
change of price for the Mar 15 item from $0.00000 to $7.20000 and advise when 
complete"
  — `corpus/giron-d/sent/57.` bytes 666–784, lines 34–36 · rewrapped
    ```
    sed -n '34,36p' corpus/giron-d/sent/57.
    ```
- "Currently in Deal Manager-Sitara, it is at $2.50 and that is 
the price that I billed them at."
  — `corpus/farmer-d/logistics/1309.` bytes 585–679, lines 20–21 · rewrapped
    ```
    sed -n '20,21p' corpus/farmer-d/logistics/1309.
    ```
- "he has the deal priced at 5.25.  I adjusted the price in Sitara."
  — `corpus/farmer-d/logistics/129.` bytes 779–843, lines 21–21
    ```
    sed -n '21,21p' corpus/farmer-d/logistics/129.
    ```
- "Can you please 
update the deal in Sitara to reflect the correct price for 03/01?"
  — `corpus/giron-d/sent/81.` bytes 810–891, lines 33–34 · rewrapped
    ```
    sed -n '33,34p' corpus/giron-d/sent/81.
    ```

## 9. Fixing deal prices in Sitara by hand before invoices go out

**$41/month** (range $8–$150) · 0.5 automatable hours/month · confidence high

*Measured:* 8 messages in 7 task instances, 5 sender(s), 13 people, 5 months. rework 75%, waiting 38%, manual_transfer 38%, deadline 25%.

**What happens.** Someone preparing an invoice or reviewing a deal notices that the price recorded against a deal ticket in Sitara does not match what was agreed — an index formula instead of a fixed price, a wrong commodity price, or a spot volume sitting on the same ticket as an exchange deal. They email the person with edit rights, quoting the deal number and the corrected price, and ask for the change to be made. That person edits the ticket, and in some threads confirms back or is asked to notify when the change has come across. The exchange ends when the requester sees the corrected price flow through and can issue the invoice or move on.

**Where it stalls.** The requester cannot make the edit themselves, so the correction waits on a second person: one message shows an attempted self-service fix ("I tried to get into the Sitara ticket # 373590 to correct the swing pricing") that turned into an escalation, and another asks to be notified once the change lands rather than being able to see it. The request also travels by relay — one sender asks a colleague to "forward this to Daren" — and it collides with a same-day invoicing deadline ("I need to send out my invoice this afternoon"). Most messages in this cluster carry rework signals, which fits work being redone in the system after it was first captured.

**Why it recurs.** Prices are captured at deal entry but only checked at invoicing, so every billing cycle surfaces another batch of tickets whose Sitara price does not match the agreed price, and edit rights sit with someone other than the person who spots the mismatch.

**What could absorb it.** A pre-invoice exception report that compares the price on each Sitara ticket against the confirmed deal terms and lists mismatches by deal number before the billing run, plus a standing change-request form that captures deal number, corrected price, affected days and requester so the edit can be applied and confirmed back without a relay email.

**How the number was reached.**

```
7.00 task instances / 5 months of coverage = 1.400 instances per month
minutes per instance = 12 handle + (1.14 touches - 1) x 5 + 0.75 rework rate x 18 + 0.38 waiting rate x 3 = 27.34 min
coordination multiplier = 1 + 0.35 x (3 median participants - 1) = 1.700
hours per month = 1.400 x 27.34 x 1.700 / 60 = 1.084
automatable hours = 1.084 x 0.45 automatable share = 0.488
dollars per month = 0.488 h x $85/h = $41.48
```

Assumptions from `config/estimation.yml#task_classes.deal_entry_correction`.

**Evidence.**

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
- "Deal 819592 - the commodity price needs to be 3.6318"
  — `corpus/farmer-d/logistics/74.` bytes 708–760, lines 22–22
    ```
    sed -n '22,22p' corpus/farmer-d/logistics/74.
    ```
- "I'll wait to see how these changes come across. Please notify me when these changes have been made."
  — `corpus/farmer-d/logistics/74.` bytes 1338–1437, lines 32–32
    ```
    sed -n '32,32p' corpus/farmer-d/logistics/74.
    ```
- "I tried to get into the Sitara ticket # 373590 to correct the swing pricing"
  — `corpus/farmer-d/logistics/106.` bytes 1341–1416, lines 39–39
    ```
    sed -n '39,39p' corpus/farmer-d/logistics/106.
    ```
- "Could you pls the pricing on this deal for March 2001 Production for days 25 & 26 to  $ 5.285?"
  — `corpus/farmer-d/logistics/176.` bytes 1231–1325, lines 36–36
    ```
    sed -n '36,36p' corpus/farmer-d/logistics/176.
    ```
- "I need to send out my invoice this afternoon"
  — `corpus/farmer-d/logistics/176.` bytes 1381–1425, lines 38–38
    ```
    sed -n '38,38p' corpus/farmer-d/logistics/176.
    ```
- "I need to have the spot deal placed on a different deal ticket than the 
exchange deal (#157288)."
  — `corpus/farmer-d/logistics/1238.` bytes 595–692, lines 23–24 · rewrapped
    ```
    sed -n '23,24p' corpus/farmer-d/logistics/1238.
    ```

## 10. Daily gas nominations mailed as Word and Excel attachments

**$31/month** (range $6–$106) · 0.4 automatable hours/month · confidence high

*Measured:* 28 messages in 28 task instances, 6 sender(s), 33 people, 14 months. manual_transfer 7%, deadline 4%.

**What happens.** Each flow day, a nomination for gas volumes is sent by email to the scheduling desk, most often as an attached document — recurringly "CALPINE DAILY GAS NOMINATION 1.doc", and in some months an Excel workbook such as "egmnom-Feb.xls". Other instances are nominations onto named pipelines stated in the message itself, for example "HPL Nom for January 4, 2001" and a nomination of volumes into Eastrans for a stated gas day forward. Recipients open the attachment, read the volumes and path out of it, and key or pass them onward; the same document filename reappears month after month, so the file is being overwritten and re-sent rather than versioned. Some messages carry monthly nominations alongside the daily one, and revisions are circulated as forwards marked "(REVISED)". The exchange ends with a short confirmation back to the sender — "Confirmed on my end. Same volumes as yesterday, no changes to the path."

**Where it stalls.** The nomination content lives inside an attachment rather than in the message, so nothing downstream can read it without a person opening the file; the manual_transfer signal appears on the spreadsheet forwards for exactly this reason. Because every day's file carries the identical name, a recipient cannot tell one day's nomination from another except by the mail date, and revisions arrive as separate forwarded copies rather than as an update to a record. Confirmation is verbal or by return mail and appears only once in this set, so whether a nomination was received and accepted is not visible in the trail. Coverage gaps are handled by hand too: one sender simply notes "Will be out Friday, will call if there are any changes."

**Why it recurs.** Nominations are per gas day with a daily pipeline cutoff, and the volumes must be restated even when they are unchanged from the previous day. The messages span fourteen months from the same small set of senders on the same fixed filenames.

**What could absorb it.** Replace the repeated attachment with a structured daily submission — a form or dated file drop whose fields (counterparty, pipeline, path, volume, gas day) are machine-readable and land directly in the scheduling system, with an automatic acknowledgement back to the sender. A roll-forward default of "same volumes as yesterday" would let unchanged days be confirmed rather than re-typed.

**How the number was reached.**

```
coverage = 27 dated / 28 messages = 0.964; instances 28 / 0.964 = 29.04 adjusted
29.04 task instances / 14 months of coverage = 2.074 instances per month
minutes per instance = 8 handle + (1.00 touches - 1) x 3 + 0.00 rework rate x 12 + 0.00 waiting rate x 2 = 8.00 min
coordination multiplier = 1 + 0.35 x (5 median participants - 1) = 2.400
hours per month = 2.074 x 8.00 x 2.400 / 60 = 0.664
automatable hours = 0.664 x 0.55 automatable share = 0.365
dollars per month = 0.365 h x $85/h = $31.03
```

Assumptions from `config/estimation.yml#task_classes.gas_nomination`.

**Evidence.**

- "CALPINE DAILY GAS NOMINATION 1.doc"
  — `corpus/farmer-d/logistics/1318.` bytes 746–780, lines 19–19
    ```
    sed -n '19,19p' corpus/farmer-d/logistics/1318.
    ```
- "This is to nominate 33,450 mmbtu/d into Eastrans for GD 6/22/2000 forward."
  — `corpus/farmer-d/logistics/1222.` bytes 1148–1222, lines 36–36
    ```
    sed -n '36,36p' corpus/farmer-d/logistics/1222.
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
- "FW: Calpine Daily Gas Nomination (REVISED)"
  — `corpus/farmer-d/logistics/773.` bytes 160–202, lines 5–5
    ```
    sed -n '5,5p' corpus/farmer-d/logistics/773.
    ```
- "Calpine Daily Gas Nomination and Monthly (JULY) Nomination"
  — `corpus/farmer-d/logistics/1245.` bytes 161–219, lines 5–5
    ```
    sed -n '5,5p' corpus/farmer-d/logistics/1245.
    ```
- "Will be out Friday, will call if there are any changes."
  — `corpus/farmer-d/logistics/169.` bytes 828–883, lines 21–21
    ```
    sed -n '21,21p' corpus/farmer-d/logistics/169.
    ```

## 11. Nomination changes confirmed by hand across Sitara, Unify and counterparties

**$20/month** (range $5–$60) · 0.2 automatable hours/month · confidence high

*Measured:* 8 messages in 8 task instances, 5 sender(s), 14 people, 6 months. rework 50%, manual_transfer 50%, deadline 12%.

**What happens.** A counterparty, pipeline scheduler or internal desk asks for a nomination volume to be changed for one or more flow dates at a named meter or point. Whoever picks the request up restates the old and new volumes in mail, asks the other side to approve, and then makes the change in whatever record they keep — Sitara, Unify, or a personal spreadsheet. The confirmation loop closes by naming the person at the counterparty who agreed ("confirmed with Patsy Shimek @ Kinder Morgan") or by stating the change has been entered. The output is an agreed volume recorded in more than one place; there is no single system in the evidence that carries the change through on its own.

**Where it stalls.** The change has to be re-keyed into each record separately, and the mail shows that half of these messages carry rework or manual-transfer markers: a volume is questioned and re-asked ("Is this correct? We'll need to change sitara"), or an amount that was already agreed cannot be confirmed with the pipeline ("Charlotte Hawkins is having trouble confirming the volume of 5,733 with El Paso"). Because approval and entry are separate steps held by different people, the requester writes back to check what was actually recorded, and one instance ends with the change likely being repeated the following day. Who owns the authoritative record — Sitara, Unify or the spreadsheet — is not visible in these messages.

**Why it recurs.** Nominations are revised against daily flow cycles, and each revision must be agreed with a named person at the counterparty and then re-entered in every system that holds the volume, so a new confirmation loop starts each time a number moves.

**What could absorb it.** A single change-request form that captures meter, dates, old and new volume, then writes those values into Sitara and Unify and generates the counterparty confirmation mail from the same record, so the number is keyed once and system mismatches are flagged automatically.

**How the number was reached.**

```
8.00 task instances / 6 months of coverage = 1.333 instances per month
minutes per instance = 8 handle + (1.00 touches - 1) x 3 + 0.50 rework rate x 12 + 0.00 waiting rate x 2 = 14.00 min
coordination multiplier = 1 + 0.35 x (2 median participants - 1) = 1.350
hours per month = 1.333 x 14.00 x 1.350 / 60 = 0.420
automatable hours = 0.420 x 0.55 automatable share = 0.231
dollars per month = 0.231 h x $85/h = $19.63
```

Assumptions from `config/estimation.yml#task_classes.gas_nomination`.

**Evidence.**

- "Will you approve revising the volume in Unify down to 2,300?  Please advise."
  — `corpus/farmer-d/logistics/1163.` bytes 715–791, lines 27–27
    ```
    sed -n '27,27p' corpus/farmer-d/logistics/1163.
    ```
- "Charlotte Hawkins is having trouble confirming the volume of 5,733 with El 
Paso."
  — `corpus/farmer-d/logistics/1163.` bytes 476–557, lines 19–20 · rewrapped
    ```
    sed -n '19,20p' corpus/farmer-d/logistics/1163.
    ```
- "Jill 
told me that on the 18th,19 th and 20th the San Jac. nom  should be 29,209.  
Is this correct?  We'll need to change sitara."
  — `corpus/farmer-d/logistics/603.` bytes 781–911, lines 29–31 · rewrapped
    ```
    sed -n '29,31p' corpus/farmer-d/logistics/603.
    ```
- "This change was 
confirmed with Patsy Shimek @ Kinder Morgan."
  — `corpus/farmer-d/logistics/2029.` bytes 783–844, lines 24–25 · rewrapped
    ```
    sed -n '24,25p' corpus/farmer-d/logistics/2029.
    ```
- "I've made the change in my spreadsheet."
  — `corpus/farmer-d/logistics/1001.` bytes 1256–1295, lines 41–41
    ```
    sed -n '41,41p' corpus/farmer-d/logistics/1001.
    ```
- "They said there is a chance they will have to do it again tomorrow."
  — `corpus/farmer-d/logistics/2108.` bytes 765–832, lines 22–22
    ```
    sed -n '22,22p' corpus/farmer-d/logistics/2108.
    ```
- "We have received a revised nomination as follows:"
  — `corpus/farmer-d/logistics/1161.` bytes 482–531, lines 19–19
    ```
    sed -n '19,19p' corpus/farmer-d/logistics/1161.
    ```
- "a nom change from
3,300 to 2,400 mmbtu/d at HPL Meter 98-6296 delivery @ HPL Thompsonville"
  — `corpus/farmer-d/logistics/1151.` bytes 880–970, lines 29–30 · rewrapped
    ```
    sed -n '29,30p' corpus/farmer-d/logistics/1151.
    ```

---

## Drafted artifacts

Ready to use on Monday morning. Every sentence asserting current practice carries a citation marker that resolves to verified evidence; recommendations carry no marker and sit under their own heading, so observation and proposal never blur.

- **Checklist: Correcting a Wrong Deal Price in Sitara** (`CHK-01-checklist-correcting-a-wrong-deal-price-in-sitara.md`) — checklist, for *Fixing wrong deal prices in Sitara after the fact*
- **Runbook: Scheduled-versus-Actual Volume Exceptions** (`RUN-01-runbook-scheduled-versus-actual-volume-exceptions.md`) — runbook, for *Scheduled-versus-actual volume exceptions, reconciled by hand in Unify*
- **Weekly California Capacity Report — standing email template** (`TPL-01-weekly-california-capacity-report-standing-email-tem.md`) — template, for *Weekly California Capacity Report, assembled and mailed by hand*
- **Monthly First-of-Month Gas Nomination — Standard Submission Template** (`TPL-02-monthly-first-of-month-gas-nomination-standard-submi.md`) — template, for *Monthly first-of-month gas nominations emailed in by counterparties*
- **Standing Daily Credit Report — Distribution Email Template** (`EML-01-standing-daily-credit-report-distribution-email-temp.md`) — email, for *"Credit Report - 1/30/01" produced daily*
- **Weekly California Capacity Report — standing cover email (draft)** (`EML-02-weekly-california-capacity-report-standing-cover-ema.md`) — email, for *"California Capacity Report for Week of 01/14-01/18" produced weekly*
- **Standing email template: Calpine Daily Gas Nomination** (`EML-03-standing-email-template-calpine-daily-gas-nomination.md`) — email, for *"Calpine Daily Gas Nomination" produced monthly*

---

## How to check any of this

```
make verify     # re-anchor every citation from scratch; recompute every number
make test       # full suite, zero model calls
make serve      # dashboard with click-through to the highlighted bytes
```

Every citation above prints the `sed` command that reproduces it. `docs/AUDIT.md` holds 25 randomly sampled citations with both `dd` and `sed` commands.

Where this is most likely wrong, and what it took on faith, is in `NOTES.md`.
