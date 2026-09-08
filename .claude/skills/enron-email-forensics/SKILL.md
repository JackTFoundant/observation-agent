---
name: enron-email-forensics
description: Domain context for reading a 2000-2002 Enron gas-pipeline email archive - who the custodians are, what the systems named in the mail actually do, which artefacts are traps. Load when classifying or characterising messages from this corpus.
---

# Reading this archive

Four mailboxes from Enron's gas business, exported off a mail server in 2002. Roughly
27 months, late 1999 to March 2002. This is a pipeline and gas-scheduling operation, not
the trading floor of the headlines.

## The four custodians

| Custodian | Folders | What they do |
|---|---|---|
| **Daren Farmer** (`farmer-d`) | `logistics` (1,194) | Gas logistics and scheduling. Nominations, meters, allocations, deal fixes. The densest operational vein in the corpus. |
| **Darron Giron** (`giron-d`) | `inbox` (380), `sent` (789) | Trading support. Produces a **daily credit report**. Also the source of most of the personal noise. |
| **Michelle Lokay** (`lokay-m`) | `inbox` (57), `sent_items` (161) | Transwestern pipeline commercial. Produces a **weekly California Capacity Report**. Handles OBA imbalances and capacity release. |
| **Bill Williams III** (`williams-w3`) | `inbox` (139), `sent_items` (520) | West-desk real-time scheduling. Forwards CAISO/FERC notices. A lot of HR and severance admin in late 2001, for obvious historical reasons. |

Their being four individuals matters: **this archive is four mailboxes, not a company.**
Any per-company total inferred from it is an extrapolation, and the report deliberately
declines to make one.

## The vocabulary

- **Nomination / nom** — telling a pipeline how much gas you intend to move on a given
  flow date. Nominations get changed, cut, and confirmed constantly. Cutoffs are daily and
  real; missing one has consequences.
- **Meter** — a physical measurement point. Meter numbers key everything and get confused
  constantly.
- **Imbalance / OBA** — the gap between what you scheduled and what actually flowed.
  Operational Balancing Agreements govern how the gap is settled. Reconciling these is
  recurring manual work.
- **Allocation** — dividing measured volumes among the parties entitled to them.
- **OFO** — Operational Flow Order. A pipeline instruction constraining flows, usually
  urgent, usually forwarded onward by hand.
- **Park and Ride / PnR** — a storage-like service Transwestern sells.
- **Sitara** — Enron's deal-capture system. Deals get entered, amended, zeroed, killed.
- **Unify** — a downstream system that has to agree with Sitara and frequently does not.
  Messages about reconciling the two are a real recurring process.
- **TAGG** — pipeline/volume accounting.
- **Enovate** — a joint-venture book; "Enovate DPR" is a recurring daily position report.
- **HPL** — Houston Pipe Line, an Enron pipeline. **TW** — Transwestern.
- **Gas Daily** — the price publication quoted in the recurring capacity report.

## Recurring work that is definitely present

Verified by subject-line frequency before any model was involved:

- **Daily credit report** — `giron-d/sent`, ~70 instances, subject `Credit Report--M/D/YY`.
  Frequently an empty body: the report itself was an attachment.
- **Weekly California Capacity Report** — `lokay-m/sent_items`, ~18 instances, subject
  `California Capacity Report for Week of MM/DD-MM/DD`. Near-identical structure each
  week: Transwestern deliveries, El Paso deliveries by point, posted Gas Daily prices.
  Assembled by hand from several sources and mailed to a fixed list of seven.
- **Calpine daily gas nomination** — ~19 instances.
- **Meter requests / corrections** — ~50 instances across several subject forms.
- **Monthly natural gas P&L request**, **Enovate DPR**, **on-call notes**,
  **work assignments** — smaller recurring sets.

## Traps in this corpus

**1. `corpus/farmer-d/logistics/3221.` — the 350 KB message.**

It is 5% of the whole corpus in one file, 70× the next largest, and its body is a 3,600-row
nomination table. **That table is machine-generated placeholder content**, proven
deterministically: 8 of its 9 columns are exact functions of the row index — `NOM_ID` is
`1000000 + n`, `SCHEDULED` is `911n mod 45000`, `ACTUAL` is `331n mod 45000`, the meter id
is `7n`, the counterparty cycles through 400 values, the status cycles with period 3, and
the pipe column is constant. Across 3,600 rows there are only two distinct first
differences where real data would have thousands.

So: **never derive a quantity from those rows.** No "3,600 nominations pending", no total
variance, no counterparty count. The pipeline caps how much of this body any model sees.

The **prose above the table is real and is excellent evidence**:

> Subject: `Full month position - attachment would not send`
> "Pasting the full month position below since the attachment keeps bouncing off the
> gateway. Please pull your own meters out of this and confirm back to me by close of
> business Thursday."

That describes a genuine recurring failure worth automating — an attachment bounces, so a
position is pasted inline, so every recipient hand-extracts their own rows and mails back a
manual confirmation. It is also the only message linking all four custodians.

**2. Personal traffic is heavy and mixed in.** UT football newsletters, eBay listings, a
Louis Vuitton bag, Maui holidays, Ken Lay's car. It sits directly alongside operational
mail from the same people. Classify by the work, not by the sender.

**3. Late-2001 severance and layoff mail** is administrative, not operational process. It
is historically loaded and easy to over-read; it is not recurring business work.

**4. Half of all bodies are quoted history.** Trailer stripping already removed it before
you see the text, so what you are given is the sender's own words. 541 messages have
*nothing* but quoted history — those are handled deterministically as acknowledgements and
never reach a model.

**5. The same person appears under several addresses** — `daren.farmer@enron.com`,
`j..farmer@enron.com` (a doubled dot where a middle initial went), and X.500 forms like
`Farmer, Daren J. </O=ENRON/OU=NA/CN=RECIPIENTS/CN=Dfarmer>`. Identity resolution handles
this upstream; do not try to count distinct people yourself.

## What good looks like

The output is a report a client president reads. That means the winning findings are dull
and frequent, tied to a named system, and supported by quotes anyone can check:

> "Scheduled-versus-actual volume reconciliation appears 60 times across 14 months,
> involves 5 people, and 22% of those messages show rework."

not

> "Communication inefficiencies were observed."