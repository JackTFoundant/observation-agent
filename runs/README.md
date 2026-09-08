# Run logs

Two runs are kept here.

**`final/`** — the shipped run. `run.jsonl` is append-only, one JSON object per unit of
work, carrying `stage`, `event`, `attempt`, `duration_ms`, `cache_hit` and `model`. Its
`summary.json` is the same report served by the dashboard out of `out/`.

**`replay/`** — the same command run again immediately afterwards against the unchanged
corpus. It exists as evidence for one specific requirement: *re-running does not repeat
finished work*. Every stage is a total cache hit and the whole run takes about six
seconds:

```
extract      cache_hits_messages=2531  model_calls=0
characterize cache_hits=12             model_calls=0
artifact     cache_hits=7              model_calls=0
```

Extractions are cached per *message* rather than per batch, so re-batching invalidates
nothing and an interrupted run resumes by simply running the command again. The cache keys
also include the sha256 of the `.claude/` files each stage's worker loads, so editing a
rubric correctly invalidates the work downstream of it — touch
`.claude/agents/message-extractor.md` and stage 1 re-executes.
