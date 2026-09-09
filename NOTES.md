# Notes

## How I drove Claude Code

The README's requirements are two different kinds of thing, and separating them decided the
whole design.

*Promises about control flow* — finishes unattended, inside thirty minutes, skips finished
work, arithmetic exactly right, tests pass with no model. A model cannot promise its own
control flow.

*Judgments* — what is this message about, where does this work stall, what should the SOP
say. Code cannot make those.

So: **a deterministic conductor whose entire workforce is Claude Code.** `observe/pipeline.py`
owns sequencing, batching, caching, concurrency, retries, deadlines and every number.
Claude Code does three things and nothing else: classify a message, describe a cluster,
write a document.

There are two front doors and **one execution path**. `make run` calls the conductor;
`/observe` launches the same conductor in the background, tails `runs/<id>/run.jsonl` and
narrates. The slash command is a doorbell, not a second implementation — two implementations
would be two half-built things.

Workers are headless `claude -p` calls on subscription OAuth. `--bare` would have been
faster and better isolated, but its own help says auth is then "strictly ANTHROPIC_API_KEY
or apiKeyHelper", which the assignment forbids, so it is disqualified. Three flags do the
real work: `--tools ""` (a worker gets no tools at all — no tool schemas in its window, no
filesystem to wander, text in and JSON out), `--strict-mcp-config --setting-sources ""`
(this machine has dozens of MCP servers configured; without these every worker pays their
schemas), and a full `--system-prompt` replacement so a worker's context is exactly the bytes
I chose regardless of whose laptop it runs on.

`.claude/` is in the build graph, not the appendix. Every worker's prompt is assembled from
the agent and skill files on disk, and `prompt_hash` over those bytes is part of the cache
key. Edit the extractor's rubric and every extraction downstream invalidates — demonstrable
in ten seconds. A `PreToolUse` hook denies hand-edits to `out/`, `.observe-cache/` and
`runs/`, so "no model is holding the arithmetic" is enforced by configuration rather than
asserted in a README.

## What went to subagents, and the context budget

Only judgments. The budget came from killing 1.7M tokens **before** the first model call:
trailer-stripping (half of every reply body is quoted history), dedup, rule-based triage,
and a hard per-message character cap. 3,240 files → 3,224 unique → 2,531 messages worth a
model's attention → about 445K tokens of novel text. The median novel span is 171
characters; most real operational mail is very short.

Extraction ran in batches of 24 with a ~2,800-token system prompt, ~100 calls at
concurrency 8, about nine minutes. Characterization is one call per promoted cluster, and it
receives **measured counts plus a deterministic spread of exemplars** — never the cluster's
raw messages. Artifact drafting is one call each. Roughly 120 model calls for a cold run.

The hardest design question was making processes *emerge* rather than be authored. No model
sees the whole corpus, so the temptation at the reduce step is to let one name a few
plausible processes and back-fill citations. The defence is structural: **the model never
names a process.** By the time it sees a cluster, the cluster exists, carries a mechanically
generated label, and has passed a numeric gate that 953 of 965 candidates failed. It can
describe; it cannot conjure. Everything declined is published in `out/residual.json` with
the gate it failed.

## What ran in parallel

Adaptive concurrency, starting at 8, halving on any rate-limit signal to a floor of 2 and
recovering after a minute of clean completions. Per-call hard kill at 240s, global deadline
at 25 minutes after which the run stops dispatching, drains, and **still emits a complete
report** with a coverage block — degraded and honest beats crashed at minute 29. Three
attempts with jittered backoff; a batch that fails validation twice is **bisected** so one
pathological message costs two extra calls instead of twenty-four lost extractions. An auth
error fails the whole run immediately rather than retrying a hundred times.

## Where Claude Code got it wrong, and how I caught it

**Paraphrased quotes — caught by design, not by luck.** The invariant is that every
published quote is *sliced from the corpus*: the model's string is only a search key, and
the citation's `quote` field is assigned from `raw_text[start:end]`. A hallucinated quote
cannot reach the report because there is nothing to assign. Measured on this run: 112 of 112
proposed quotes anchored, 86 byte-exact, 25 whitespace-rewrapped, 1 quoted-printable-decoded,
1 repaired from a paraphrase to the file's own wording. On an early three-batch slice it was
61 of 61. The instruction to copy characters exactly works better than I expected — but the
system does not depend on it working.

**A guard that ate its own most important field.** My schema guard rejects any response
containing a duration or an amount. Its first version matched substrings, so the pattern
`hrs?` matched the "hr" inside `process_phrase` and it rejected every extraction. Caught
because the run failed loudly rather than degrading. Now matched against whole key segments.

**The same guard then rejected real evidence.** It flagged verbatim corpus quotes containing
dollar figures — a line about a payment amount is exactly the evidence an
invoice-and-settlement finding needs, and rejecting it would have blinded the report to a
whole task class. The fix draws the line correctly: the guard stops a model *asserting* a
quantity, not *quoting* the archive.

**Bisection amplifying a systematic failure.** When every message in a batch failed
validation for the same reason, bisection turned one wasted call into forty. It now only
splits when the rejection looks localized, which is the case it exists for.

**Two dedup bugs that silently deleted the best finding in the corpus.** The clearest
recurring process is a daily credit report, 69 instances over 14 weeks. Its bodies are empty
— the report was an attachment — and the subject key strips dates, so (a) every day's report
hashed identically for exact-dedup and (b) they all shingled to the same empty MinHash
signature. 48 of 71 were being dropped as duplicates. A genuine duplicate is one message
stored twice and shares a `Date` header; two instances of a recurring task do not. Found by
asking why a process I could see by eye in the subject lines was not in the output.

That investigation produced the design's best idea: content clustering is structurally blind
to attachment-only recurring work, so `observe/recurring.py` finds recurring **subject
templates** with no model at all, and cites the `Subject:` line itself — which is in the raw
bytes like any other quote.

**A cache key that was too coarse.** `prompt_hash` globbed `agents/*.md`, so merely *adding*
the artifact-drafter agent invalidated all 2,531 cached extractions. Now scoped per stage.
Extractions are also cached per *message*, not per batch: dedup got more conservative
mid-build, the survivor set changed, every batch boundary moved, and a batch-keyed cache
would have thrown away every completed extraction.

**A threshold I had to walk back.** I set the artifact floor at $250/month — sound reasoning
that ignored my own `extrapolation_factor: 1.0`. Applied to four-mailbox figures it cleared
three items, all "send this report on a schedule", and excluded every operational finding.
The gate is now evidence and recurrence, with a low dollar floor, and `config/thresholds.yml`
records the mistake and the reason.

**Logging that could kill a run.** A `FileNotFoundError` from the run log propagated out of a
worker thread and took down twenty minutes of work. A run that cannot write its log should
lose the log, not the run.

**A cold run silently covered 98% of a corpus it claimed to read in full.** Every run
during development used a warm cache, so I only exercised the cold path at the very end. It
finished in 23.6 minutes and `make verify` passed — but two batches had hit rate limits on
all three attempts and been dropped, losing 48 messages, and the resulting report was
materially smaller (11 opportunities instead of 14, 89 citations instead of 112). The
headline still said it had read every message.

Two things were wrong. A throttle consumed one of three *content* attempts, when a throttle
is transient and not the unit's fault while malformed JSON is and deserves to give up; they
now have separate budgets, and throttles back off up to 180s and retry up to twelve times,
with the run deadline as the real stop. And the loss was under-reported: coverage now
travels with the report, `out/summary.json` names every message that never got an
extraction, and an incomplete run says so in bold at the top of `report.md`.

**Then my fix for that broke the run in a worse way.** The second cold run lost no
messages — and shipped a report with *no narratives and no artifacts at all*. Thirteen
throttles had cost 29 minutes of cumulative backoff sleep, extraction ran to 28.7 of a
25-minute budget, and characterization and artifact drafting were then cut off with zero
calls each. It still printed a normal headline and `make verify` still said PASS, because
verify was checking whether what shipped was *true*, not whether it was *complete*.

Three things were wrong, and all three are now fixed:

- **One global deadline let the first stage eat everything.** Stages now have reserved
  shares of the budget (`Context.STAGE_BUDGET`), so extraction can take most of a run but
  never all of it.
- **The backoff was a double penalty.** The adaptive semaphore already halves concurrency
  on a throttle; sleeping up to 180 seconds on top of that was what burned the clock.
  Backoff is now capped at 45s with more retries — retry often, sleep briefly, let the
  semaphore do the throttling.
- **A degraded run looked like a good one.** Any stage cut short is now recorded, printed
  as a banner above the headline in `report.md`, published as `degraded_stages` in
  `summary.json`, and raised as a warning by `verify` — which also warns when a run with
  counted opportunities drafted no artifacts at all.

**And underneath both of those was a bug of my own making.** Every cold run lost exactly
one batch of 32 messages, and I had blamed rate limiting twice. It was self-inflicted: the
rate-limit detector regexed the worker's *answer* for `429`, and a message uid is a hex
hash. `m_64293e33900a` contains `429`. So a worker returned a perfectly valid batch, its
own message id tripped the detector, the response was thrown away as a rate limit, and the
batch retried until a deadline killed it. Deterministic, because uids are content hashes -
which is exactly why the *same single batch* died on every run, and why the "four throttles"
I recorded on the third run were almost certainly this and not real limits.

The fix is a principle rather than a patch: **parse first, and never pattern-match a
payload that parses.** Rate limiting and auth failure are detected structurally - a
non-zero exit, or an error envelope - and text matching survives only as a fallback for
when the CLI hands back prose instead of JSON. One of the new tests immediately caught my
replacement regex still firing on ordinary corpus prose ("deal 429 was rebooked in
Sitara").

**The fourth cold run is the one that shipped:** 12 minutes 20 seconds, 80 of 80 batches,
coverage 2,531 of 2,531, no throttles, no deadline pressure, `make verify` clean. The
progression was 28.8 min with nothing but numbers, then 25.0 with narratives and artifacts
but a hidden gap, then 17.1 with the gap correctly reported, then 12.3 clean.

I am reporting all four rather than only the last because the pattern is the interesting
part. The first fix was right in isolation and wrong in the system. The second exposed a
reporting hole. The third revealed that the thing I had been diagnosing for two runs was
not the thing that was wrong. And the only reason I found any of it is that I made myself
run the path the grader would actually take instead of the warm path I had been developing
against - every one of these failures was invisible from a cached run.

## Where this system is most likely to be wrong

1. **The handling-minute assumptions are guesses and they dominate the output.** Instances,
   touches, participants, months and signal rates are all measured and re-verifiable. The
   minutes-per-task in `config/estimation.yml` are my estimates by analogy. Nobody timed this
   work and nobody could — the people left in 2002 and the systems no longer exist. The total
   moves close to linearly with these values, which is why nothing ships as a point estimate.
   If one number here is wrong, it is this one.

2. **`automatable_share` is the second-largest act of faith.** Judging that 55% of a
   nomination change is automatable is a claim about Sitara, Unify and TAGG, which are names
   in 2001 emails to me and nothing more. A reader who used them should overwrite that column
   first.

3. **The headline is a floor, and a low one.** Only about 8% of operational messages could be
   attributed to an identified recurring process. The rest is a long tail that failed the
   promotion gate, and it is real work left deliberately uncosted. A stricter gate produces a
   smaller, more defensible number and a larger blind spot; I chose that direction knowingly,
   but the true recoverable figure is certainly higher than what is printed.

4. **Email volume is a biased proxy for work.** Work done by phone, in a terminal or across
   a desk is invisible. Work that generated argument is over-weighted. Threading reduces this
   — a forty-message thread is one task instance — but does not remove it: a chatty process
   still looks larger than a quiet one of equal cost.

5. **Four mailboxes is not a company.** Every figure is scoped to these four custodians and
   deliberately not extrapolated. The real company-wide number is larger by an unknown factor.
   Multiplying up would have produced a more impressive and much less defensible report.

6. **Task classification is a model judgment and the weakest semantic link.** The citation
   layer proves a quote exists in the file it names. It does not prove that a message labelled
   `gas_nomination` belongs to that class, and class confusion flows straight into instance
   counts and from there into dollars. The published `confidence` field is itself a model
   self-report.

7. **Clustering and threading are heuristics I tested mechanically, not for accuracy.** I
   have no hand-labelled sample, so I cannot tell you the false-merge or false-split rate. I
   did catch and fix one bad case — transitive closure over "shares a participant" merged 30
   unrelated `meter` messages across 28 people — but by inspection, not measurement.

8. **The noise classifier's precision is unmeasured.** It is biased toward keeping things
   (unmatched defaults to operational), but a wrongly excluded operational thread is invisible
   to the final report by construction, and I have no estimate of how often that happens.

9. **Undated messages get a crude proportional uplift.** They inflate instance counts but
   never widen a coverage window. If undated messages cluster in one period — plausible, given
   one mail server — this is wrong in an unknown direction.

10. **The 350 KB message is a judgment call in both directions.** I proved its 3,600-row
    table is machine-generated (8 of 9 columns are exact functions of the row index, including
    `911n mod 45000`) and derived no quantity from it. But I may also have discarded something
    real inside it, and I did not look row by row.

11. **The artifacts are unreviewed drafts.** Every current-practice sentence is citation-
    backed and every gap is marked `<to be confirmed>`, but the recommended steps encode my
    assumptions about how gas scheduling ought to work. Nobody who does this work has read
    them, and each says so in its front matter.

12. **I did not measure whether a quote *supports* its claim.** Deterministic code proves the
    quote exists where it says. Whether a human reader would agree it supports the sentence it
    is attached to is unverified — `/verify-claims` exists to attack exactly that, but it is a
    manual pass I ran on a sample, not a gate.

## A note on timing

The shipped cold run took **12 minutes 20 seconds** on an unthrottled account: 100 model
calls, of which 83 are extraction, against a 28-minute deadline that never came close to
firing. A warm re-run over the unchanged corpus takes about **5 seconds** with zero model
calls, and a resume that fills a partial run does only the missing work - filling one
32-message gap took 79 seconds.

The deadline is a safety net, not the expected duration, and it is divided per stage
(`Context.STAGE_BUDGET`) so no single stage can consume the run. If it does run long on
someone else's machine, the levers are `--concurrency`, `OBSERVE_BATCH_SIZE`, and
`OBSERVE_EXTRACT_MODEL=haiku`. The last is safe in a way worth spelling out: because a
published quote is always *sliced from the corpus* and the model's string is only a search
key, a cheaper model that paraphrases more costs recall, not correctness.

## What I would build next, in order

1. **Hand-label 200 messages** and measure classification, threading and noise-classifier
   accuracy. Every number above rests on these being roughly right and I currently cannot say
   how right.
2. **Replace one minute-assumption with a real observation** — even one interview — and see
   how far the total moves. That single measurement would tell you whether the estimation
   layer is worth trusting at all.
3. **Close the attribution gap.** 8% is too low. A softer second tier for the long tail, with
   its own confidence label, would report more of the observed workload without pretending the
   weak findings are strong.
4. **Make the support audit a gate rather than a manual pass**: one cheap call per shipped
   citation asking only whether it supports its claim, able to demote but never to promote.
5. **A per-opportunity "what would change my mind" field**, so each finding ships the
   observation that would falsify it.