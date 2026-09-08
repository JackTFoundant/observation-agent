# Observation agent

Reads a company's entire email archive, works out where it is losing time, proves every
claim against the raw files, and serves the result on a dashboard. It also acts on what it
finds: for the biggest opportunities it drafts a document someone could use the next
morning.

Built to run inside Claude Code on a subscription. No API keys, no API spend, everything
local.

## Quick start

```bash
uv sync --extra dev          # Python 3.12, pinned by uv.lock
make doctor                  # one real model call, to fail fast with a specific remedy
make run                     # the whole pipeline
make serve                   # dashboard on http://localhost:8787
```

`make run` is safe to re-run. Everything is content-addressed, so an unchanged corpus
replays from cache in seconds and an interrupted run resumes by running it again.

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

| Stage | Kind |
|---|---|
| parse, decode, resolve identity, dedupe, thread, triage | deterministic |
| classify each message | **model**, ~100 batched calls |
| block, cluster, gate, label | deterministic |
| describe each promoted cluster | **model**, one call each |
| measure, cost, rank | deterministic |
| anchor every quote to raw bytes, gate claims | deterministic |
| draft artifacts above the threshold | **model**, up to 7 calls |
| render report and dashboard data | deterministic |

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
