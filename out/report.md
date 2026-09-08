# Where this company is losing time

*Run `full01` · generated 2026-09-08T19:58:53Z · corpus digest `c94acc4b08cb`*

## $1,610 per month

Range $373 – $5,216. 19 automatable hours per month at a blended $85/hour, across 14 opportunities.

Observed across 4 mailboxes and 3,240 messages, 1999-12-13 to 2002-03-25 (28 months). Not extrapolated beyond what was observed.

The range is not decoration. The counts behind these figures are measured from the corpus; the minutes-per-task are estimates nobody was able to verify, so the base number should be read as the middle of a band, not as a measurement.

**This is a floor, not a total.** 202 of 2,531 operational messages (8%) could be attributed to an identified recurring process. The other 2,329 are a long tail that failed the promotion gate - too few repetitions, too short a window, or too few people to call it a process. That work is real and is deliberately left uncosted rather than estimated. Every rejected candidate is published in `out/residual.json` with the gate it failed.

### What was read

- **3,240 files**, every one of them, 3,224 unique after removing 16 duplicates in 16 groups
- grouped into **2,823 task instances**, because a forty-message argument about one nomination is one task
- **2,531 messages** were shown to a model; 596 were acknowledgements with no new text and were counted deterministically instead
- **112 citations** verified against raw bytes, 0 rejected and published in `out/quarantine.json`

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
| 1 | "Credit Report--5/9/01" produced daily | $544 | $155–$1,534 | 6.4 | 69 | 4 | 8 | medium |
| 2 | "California Capacity Report for Week of 10/22-10/26" produced weekly | $266 | $51–$929 | 3.1 | 15 | 5 | 8 | medium |
| 3 | Weekly California Capacity Report, assembled and mailed by hand | $248 | $48–$865 | 2.9 | 16 | 6 | 8 | high |
| 4 | Monthly meter variance clean-up between scheduled and actual volumes | $108 | $24–$369 | 1.3 | 41 | 17 | 8 | high |
| 5 | "Calpine Daily Gas Nomination" produced monthly | $87 | $19–$284 | 1.0 | 17 | 11 | 8 | medium |
| 6 | Moving deals between trading books by hand-run script requests | $83 | $15–$340 | 1.0 | 10 | 3 | 8 | medium |
| 7 | Extending existing deal tickets to cover unbooked meter flow | $55 | $12–$182 | 0.6 | 8 | 4 | 8 | high |
| 8 | Mid-month nomination revisions re-keyed by hand for Josey, Katy and El Paso | $44 | $9–$147 | 0.5 | 8 | 5 | 8 | high |
| 9 | Monthly gas nominations mailed in by counterparties, then revised by hand | $38 | $7–$133 | 0.4 | 12 | 6 | 8 | high |
| 10 | Fixing wrong deal prices in Sitara by email request | $36 | $8–$120 | 0.4 | 8 | 6 | 8 | high |
| 11 | Daily Calpine and HPL gas nominations mailed as attached documents | $33 | $6–$113 | 0.4 | 26 | 13 | 8 | high |
| 12 | Real-time West power position handoff notes to the next scheduling shift | $24 | $6–$72 | 0.3 | 10 | 4 | 8 | high |
| 13 | Monthly nomination volume estimates for Josey Ranch and counterparty points | $22 | $5–$66 | 0.3 | 8 | 3 | 8 | medium |
| 14 | Ad-hoc requests for system and deal-book access, by email | $22 | $7–$63 | 0.3 | 7 | 5 | 7 | medium |

### Not counted

0 opportunities were demoted to low confidence ($0/month not included in the headline) and 1 were quarantined for insufficient evidence ($34/month excluded). See `out/quarantine.json`.

---

## 1. "Credit Report--5/9/01" produced daily

**$544/month** (range $155–$1,534) · 6.4 automatable hours/month · confidence medium

*Measured:* 69 messages in 69 task instances, 1 sender(s), 4 people, 4 months. manual_transfer 100%.

**What happens.** The same message, "Credit Report--5/9/01", is produced and sent daily by one person to 3 recipient(s). 69 instances span 4 months and 14 distinct weeks, with a median gap of 1.0 days. 58% of them carry no message body at all, meaning the content was an attachment assembled outside the mail system. 

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

## 2. "California Capacity Report for Week of 10/22-10/26" produced weekly

**$266/month** (range $51–$929) · 3.1 automatable hours/month · confidence medium

*Measured:* 15 messages in 15 task instances, 1 sender(s), 9 people, 5 months. .

**What happens.** The same message, "California Capacity Report for Week of 10/22-10/26", is produced and sent weekly by one person to 7 recipient(s). 15 instances span 5 months and 15 distinct weeks, with a median gap of 7.01 days. 

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

*Measured:* 18 messages in 16 task instances, 2 sender(s), 10 people, 6 months. rework 6%, manual_transfer 83%.

**What happens.** Each week someone on the Transwestern commercial side compiles a California Interstate Capacity Report and mails it to a fixed distribution list. The body follows the same structure every time: average Transwestern deliveries to California against capacity, San Juan lateral throughput, El Paso deliveries broken out by delivery point, and posted Gas Daily prices. The figures are pulled together from several upstream sources and pasted into the mail body rather than generated by a reporting system; a spreadsheet appears alongside the mail in a few instances. The week ends when the mail goes out; there is no visible approval step and almost no reply traffic. One message in the set marks a handover — "Below is my last California Interstate Capacity Report" — after which the same report continues under another sender.

**Where it stalls.** This does not stall on other people: the waiting rate is zero and there are no deadline signals. The friction is entirely in assembly. Nearly every message carries a manual-transfer signal, meaning the numbers are re-keyed or pasted into the mail body each week from wherever they were measured. That hand-assembly is where the one visible error comes from: a follow-up correcting the reporting period itself — "Sorry, the effective date for this new report is 01/07-01/11" — a mistake in the header of a report whose content is otherwise identical week to week. Because the report is issued rather than requested, a bad figure or wrong week is only caught by the sender noticing afterwards.

**Why it recurs.** A fixed weekly reporting cadence to a standing distribution list, with the same field structure every issue and no system that publishes the figures directly to recipients.

**What could absorb it.** A scheduled job that reads the delivery, lateral-throughput and posted-price figures from their source of record, renders them into the existing fixed template with the week's date range derived from the run date, and mails it to the standing list — leaving a human to review rather than transcribe. Deriving the effective-date line automatically removes the one error class visible in the set.

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

- "Sorry, the effective date for this new report is 01/07-01/11."
  — `corpus/lokay-m/sent_items/46.` bytes 1231–1292, lines 23–23
    ```
    sed -n '23,23p' corpus/lokay-m/sent_items/46.
    ```
- "Below is my last California Interstate Capacity Report."
  — `corpus/lokay-m/inbox/20.` bytes 728–783, lines 19–19
    ```
    sed -n '19,19p' corpus/lokay-m/inbox/20.
    ```
- "Transwestern's average deliveries to California were 1015 MMBtu/d (93%), with San Juan lateral throughput at 873 MMBtu/d."
  — `corpus/lokay-m/sent_items/110.` bytes 1339–1460, lines 23–23
    ```
    sed -n '23,23p' corpus/lokay-m/sent_items/110.
    ```
- "El Paso's average deliveries to California were 1782 MMBtu/d (66%):"
  — `corpus/lokay-m/inbox/10.` bytes 1487–1554, lines 24–24
    ```
    sed -n '24,24p' corpus/lokay-m/inbox/10.
    ```
- "Transwestern's average deliveries to California were 1122 MMBtu/d (103%), with San Juan lateral throughput at 844 MMBtu/d."
  — `corpus/lokay-m/sent_items/18.` bytes 1339–1461, lines 23–23
    ```
    sed -n '23,23p' corpus/lokay-m/sent_items/18.
    ```
- "Transwestern's average deliveries to California were 815 MMBtu/d (75%), with San Juan lateral throughput at 879 MMBtu/d."
  — `corpus/lokay-m/sent_items/117.` bytes 1338–1458, lines 23–23
    ```
    sed -n '23,23p' corpus/lokay-m/sent_items/117.
    ```
- "Transwestern's average deliveries to California were 884 MMBtu/d (81%), with San Juan lateral throughput at 773 MMBtu/d."
  — `corpus/lokay-m/inbox/32.` bytes 1333–1453, lines 23–23
    ```
    sed -n '23,23p' corpus/lokay-m/inbox/32.
    ```
- "Transwestern's average deliveries to California were 959 MMBtu/d (88%), with San Juan lateral throughput at 827 MMBtu/d."
  — `corpus/lokay-m/sent_items/63.` bytes 1338–1458, lines 23–23
    ```
    sed -n '23,23p' corpus/lokay-m/sent_items/63.
    ```

## 4. Monthly meter variance clean-up between scheduled and actual volumes

**$108/month** (range $24–$369) · 1.3 automatable hours/month · confidence high

*Measured:* 47 messages in 41 task instances, 29 sender(s), 81 people, 17 months. rework 45%, waiting 23%, manual_transfer 30%, deadline 9%.

**What happens.** A variance or exception report — the UA4 report, a meter exception report, or a counterparty's meter statement — shows a meter where the confirmed nomination and the measured flow do not agree, or where flow cannot be allocated to any contract. Whoever owns the meter emails the scheduler, the allocation group or the counterparty contact asking for the missing piece: a contract or purchase for the unallocatable volume, a transport delivery to clear an exception, or a correction to estimated volumes so Unify matches what the pipeline shows was allocated. The recipient investigates, sometimes reallocating flow by hand as a temporary fix, and the thread ends when the numbers agree or the item is dropped off a running exception list. Supporting figures move by email, spreadsheet and in some cases fax, and the same meters and contracts reappear in later months.

**Where it stalls.** The variance cannot be cleared by the person who spots it: they need someone else to create a contract or purchase, adjust Unify or Sitara, or supply the counterparty's meter statement, and that reply frequently does not come. Escalation messages in this cluster are chasing an earlier unanswered mail ("I sent Jackie Young an email back showing her TETCO's numbers and I haven't received a response"), and several months are resolved only by a manual reallocation described as a temporary fix, which leaves the underlying mismatch to surface again. Ownership is also not stable — one message has to tell a colleague who now runs the daily imbalance check and where to send the numbers.

**Why it recurs.** Measurement and allocation close monthly while nominations are set daily, so every cycle produces a fresh exception list; senders describe it as "an ongoing issue every month" and "booking an imbalance every month" on the same contracts.

**What could absorb it.** A standing monthly reconciliation queue that pulls the exception rows (UA4 / meter exception output) against Unify and Sitara positions, names the meter's current owner and the specific missing artefact — contract, purchase, or counterparty statement — and re-raises any item still open after a set number of days instead of relying on a chase email. Repeat-offender meters and contracts should be flagged so recurring imbalances get a permanent contract fix rather than another hand reallocation.

**How the number was reached.**

```
41.00 task instances / 17 months of coverage = 2.412 instances per month
minutes per instance = 20 handle + (1.15 touches - 1) x 7 + 0.45 rework rate x 20 + 0.23 waiting rate x 4 = 30.90 min
coordination multiplier = 1 + 0.35 x (3 median participants - 1) = 1.700
hours per month = 2.412 x 30.90 x 1.700 / 60 = 2.111
automatable hours = 2.111 x 0.6 automatable share = 1.267
dollars per month = 1.267 h x $85/h = $107.68
```

Assumptions from `config/estimation.yml#task_classes.volume_imbalance_reconciliation`.

**Evidence.**

- "I received another email, which I will copy below, asking me to go in for the 
month of October and adjust all of my estimated volumes in Unify to match 
what HPL shows that we were allocated."
  — `corpus/farmer-d/logistics/1972.` bytes 2862–3054, lines 56–58 · rewrapped
    ```
    sed -n '56,58p' corpus/farmer-d/logistics/1972.
    ```
- "I sent Jackie Young an email 
back showing her TETCO's numbers and I haven't received a response."
  — `corpus/farmer-d/logistics/1972.` bytes 3360–3457, lines 62–63 · rewrapped
    ```
    sed -n '62,63p' corpus/farmer-d/logistics/1972.
    ```
- "The two meters below are new and have unallocatable flow.......I will need a 
purchase for each of them."
  — `corpus/farmer-d/logistics/1413.` bytes 519–623, lines 19–20 · rewrapped
    ```
    sed -n '19,20p' corpus/farmer-d/logistics/1413.
    ```
- "Please take a look at the following meters which are showing up with 
variances on my UA4 report."
  — `corpus/farmer-d/logistics/1413.` bytes 997–1094, lines 38–39 · rewrapped
    ```
    sed -n '38,39p' corpus/farmer-d/logistics/1413.
    ```
- "We have an ongoing issue every month between what we nominate from GEPL into HGPL"
  — `corpus/farmer-d/logistics/160.` bytes 1277–1358, lines 23–23
    ```
    sed -n '23,23p' corpus/farmer-d/logistics/160.
    ```
- "Would you please fax the meter statements from GEPL for February so that I can try to determine which meters are flowing over what is nominated"
  — `corpus/farmer-d/logistics/160.` bytes 1587–1730, lines 23–23
    ```
    sed -n '23,23p' corpus/farmer-d/logistics/160.
    ```
- "scheduling had 8,928 
MMBtu confirmed at this point and only 646 MMBtu flowed"
  — `corpus/farmer-d/logistics/2100.` bytes 1460–1537, lines 36–37 · rewrapped
    ```
    sed -n '36,37p' corpus/farmer-d/logistics/2100.
    ```
- "As a temporary fix I reallocated 
the meter and gave the total flow to Alpine Resources"
  — `corpus/farmer-d/logistics/2100.` bytes 1600–1687, lines 38–39 · rewrapped
    ```
    sed -n '38,39p' corpus/farmer-d/logistics/2100.
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

## 6. Moving deals between trading books by hand-run script requests

**$83/month** (range $15–$340) · 1.0 automatable hours/month · confidence medium

*Measured:* 14 messages in 10 task instances, 5 sender(s), 24 people, 3 months. waiting 7%, manual_transfer 21%, deadline 21%.

**What happens.** Someone who owns a book decides a set of deals sits in the wrong place — index deals in FT-WEST that belong in GD-NEW, an INTRA-EMWMEH book that should become FT-IM-ENOV, or, in January 2002, financial deals being swept into "bankruptcy books". They mail a request naming the source book, the destination book and any counterparty or TAGG short name needed to identify the deals, often with a date by which the move must be done. Whoever runs the move answers clarifying questions about which book and which deal types are in scope, then re-runs a script that was already used for a previous book pair. The thread closes with a confirmation back to the requester, and stragglers are frequently mailed in afterwards as a follow-up request.

**Where it stalls.** The move cannot be executed until the requester answers identification questions — which exact book name, whether financial deals only, which counterparty short name — and the exemplars show that dependency explicitly ("If I can have all the answers soon then I think the deals move can be completed around 3:00p.m.", "the book is ENA-FT-WT-SOCAL. Answer to question 2 & 3 - yes"). The scope is also not settled on the first pass: further deals arrive later as "a few more stragglers to move into the bankruptcy books", so the same script is run again for the same reclassification. Who owns the execution step beyond running the script is not visible in these messages.

**Why it recurs.** Book structures change — new books, joint-venture books, and in January 2002 a bankruptcy reclassification — and there is no self-service way for a book owner to reassign deals, so each change becomes an emailed request plus a hand-run script.

**What could absorb it.** A parameterised book-transfer job with a required intake form (source book, destination book, deal type filter, counterparty/TAGG short name, effective date) so the same script can be re-run without a clarification round trip, plus a residual query that lists any deals still in the source book after the run to catch stragglers before the requester finds them.

**How the number was reached.**

```
10.00 task instances / 3 months of coverage = 3.333 instances per month
minutes per instance = 12 handle + (1.40 touches - 1) x 5 + 0.00 rework rate x 18 + 0.07 waiting rate x 3 = 14.21 min
coordination multiplier = 1 + 0.35 x (6 median participants - 1) = 2.750
hours per month = 3.333 x 14.21 x 2.750 / 60 = 2.172
automatable hours = 2.172 x 0.45 automatable share = 0.977
dollars per month = 0.977 h x $85/h = $83.06
```

Assumptions from `config/estimation.yml#task_classes.deal_entry_correction`.

**Evidence.**

- "move any deals with the FT-TERMIN-GD book to the bankruptcy book from NG-Price.  Financial deals only."
  — `corpus/giron-d/inbox/44.` bytes 1057–1159, lines 22–22
    ```
    sed -n '22,22p' corpus/giron-d/inbox/44.
    ```
- "should be the exact same script as yesterday, just substitute FT_TERMIN-GD for the two books"
  — `corpus/giron-d/inbox/44.` bytes 1221–1313, lines 22–22
    ```
    sed -n '22,22p' corpus/giron-d/inbox/44.
    ```
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
- "If I can have all the answers soon then I think the deals move can be completed around 3:00p.m."
  — `corpus/giron-d/inbox/67.` bytes 1166–1261, lines 29–29
    ```
    sed -n '29,29p' corpus/giron-d/inbox/67.
    ```
- "Currently, all of our index deals are in the FT-WEST book.  I would like to 
move them all to the GD-NEW book."
  — `corpus/giron-d/sent/575.` bytes 449–559, lines 19–20 · rewrapped
    ```
    sed -n '19,20p' corpus/giron-d/sent/575.
    ```
- "Here are a few more stragglers to move into the bankruptcy books:"
  — `corpus/giron-d/inbox/57.` bytes 1171–1236, lines 23–23
    ```
    sed -n '23,23p' corpus/giron-d/inbox/57.
    ```
- "the book is ENA-FT-WT-SOCAL.  Answer to question 2 & 3 - yes"
  — `corpus/giron-d/inbox/65.` bytes 723–783, lines 20–20
    ```
    sed -n '20,20p' corpus/giron-d/inbox/65.
    ```

## 7. Extending existing deal tickets to cover unbooked meter flow

**$55/month** (range $12–$182) · 0.6 automatable hours/month · confidence high

*Measured:* 12 messages in 8 task instances, 5 sender(s), 13 people, 4 months. rework 92%, waiting 25%, manual_transfer 8%.

**What happens.** Gas is found to have flowed at a meter with no deal or nomination behind it, sometimes for a month that has already closed. The person who spots the gap mails the deal owner with the meter, the dates, the volume and the last deal number used, and asks that the existing deal ticket be extended to cover the flow rather than a new deal being written. Once extended, Volume Management can create the accounting arrangement and the volumes can be cleared. The thread ends when the requester confirms the extension has appeared in Unify; several threads instead continue with "This has not yet shown up in Unify. Did you use the same deal ticket?" until someone re-checks.

**Where it stalls.** Two places. First, the extension is entered in one system but does not surface in Unify, so the requester has to ask again whether the same deal ticket was used before accounting can proceed — the confirmation messages here are re-asks, not sign-offs. Second, some gaps surface long after the flow month, and the record needed to resolve them lives outside current systems: one response explains the East Desk was not on Unify for the flow period and the pathing sat in Autonoms, which is not Y2K compatible, drawing the escalation "Hopefully we're not just finding out about this?"

**Why it recurs.** Flow at a meter and the deal that books it are captured separately, so unbooked volume only appears after the fact and must be patched by hand-extending an existing ticket; nothing reconciles the two systems on a schedule.

**What could absorb it.** A scheduled reconciliation comparing measured meter flow against booked deal coverage by meter and date, raising each exception with the last deal number pre-filled, plus a confirmation hook that reports back when the extended deal has propagated to Unify — removing the "has it shown up yet" round trips.

**How the number was reached.**

```
8.00 task instances / 4 months of coverage = 2.000 instances per month
minutes per instance = 12 handle + (1.50 touches - 1) x 5 + 0.92 rework rate x 18 + 0.25 waiting rate x 3 = 31.75 min
coordination multiplier = 1 + 0.35 x (2 median participants - 1) = 1.350
hours per month = 2.000 x 31.75 x 1.350 / 60 = 1.429
automatable hours = 1.429 x 0.45 automatable share = 0.643
dollars per month = 0.643 h x $85/h = $54.65
```

Assumptions from `config/estimation.yml#task_classes.deal_entry_correction`.

**Evidence.**

- "This has not yet shown up in Unify.  Did you use the same deal ticket?"
  — `corpus/farmer-d/logistics/2123.` bytes 472–542, lines 19–19
    ```
    sed -n '19,19p' corpus/farmer-d/logistics/2123.
    ```
- "The East Desk was not up and 
running on Unify in June of 1999.  All of our pathing for June of 1999 was in 
Autonoms and it's not y2K compatabile."
  — `corpus/farmer-d/logistics/1489.` bytes 976–1123, lines 25–27 · rewrapped
    ```
    sed -n '25,27p' corpus/farmer-d/logistics/1489.
    ```
- "Is this date really June of 1999?  Hopefully we're not just finding out about 
this?"
  — `corpus/farmer-d/logistics/1492.` bytes 1357–1441, lines 38–39 · rewrapped
    ```
    sed -n '38,39p' corpus/farmer-d/logistics/1492.
    ```
- "Last deal used was 289396 could you extend it."
  — `corpus/farmer-d/logistics/2125.` bytes 598–644, lines 20–20
    ```
    sed -n '20,20p' corpus/farmer-d/logistics/2125.
    ```
- "I'll get Accounting Arrangements for these when you let me know the deal 
status and get them cleared up."
  — `corpus/farmer-d/logistics/2125.` bytes 891–996, lines 26–27 · rewrapped
    ```
    sed -n '26,27p' corpus/farmer-d/logistics/2125.
    ```
- "Could you extend this deal thru the 30th so that I 
can have Vol. Management create an accounting arrangement for it."
  — `corpus/farmer-d/logistics/1277.` bytes 548–665, lines 18–19 · rewrapped
    ```
    sed -n '18,19p' corpus/farmer-d/logistics/1277.
    ```
- "Can this deal be extended to cover the January and February flow?"
  — `corpus/farmer-d/logistics/2122.` bytes 649–714, lines 26–26
    ```
    sed -n '26,26p' corpus/farmer-d/logistics/2122.
    ```
- "there was no nomination at the Enerfin meter."
  — `corpus/farmer-d/logistics/1486.` bytes 659–704, lines 21–21
    ```
    sed -n '21,21p' corpus/farmer-d/logistics/1486.
    ```

## 8. Mid-month nomination revisions re-keyed by hand for Josey, Katy and El Paso

**$44/month** (range $9–$147) · 0.5 automatable hours/month · confidence high

*Measured:* 9 messages in 8 task instances, 4 sender(s), 7 people, 5 months. rework 100%, waiting 11%, manual_transfer 11%.

**What happens.** A counterparty or plant changes the gas volume it wants to move partway through an already-nominated month, and someone mails the revision into the logistics desk. The desk re-issues the affected month's setup — messages take the form "Here's REVISED March 2000 (effective 3/18/00) setup for Josey" — or, where a volume is already loaded, edits it directly, as in "I went ahead and changed the volume down to 12,400 from 13,000." Some revisions arrive as an announcement to be actioned ("Prize Energy revised their nom eff. 6/26 through 6/29 for the following meters"), others as a request for approval before the number is changed in Unify. The work ends when the new volume is reflected in the nomination setup and, where a counterparty is involved, confirmed back. Every message in this cluster carries a rework signal: the nomination existed and is being redone.

**Where it stalls.** The revision cannot always be applied on the sender's own authority: one message asks "Will you approve revising the volume in Unify down to 2,300? Please advise" while the same thread notes "Charlotte Hawkins is having trouble confirming the volume of 5,733 with El Paso" — the change sits pending both an internal approval and a counterparty confirmation that has not come. Revisions also arrive keyed to specific effective dates and nomination cycles (an "effective 3/21/00 9:00am cycle" setup), so a late change forces the whole month's setup to be re-issued rather than patched, and one sender sends early explicitly because the next month's work is already crowding in.

**Why it recurs.** Nominations are set for a month but volumes change mid-month at plant and counterparty level, so each change re-opens a setup that was already complete, across several meters and multiple months.

**What could absorb it.** A revision intake form that captures counterparty, meters, effective date and cycle, then writes the delta into Unify and returns a confirmation request to the counterparty automatically, so only the changed days are re-issued instead of the whole monthly setup. Pending confirmations could be tracked in a standing list rather than chased by mail.

**How the number was reached.**

```
8.00 task instances / 5 months of coverage = 1.600 instances per month
minutes per instance = 8 handle + (1.12 touches - 1) x 3 + 1.00 rework rate x 12 + 0.11 waiting rate x 2 = 20.60 min
coordination multiplier = 1 + 0.35 x (3 median participants - 1) = 1.700
hours per month = 1.600 x 20.60 x 1.700 / 60 = 0.934
automatable hours = 0.934 x 0.55 automatable share = 0.514
dollars per month = 0.514 h x $85/h = $43.65
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
- "I went ahead and changed the volume 
down to 12,400 from 13,000."
  — `corpus/farmer-d/logistics/803.` bytes 637–701, lines 19–20
    ```
    sed -n '19,20p' corpus/farmer-d/logistics/803.
    ```
- "Here's REVISED March 2000 (effective 3/18/00 ) setup for Josey"
  — `corpus/farmer-d/logistics/913.` bytes 987–1049, lines 31–31
    ```
    sed -n '31,31p' corpus/farmer-d/logistics/913.
    ```
- "This change is for the last two days of the month of March (I am sending a
day earlier than normal deadline because I'm getting covered up with April!)"
  — `corpus/farmer-d/logistics/984.` bytes 938–1089, lines 31–32 · rewrapped
    ```
    sed -n '31,32p' corpus/farmer-d/logistics/984.
    ```
- "Prize Energy revised their nom eff. 6/26 through 6/29 for the following 
meters:"
  — `corpus/farmer-d/logistics/1239.` bytes 455–535, lines 19–20
    ```
    sed -n '19,20p' corpus/farmer-d/logistics/1239.
    ```
- "There has been a change for the Katy Plant.  First of the month nom is now 
expected to be 5,479 MMBtu/d."
  — `corpus/farmer-d/logistics/1467.` bytes 798–903, lines 26–27 · rewrapped
    ```
    sed -n '26,27p' corpus/farmer-d/logistics/1467.
    ```
- "Here's REVISED February 2000 (effective 2/17/00 ) setup for Josey"
  — `corpus/farmer-d/logistics/800.` bytes 897–962, lines 29–29
    ```
    sed -n '29,29p' corpus/farmer-d/logistics/800.
    ```

## 9. Monthly gas nominations mailed in by counterparties, then revised by hand

**$38/month** (range $7–$133) · 0.4 automatable hours/month · confidence high

*Measured:* 12 messages in 12 task instances, 6 sender(s), 31 people, 6 months. rework 17%, waiting 8%, deadline 17%.

**What happens.** Each month, counterparties and internal customers e-mail the gas logistics desk the volumes they intend to move for the coming month. The most repetitive form is a near-identical note from EGPFC nominating natural gas requirements for the MTBE Plant at Morgan's Point, restated month after month with only the month and volumes changing; others arrive as attached documents such as "CALPINE MONTHLY GAS NOMINATION___.doc" or as mail forwarded on from outside parties. The scheduler reads the mail and sets up the nomination for the month, and where something changes mid-month re-issues a corrected setup — the exemplars include "REVISED December 1999 (effective 12/9/99) setup for Josey" and a second revision effective 12/15/99 for the same month. Some notes are purely informational, flagging that a nomination is ending ("This is the last month we will be buying this gas!!!!"). The work closes when the setup matches what the counterparty asked for and the month's flow is covered.

**Where it stalls.** Two failure modes are visible. First, changes agreed verbally do not reach the setup: one correction says plainly "this change was missed but was discussed with you last week," and the same month required two separate revised setups with different effective dates, so the month is built more than once. Second, a nomination cannot be completed because a required reference sits with someone else — "I am still waiting on a transport number from lori Allen in your" — leaving the scheduler chasing a third party as a monthly effective date approaches. Because intake is free-form e-mail and attachments rather than a form, there is no visible completeness check before setup begins.

**Why it recurs.** Nominations are per-month by construction, so the same counterparties send the same shaped request every month for the same plant and points, and any mid-month change forces a re-issued setup with a new effective date.

**What could absorb it.** A structured monthly nomination intake — a fixed template per counterparty capturing point, volume, effective date and transport number, and not accepted until those fields are present — feeding setup directly, with a reminder to recurring senders ahead of the monthly cutoff and a change log so a revision supersedes rather than duplicates the prior setup.

**How the number was reached.**

```
12.00 task instances / 6 months of coverage = 2.000 instances per month
minutes per instance = 8 handle + (1.00 touches - 1) x 3 + 0.17 rework rate x 12 + 0.08 waiting rate x 2 = 10.17 min
coordination multiplier = 1 + 0.35 x (5 median participants - 1) = 2.400
hours per month = 2.000 x 10.17 x 2.400 / 60 = 0.813
automatable hours = 0.813 x 0.55 automatable share = 0.447
dollars per month = 0.447 h x $85/h = $38.02
```

Assumptions from `config/estimation.yml#task_classes.gas_nomination`.

**Evidence.**

- "this change was missed but was discussed with you
last week."
  — `corpus/farmer-d/logistics/586.` bytes 908–968, lines 30–31 · rewrapped
    ```
    sed -n '30,31p' corpus/farmer-d/logistics/586.
    ```
- "Here's REVISED December 1999 (effective 12/9/99 ) setup for
Josey"
  — `corpus/farmer-d/logistics/586.` bytes 1206–1271, lines 36–37 · rewrapped
    ```
    sed -n '36,37p' corpus/farmer-d/logistics/586.
    ```
- "Here's REVISED December 1999 (effective 12/15/99 ) setup for
Josey"
  — `corpus/farmer-d/logistics/587.` bytes 931–997, lines 29–30 · rewrapped
    ```
    sed -n '29,30p' corpus/farmer-d/logistics/587.
    ```
- "I am still waiting on a transport number from lori Allen in your"
  — `corpus/farmer-d/logistics/1539.` bytes 823–887, lines 21–21
    ```
    sed -n '21,21p' corpus/farmer-d/logistics/1539.
    ```
- "EGPFC nominates the following natural gas requirements for the MTBE Plant at 
Morgan's Point for October 2000:"
  — `corpus/farmer-d/logistics/1423.` bytes 1192–1302, lines 28–29 · rewrapped
    ```
    sed -n '28,29p' corpus/farmer-d/logistics/1423.
    ```
- "EGPFC nominates the following requirements for the MTBE Plant at Morgan's 
Point for January 2000:"
  — `corpus/farmer-d/logistics/607.` bytes 1180–1278, lines 28–29 · rewrapped
    ```
    sed -n '28,29p' corpus/farmer-d/logistics/607.
    ```
- "CALPINE MONTHLY GAS NOMINATION___.doc"
  — `corpus/farmer-d/logistics/619.` bytes 556–593, lines 19–19
    ```
    sed -n '19,19p' corpus/farmer-d/logistics/619.
    ```
- "This is the last month we will be buying this gas!!!!"
  — `corpus/farmer-d/logistics/1424.` bytes 793–846, lines 31–31
    ```
    sed -n '31,31p' corpus/farmer-d/logistics/1424.
    ```

## 10. Fixing wrong deal prices in Sitara by email request

**$36/month** (range $8–$120) · 0.4 automatable hours/month · confidence high

*Measured:* 9 messages in 8 task instances, 7 sender(s), 14 people, 6 months. rework 100%, waiting 22%, manual_transfer 22%, deadline 33%.

**What happens.** Someone downstream of deal capture — an invoicing or settlement person, or a scheduler reviewing a daily deal summary — notices that the price on a booked deal in Sitara is wrong, either a plain keying error or the wrong index formula. They email the person who has write access to that deal, naming the deal or ticket number and stating the price and volume it should carry, sometimes for specific production days. The recipient makes the edit and replies that the price has been adjusted, or in one case says the ticket cannot be opened because access is denied. The requester frequently asks to be notified when the change is done so the invoice or the flash figure can be produced from corrected data. The exchange ends with a confirmation message rather than any system-generated evidence of the change.

**Where it stalls.** The requester cannot make the correction themselves: every message here is one person asking another to type a value into Sitara, and one exemplar is an escalation because the sender was locked out of the ticket they needed to fix. Because the change is made by hand and confirmed by reply, the requester waits on a human before an invoice can go out or a morning flash can be recalculated, and several requests carry an explicit same-day deadline. The corpus shows no check that the entered value matched what was asked for.

**Why it recurs.** Prices are keyed once at deal capture and only surface as wrong later, when an invoice, a daily deal summary or a monthly settlement is built from them — so each billing cycle produces a fresh batch of correction requests.

**What could absorb it.** Give the settlement and invoicing requesters scoped edit rights on price fields with an audit trail, so the correction is made once by the person who found it; alternatively, a structured correction form that writes the deal number, effective days and new price straight to Sitara and returns a confirmation would remove the free-text email round trip.

**How the number was reached.**

```
8.00 task instances / 6 months of coverage = 1.333 instances per month
minutes per instance = 12 handle + (1.12 touches - 1) x 5 + 1.00 rework rate x 18 + 0.22 waiting rate x 3 = 31.29 min
coordination multiplier = 1 + 0.35 x (2 median participants - 1) = 1.350
hours per month = 1.333 x 31.29 x 1.350 / 60 = 0.939
automatable hours = 0.939 x 0.45 automatable share = 0.422
dollars per month = 0.422 h x $85/h = $35.91
```

Assumptions from `config/estimation.yml#task_classes.deal_entry_correction`.

**Evidence.**

- "For June, I need a couple of things changed in Sitara: 
Deal 819592 - the commodity price needs to be 3.6318"
  — `corpus/farmer-d/logistics/74.` bytes 652–760, lines 21–22
    ```
    sed -n '21,22p' corpus/farmer-d/logistics/74.
    ```
- "Please notify me when these changes have been made."
  — `corpus/farmer-d/logistics/74.` bytes 1386–1437, lines 32–32
    ```
    sed -n '32,32p' corpus/farmer-d/logistics/74.
    ```
- "Could you pls the pricing on this deal for March 2001 Production for days 25 & 26 to  $ 5.285?"
  — `corpus/farmer-d/logistics/177.` bytes 900–994, lines 24–24
    ```
    sed -n '24,24p' corpus/farmer-d/logistics/177.
    ```
- "I need to send out my invoice this afternoon"
  — `corpus/farmer-d/logistics/177.` bytes 1050–1094, lines 26–26
    ```
    sed -n '26,26p' corpus/farmer-d/logistics/177.
    ```
- "I tried to get into the Sitara ticket # 373590 to correct the swing pricing
....but I am not allowed to access it"
  — `corpus/farmer-d/logistics/106.` bytes 1341–1454, lines 39–40
    ```
    sed -n '39,40p' corpus/farmer-d/logistics/106.
    ```
- "I changed the El Paso Electric deal #697528 price from $4 to $68."
  — `corpus/williams-w3/sent_items/366.` bytes 579–644, lines 18–18
    ```
    sed -n '18,18p' corpus/williams-w3/sent_items/366.
    ```
- "Is there any way to recalculate this (or simply zero it out) prior to the morning flash?"
  — `corpus/williams-w3/sent_items/366.` bytes 723–811, lines 18–18
    ```
    sed -n '18,18p' corpus/williams-w3/sent_items/366.
    ```
- "Currently, Sitara is showing a price of  HSC GDP +.05."
  — `corpus/farmer-d/logistics/179.` bytes 791–845, lines 18–18
    ```
    sed -n '18,18p' corpus/farmer-d/logistics/179.
    ```

## 11. Daily Calpine and HPL gas nominations mailed as attached documents

**$33/month** (range $6–$113) · 0.4 automatable hours/month · confidence high

*Measured:* 26 messages in 26 task instances, 4 sender(s), 27 people, 13 months. rework 4%, deadline 4%.

**What happens.** Each flow day a scheduler prepares a nomination for a named counterparty or pipeline — most often "Calpine Daily Gas Nomination", sometimes Hidalgo, sometimes "HPL Nominations for <date>" — and mails it out. The nomination itself travels as an attached document (repeatedly the same file name, `CALPINE DAILY GAS NOMINATION 1.doc`) rather than as text in the body, so the message is little more than a carrier for the file; in at least one instance a monthly nomination document is attached alongside the daily one. Most messages carry a request role: the sender is asking the recipient to act on the attached volumes. A small number close the loop the same way — a short reply confirming the volumes and that the path is unchanged from the previous day. The same pattern reappears from late 1999 into 2001 across several senders and a wide recipient set.

**Where it stalls.** The nomination lives in a document attached to mail, not in a system that both sides read, so nothing about a given day's volumes is queryable — confirmation depends on someone replying in prose ("Confirmed on my end. Same volumes as yesterday"). When volumes change, the fix is a re-issued document forwarded onward and marked REVISED, which is the visible rework path. Waiting and manual-transfer signals are not present in these messages, so this cluster shows the send-and-attach step rather than any chasing that may follow; the review or approval step, if there is one, is not visible in the mail.

**Why it recurs.** Nominations have a daily flow-date cutoff, so the same document is rebuilt and mailed again every day for each counterparty and pipeline, with a monthly variant alongside it.

**What could absorb it.** Hold the daily nomination as structured records rather than a re-typed document: a scheduled job that renders the day's volumes per counterparty from the deal/scheduling source, sends them on the daily cycle, and records the counterparty's confirmation against the flow date, so revisions supersede rather than being forwarded as a new file.

**How the number was reached.**

```
coverage = 25 dated / 26 messages = 0.962; instances 26 / 0.962 = 27.04 adjusted
27.04 task instances / 13 months of coverage = 2.080 instances per month
minutes per instance = 8 handle + (1.00 touches - 1) x 3 + 0.04 rework rate x 12 + 0.00 waiting rate x 2 = 8.46 min
coordination multiplier = 1 + 0.35 x (5 median participants - 1) = 2.400
hours per month = 2.080 x 8.46 x 2.400 / 60 = 0.704
automatable hours = 0.704 x 0.55 automatable share = 0.387
dollars per month = 0.387 h x $85/h = $32.91
```

Assumptions from `config/estimation.yml#task_classes.gas_nomination`.

**Evidence.**

- "FW: Calpine Daily Gas Nomination (REVISED)"
  — `corpus/farmer-d/logistics/773.` bytes 160–202, lines 5–5
    ```
    sed -n '5,5p' corpus/farmer-d/logistics/773.
    ```
- "Confirmed on my end. Same volumes as yesterday, no changes to the path."
  — `corpus/giron-d/sent/795.` bytes 452–523, lines 16–16
    ```
    sed -n '16,16p' corpus/giron-d/sent/795.
    ```
- "- CALPINE MONTHLY GAS NOMINATION___.doc"
  — `corpus/farmer-d/logistics/1370.` bytes 994–1033, lines 31–31 · decoded_exact
    ```
    sed -n '31,31p' corpus/farmer-d/logistics/1370.
    ```
- "HPL Nom for January 4, 2001"
  — `corpus/farmer-d/logistics/2025.` bytes 313–340, lines 7–7
    ```
    sed -n '7,7p' corpus/farmer-d/logistics/2025.
    ```
- "HPL Nominations for December 28, 1999"
  — `corpus/farmer-d/logistics/615.` bytes 240–277, lines 6–6
    ```
    sed -n '6,6p' corpus/farmer-d/logistics/615.
    ```
- "HIDALGO DAILY GAS NOMINATION.doc"
  — `corpus/farmer-d/logistics/1229.` bytes 667–699, lines 19–19
    ```
    sed -n '19,19p' corpus/farmer-d/logistics/1229.
    ```
- "Calpine Daily Gas Nomination"
  — `corpus/farmer-d/logistics/1561.` bytes 167–195, lines 5–5
    ```
    sed -n '5,5p' corpus/farmer-d/logistics/1561.
    ```
- "CALPINE DAILY GAS NOMINATION 1.doc"
  — `corpus/farmer-d/logistics/1318.` bytes 746–780, lines 19–19
    ```
    sed -n '19,19p' corpus/farmer-d/logistics/1318.
    ```

## 12. Real-time West power position handoff notes to the next scheduling shift

**$24/month** (range $6–$72) · 0.3 automatable hours/month · confidence high

*Measured:* 10 messages in 10 task instances, 2 sender(s), 19 people, 4 months. rework 10%, manual_transfer 40%, deadline 10%.

**What happens.** A West-desk scheduler writes a free-text note to the real-time desk describing the current power position and the actions the next shift must take: buy or sell to cover a long or short, book purchases from the APX or Calimbalance and matching sales under the ST-WBOM book in Enpower, and schedule specific hour-ending blocks at named points such as PV, SP-15 and PNM. Each note carries the megawatts, the hours, the price and the counterparty in prose, and often the deal numbers already booked. Most messages are status reports of what the sender has already done; a minority are direct requests asking the recipient to place a trade, cover a short, or adjust their own sheets for the following day. The work ends when the receiving scheduler enters the transactions in Enpower and the position reconciles, though that confirmation is not visible in these messages.

**Where it stalls.** The position and the instruction live only in the body of an email, so the receiving desk retypes megawatts, hours, prices and books into Enpower and into their own spreadsheets — the manual-transfer signal appears on a sizeable share of these notes, including one that simply asks the recipient to "adjust your sheets for tomorrow". Where the physical constraint moves after the note is written, the transaction is redone rather than corrected in place: one message records cutting IID from 120mw to 100mw and cutting a 25mw PNM purchase to 13mw because imports were over capacity. Price is also not always settled in the note itself — one instruction defers to a colleague to check the price — so the booking depends on a second conversation that is not in the mail.

**Why it recurs.** Real-time power runs on a continuous shift handover: every day and every hour-ending block produces a new position that has to be passed to whoever is covering next, and the mailbox is the handover medium.

**What could absorb it.** A structured shift-handover form that captures book, point, counterparty, hour-ending range, megawatts and price as fields rather than prose, and writes the entries straight into Enpower as draft transactions for the receiving scheduler to confirm — removing the retyping and giving a record of what changed when a cut is later needed.

**How the number was reached.**

```
10.00 task instances / 4 months of coverage = 2.500 instances per month
minutes per instance = 8 handle + (1.00 touches - 1) x 3 + 0.10 rework rate x 12 + 0.00 waiting rate x 2 = 9.20 min
coordination multiplier = 1 + 0.35 x (2 median participants - 1) = 1.350
hours per month = 2.500 x 9.20 x 1.350 / 60 = 0.518
automatable hours = 0.518 x 0.55 automatable share = 0.285
dollars per month = 0.285 h x $85/h = $24.19
```

Assumptions from `config/estimation.yml#task_classes.gas_nomination`.

**Evidence.**

- "I have made the purchase from the APX and the sale to imbalance (#685979, #685978)."
  — `corpus/williams-w3/sent_items/392.` bytes 1968–2051, lines 27–27
    ```
    sed -n '27,27p' corpus/williams-w3/sent_items/392.
    ```
- "Please make real-time purchases from the Calimbalance and corresponding sales under ST-WBOM in Enpower during real time."
  — `corpus/williams-w3/sent_items/392.` bytes 2356–2476, lines 41–41
    ```
    sed -n '41,41p' corpus/williams-w3/sent_items/392.
    ```
- "I cut IID to a 100mw from a 120mw which integrated to a 115mw"
  — `corpus/williams-w3/inbox/133.` bytes 759–820, lines 19–19
    ```
    sed -n '19,19p' corpus/williams-w3/inbox/133.
    ```
- "I was forced to cut one of a 25mw purchase from PNM @ $32.00 to a 13mw because our imports were over capacity"
  — `corpus/williams-w3/inbox/133.` bytes 871–980, lines 21–21
    ```
    sed -n '21,21p' corpus/williams-w3/inbox/133.
    ```
- "Please buy energy to cover this 15 mw short on Monday under the ST-WBOM book and sell to EPE at $0 under the ST-WBOM book."
  — `corpus/williams-w3/sent_items/380.` bytes 985–1107, lines 23–23
    ```
    sed -n '23,23p' corpus/williams-w3/sent_items/380.
    ```
- "ST-WBOM is long at PV parking with PNM for HE 2 through HE 5, 20 mws each hour--for Friday and Saturday."
  — `corpus/williams-w3/sent_items/168.` bytes 555–659, lines 19–19
    ```
    sed -n '19,19p' corpus/williams-w3/sent_items/168.
    ```
- "If you could adjust your sheets for tomorrow I would appreciate it."
  — `corpus/williams-w3/sent_items/164.` bytes 731–798, lines 19–19
    ```
    sed -n '19,19p' corpus/williams-w3/sent_items/164.
    ```
- "50 mws off-peak Sunday and Monday(that's all day Sunday and off-peak Monday) at @$36-check with Kysa on price."
  — `corpus/williams-w3/sent_items/295.` bytes 543–653, lines 20–20
    ```
    sed -n '20,20p' corpus/williams-w3/sent_items/295.
    ```

## 13. Monthly nomination volume estimates for Josey Ranch and counterparty points

**$22/month** (range $5–$66) · 0.3 automatable hours/month · confidence medium

*Measured:* 8 messages in 8 task instances, 2 sender(s), 6 people, 3 months. .

**What happens.** Ahead of each new gas month, someone circulates an estimated nomination volume for the coming month — the Josey Ranch estimate is mailed out as a standing "this is the estimated nomination for the month of..." note in consecutive months. Separately, when a monthly nomination has to be set for a named counterparty or point, a colleague is asked whether a historical average is a fair basis, and the answers come back as per-point figures for Calpine, Midcon, Southern Union and Tville. The output is a set of assumed per-day or per-month volumes stated in email prose rather than in a system. The exchange ends when the estimator states an assumption the requester accepts; no confirmation or system entry is visible in these messages.

**Where it stalls.** There is no measured rework, waiting, manual-transfer or deadline signal here, so the visible friction is not chasing or correction. What is visible is that the basis for each estimate lives only in the reply — one message asks whether an average is "a good estimate", another answers that a round figure is "a safe assumption" — so the reasoning is re-derived per counterparty each month and is not recorded anywhere the next person can check. Which system, if any, receives these numbers is not visible in the evidence.

**Why it recurs.** Nominations are set on a monthly cycle, so a fresh estimate is needed for each point every month; the Josey Ranch note repeats in consecutive months with identical wording.

**What could absorb it.** A scheduled job that pulls prior-month scheduled and actual volumes per meter and counterparty and mails a pre-filled monthly estimate sheet before the new gas month, so the estimator confirms or overrides figures rather than deriving averages by hand in email.

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
- "This is the estimated Josey Ranch nomination for the month of
February 2000"
  — `corpus/farmer-d/logistics/724.` bytes 1009–1084, lines 34–35 · rewrapped
    ```
    sed -n '34,35p' corpus/farmer-d/logistics/724.
    ```
- "This is the estimated Josey Ranch nomination for the month of March"
  — `corpus/farmer-d/logistics/850.` bytes 980–1047, lines 31–31
    ```
    sed -n '31,31p' corpus/farmer-d/logistics/850.
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
  — `corpus/farmer-d/logistics/1056.` bytes 770–820, lines 37–39 · rewrapped
    ```
    sed -n '37,39p' corpus/farmer-d/logistics/1056.
    ```

## 14. Ad-hoc requests for system and deal-book access, by email

**$22/month** (range $7–$63) · 0.3 automatable hours/month · confidence medium

*Measured:* 8 messages in 7 task instances, 6 sender(s), 16 people, 5 months. waiting 25%.

**What happens.** When someone cannot see a deal book or run a report, they email a colleague or administrator asking to be granted access — to West and Chicago/Midwest deals in Sitara, to EOL, to a supervisor review role in PEP, or to a set of Netco books across regions. The request is written in free prose rather than on a form, and the sender often has to guess what the approver needs: which book, which region, whose cost center it should be charged to, and which groups belong on the request. Some messages are on behalf of the sender, others on behalf of a new or transferring staff member. The thread ends when the requester is told access has been set up, or when a confirmation email from the system is expected to arrive. Most of these messages carry the request role; only one is a notification that access is coming.

**Where it stalls.** The requester does not know the approval path or the required fields, so the mail goes out incomplete and comes back as a question — one sender asks whether a second request had to be filed and put on a different cost center, another asks how a supervisor role gets changed in PEP, and a third has to remind the recipient to add the Financial and Control group to book requests that were missing it. A quarter of the messages show waiting: the requester is blocked from running a book and asking someone else to obtain authorization on their behalf. Who owns provisioning for each system is not visible in these messages.

**Why it recurs.** Access is tied to people moving between desks, regions and books (including a whole new set of Netco books), and each system — Sitara, EOL, PEP — has its own separate request path with no shared intake.

**What could absorb it.** A single structured intake that captures person, system, book or region, role, approver and cost center up front, routes to the owner of that system, and returns a confirmation — so requests cannot be submitted missing the fields that currently generate a round trip.

**How the number was reached.**

```
7.00 task instances / 5 months of coverage = 1.400 instances per month
minutes per instance = 10 handle + (1.14 touches - 1) x 4 + 0.00 rework rate x 10 + 0.25 waiting rate x 4 = 11.57 min
coordination multiplier = 1 + 0.35 x (2 median participants - 1) = 1.350
hours per month = 1.400 x 11.57 x 1.350 / 60 = 0.364
automatable hours = 0.364 x 0.7 automatable share = 0.255
dollars per month = 0.255 h x $85/h = $21.69
```

Assumptions from `config/estimation.yml#task_classes.access_provisioning`.

**Evidence.**

- "I need access to West deals in Sitara.  At a 
mininum I still need access to all Chicago/Midwest deals also."
  — `corpus/giron-d/sent/618.` bytes 486–594, lines 19–20 · rewrapped
    ```
    sed -n '19,20p' corpus/giron-d/sent/618.
    ```
- "I don't have access to run this book.  Will you please get me authorization?"
  — `corpus/giron-d/sent/532.` bytes 445–521, lines 19–19
    ```
    sed -n '19,19p' corpus/giron-d/sent/532.
    ```
- "was I supposed to send in 
another request for her and put it on Tom's Cost Center"
  — `corpus/farmer-d/logistics/1992.` bytes 503–585, lines 17–18 · rewrapped
    ```
    sed -n '17,18p' corpus/farmer-d/logistics/1992.
    ```
- "Please add Financial and Control group to these book requests if they are missing."
  — `corpus/giron-d/inbox/159.` bytes 1056–1138, lines 22–22
    ```
    sed -n '22,22p' corpus/giron-d/inbox/159.
    ```
- "I don't believe I am set up to review as a supervisor in the PEP system.  How 
do I get this changed in the system?"
  — `corpus/giron-d/sent/789.` bytes 447–562, lines 18–19
    ```
    sed -n '18,19p' corpus/giron-d/sent/789.
    ```
- "These are book requests for the Netco books for all regions."
  — `corpus/giron-d/inbox/161.` bytes 1078–1138, lines 23–23
    ```
    sed -n '23,23p' corpus/giron-d/inbox/161.
    ```
- "You should be receiving an email regarding access to EOL."
  — `corpus/williams-w3/sent_items/224.` bytes 528–585, lines 18–18
    ```
    sed -n '18,18p' corpus/williams-w3/sent_items/224.
    ```

---

## Drafted artifacts

Ready to use on Monday morning. Every sentence asserting current practice carries a citation marker that resolves to verified evidence; recommendations carry no marker and sit under their own heading, so observation and proposal never blur.

- **Template: Weekly California Interstate Capacity Report** (`TPL-01-template-weekly-california-interstate-capacity-repor.md`) — template, for *Weekly California Capacity Report, assembled and mailed by hand*
- **Daily Credit Report — standing distribution email template** (`EML-01-daily-credit-report-standing-distribution-email-temp.md`) — email, for *"Credit Report--5/9/01" produced daily*
- **Weekly California Capacity Report — standing send email template** (`EML-02-weekly-california-capacity-report-standing-send-emai.md`) — email, for *"California Capacity Report for Week of 10/22-10/26" produced weekly*

---

## How to check any of this

```
make verify     # re-anchor every citation from scratch; recompute every number
make test       # full suite, zero model calls
make serve      # dashboard with click-through to the highlighted bytes
```

Every citation above prints the `sed` command that reproduces it. `docs/AUDIT.md` holds 25 randomly sampled citations with both `dd` and `sed` commands.

Where this is most likely wrong, and what it took on faith, is in `NOTES.md`.
