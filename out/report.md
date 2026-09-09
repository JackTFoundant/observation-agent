# Where this company is losing time

*Run `cold5` · generated 2026-09-09T15:11:36Z · corpus digest `c94acc4b08cb`*

## $1,439 per month

Range $335 – $4,623. 17 automatable hours per month at a blended $85/hour, across 11 opportunities.

Observed across 4 mailboxes and 3,240 messages, 1999-12-13 to 2002-03-25 (28 months). Not extrapolated beyond what was observed.

The range is not decoration. The counts behind these figures are measured from the corpus; the minutes-per-task are estimates nobody was able to verify, so the base number should be read as the middle of a band, not as a measurement.

**This is a floor, not a total.** 178 of 2,531 operational messages (7%) could be attributed to an identified recurring process. The other 2,353 are a long tail that failed the promotion gate - too few repetitions, too short a window, or too few people to call it a process. That work is real and is deliberately left uncosted rather than estimated. Every rejected candidate is published in `out/residual.json` with the gate it failed.

### What was read

- **3,240 files**, every one of them, 3,224 unique after removing 16 duplicates in 16 groups
- grouped into **2,823 task instances**, because a forty-message argument about one nomination is one task
- **2,531 messages** were shown to a model; 596 were acknowledgements with no new text and were counted deterministically instead
- **89 citations** verified against raw bytes, 2 rejected and published in `out/quarantine.json`

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
| 4 | Meter-level scheduled-vs-actual volume reconciliation, chased by email | $87 | $19–$299 | 1.0 | 34 | 18 | 8 | high |
| 5 | "Calpine Daily Gas Nomination" produced monthly | $87 | $19–$284 | 1.0 | 17 | 11 | 8 | medium |
| 6 | Extending Sitara deals by request to cover unallocated meter flow | $56 | $12–$203 | 0.7 | 15 | 7 | 8 | high |
| 7 | Correcting mispriced deals by hand in Sitara after the fact | $37 | $8–$124 | 0.4 | 7 | 5 | 8 | high |
| 8 | Daily gas nominations mailed as attached Word and Excel files | $33 | $6–$113 | 0.4 | 30 | 14 | 8 | high |
| 9 | Monthly first-of-month gas nominations mailed in by plant customers | $29 | $5–$100 | 0.3 | 14 | 9 | 8 | high |
| 10 | Fixing miskeyed Sitara deal entries after the fact | $26 | $6–$88 | 0.3 | 8 | 5 | 4 | medium |
| 11 | Nomination changes confirmed by hand with pipelines and counterparties | $25 | $5–$82 | 0.3 | 11 | 8 | 8 | high |

### Not counted

0 opportunities were demoted to low confidence ($0/month not included in the headline) and 2 were quarantined for insufficient evidence ($48/month excluded). See `out/quarantine.json`.

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

**What happens.** Each week a Transwestern commercial analyst compiles a California capacity summary and mails it to a fixed distribution list. The body follows the same structure every time: average Transwestern deliveries to California against capacity, San Juan lateral throughput, El Paso deliveries broken out by delivery point, and posted Gas Daily prices. The figures are pulled from other sources — spreadsheets appear alongside email in most of these messages — and retyped into the mail body rather than generated by the reporting system itself. The output is the mail itself; the thread ends when it is sent, with no reply expected. One message in the set is a backup handoff, where a colleague forwards their last version of the Interstate Capacity Report so the series can continue.

**Where it stalls.** There is no waiting and no deadline pressure visible here — nobody is chased and nothing is blocked. The friction is entirely in assembly: nearly every message carries a manual-transfer signal, meaning numbers are moved by hand out of spreadsheets into a prose email that reads identically week to week. Because the header and the numbers are hand-keyed together, the labelling can drift from the data: one message is a correction issued purely to restate the report's effective week ("Sorry, the effective date for this new report is 01/07-01/11"), which means the recipients had already read a report stamped with the wrong period.

**Why it recurs.** A fixed weekly reporting obligation to a standing distribution list. The report period rolls forward every week and the source figures live in spreadsheets that do not themselves mail anything, so a person regenerates the same document each cycle.

**What could absorb it.** A scheduled job that reads the delivery, lateral-throughput and Gas Daily figures from their source tables, renders them into the existing fixed sentence template with the report week derived from the run date, and mails it to the standing list — leaving the analyst to review rather than retype. Deriving the effective-date line from the data window would remove the class of correction seen here.

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
- "Below is my last California Interstate Capacity Report"
  — `corpus/lokay-m/inbox/20.` bytes 728–782, lines 19–19
    ```
    sed -n '19,19p' corpus/lokay-m/inbox/20.
    ```
- "Transwestern's average deliveries to California were 1058 MMBtu/d (97%), with San Juan lateral throughput at 864 MMBtu/d."
  — `corpus/lokay-m/sent_items/79.` bytes 1337–1458, lines 23–23
    ```
    sed -n '23,23p' corpus/lokay-m/sent_items/79.
    ```
- "Transwestern's average deliveries to California were 855 MMBtu/d (79%), with San Juan lateral throughput at 839 MMBtu/d."
  — `corpus/lokay-m/sent_items/47.` bytes 1343–1463, lines 23–23
    ```
    sed -n '23,23p' corpus/lokay-m/sent_items/47.
    ```
- "Transwestern's average deliveries to California were 1015 MMBtu/d (93%), with San Juan lateral throughput at 873 MMBtu/d."
  — `corpus/lokay-m/sent_items/110.` bytes 1339–1460, lines 23–23
    ```
    sed -n '23,23p' corpus/lokay-m/sent_items/110.
    ```
- "Transwestern's average deliveries to California were 1122 MMBtu/d (103%)"
  — `corpus/lokay-m/sent_items/18.` bytes 1339–1411, lines 23–23
    ```
    sed -n '23,23p' corpus/lokay-m/sent_items/18.
    ```

## 4. Meter-level scheduled-vs-actual volume reconciliation, chased by email

**$87/month** (range $19–$299) · 1.0 automatable hours/month · confidence high

*Measured:* 38 messages in 34 task instances, 26 sender(s), 75 people, 18 months. rework 50%, waiting 26%, manual_transfer 29%, deadline 8%.

**What happens.** Someone notices that the gas volume recorded as flowing at a meter does not match what was nominated, confirmed or entered as a deal — a nomination of 24,000 against roughly 16,000 flowing, 8,928 MMBtu confirmed against 646 flowed, or recorded flow at a meter with no deal at all. The finder emails the scheduler or logistics contact with the meter number, the dates and the two figures, and asks whether to adjust the nomination, cut the deal, or correct the volumes. Resolution means someone going back into a volume system — Unify, MOPS/POPS, position manager — and re-keying prior-period numbers to match what the pipeline or counterparty allocated. Related OBA cases run the same way: measured-versus-scheduled histories are assembled and sent over, sometimes with daily volume statements requested by fax. The thread closes when both sides agree on a number and the system is edited by hand; often the requester is still waiting for a reply.

**Where it stalls.** The person who spots the discrepancy cannot fix it themselves — they must ask another party to agree the number and then edit it in a system they do not own. Half of these messages carry rework signals and escalation is the second most common role: threads are reopened ("We need to revisit this issue again. There is an exception at meter 4045 for 2/99"), and one sender reports emailing TETCO's numbers to a counterpart and getting no response. Bad data also propagates before anyone catches it — POPS showing Oct 28th identical to Oct 27th — so corrections are made retroactively across whole months rather than at the time of flow.

**Why it recurs.** Nominated, confirmed and actual volumes are captured in separate systems that do not reconcile themselves, and allocations arrive from pipelines and counterparties after the flow date, so every month produces a fresh batch of meter-level exceptions to argue out and re-key.

**What could absorb it.** A scheduled comparison that joins nominated/confirmed volumes to actualised volumes per meter per day and emits an exception list — meter, dates, both figures, deal number if any, missing-deal flag — to a named owner, so the discrepancy arrives already quantified instead of being discovered by eye. Pair it with a logged adjustment path so a corrected volume is entered once and visible to both sides rather than re-keyed after email agreement.

**How the number was reached.**

```
34.00 task instances / 18 months of coverage = 1.889 instances per month
minutes per instance = 20 handle + (1.12 touches - 1) x 7 + 0.50 rework rate x 20 + 0.26 waiting rate x 4 = 31.88 min
coordination multiplier = 1 + 0.35 x (3 median participants - 1) = 1.700
hours per month = 1.889 x 31.88 x 1.700 / 60 = 1.706
automatable hours = 1.706 x 0.6 automatable share = 1.024
dollars per month = 1.024 h x $85/h = $87.00
```

Assumptions from `config/estimation.yml#task_classes.volume_imbalance_reconciliation`.

**Evidence.**

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
- "The actuals on this contract did not come in as scheduled.   The scheduled 
deliveries at Texoma are 374,503, but the actuals are 352,568."
  — `corpus/farmer-d/logistics/972.` bytes 1522–1660, lines 44–45 · rewrapped
    ```
    sed -n '44,45p' corpus/farmer-d/logistics/972.
    ```
- "can you let me know first 
if you agree with PG&E Texas numbers and if you do, will you please make the 
necessary changes in unify."
  — `corpus/farmer-d/logistics/972.` bytes 1805–1937, lines 47–49 · rewrapped
    ```
    sed -n '47,49p' corpus/farmer-d/logistics/972.
    ```
- "We are getting bad numbers in POPS for Sat. Oct. 28th.  They are the same as
Oct. 27th (27th is correct)."
  — `corpus/farmer-d/logistics/1476.` bytes 1309–1414, lines 27–28 · rewrapped
    ```
    sed -n '27,28p' corpus/farmer-d/logistics/1476.
    ```
- "Please watch imbalances very closely.  Double 
check
all numbers."
  — `corpus/farmer-d/logistics/1476.` bytes 1417–1482, lines 28–30 · rewrapped
    ```
    sed -n '28,30p' corpus/farmer-d/logistics/1476.
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

## 6. Extending Sitara deals by request to cover unallocated meter flow

**$56/month** (range $12–$203) · 0.7 automatable hours/month · confidence high

*Measured:* 20 messages in 15 task instances, 7 sender(s), 19 people, 7 months. rework 55%, waiting 20%, deadline 5%.

**What happens.** Volume Management or a scheduler finds gas that flowed at a meter on a date the underlying deal does not cover — an extra day or two after a deal's end date, a small decatherm volume, or a whole additional month. They email the deal owner (most often Daren) with the meter number, the deal number, the dates and the volume, and ask that the existing deal be extended so an accounting arrangement can be created against it. The alternative, named in the messages themselves, is to allocate the gas "off to strangers" until someone decides what to do. The exchange ends when the deal owner extends the deal in Sitara/Unify and replies, or when a different deal is put in place instead.

**Where it stalls.** The requester cannot act on the deal themselves, so each item waits on one person; escalation messages say plainly that "Logistics is waiting to hear from Daren on this issue" and repeat the same ask days later. Discovery is late rather than continuous — one thread surfaces flow dated June 1999 and draws the reply "Hopefully we're not just finding out about this?", with the follow-up explaining the pathing sat in Autonoms, not Unify, and was not Y2K compatible. The high rework rate reflects deals being reopened after the fact, including one requester asking to extend "one more time for me".

**Why it recurs.** Physical flow routinely runs past the deal's end date — a valve not fully shut, a day or two of tail flow — and Volume Management cannot build an accounting arrangement until the deal term covers it, so every allocation cycle produces a new batch of extension requests.

**What could absorb it.** An exception report that joins allocated meter volumes against deal start/end dates and lists every meter-day with flow outside its deal term, routed to the deal owner as a queue with the deal number, meter, dates and volume prefilled — plus an in-system extend action so the requester is not composing free-text mail and waiting on one person's inbox.

**How the number was reached.**

```
15.00 task instances / 7 months of coverage = 2.143 instances per month
minutes per instance = 12 handle + (1.33 touches - 1) x 5 + 0.55 rework rate x 18 + 0.20 waiting rate x 3 = 24.17 min
coordination multiplier = 1 + 0.35 x (3 median participants - 1) = 1.700
hours per month = 2.143 x 24.17 x 1.700 / 60 = 1.467
automatable hours = 1.467 x 0.45 automatable share = 0.660
dollars per month = 0.660 h x $85/h = $56.12
```

Assumptions from `config/estimation.yml#task_classes.deal_entry_correction`.

**Evidence.**

- "Logistics is waiting to hear from Daren on this issue.  He will either need 
to extend the deal or maybe there should be another deal in place."
  — `corpus/farmer-d/logistics/782.` bytes 873–1016, lines 34–35 · rewrapped
    ```
    sed -n '34,35p' corpus/farmer-d/logistics/782.
    ```
- "Can the deal be extended 
for 6/4 (548 dec.) and 6/9 (40 dec.) to cover this flow so that Volume 
Management can create an accounting arrangement for these two days?"
  — `corpus/farmer-d/logistics/1486.` bytes 759–924, lines 23–25 · rewrapped
    ```
    sed -n '23,25p' corpus/farmer-d/logistics/1486.
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
- ".16 decatherms allocated at this meter for 5/31/2000.  Can you please extend 
deal (one more time for me) for 5/31/2000."
  — `corpus/farmer-d/logistics/1174.` bytes 524–644, lines 21–22 · rewrapped
    ```
    sed -n '21,22p' corpus/farmer-d/logistics/1174.
    ```
- "The East Desk was not up and 
running on Unify in June of 1999.  All of our pathing for June of 1999 was in 
Autonoms and it's not y2K compatabile."
  — `corpus/farmer-d/logistics/1489.` bytes 976–1123, lines 25–27 · rewrapped
    ```
    sed -n '25,27p' corpus/farmer-d/logistics/1489.
    ```
- "Can you extend the deal, or should I allocated off to strangers?"
  — `corpus/farmer-d/logistics/1479.` bytes 751–815, lines 24–24
    ```
    sed -n '24,24p' corpus/farmer-d/logistics/1479.
    ```
- "Could you extend this deal thru the 30th so that I 
can have Vol. Management create an accounting arrangement for it."
  — `corpus/farmer-d/logistics/1277.` bytes 548–665, lines 18–19 · rewrapped
    ```
    sed -n '18,19p' corpus/farmer-d/logistics/1277.
    ```

## 7. Correcting mispriced deals by hand in Sitara after the fact

**$37/month** (range $8–$124) · 0.4 automatable hours/month · confidence high

*Measured:* 8 messages in 7 task instances, 4 sender(s), 12 people, 5 months. rework 100%, waiting 12%, manual_transfer 62%, deadline 12%.

**What happens.** Someone notices that a deal carries the wrong commodity price — often a prior month's rate left in place, a placeholder of zero, or a figure that was superseded before the deal was booked. The person who spotted it mails the deal number and the price it should be to whoever can edit the record, usually asking for the change in Sitara, and in some instances in a second place as well (Enpower, a deal summary report, or a reconciliation spreadsheet). The editor makes the change and replies that it has been adjusted; the requester then watches the downstream report to see whether the corrected figure comes across. The thread ends when the requester confirms the new price and any revenue it drives look right, or asks for the entry to be zeroed out instead.

**Where it stalls.** The correction cannot be verified by the person who requested it. Every message in the group carries a rework signal, and most also carry manual transfer: the requester hands a deal number and a price to another person, has no way to edit or check the record, and asks to be notified when the change lands — "I'll wait to see how these changes come across. Please notify me when these changes have been made." Where a report has already been produced from the bad price, the fix races a fixed publication point, as in the request to recalculate or zero an entry before the morning flash. At least one instance is a correction to a correction: an earlier price change was itself not the final price.

**Why it recurs.** Prices are entered once and then move; a deal booked at a placeholder or last month's rate is only caught when a report, invoice or reconciliation sheet disagrees, which happens every month.

**What could absorb it.** A validation step at deal capture that flags a commodity price equal to zero or unchanged from the prior month's rate for the same counterparty and deal, plus a confirmation mail fired automatically when the price field on a named deal changes, so the requester is notified by the system rather than by the editor. A reconciliation query comparing invoiced rate to booked rate would surface the same mismatches before a report is published.

**How the number was reached.**

```
7.00 task instances / 5 months of coverage = 1.400 instances per month
minutes per instance = 12 handle + (1.14 touches - 1) x 5 + 1.00 rework rate x 18 + 0.12 waiting rate x 3 = 31.09 min
coordination multiplier = 1 + 0.35 x (2 median participants - 1) = 1.350
hours per month = 1.400 x 31.09 x 1.350 / 60 = 0.979
automatable hours = 0.979 x 0.45 automatable share = 0.441
dollars per month = 0.441 h x $85/h = $37.46
```

Assumptions from `config/estimation.yml#task_classes.deal_entry_correction`.

**Evidence.**

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
- "Can you please update the 04/01 price for deal # 27253 in Sitara? It 
currently has a rate of $2.3043 (last month's price). The customer invoiced a 
rate of $1.8351."
  — `corpus/giron-d/sent/12.` bytes 677–842, lines 29–31
    ```
    sed -n '29,31p' corpus/giron-d/sent/12.
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
- "Unfortunately the change to $290 was not the final price for deal #620476 on 05/23.  It should be $295 for HE 15-17"
  — `corpus/williams-w3/sent_items/501.` bytes 573–688, lines 19–19
    ```
    sed -n '19,19p' corpus/williams-w3/sent_items/501.
    ```
- "please change and/or review a 
change of price for the Mar 15 item from $0.00000 to $7.20000 and advise when 
complete"
  — `corpus/giron-d/sent/57.` bytes 666–784, lines 34–36 · rewrapped
    ```
    sed -n '34,36p' corpus/giron-d/sent/57.
    ```
- "I adjusted the price in Sitara."
  — `corpus/farmer-d/logistics/129.` bytes 812–843, lines 21–21
    ```
    sed -n '21,21p' corpus/farmer-d/logistics/129.
    ```

## 8. Daily gas nominations mailed as attached Word and Excel files

**$33/month** (range $6–$113) · 0.4 automatable hours/month · confidence high

*Measured:* 30 messages in 30 task instances, 5 sender(s), 32 people, 14 months. manual_transfer 10%, deadline 3%.

**What happens.** Each flow day, a counterparty or scheduler sends the day's gas nomination to logistics as an attached document rather than as data — recurring examples are "CALPINE DAILY GAS NOMINATION 1.doc", "HIDALGO DAILY GAS NOMINATION.doc", monthly nomination spreadsheets such as "egmnom-Feb.xls", and dated pipeline noms like "HPL Nom for January 4, 2001". The mail body is usually empty or a single line; the volumes and paths live inside the attachment, so the recipient opens the file and re-keys or re-forwards the numbers onward. A small number of messages close the loop as confirmations ("Confirmed on my end. Same volumes as yesterday, no changes to the path.") or as coverage notes when the usual sender is away. The same filenames repeat month after month across fourteen months and five senders, indicating a fixed daily routine rather than one-off requests.

**Where it stalls.** The nomination never arrives in machine-readable form. It comes as a Word or Excel attachment — and in a number of cases by fax — with no data in the mail body, so the scheduler must open each file and transfer volumes and points by hand into the nomination system; the manual_transfer signal appears on some of these messages and fax is named repeatedly. Confirmation back to the sender is also by hand and is present on only one message in the set, so there is little visible evidence that a submitted nomination was received and accepted. When the regular sender is out, continuity depends on a phone call rather than the file itself.

**Why it recurs.** Nominations are per-flow-day with a daily pipeline cutoff, and the counterparties submit on a standing arrangement using the same document template each day, so the same re-keying happens every cycle.

**What could absorb it.** Replace the attached document with a fixed-column submission (a shared sheet or a mailbox parser keyed on the recurring filenames) that lands the volumes, points and flow date directly in the nomination system and auto-replies with a receipt showing what was booked, flagging only rows that differ from the prior day.

**How the number was reached.**

```
coverage = 29 dated / 30 messages = 0.967; instances 30 / 0.967 = 31.03 adjusted
31.03 task instances / 14 months of coverage = 2.217 instances per month
minutes per instance = 8 handle + (1.00 touches - 1) x 3 + 0.00 rework rate x 12 + 0.00 waiting rate x 2 = 8.00 min
coordination multiplier = 1 + 0.35 x (5 median participants - 1) = 2.400
hours per month = 2.217 x 8.00 x 2.400 / 60 = 0.709
automatable hours = 0.709 x 0.55 automatable share = 0.390
dollars per month = 0.390 h x $85/h = $33.16
```

Assumptions from `config/estimation.yml#task_classes.gas_nomination`.

**Evidence.**

- "CALPINE DAILY GAS NOMINATION 1.doc"
  — `corpus/farmer-d/logistics/1329.` bytes 748–782, lines 19–19
    ```
    sed -n '19,19p' corpus/farmer-d/logistics/1329.
    ```
- "HPL Nom for January 4, 2001"
  — `corpus/farmer-d/logistics/2025.` bytes 313–340, lines 7–7
    ```
    sed -n '7,7p' corpus/farmer-d/logistics/2025.
    ```
- "(See attached file: egmnom-Feb.xls)"
  — `corpus/farmer-d/logistics/764.` bytes 858–893, lines 32–32
    ```
    sed -n '32,32p' corpus/farmer-d/logistics/764.
    ```
- "HIDALGO DAILY GAS NOMINATION.doc"
  — `corpus/farmer-d/logistics/1229.` bytes 667–699, lines 19–19
    ```
    sed -n '19,19p' corpus/farmer-d/logistics/1229.
    ```
- "Confirmed on my end. Same volumes as yesterday, no changes to the path."
  — `corpus/giron-d/sent/795.` bytes 452–523, lines 16–16
    ```
    sed -n '16,16p' corpus/giron-d/sent/795.
    ```
- "HPL Nomination for January 26, 2000"
  — `corpus/farmer-d/logistics/716.` bytes 263–298, lines 6–6
    ```
    sed -n '6,6p' corpus/farmer-d/logistics/716.
    ```
- "Will be out Friday, will call if there are any changes."
  — `corpus/farmer-d/logistics/169.` bytes 828–883, lines 21–21
    ```
    sed -n '21,21p' corpus/farmer-d/logistics/169.
    ```
- "(See attached file: egmnom-Feb.xls)"
  — `corpus/farmer-d/logistics/767.` bytes 840–875, lines 31–31
    ```
    sed -n '31,31p' corpus/farmer-d/logistics/767.
    ```

## 9. Monthly first-of-month gas nominations mailed in by plant customers

**$29/month** (range $5–$100) · 0.3 automatable hours/month · confidence high

*Measured:* 14 messages in 14 task instances, 6 sender(s), 31 people, 9 months. rework 14%, waiting 7%.

**What happens.** Each month, counterparties and plant representatives email the logistics desk their gas requirements for the upcoming month — most often the MTBE Plant at Morgan's Point under the EGPFC heading, plus Josey Ranch, the Katy Plant and Forest volumes. The message body carries the daily volumes in MMBtu/d, sometimes broken out by specific dates ("March 1st & 2nd ... 32,000 mmbtu per day"), and is addressed to the scheduler who has to turn it into a nomination. A smaller number of messages are follow-ups on the same volumes: a revised first-of-the-month nomination, a change for a named plant, or a note that a transport number is still outstanding. The desk receives these as free-text mail and re-keys them; the exemplars show no system of record other than email, with one other system mentioned once. Threads end when the volumes are acknowledged or superseded by a revision.

**Where it stalls.** The nomination arrives as prose and numbers in a mail body, so the scheduler is the transcription step. Two of the fourteen messages are corrections that restate an already-submitted first-of-month volume ("First of the month nom is now expected to be 5,479 MMBtu/d"; "revision PER JOHN KJELMYR, 12/26 am"), meaning the same nomination is handled more than once. One message stalls on an input the sender does not control — a transport number owed by someone in the counterparty's shop — and the requester is left waiting rather than able to complete the nomination. Who owns reconciling a revision against the original submission is not visible in these messages.

**Why it recurs.** The nomination cycle is monthly and per-plant, so each customer sends a fresh requirement every month for as long as they buy gas; one exemplar notes a plant's last month of purchases, which is how an instance stops.

**What could absorb it.** A structured intake form or fixed-format template per plant that lands the volumes as fields rather than prose, feeding the nomination directly and versioning revisions against the original submission so a change is visibly a change. Pair it with a standing prerequisite check (e.g. transport number present) that blocks submission rather than surfacing after the fact.

**How the number was reached.**

```
14.00 task instances / 9 months of coverage = 1.556 instances per month
minutes per instance = 8 handle + (1.00 touches - 1) x 3 + 0.14 rework rate x 12 + 0.07 waiting rate x 2 = 9.86 min
coordination multiplier = 1 + 0.35 x (5 median participants - 1) = 2.400
hours per month = 1.556 x 9.86 x 2.400 / 60 = 0.613
automatable hours = 0.613 x 0.55 automatable share = 0.337
dollars per month = 0.337 h x $85/h = $28.67
```

Assumptions from `config/estimation.yml#task_classes.gas_nomination`.

**Evidence.**

- "There has been a change for the Katy Plant.  First of the month nom is now 
expected to be 5,479 MMBtu/d."
  — `corpus/farmer-d/logistics/1467.` bytes 798–903, lines 26–27 · rewrapped
    ```
    sed -n '26,27p' corpus/farmer-d/logistics/1467.
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
- "EGPFC nominates the following natural gas requirements for the MTBE Plant at 
Morgan's Point for October 2000"
  — `corpus/farmer-d/logistics/1423.` bytes 1192–1301, lines 28–29 · rewrapped
    ```
    sed -n '28,29p' corpus/farmer-d/logistics/1423.
    ```
- "EGPFC nominates the following requirements for the MTBE Plant at Morgan's 
Point for February 2000"
  — `corpus/farmer-d/logistics/719.` bytes 1172–1270, lines 28–29 · rewrapped
    ```
    sed -n '28,29p' corpus/farmer-d/logistics/719.
    ```
- "This is the estimated Josey Ranch nomination for the month of April
2000."
  — `corpus/farmer-d/logistics/993.` bytes 1013–1086, lines 30–31 · rewrapped
    ```
    sed -n '30,31p' corpus/farmer-d/logistics/993.
    ```
- "March 1st &2nd                            32,000  mmbtu per day"
  — `corpus/farmer-d/logistics/834.` bytes 1157–1220, lines 26–26
    ```
    sed -n '26,26p' corpus/farmer-d/logistics/834.
    ```

## 10. Fixing miskeyed Sitara deal entries after the fact

**$26/month** (range $6–$88) · 0.3 automatable hours/month · confidence medium

*Measured:* 10 messages in 8 task instances, 5 sender(s), 12 people, 5 months. rework 30%, waiting 10%.

**What happens.** Someone notices that a deal already captured in Sitara does not match what was intended or what actually flowed — wrong contract months, the wrong EOL meter, or a volume that has since been split between two delivery points. The person who spots it mails the deal owner or a colleague to ask whether the entry was intentional and to get it changed. A second person then amends the deal and the originator confirms the fix by mail, sometimes naming who made the correction. Most of the traffic in this cluster is short notification mail with no explicit ask; the correction itself happens outside the mailbox, in the deal system.

**Where it stalls.** The person who finds the error is not the person who can change the record, so each instance becomes a hand-off by email and then a wait: one exemplar is a bare chase ("Have you had a chance to look at this yet?"), and closure arrives as a third-party confirmation ("Elizabeth Hernandez fixed this deal for me") rather than as a system notification. Nothing in these messages shows a check that would have caught the wrong-year or split-point entry before it was booked, so the discovery is incidental.

**Why it recurs.** Deals are keyed by hand into Sitara and downstream systems, and mismatches surface later when volumes or months are compared against what actually flowed — so the same correct-and-confirm loop reappears whenever a counterparty changes points or a date is mistyped.

**What could absorb it.** Validation at entry that flags implausible contract months and meter/point combinations against the counterparty's active points, plus an automatic notification to the original enterer when a deal is amended, so the confirmation loop does not have to be carried by mail.

**How the number was reached.**

```
8.00 task instances / 5 months of coverage = 1.600 instances per month
minutes per instance = 12 handle + (1.25 touches - 1) x 5 + 0.30 rework rate x 18 + 0.10 waiting rate x 3 = 18.95 min
coordination multiplier = 1 + 0.35 x (2 median participants - 1) = 1.350
hours per month = 1.600 x 18.95 x 1.350 / 60 = 0.682
automatable hours = 0.682 x 0.45 automatable share = 0.307
dollars per month = 0.307 h x $85/h = $26.09
```

Assumptions from `config/estimation.yml#task_classes.deal_entry_correction`.

**Evidence.**

- "Did you mean to put the deal in for July and November of 1999 and"
  — `corpus/farmer-d/logistics/1184.` bytes 795–861, lines 24–24 · decoded_exact
    ```
    sed -n '24,24p' corpus/farmer-d/logistics/1184.
    ```
- "Aquila split the volume between two points, that is why the deal changed."
  — `corpus/farmer-d/logistics/1303.` bytes 568–641, lines 24–24
    ```
    sed -n '24,24p' corpus/farmer-d/logistics/1303.
    ```
- "Elizabeth Hernandez fixed this deal for me."
  — `corpus/farmer-d/logistics/90.` bytes 607–650, lines 18–18
    ```
    sed -n '18,18p' corpus/farmer-d/logistics/90.
    ```
- "Have you had a chance to look at this yet?"
  — `corpus/farmer-d/logistics/16.` bytes 552–594, lines 19–19
    ```
    sed -n '19,19p' corpus/farmer-d/logistics/16.
    ```

## 11. Nomination changes confirmed by hand with pipelines and counterparties

**$25/month** (range $5–$82) · 0.3 automatable hours/month · confidence high

*Measured:* 11 messages in 11 task instances, 8 sender(s), 28 people, 8 months. rework 45%, waiting 9%, manual_transfer 27%, deadline 9%.

**What happens.** A counterparty or an internal desk asks for a nominated volume at a named meter to be changed — dropped, cut, or revised — for a specific gas day. A scheduler in the logistics mailbox picks up the request, works out what the new number should be, and then has to make two things agree: the pipeline's or counterparty's confirmation, and Enron's own record in Sitara, Unify or the confirm screen ("Pops"). Confirming means reaching a named person at El Paso, Kinder Morgan, PG&E or the like by mail or phone, then hand-editing the deal record to match. The thread closes when the new volume is echoed back as confirmed, sometimes with a note that the same change may be needed again the next day.

**Where it stalls.** The change cannot be closed out until a named individual at the pipeline or counterparty confirms the volume, and those people are not always reachable — one exemplar records being unable to reach any PG&E scheduler to check the contractual impact, another that a colleague was "having trouble confirming the volume of 5,733 with El Paso." Meanwhile the number has to be re-keyed into the deal system by hand, so the confirmed volume and the system volume drift apart; nearly half these messages carry rework signals, and several are second or third revisions of the same volume, with one flagging that changing it will leave another person's meter in imbalance.

**Why it recurs.** Nominations are per gas day with daily cutoffs, counterparties revise volumes after the fact, and the confirmation lives with an external scheduler while the record lives in Sitara/Unify — nothing links the two automatically.

**What could absorb it.** A single nomination-change ticket that carries meter, gas day, old and new volume and the confirming party, and writes the agreed number into Sitara/Unify once instead of it being re-keyed, with an exception list of externally confirmed changes not yet reflected in the deal record.

**How the number was reached.**

```
11.00 task instances / 8 months of coverage = 1.375 instances per month
minutes per instance = 8 handle + (1.00 touches - 1) x 3 + 0.45 rework rate x 12 + 0.09 waiting rate x 2 = 13.64 min
coordination multiplier = 1 + 0.35 x (3 median participants - 1) = 1.700
hours per month = 1.375 x 13.64 x 1.700 / 60 = 0.531
automatable hours = 0.531 x 0.55 automatable share = 0.292
dollars per month = 0.292 h x $85/h = $24.84
```

Assumptions from `config/estimation.yml#task_classes.gas_nomination`.

**Evidence.**

- "he decided to go ahead and cut 
the nom down to 30 for Saturday's gas day.  I changed the confirm in Pops to 
reflect it."
  — `corpus/farmer-d/logistics/2110.` bytes 1276–1397, lines 28–30 · rewrapped
    ```
    sed -n '28,30p' corpus/farmer-d/logistics/2110.
    ```
- "I could not get a hold of any scheduler with PG&E to see the 
contractual impact."
  — `corpus/farmer-d/logistics/2110.` bytes 1843–1924, lines 41–42 · rewrapped
    ```
    sed -n '41,42p' corpus/farmer-d/logistics/2110.
    ```
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
- "the San Jac. nom  should be 29,209.  
Is this correct?  We'll need to change sitara."
  — `corpus/farmer-d/logistics/603.` bytes 827–911, lines 30–31 · rewrapped
    ```
    sed -n '30,31p' corpus/farmer-d/logistics/603.
    ```
- "They would like to drop the volume again to 4400.  If we 
change don't Kim will have an imbalance at this meter"
  — `corpus/farmer-d/logistics/866.` bytes 680–791, lines 21–22 · rewrapped
    ```
    sed -n '21,22p' corpus/farmer-d/logistics/866.
    ```
- "This change was 
confirmed with Patsy Shimek @ Kinder Morgan."
  — `corpus/farmer-d/logistics/2029.` bytes 783–844, lines 24–25 · rewrapped
    ```
    sed -n '24,25p' corpus/farmer-d/logistics/2029.
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

- **Runbook: Meter-Level Scheduled-vs-Actual Volume Reconciliation** (`RUN-01-runbook-meter-level-scheduled-vs-actual-volume-recon.md`) — runbook, for *Meter-level scheduled-vs-actual volume reconciliation, chased by email*
- **Deal price correction in Sitara: request and confirmation mail template** (`TPL-01-deal-price-correction-in-sitara-request-and-confirma.md`) — template, for *Correcting mispriced deals by hand in Sitara after the fact*
- **Template: Weekly California Capacity Report** (`TPL-02-template-weekly-california-capacity-report.md`) — template, for *Weekly California Capacity Report, assembled and mailed by hand*
- **Runbook: Extending a Sitara deal to cover meter flow outside the deal term** (`RUN-02-runbook-extending-a-sitara-deal-to-cover-meter-flow-.md`) — runbook, for *Extending Sitara deals by request to cover unallocated meter flow*
- **Daily Credit Report: standing distribution email (draft)** (`EML-01-daily-credit-report-standing-distribution-email-draf.md`) — email, for *"Credit Report - 1/30/01" produced daily*
- **Weekly California Capacity Report — transmittal email draft** (`EML-02-weekly-california-capacity-report-transmittal-email-.md`) — email, for *"California Capacity Report for Week of 01/14-01/18" produced weekly*
- **Standing email: Calpine Daily Gas Nomination notice** (`EML-03-standing-email-calpine-daily-gas-nomination-notice.md`) — email, for *"Calpine Daily Gas Nomination" produced monthly*

---

## How to check any of this

```
make verify     # re-anchor every citation from scratch; recompute every number
make test       # full suite, zero model calls
make serve      # dashboard with click-through to the highlighted bytes
```

Every citation above prints the `sed` command that reproduces it. `docs/AUDIT.md` holds 25 randomly sampled citations with both `dd` and `sed` commands.

Where this is most likely wrong, and what it took on faith, is in `NOTES.md`.
