# Observation agent

Reads a company's entire email archive, works out where it is losing time, proves every
claim against the raw files, and serves the result on a dashboard. It also acts on what it
finds: for the biggest opportunities it drafts a document someone could use the next
morning.

Built to run inside Claude Code on a subscription. No API keys, no API spend, everything
local.

## Look at the finished run first — no model calls, no auth

A complete run is already committed, so you can read everything before running anything.
None of this makes a model call or needs the CLI authenticated:

```bash
uv sync --extra dev     # Python 3.12, pinned by uv.lock
make serve              # dashboard on http://localhost:8787 (opens your browser)
make verify             # re-anchors every citation from scratch; PASS, 133 checks
make test               # 169 tests, zero model calls
```

In the dashboard: click the headline dollar figure to see what sums into it, click any
opportunity for its derivation (**measured** and **assumed** in two columns), then click a
file path under any quote — the raw message opens with the quote highlighted, sliced at the
published byte offsets rather than found by searching. `out/report.md` is the same content
as a document, and `docs/AUDIT.md` has 25 random citations with paste-able `dd` and `sed`
commands if you want to check the evidence by hand.

## Running it yourself

```bash
make doctor             # one real model call, fails fast with a specific remedy
make run                # the whole pipeline: ~12 minutes from an empty cache
```

`make run` is safe to re-run. Everything is content-addressed, so an unchanged corpus
replays in about five seconds with zero model calls, and an interrupted run resumes by
running it again — filling a 32-message gap left by a partial run took 79 seconds and
touched nothing else.

The run in `out/` and its log in `runs/final/` are the same execution: 3,240 files read,
2,531 messages classified (100% coverage), 11 opportunities, 88 citations all anchored to
exact byte ranges, 7 drafted artifacts, 97 model calls, 12 minutes 2 seconds.

If the `claude` CLI is not on your `PATH`, the runner finds it anyway (including inside a
VS Code extension directory). Set `CLAUDE_BIN` to override. If it is not authenticated,
`make doctor` says exactly what to run.

## Check it rather than trust it

```bash
make verify    # re-anchors every citation from scratch, recomputes every number
make test      # full suite, zero model calls
```

`make verify` shares no state with the pipeline. It re-reads the corpus off disk, re-hashes
every file, re-slices every published byte range, and asserts each citation matches at the
tier it claims **and no weaker one**. Then it recomputes every hours-and-dollars figure from
its own published derivation and asserts equality to the cent, and that the headline equals
the sum of its parts.

`docs/AUDIT.md` holds 25 randomly sampled citations with the `dd` and `sed` commands that
reproduce each one. Every citation in the dashboard shows both.

## How it works

A deterministic conductor whose entire workforce is Claude Code.

| Stage | Kind | Cost on the shipped run |
|---|---|---|
| parse, decode, resolve identity, dedupe, thread, triage | deterministic | 3s |
| classify each message | **model** | 80 batched calls |
| block, cluster, gate, label | deterministic | 1.5s |
| describe each promoted cluster | **model** | 9 calls, one per cluster |
| measure, cost, rank | deterministic | <1s |
| anchor every quote to raw bytes, gate claims | deterministic | <1s |
| draft artifacts above the threshold | **model** | 8 calls |
| render report and dashboard data | deterministic | <1s |

**97 model calls, 12 minutes 2 seconds, from an empty cache.** A re-run over the unchanged
corpus takes about five seconds and makes no model calls at all.

The split is not arbitrary. *Promises about control flow* — finishes unattended, inside a
time budget, resumable, arithmetic exact, tests pass with no model — cannot be delegated to
a model, because a model cannot promise its own control flow. *Judgments* — what is this
message about, where does this work stall, what should the SOP say — cannot be delegated to
code.

Two invariants hold the whole thing up, and both are enforced rather than asserted:

- **Every published quote is sliced out of a corpus file**, never copied from model output.
  A hallucinated quote cannot reach the report because there is nothing to assign.
- **No model produces a duration or an amount.** A guard rejects any response containing
  one, and a test proves it with a recorded poisoned response.

`NOTES.md` covers how Claude Code was driven, what went wrong along the way, and — at
length — where this system is most likely to be wrong.

## Layout

```
observe/            the pipeline; cli.py is the entrypoint
  ingest/qp.py      quoted-printable decoding with a byte-offset map
  evidence/anchor.py  quote -> byte range; the slice-never-copy invariant
  estimate/model.py   counts -> hours -> dollars, in Decimal
  verify.py         the independent re-verifier
  serve.py          the dashboard server; reads files, computes nothing
config/             every assumption, commented, with low/base/high bands
.claude/            agents, skills, hooks, slash commands, settings as used
out/                the report, dashboard data, drafted artifacts
runs/<id>/          run.jsonl: one JSON event per unit of work
tests/              full suite; a fixture makes model calls impossible
```
