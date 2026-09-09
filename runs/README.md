# Run logs

Two runs, kept because between them they evidence two separate requirements.

## `final/` — the shipped run

The report in `out/` came from this execution. It started from an **empty cache** and
completed in one pass, no resume:

```
3,240 files -> 3,224 unique -> 2,823 task instances -> 2,531 shown to a model
80 of 80 extraction batches, 80 calls, no retries
coverage 2,531/2,531, complete_run true
0 throttles, no deadline pressure on any stage
1,625 extractions -> 918 candidate clusters -> 9 promoted (909 declined, all published)
11 opportunities, 88 citations (65 byte-exact, 23 rewrapped, 0 repaired)
7 drafted artifacts, 5 opportunities recorded as not warranting one
97 model calls total, 12 minutes 2 seconds against a 28-minute deadline
make verify: PASS, 133 checks, 0 failures
```

`run.jsonl` is append-only, one JSON object per unit of work, carrying `stage`, `event`,
`attempt`, `duration_ms`, `cache_hit` and `model`. 108 events spanning 11.9 minutes.
Extraction batches ran a median of 65s, p95 144s.

It took several cold runs to reach this, and `NOTES.md` describes all of them rather than
only this one. The failures are the interesting part — the last was a bug of mine that had
been silently costing every run a batch of messages.

## `replay/` — evidence that re-running repeats no finished work

The same command, immediately afterwards, against the unchanged corpus. Every stage is a
total cache hit and the run takes about five seconds:

```
extract      cache_hits_messages=2531  model_calls=0
characterize cache_hits=9              model_calls=0
artifact     cache_hits=7              model_calls=0
```

Extractions are cached per *message* rather than per batch, so re-batching invalidates
nothing and an interrupted run resumes by simply running the command again — filling a
32-message gap left by a partial run took 79 seconds and touched nothing else.

Cache keys also include the sha256 of the `.claude/` files each stage's worker loads, so
editing a rubric correctly invalidates the work downstream of it: touch
`.claude/agents/message-extractor.md` and stage 1 re-executes.
