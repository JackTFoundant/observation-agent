---
description: Run the observation pipeline over the corpus and report what it found
---

Run the full pipeline and report the result.

This command is a doorbell, not a second implementation. There is exactly one execution
path in this system — `observe/pipeline.py` — and both front doors ring it. That matters:
two front doors with two implementations would be two half-built things, and the promises
this assignment makes (unattended, under 30 minutes, skips finished work, arithmetic exact,
tests pass with no model) are promises about control flow that a deterministic conductor
has to keep.

Do this:

1. Run `make doctor`. If it fails, stop and report the remedy it printed — do not try to
   work around an unauthenticated CLI.

2. Start the run in the background so it is not bounded by a tool timeout:

   ```
   nohup uv run python -m observe.cli run > /tmp/observe-run.log 2>&1 &
   ```

3. Poll `/tmp/observe-run.log` and `runs/<run_id>/run.jsonl` and narrate progress by stage.
   `run.jsonl` is append-only, one JSON object per event, with `stage`, `event`,
   `duration_ms` and `cache_hit` — that file *is* the run-log deliverable.

4. When it finishes, read `out/summary.json` and report:
   - the headline dollars per month **with its low–high range**, never the base alone;
   - how many opportunities were counted, and how many were quarantined or demoted;
   - the verified citation count and the tier breakdown;
   - the share of operational messages attributed to an identified process, which is the
     most important caveat on the headline and makes it a floor rather than a total;
   - anything in `out/quarantine.json` worth the reader's attention.

5. Say plainly whether `make verify` passed. If it did not, that is the headline, not a
   footnote.

Then offer `/verify-claims` for an adversarial check, and `make serve` for the dashboard.

Do **not** summarise the findings from memory or from the report's prose. Read the JSON.
