# Notes

## How I drove Claude Code

The brief's requirements are two different kinds of thing. *Promises about control flow* —
unattended, inside thirty minutes, skips finished work, arithmetic exact, tests pass with no
model — cannot be delegated to a model, because a model cannot promise its own control flow.
*Judgments* — what is this message about, where does this work stall, what should the SOP say
— cannot be delegated to code.

So: **a deterministic conductor whose entire workforce is Claude Code.** `observe/pipeline.py`
owns sequencing, batching, caching, concurrency, retries, deadlines and every number. Claude
Code does three things: classify a message, describe a cluster, write a document.

Two front doors, **one execution path**. `make run` calls the conductor; `/observe` launches
the same conductor and narrates it. The slash command is a doorbell, not a second
implementation.

Workers are headless `claude -p` calls on subscription OAuth. `--bare` would be faster and
better isolated but forces `ANTHROPIC_API_KEY`, which the brief forbids. Three flags do the
real work: `--tools ""` (no tools means no tool schemas in the window and no filesystem to
wander — text in, JSON out), `--strict-mcp-config --setting-sources ""` (this machine has
dozens of MCP servers; without these every worker pays their schemas), and a full
`--system-prompt` replacement so a worker's context is exactly the bytes I chose regardless
of whose laptop it runs on.

`.claude/` is in the build graph, not the appendix: worker prompts are assembled from the
agent and skill files on disk and their sha256 is part of the cache key, so editing a rubric
invalidates the work downstream of it. A `PreToolUse` hook denies hand-edits to `out/`, so
"no model holds the arithmetic" is enforced rather than asserted.

## What went to subagents, and the context budget

Only judgments. The budget came from killing 1.7M tokens **before** the first model call:
trailer-stripping (half of every reply is quoted history), dedup, rule-based triage, and a
per-message character cap. 3,240 files → 3,224 unique → 2,531 worth a model's attention →
about 445K tokens of novel text. The median novel span is 171 characters.

Extraction ran in batches of 32: 80 calls at concurrency 8, median 65s. Characterization is
one call per promoted cluster and receives **measured counts plus a deterministic spread of
exemplars**, never the cluster's raw messages. Artifact drafting is one call each. **97 model
calls, 12 minutes 2 seconds** for the whole cold run.

The hardest design question was making processes *emerge* rather than be authored. No model
sees the whole corpus, so the temptation at the reduce step is to let one name a few plausible
processes and back-fill citations. The defence is structural: **the model never names a
process.** By the time it sees a cluster, the cluster exists, carries a mechanical label, and
has passed a numeric gate that 909 of 918 candidates failed. It can describe; it cannot
conjure. Everything declined is published in `out/residual.json` with the gate it failed.

## What ran in parallel

Adaptive concurrency from 8, halving on a rate-limit signal and recovering after clean
completions. A 28-minute deadline split into reserved per-stage shares so no one stage can
starve the rest, after which the run drains and **still emits a complete report that says
what it cut**. A batch failing validation twice is **bisected**, so one pathological message
costs two extra calls rather than 32 lost extractions. An auth error fails the run at once.

## What I chose to produce, and why

Artifacts are gated on **evidence and recurrence, not money**: five verified citations
across four messages, six task instances, three months, and a shape worth writing (`none`
is a real answer and disqualifies). The dollar floor is deliberately low at $55/month,
which needs explaining, because my first attempt set it at $250 on the reasoning that below
about an hour a week a written procedure costs more attention to maintain than it returns.
That is sound in the abstract and wrong here: it ignored my own `extrapolation_factor: 1.0`.
Applied to four-mailbox figures, a company-sized floor cleared exactly three items — all of
them "send this recurring report on a schedule" — and excluded every operational finding in
the archive. So the floor now excludes noise rather than ranks, and the evidence bar does
the work.

Capped at six, because six documents is what a team adopts in a quarter and twelve is
shelfware, plus one slot for the best-evidenced item that fails *only* the dollar test,
labelled in its front matter as a judgment call. A purely numeric cutoff is not a strategy.
Seven shipped; five opportunities are recorded as not warranting one, with reasons.

Every artifact follows one convention that makes it checkable: **any sentence asserting
current practice ends with a citation id, recommendations carry none and sit under their own
heading**, and a linter withholds any document whose markers do not resolve. A reader can
always tell what was observed from what is being proposed.

## Where it went wrong, and what caught it

**Paraphrase, caught structurally rather than noticed.** Every published quote is *sliced
from the corpus*: the model's string is only a search key, and the citation's `quote` field
is assigned from `raw_text[start:end]`. A hallucinated quote cannot reach the report because
there is nothing to assign. On the shipped run 88 of 88 quotes anchored — 65 byte-exact, 23
rewrapped by line-wrapping, none repaired. The instruction to copy characters exactly works
better than I expected; the system does not depend on it working, which is the point.

**Quantities, refused at the boundary.** Workers try to be helpful and estimate hours. A
guard rejects any response carrying a duration or an amount, and a test proves it with a
recorded poisoned response. Drawing that line correctly took two corrections: the first
version pattern-matched too loosely and rejected the extractor's own most important field,
and the second rejected verbatim corpus quotes that happened to mention money — which would
have blinded the report to every invoice and settlement finding. The rule that survives is
that the guard stops a model *asserting* a quantity, never *quoting* the archive.

**A missing process, found by disbelief.** The clearest recurring work in the corpus is a
daily credit report — 69 instances over 14 weeks — and it was absent from early output. Its
bodies are empty, because the report was an attachment, so two dedup tiers collapsed every
day's report into one. Chasing that produced the design's best idea: content clustering is
structurally blind to attachment-only work, so `observe/recurring.py` finds recurring
*subject templates* with no model at all and cites the `Subject:` line itself.

**Warm testing hid three classes of failure.** I developed against a warm cache and only
exercised the cold path late. It hid a rate-limit policy that dropped messages, a deadline
that let one stage starve the rest, and — sharpest of all — a bug where my own rate-limit
detector matched `429` inside a message uid (`m_64293e33900a`), discarded a perfectly valid
batch as throttled, and retried it until a deadline killed it. Deterministic, because uids
are content hashes, which is why the same batch died on every run while I misdiagnosed it as
load. The fix is a principle: parse first, and never pattern-match a payload that parses.
Coverage is now derived by comparing the eligible set against the extracted set, so no
message can go missing unremarked whatever the cause.

## Where this system is most likely to be wrong

1. **The handling-minute assumptions are estimates, and they dominate the output.**
   Instances, touches, participants, months and signal rates are all measured from the
   corpus and re-verifiable. The minutes-per-task in `config/estimation.yml` are my
   judgment by analogy — nobody timed this work and nobody could. The total moves close to
   linearly with them, which is why nothing ships as a point estimate.
2. **`automatable_share` is the second-largest act of faith.** Judging that 55% of a
   nomination change is automatable is a claim about Sitara, Unify and TAGG, which are names
   in 2001 emails to me and nothing more.
3. **The headline is a floor.** Only ~7% of operational messages could be attributed to an
   identified recurring process; the rest is a long tail left deliberately uncosted. A
   stricter gate buys a defensible number and a larger blind spot. I chose that knowingly.
4. **Email volume is a biased proxy for work.** Phone, terminal and hallway work is
   invisible; argumentative processes are over-weighted. Threading reduces this — a
   forty-message thread is one task instance — but does not remove it.
5. **Four mailboxes is not a company.** Every figure is scoped to these custodians and
   deliberately not extrapolated (`extrapolation_factor: 1.0`). The real figure is larger by
   an unknown factor; multiplying up would be more impressive and much less defensible.
6. **Task classification is a model judgment and the weakest semantic link.** The citation
   layer proves a quote exists where it says. It does not prove the class label is right, and
   class confusion flows straight into instance counts and from there into dollars.
7. **Clustering and threading are heuristics I tested mechanically, not for accuracy.** No
   hand-labelled sample exists, so I cannot give you a false-merge rate.
8. **Whether a quote *supports* its claim is unverified.** Deterministic code proves it
   exists; `/verify-claims` attacks the rest, but as a manual pass, not a gate.
9. **The artifacts are unreviewed drafts.** Every current-practice sentence is
   citation-backed and every gap marked `<to be confirmed>`, but nobody who does this work
   has read them.

**Timing.** The shipped cold run took 12 minutes 2 seconds: 97 model calls against a
28-minute deadline that never came close to firing. A warm re-run is about five seconds with
zero model calls, and a resume does only the missing work — filling a 32-message gap took 79
seconds. The deadline is a safety net, not the expected duration. If it runs long elsewhere
the levers are `--concurrency`, `OBSERVE_BATCH_SIZE`, and `OBSERVE_EXTRACT_MODEL=haiku` —
the last is safe because a published quote is always sliced from the corpus and the model's
string is only a search key, so a cheaper model costs recall, not correctness.

## What I would build next, in order

1. **Hand-label 200 messages** to measure classification, threading and noise-classifier
   accuracy. Every number here rests on those being roughly right and I cannot say how right.
2. **Replace one minute-assumption with a real observation** — even one interview — and see
   how far the total moves. That alone would tell you whether the estimation layer is worth
   trusting.
3. **Close the attribution gap.** 7% is too low; a softer second tier for the long tail, with
   its own confidence label, would report more of the observed workload without pretending
   weak findings are strong.
4. **Make the support audit a gate**, not a manual pass: one cheap call per shipped citation
   asking only whether it supports its claim, able to demote but never promote.
5. **A per-opportunity "what would change my mind" field**, so each finding ships the
   observation that would falsify it.