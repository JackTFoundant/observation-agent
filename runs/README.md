# Run logs

Two runs, kept because between them they evidence two separate requirements.

## `cold5/` — the shipped run

The report in `out/` came from this run. It started from an **empty cache** and completed
in one pass, no resume:

```
3,240 files -> 3,224 unique -> 2,823 task instances -> 2,531 shown to a model
80 of 80 extraction batches, coverage 2,531/2,531, complete_run true
0 throttles, no deadline pressure on any stage
11 opportunities, 89 citations, 7 drafted artifacts
make verify: PASS, 137 checks, 0 failures
12 minutes 20 seconds, against a 28-minute deadline
```

`run.jsonl` is append-only, one JSON object per unit of work, carrying `stage`, `event`,
`attempt`, `duration_ms`, `cache_hit` and `model`. 111 events spanning 12.2 minutes.

It took four cold runs to get here, and `NOTES.md` describes all four rather than only this
one — the failures are the interesting part, and the last of them was a bug of my own that
had been silently costing every run a batch of messages.

## `replay/` — evidence that re-running repeats no finished work

The same command, run again immediately afterwards against the unchanged corpus. Every
stage is a total cache hit and the whole run takes about five seconds:

```
extract      cache_hits_messages=2531  model_calls=0
characterize cache_hits=10             model_calls=0
artifact     cache_hits=7              model_calls=0
```

Extractions are cached per *message* rather than per batch, so re-batching invalidates
nothing and an interrupted run resumes by simply running the command again — filling a
32-message gap left by a partial run took 79 seconds and touched nothing else.

Cache keys also include the sha256 of the `.claude/` files each stage's worker loads, so
editing a rubric correctly invalidates the work downstream of it: touch
`.claude/agents/message-extractor.md` and stage 1 re-executes.
