# Working on this repo

An observation agent over a 3,240-message email archive. It reads every message, finds the
recurring work, costs it, proves every claim against raw bytes, drafts usable documents for
the biggest findings, and serves a drill-through dashboard.

## The two invariants. Do not weaken either.

**1. Every published quote is sliced out of a corpus file.** It is never copied from model
output. A model's proposed quote is only a *search key*: `observe/evidence/anchor.py`
locates it and the citation's `quote` field is assigned from `raw_text[start:end]`. If no
anchor is found there is no quote, and the claim that needed it does not ship. A
hallucinated quote therefore cannot reach the report — that is structural, not a check that
runs at the end.

**2. No model ever produces a duration or an amount.** Every worker response passes through
`observe/llm/schema_guard.py`, which rejects a key or value naming one.
`tests/test_schema_guard.py` feeds it a recorded poisoned response containing
`"hours_saved": 40` and asserts the rejection. Hours and dollars are computed in `Decimal`
by `observe/estimate/model.py` from counts measured by deterministic code, and every figure
ships the derivation that produced it so `observe/verify.py` can recompute it.

If you find yourself wanting a model to "just estimate" something, that is the signal to
add a measurement or an assumption in `config/estimation.yml` instead.

## Where the line falls

Deterministic: parsing, quoted-printable decoding and offset mapping, identity resolution,
dedup, threading, triage, clustering, the promotion gates, all arithmetic, citation
anchoring and validation, rendering, the server.

Model: what a message is about (`agents/message-extractor.md`), what a cluster means
(`agents/process-characterizer.md`), writing a document (`agents/artifact-drafter.md`).
Those three, and nothing else.

## Conventions

- **Python 3.12 via uv.** `uv run` everything; `uv.lock` is committed.
- **Comments explain *why*, especially where the obvious approach is wrong.** Several
  modules carry a note about a bug that cost real findings — the CRLF-composition bug in
  `ingest/qp.py`, the timestamp in `parse.py`'s content hash, the content floor in
  `dedupe.py`. Keep those notes; they are the reason the code looks the way it does.
- **Tests never invoke a model.** `tests/conftest.py` makes that mechanical. Model-shaped
  stages read frozen fixtures from `tests/golden/`.
- **Negative tests carry the weight.** A citation validator that only sees well-formed
  input proves nothing. See `tests/test_citation_validator.py`.
- Prefer a real corpus file as a fixture over a synthetic string. The failure modes that
  matter only exist in real 2002 mail.

## Cache invalidation is per stage

`prompt_hash(claude_dir, *files)` requires an explicit file list. Do not glob: hashing every
`agents/*.md` means adding one unrelated agent invalidates 2,500 cached extractions. The
per-stage lists are in `observe/cache.py`.

Extractions are cached **per message**, not per batch, so re-batching invalidates nothing
and an interrupted run resumes by simply running again.

## Commands

```
make doctor    one real model call; fails fast with a specific remedy
make run       the whole thing; safe to re-run
make verify    re-anchor every citation, recompute every number; no model
make test      full suite; no model
make serve     dashboard on :8787
make audit     regenerate docs/AUDIT.md
```

## The corpus has a trap

`corpus/farmer-d/logistics/3221.` is 5% of the corpus in one file and its 3,600-row table
is **machine-generated placeholder data** — 8 of 9 columns are exact functions of the row
index. Never derive a quantity from those rows. `observe/classify.py` proves it and the
prose above the table stays citable. See `.claude/skills/enron-email-forensics/SKILL.md`.
