---
description: Adversarially attack the published report's citations, the way a sceptical reader would
---

Try to break the report. You are not confirming it.

This command deliberately sits *outside* the pipeline. It holds no correctness — nothing it
concludes can change what shipped — which is exactly why it is safe for a model to do the
work here, while the pipeline's own correctness lives in deterministic code.

1. Run `uv run python -m observe.cli verify --sample 12 --seed $RANDOM`. That prints twelve
   random citations with the `dd` and `sed` commands that reproduce each.

2. For each one, run **both** commands and compare the bytes to the published quote. They
   are two independent hand-checks of the same claim; if they disagree with each other,
   that is a finding on its own.

3. Then attack the part deterministic code cannot check: **does the quote actually support
   the claim it was attached to?** Open the source file with `Read` and read *around* the
   quote — the whole message, and the quoted history beneath it. Ask:

   - Is the quote load-bearing, or merely adjacent to the claim?
   - Is it lifted out of a context that inverts its meaning? A line inside a
     `-----Original Message-----` block was written by someone else, possibly years earlier.
   - Is the speaker describing what happens, or proposing what should happen? "We should
     start confirming these in the system" is evidence of a *gap*, not of a practice.
   - Does the citation's date and sender match the process it is attached to?

4. Pick two opportunities and check their *counts*, not their quotes. Take
   `derivation.measured.instances` from `out/opportunities/<id>.json`, then count the actual
   distinct threads yourself with `grep`/`Read` over the member messages. A count that
   cannot be reproduced is a more serious defect than a weak quote.

5. Report only what you could substantiate:
   - citations that failed byte verification (there should be none — say so if so);
   - citations that verify but do **not** support their claim;
   - counts you could not reproduce;
   - anything that reads as overstated relative to its evidence.

Be specific and quote what you found. "Citation cit_ab12 verifies, but the line is inside a
forwarded 1999 message from a third party and is attached to a claim about 2001 practice" is
useful. "Evidence looks solid" is not — if you genuinely found nothing, say which twelve you
checked and how, so the reader knows what was and was not examined.
