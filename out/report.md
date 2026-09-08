# Where this company is losing time

*Run `final` · generated 2026-09-08T22:28:23Z · corpus digest `c94acc4b08cb`*

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
| 1 | "Credit Report - 1/30/01" produced daily | $544 | $155–$1,534 | 6.4 | 69 | 4 | 8 | medium |
| 2 | "California Capacity Report for Week of 01/14-01/18" produced weekly | $266 | $51–$929 | 3.1 | 15 | 5 | 8 | medium |
| 3 | Weekly California Capacity Report, assembled and mailed by hand | $248 | $48–$865 | 2.9 | 16 | 6 | 8 | high |
| 4 | Meter-level scheduled-vs-actual variance clearing across Unify, Sitara and UA4 | $108 | $24–$369 | 1.3 | 41 | 17 | 8 | high |
| 5 | "Calpine Daily Gas Nomination" produced monthly | $87 | $19–$284 | 1.0 | 17 | 11 | 8 | medium |
| 6 | Moving deals between trading books by hand-run script requests | $83 | $15–$340 | 1.0 | 10 | 3 | 8 | medium |
| 7 | Extending existing deal tickets in Sitara/Unify to cover unbooked meter flow | $55 | $12–$182 | 0.6 | 8 | 4 | 8 | high |
| 8 | Mid-month nomination revisions re-keyed by hand for Josey, Katy and El Paso | $44 | $9–$147 | 0.5 | 8 | 5 | 8 | high |
| 9 | Monthly gas nominations mailed in by counterparties, then revised by hand | $38 | $7–$133 | 0.4 | 12 | 6 | 8 | high |
| 10 | Sitara deal price corrections requested by email | $36 | $8–$120 | 0.4 | 8 | 6 | 8 | high |
| 11 | Daily gas nominations mailed as Word attachments (Calpine, HPL) | $33 | $6–$113 | 0.4 | 26 | 13 | 8 | high |
| 12 | Real-time West power desk shift handoff and booking instructions by email | $24 | $6–$72 | 0.3 | 10 | 4 | 8 | high |
| 13 | Monthly nomination volume estimates agreed by email before month start | $22 | $5–$66 | 0.3 | 8 | 3 | 8 | medium |
| 14 | Ad-hoc requests for system and deal-book access, by email | $22 | $7–$63 | 0.3 | 7 | 5 | 7 | medium |

### Not counted

0 opportunities were demoted to low confidence ($0/month not included in the headline) and 1 were quarantined for insufficient evidence ($34/month excluded). See `out/quarantine.json`.

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

*Measured:* 18 messages in 16 task instances, 2 sender(s), 10 people, 6 months. rework 6%, manual_transfer 83%.

**What happens.** Each week someone on the Transwestern commercial side compiles a California interstate capacity report and mails it to a fixed distribution list. The body follows the same template every time: average Transwestern deliveries to California with utilisation against capacity, San Juan lateral throughput, and El Paso deliveries broken out by delivery point. The figures are pulled together outside the mail itself — spreadsheets appear in a minority of the messages — and then typed or pasted into the message body rather than attached. The output is the mail itself; there is no visible approval step and recipients generally do not reply. One message hands the report off ("Below is my last California Interstate Capacity Report"), showing the duty passes between people while the format stays fixed.

**Where it stalls.** There is no waiting or deadline signal here — nobody is chased and nothing is blocked. The friction is in assembly and transcription: nearly every message is flagged as a manual transfer of numbers from source systems into an email body, which is why the one correction in the set is a header error rather than a data error ("Sorry, the effective date for this new report is 01/07-01/11"). Because the report is re-keyed each week, the reporting period itself has to be restated by hand and can be stated wrong, forcing a second mail to the whole list. Where the underlying delivery and throughput figures originate is not visible in these messages.

**Why it recurs.** It is a standing weekly obligation to a fixed distribution list, with an unchanging template and no system that mails the figures on its own, so the same assembly-and-paste sequence repeats every week the pipeline runs.

**What could absorb it.** A scheduled job that reads the delivery and throughput figures for the reporting week, renders them into the existing template — including the period dates derived from the run date rather than typed — and mails it to the standing list, leaving the sender only to review before release.

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
- "El Paso's average deliveries to California were 1782 MMBtu/d (66%):"
  — `corpus/lokay-m/inbox/10.` bytes 1487–1554, lines 24–24
    ```
    sed -n '24,24p' corpus/lokay-m/inbox/10.
    ```
- "Transwestern's average deliveries to California were 1015 MMBtu/d (93%), with San Juan lateral throughput at 873 MMBtu/d."
  — `corpus/lokay-m/sent_items/110.` bytes 1339–1460, lines 23–23
    ```
    sed -n '23,23p' corpus/lokay-m/sent_items/110.
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
- "Transwestern's average deliveries to California were 959 MMBtu/d (88%), with San Juan lateral throughput at 827 MMBtu/d."
  — `corpus/lokay-m/sent_items/63.` bytes 1338–1458, lines 23–23
    ```
    sed -n '23,23p' corpus/lokay-m/sent_items/63.
    ```
- "Transwestern's average deliveries to California were 1059 MMBtu/d (97%), with San Juan lateral throughput at 839 MMBtu/d."
  — `corpus/lokay-m/sent_items/67.` bytes 1340–1461, lines 24–24
    ```
    sed -n '24,24p' corpus/lokay-m/sent_items/67.
    ```

## 4. Meter-level scheduled-vs-actual variance clearing across Unify, Sitara and UA4

**$108/month** (range $24–$369) · 1.3 automatable hours/month · confidence high

*Measured:* 47 messages in 41 task instances, 29 sender(s), 81 people, 17 months. rework 45%, waiting 23%, manual_transfer 30%, deadline 9%.

**What happens.** A variance surfaces when measured flow at a meter does not match what was nominated or confirmed — typically flagged by an exception or variance report (the UA4 and meter exception reports are named repeatedly), or noticed when an imbalance is booked again on a contract. Whoever holds the meter emails the person who can explain or fix it, asking for a contract, a purchase, a reallocation, or a correction to the estimated volumes carried in Unify so they agree with what the pipeline shows was allocated. Supporting numbers move by hand: meter statements are requested by fax, positions are pasted into mail, and counterparty figures are copied back and forth. The thread closes when someone makes the adjustment in the system of record or applies a temporary reallocation to get the volume off the exception list. Some months the same contract or interconnect reappears, so the fix is redone for the next period.

**Where it stalls.** The person who spots the variance is almost never the person who can clear it, so nearly half these messages are second or third attempts at the same meter and month, and escalation is the second most common role after request. Requests sit unanswered ("I sent Jackie Young an email back showing her TETCO's numbers and I haven't received a response"), and back-period items ("meter 4045 for 2/99", "an interconnect variance at meter 980071 for 2/99") persist long enough that settlement payments wait on them. Ownership of the recurring imbalance check is passed person to person and is only visible in mail, not in a system.

**Why it recurs.** Unify, Sitara and the pipeline's allocation figures are reconciled by hand each month rather than fed to each other, and the exception reports regenerate the same unmatched meters until someone books a contract or adjustment.

**What could absorb it.** A scheduled comparison that joins nominated/confirmed volumes to pipeline-allocated actuals per meter and month, and opens a tracked item naming the meter, the period, the responsible scheduler and the required fix (contract, purchase, reallocation, Unify adjustment) instead of an email thread. Repeat offenders — the same contract or interconnect variance recurring month over month — should be flagged for a standing fix rather than re-cleared.

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

**What happens.** A trader or commercial person decides that a set of deals sitting in one trading book belongs in another — index deals out of FT-WEST into GD-NEW, INTRA-EMWMEH into FT-IM-ENOV, financial deals from FT-TERMIN-GD into the bankruptcy books — and emails the group that can effect the move in the deal/risk systems. The request names the source and destination book, sometimes a counterparty and its TAGG short name, and sometimes a target date ("by Monday", "I need this done this week"). Whoever runs the move replies with clarifying questions about which book and which deal types are in scope, gets answers by return mail, and then re-runs what is described as the same script used the day before with different book names substituted. The thread closes with a confirmation or an FYI to the wider list; stragglers found later are sent through as a follow-up request in the same form.

**Where it stalls.** The move cannot be executed until the requester answers the operator's questions about book identity and scope — one exemplar states plainly that the move can only be completed once "all the answers" arrive, and another has to confirm "the book is ENA-FT-WT-SOCAL" plus yes/no answers to two further questions. Because the request arrives as free-text email rather than a specified parameter set, each instance needs a clarification round-trip, and deals missed on the first pass come back later as "a few more stragglers". Some requests carry a same-day or by-Monday deadline, so the clarification loop sits directly in front of a cutoff.

**Why it recurs.** Book structures keep changing — new books, reorganised desks, bankruptcy books in 2002 — and each reorganisation generates fresh batches of deals to reassign, with no self-service way for the requester to move them.

**What could absorb it.** Since the operator already runs a parameterised script, expose it behind a fixed request form that requires source book, destination book, deal-type filter, counterparty/TAGG short name and effective date before submission, and have it return the list of deals it matched so the requester can spot stragglers before the run rather than after.

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
- "If I can have all the answers soon then I think the deals move can be completed around 3:00p.m."
  — `corpus/giron-d/inbox/67.` bytes 1166–1261, lines 29–29
    ```
    sed -n '29,29p' corpus/giron-d/inbox/67.
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
- "Currently, all of our index deals are in the FT-WEST book.  I would like to 
move them all to the GD-NEW book."
  — `corpus/giron-d/sent/575.` bytes 449–559, lines 19–20 · rewrapped
    ```
    sed -n '19,20p' corpus/giron-d/sent/575.
    ```
- "the book is ENA-FT-WT-SOCAL.  Answer to question 2 & 3 - yes"
  — `corpus/giron-d/inbox/65.` bytes 723–783, lines 20–20
    ```
    sed -n '20,20p' corpus/giron-d/inbox/65.
    ```
- "Here are a few more stragglers to move into the bankruptcy books:"
  — `corpus/giron-d/inbox/57.` bytes 1171–1236, lines 23–23
    ```
    sed -n '23,23p' corpus/giron-d/inbox/57.
    ```

## 7. Extending existing deal tickets in Sitara/Unify to cover unbooked meter flow

**$55/month** (range $12–$182) · 0.6 automatable hours/month · confidence high

*Measured:* 12 messages in 8 task instances, 5 sender(s), 13 people, 4 months. rework 92%, waiting 25%, manual_transfer 8%.

**What happens.** Someone reconciling measured volumes finds gas that flowed at a meter with no deal or nomination behind it — sometimes for a month, sometimes for a single day, and in one case for a flow month well over a year old. Rather than write a new deal, they mail the person who owns the deal in the system and ask for the last deal used to be extended to cover the missing dates ("Last deal used was 289396 could you extend it", "Can this deal be extended to cover the January and February flow?"). The extension is expected to appear in Unify, after which Volume Management can create the accounting arrangement and the imbalance can be cleared. The exchange ends when the requester confirms the deal now shows in the downstream system; frequently the next message is a chaser saying it has not appeared yet.

**Where it stalls.** Two places. First, confirmation: after the extension is requested the requester checks the downstream system and finds nothing — "This has not yet shown up in Unify. Did you use the same deal ticket?" — so the same thread is re-opened to establish whether the edit was made against the right ticket. Second, age of discovery: one thread escalates because the flow being covered dates to June 1999 ("Hopefully we're not just finding out about this?"), and the answer is that the East Desk pathing for that period sat in Autonoms rather than Unify, so there is no clean record to extend against. Nearly every message in the group carries a rework signal; almost none carry a deadline.

**Why it recurs.** Flow is measured at meters independently of what was booked, so gaps surface after the fact on every reconciliation pass; the deal system and Unify do not confirm to each other, so each fix needs a manual request and a manual check.

**What could absorb it.** A standing exception report that matches measured meter volumes against booked deal coverage and lists uncovered flow dates with the last deal used on that meter, so the extension request is pre-filled rather than reconstructed by mail. Pair it with an automatic notice back to the requester when the extended deal propagates into Unify, which removes the "has this shown up yet" round trip.

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
- "Is this date really June of 1999?  Hopefully we're not just finding out about 
this?"
  — `corpus/farmer-d/logistics/1492.` bytes 1357–1441, lines 38–39 · rewrapped
    ```
    sed -n '38,39p' corpus/farmer-d/logistics/1492.
    ```
- "The East Desk was not up and 
running on Unify in June of 1999.  All of our pathing for June of 1999 was in 
Autonoms and it's not y2K compatabile."
  — `corpus/farmer-d/logistics/1489.` bytes 976–1123, lines 25–27 · rewrapped
    ```
    sed -n '25,27p' corpus/farmer-d/logistics/1489.
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
- "can you please extend deal #465322 for cover a flow volume of 140 
dec. for 11/21/2000"
  — `corpus/farmer-d/logistics/1999.` bytes 714–800, lines 22–23 · rewrapped
    ```
    sed -n '22,23p' corpus/farmer-d/logistics/1999.
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

## 10. Sitara deal price corrections requested by email

**$36/month** (range $8–$120) · 0.4 automatable hours/month · confidence high

*Measured:* 9 messages in 8 task instances, 7 sender(s), 14 people, 6 months. rework 100%, waiting 22%, manual_transfer 22%, deadline 33%.

**What happens.** Someone reviewing a deal, an invoice or a daily deal summary finds the commodity price or volume recorded in Sitara is wrong — a placeholder price, a wrong index basis, or the wrong pricing for particular production days. Because the requester either lacks access to the ticket or is not the owner of the deal, they email the person who can edit it, quoting the deal or ticket number and the price it should be. That person makes the change in Sitara (or an adjoining system or spreadsheet) and replies to confirm. In some instances the requester also asks for a downstream recalculation, such as zeroing out a deal before the morning flash, or asks to be notified once the edit lands so they can proceed with an invoice.

**Where it stalls.** The correction cannot be made by the person who spots it: one exemplar is an explicit escalation because the sender was not allowed to access the Sitara ticket to fix swing pricing, and another asks a third party to forward the request onward to the person who can edit the price. That handoff collides with fixed cutoffs — an invoice going out that afternoon, or the morning flash — so the requester waits on a reply they need before their own step can complete. Every message in this cluster carries a rework signal: the deal was already booked once and is being booked again.

**Why it recurs.** Deals are captured with prices that later prove wrong or provisional, while invoicing and daily summary cycles force the discrepancy to surface on a deadline; edit rights sit with someone other than the reviewer.

**What could absorb it.** A standing price-correction request form that captures deal or ticket number, affected production days, the corrected price or index basis, and the downstream deadline, routed to whoever holds edit rights on that deal and closing the loop with an automatic confirmation to the requester. A pre-invoice check that flags deals whose recorded price is a placeholder or differs from the contract index would surface these before the cutoff rather than after.

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

- "I tried to get into the Sitara ticket # 373590 to correct the swing pricing
....but I am not allowed to access it"
  — `corpus/farmer-d/logistics/106.` bytes 1341–1454, lines 39–40
    ```
    sed -n '39,40p' corpus/farmer-d/logistics/106.
    ```
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
- "pls forward this to Daren so that he can change the price in Sitara to $ 5.235 +.05"
  — `corpus/farmer-d/logistics/179.` bytes 889–972, lines 20–20
    ```
    sed -n '20,20p' corpus/farmer-d/logistics/179.
    ```
- "Could you pls the pricing on this deal for March 2001 Production for days 25 & 26 to  $ 5.285?"
  — `corpus/farmer-d/logistics/177.` bytes 900–994, lines 24–24
    ```
    sed -n '24,24p' corpus/farmer-d/logistics/177.
    ```

## 11. Daily gas nominations mailed as Word attachments (Calpine, HPL)

**$33/month** (range $6–$113) · 0.4 automatable hours/month · confidence high

*Measured:* 26 messages in 26 task instances, 4 sender(s), 27 people, 13 months. rework 4%, deadline 4%.

**What happens.** Each flow date, a scheduler prepares that day's gas nomination and sends it out by email, almost always as an attached Word document with a standard file name such as "CALPINE DAILY GAS NOMINATION 1.doc" or, for another point, "HIDALGO DAILY GAS NOMINATION.doc". Other instances follow the same pattern for HPL, where the flow date is carried in the subject line ("HPL Nom for January 4, 2001", "HPL Nominations for December 28, 1999"). The body is usually empty or minimal — the nomination itself lives in the attachment or the subject, so the mail is a delivery envelope rather than a message. Recipients on the far end reply when they have something to say; one exemplar is a bare confirmation that volumes are unchanged from the prior day and the path is the same. The instance closes once the nomination has been sent for that date, and the same document name is re-sent the next day with new contents.

**Where it stalls.** The nomination is re-keyed into a document and re-attached under a recycled file name every day, so nothing outside the attachment identifies which flow date a given file holds — the date only exists in the subject line, and in the Calpine set not even there. That makes verification impossible without opening the attachment, and it is what makes revisions visible only as a forwarded "(REVISED)" copy rather than as an amendment to a record. Waiting and manual-transfer signals are near zero here, so this cluster does not show chasing; the friction is the repeated hand-assembly and re-issue itself, plus at least one instance where a revised nomination had to be forwarded on after the original went out.

**Why it recurs.** Nominations are per-flow-date with a daily pipeline cutoff, so a fresh document and a fresh email are required every single day for each counterparty and point; the exemplars span thirteen months across four senders.

**What could absorb it.** Generate the nomination from the scheduling record and mail it on the daily cutoff schedule, with the flow date and counterparty in both the subject and the file name so a revision supersedes a prior version instead of arriving as a forwarded copy. Where volumes repeat the prior day, default to carry-forward and require only an exception to be entered.

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
- "HPL Nom for January 4, 2001"
  — `corpus/farmer-d/logistics/2025.` bytes 313–340, lines 7–7
    ```
    sed -n '7,7p' corpus/farmer-d/logistics/2025.
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

## 12. Real-time West power desk shift handoff and booking instructions by email

**$24/month** (range $6–$72) · 0.3 automatable hours/month · confidence high

*Measured:* 10 messages in 10 task instances, 2 sender(s), 19 people, 4 months. rework 10%, manual_transfer 40%, deadline 10%.

**What happens.** Real-time schedulers on the West desk email the incoming shift, and the day-ahead and books groups, a written account of the position they are leaving behind and the bookings that still need to be made. The notes state where a book such as ST-WBOM is long or short, at which point and for which hours, what was parked or sold with a counterparty, what was purchased from the exchange or sold to imbalance, and at what price. Where the sender could not complete the entry themselves, the note becomes an instruction: buy energy to cover a short under a named book, sell the resulting length in the off-peak, or schedule specific pieces with the exchange as counterparty. Some notes also record cuts made during the hour and why, so the next person can reconcile what integrated against what was nominated. The output is an email; the work ends when the receiving desk books the transactions and adjusts its own sheets.

**Where it stalls.** The position and the booking do not travel together. The sender knows the hours, points, counterparties and prices, but the entry into the position and deal systems is done by someone else off the back of prose, so the transfer is manual and re-keyed — the manual-transfer signal is on a large share of these messages. One note shows the consequence: a purchase from a counterparty had to be cut back because imports were over capacity, and a scheduled leg integrated at a different level than it was cut to, leaving a discrepancy the next shift has to chase. Requests such as adjusting sheets for the following day depend entirely on the recipient reading and acting on the mail; nothing in the evidence shows a confirmation back.

**Why it recurs.** Real-time scheduling runs continuously in hourly blocks and changes hands at every shift and weekend, so an open position and its unbooked legs must be described in writing each time.

**What could absorb it.** A structured shift-handoff form that captures book, point, hour range, direction, counterparty and price as fields rather than prose, and writes the resulting legs directly into the position and deal systems as draft entries for the incoming scheduler to confirm — replacing free-text instructions to buy, sell or park with pre-staged bookings.

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
- "These pieces will need to be scheduled with the APX as the counterparty for HE 12-20."
  — `corpus/williams-w3/sent_items/405.` bytes 1576–1661, lines 27–27
    ```
    sed -n '27,27p' corpus/williams-w3/sent_items/405.
    ```
- "We will be long 10 mws each hour in position manager in SP-15 as a result. Please sell this energy in the off-peak"
  — `corpus/williams-w3/sent_items/148.` bytes 2084–2198, lines 27–27
    ```
    sed -n '27,27p' corpus/williams-w3/sent_items/148.
    ```
- "If you could adjust your sheets for tomorrow I would appreciate it."
  — `corpus/williams-w3/sent_items/164.` bytes 731–798, lines 19–19
    ```
    sed -n '19,19p' corpus/williams-w3/sent_items/164.
    ```

## 13. Monthly nomination volume estimates agreed by email before month start

**$22/month** (range $5–$66) · 0.3 automatable hours/month · confidence medium

*Measured:* 8 messages in 8 task instances, 2 sender(s), 6 people, 3 months. .

**What happens.** Ahead of each new gas month, someone needs a volume figure to nominate for a given point or counterparty — Josey Ranch, Calpine, Midcon, Southern Union, T-Ville — and the figure is settled in email rather than pulled from a system. In one pattern a sender simply forwards the estimated monthly nomination for a named point ("This is the estimated Josey Ranch nomination for the month of February 2000") to whoever needs it, with no reply expected. In the other pattern someone asks whether a figure looks right ("Does this average represent a good estimate of the Calpine May nom?") and a colleague answers with a per-day or total number and a rationale ("So, 5000 total is a safe assumption", "I would assume 40000 for Midcon"). The exchange ends when the estimate is stated plainly enough for the recipient to nominate against it; no confirmation back into a system is visible in these messages. Most of the traffic here is the answering half of that exchange.

**Where it stalls.** Nothing in these eight messages shows chasing, rework or a missed cutoff — the signal rates measured across them are flat. The weakness is instead that the number of record lives only in the mail body: the estimate is derived from an average or an assumption held by one of two people, stated in prose, and never written back anywhere the next person could look it up. Who owns the estimate for a given point, and what source the average was taken from, is not visible in the evidence.

**Why it recurs.** Nominations are set per gas month, so a fresh estimate is needed for every point and counterparty each month; the figures are judgement calls carried in a person's head rather than output by a system.

**What could absorb it.** A standing per-point estimate sheet, refreshed before each month rolls, that shows the prior months' scheduled and actual volumes for Josey Ranch, Calpine, Midcon and the other named points so the estimate is read off a computed average rather than recalled — with the agreed figure recorded next to it instead of only in a reply.

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
- "This is the estimated Josey Ranch nomination for the month of
February 2000"
  — `corpus/farmer-d/logistics/724.` bytes 1009–1084, lines 34–35 · rewrapped
    ```
    sed -n '34,35p' corpus/farmer-d/logistics/724.
    ```
- "I would assume 40000 for Midcon."
  — `corpus/farmer-d/logistics/1051.` bytes 444–476, lines 17–17
    ```
    sed -n '17,17p' corpus/farmer-d/logistics/1051.
    ```
- "This is the estimated Josey Ranch nomination for the month of March"
  — `corpus/farmer-d/logistics/850.` bytes 980–1047, lines 31–31
    ```
    sed -n '31,31p' corpus/farmer-d/logistics/850.
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

- **Book Transfer Request — standard email template for moving deals between trading books** (`TPL-01-book-transfer-request-standard-email-template-for-mo.md`) — template, for *Moving deals between trading books by hand-run script requests*
- **Runbook: Extending an existing deal ticket to cover unbooked meter flow** (`RUN-01-runbook-extending-an-existing-deal-ticket-to-cover-u.md`) — runbook, for *Extending existing deal tickets in Sitara/Unify to cover unbooked meter flow*
- **Runbook: Clearing Meter-Level Scheduled-vs-Actual Variances (Unify / Sitara / UA4)** (`RUN-02-runbook-clearing-meter-level-scheduled-vs-actual-var.md`) — runbook, for *Meter-level scheduled-vs-actual variance clearing across Unify, Sitara and UA4*
- **Weekly California Interstate Capacity Report — mail template** (`TPL-02-weekly-california-interstate-capacity-report-mail-te.md`) — template, for *Weekly California Capacity Report, assembled and mailed by hand*
- **Daily Credit Report — standing distribution email (draft)** (`EML-01-daily-credit-report-standing-distribution-email-draf.md`) — email, for *"Credit Report - 1/30/01" produced daily*
- **Weekly California Capacity Report — standing email template and send procedure** (`EML-02-weekly-california-capacity-report-standing-email-tem.md`) — email, for *"California Capacity Report for Week of 01/14-01/18" produced weekly*
- **Standing email template: Calpine Daily Gas Nomination notice** (`EML-03-standing-email-template-calpine-daily-gas-nomination.md`) — email, for *"Calpine Daily Gas Nomination" produced monthly*

---

## How to check any of this

```
make verify     # re-anchor every citation from scratch; recompute every number
make test       # full suite, zero model calls
make serve      # dashboard with click-through to the highlighted bytes
```

Every citation above prints the `sed` command that reproduces it. `docs/AUDIT.md` holds 25 randomly sampled citations with both `dd` and `sed` commands.

Where this is most likely wrong, and what it took on faith, is in `NOTES.md`.
