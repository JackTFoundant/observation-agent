"""Deterministic triage: what is worth a model's attention, and what must never get one.

Two jobs, both rule-based and both biased toward *precision over recall*. A message we
wrongly call noise is invisible to the final report by construction, which is the worst
failure mode available here, so anything unmatched defaults to operational. We would
rather spend tokens than lose evidence.

The second job is the more interesting one. `corpus/farmer-d/logistics/3221.` is 350 KB —
5% of the entire corpus in a single file, and 70× the next largest. Its body is a 3,600-row
nomination table, and that table is *arithmetically generated*: every numeric column is an
exact linear function of the row index. Reporting statistics from it would be reporting
statistics about a placeholder. So we prove it is generated, refuse to derive any estimate
from its rows, and publish the proof. The prose above the table is real and stays citable.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from fractions import Fraction

from observe.parse import ParsedMessage

CLASSIFIER_VERSION = "1.1.0"

# Sending addresses that are machinery, not people.
_AUTOMATED_SENDERS = re.compile(
    r"^(no\.?address|no-?reply|noreply|postmaster|mailer-daemon|enron\.announcements?"
    r"|announcements?|notification|listserv|majordomo|owner-|.*-request)@|@mailman\.",
    re.I,
)

_NOISE_SUBJECTS = (
    ("ooo", re.compile(r"\b(out of (the )?office|automatic reply|auto.?reply|vacation reply)\b", re.I)),
    ("newsletter", re.compile(
        r"\b(inside ut football|newsletter|daily digest|e-?speak|espeak|horoscope"
        r"|this week at enron|enron business|ebiz|weekly bulletin)\b", re.I)),
    ("social", re.compile(
        r"\b(lunch|happy hour|birthday|congratulations|baby shower|potluck|golf|tickets?"
        r"|come early be loud stay late|super ?bowl|march madness|fantasy (foot|basket)ball)\b", re.I)),
    ("marketplace", re.compile(r"\b(ebay item|for sale|fs:|wtb:|garage sale)\b", re.I)),
    ("undeliverable", re.compile(r"\b(undeliverable|delivery (failure|status notification)|returned mail)\b", re.I)),
)

_NOISE_BODY = (
    ("listserv", re.compile(r"\b(to unsubscribe|click here to unsubscribe|you are subscribed|manage your subscription)\b", re.I)),
    ("undeliverable", re.compile(r"^\s*Your message did not reach", re.I | re.M)),
)

# Vocabulary of the actual operating business. Presence of these is a strong positive
# signal and overrides a weak noise match.
_OPERATIONAL_TERMS = re.compile(
    r"\b(nomination|nom\b|nominate|scheduling|scheduled|imbalance|allocation|meter"
    r"|sitara|unify|tagg|enovate|pipeline|counterparty|confirm(ation)?s?|invoice|settlement"
    r"|volume|mmbtu|deal ticket|deal entry|month.?end|close|reconcil|capacity|tariff"
    r"|transwestern|hpl|ofo|park.?n.?ride|storage|estimate|actuals?|variance|flow date)\b",
    re.I,
)

_ATTACHMENT_ONLY = re.compile(r"\.(xls|xlsx|doc|docx|pdf|ppt|zip)\s*$", re.I)


@dataclass
class Classification:
    category: str            # "operational" | "noise" | "ack" | "automated"
    reason: str
    is_operational: bool
    operational_terms: int
    send_to_model: bool
    flags: list[str] = field(default_factory=list)


def classify(msg: ParsedMessage) -> Classification:
    """Decide whether a message reaches a model. Deterministic and auditable."""
    flags: list[str] = []
    subject = msg.subject or ""
    novel = msg.novel_text
    op_hits = len(_OPERATIONAL_TERMS.findall(f"{subject}\n{novel}"))

    if msg.sender and _AUTOMATED_SENDERS.search(msg.sender):
        flags.append("automated_sender")
    if "bulk_x_to" in msg.flags:
        flags.append("bulk_recipient_list")

    # An ack-only message is real work (someone read and forwarded something) but has no
    # novel text for a model to read. We count it deterministically instead.
    if msg.is_ack_only:
        return Classification("ack", "body is entirely quoted history", True, op_hits, False, flags)

    if not novel.strip():
        if _ATTACHMENT_ONLY.search(subject):
            return Classification(
                "ack", "attachment-only message: subject names a file, body empty",
                True, op_hits, False, flags + ["attachment_only"])
        return Classification("ack", "empty body", False, op_hits, False, flags + ["empty_body"])

    for name, pat in _NOISE_BODY:
        if pat.search(novel):
            return Classification("noise", f"body matches {name}", False, op_hits, False, flags)

    for name, pat in _NOISE_SUBJECTS:
        if pat.search(subject):
            # Precision guard: a strongly operational message whose subject happens to
            # mention lunch is still operational.
            if op_hits >= 3:
                flags.append(f"noise_subject_overridden:{name}")
                break
            return Classification("noise", f"subject matches {name}", False, op_hits, False, flags)

    if "automated_sender" in flags and op_hits < 2:
        return Classification("automated", "automated sender, no operational vocabulary",
                              False, op_hits, False, flags)

    return Classification("operational", "default: unmatched by any noise rule",
                          True, op_hits, True, flags)


# ---------------------------------------------------------------------------
# Generated-table detection
# ---------------------------------------------------------------------------

_NUMERIC = re.compile(r"^[-+]?[\d,]+(?:\.\d+)?$")
_LABELLED = re.compile(r"^([A-Z][A-Z0-9]*)-(\d+)$")


@dataclass
class TableFinding:
    """A structured block inside a message body, and whether it is machine-generated."""

    row_count: int
    column_count: int
    start: int                 # offset into the decoded body
    end: int
    generated: bool
    proof: list[str] = field(default_factory=list)
    distinct_values: dict[str, int] = field(default_factory=dict)

    @property
    def char_span(self) -> int:
        return self.end - self.start


def _split_row(line: str) -> list[str]:
    """Tokenize an aligned table row.

    Splitting on runs of two-or-more spaces rather than on any whitespace, because a
    column can contain a single internal space and a plain `split()` then shifts every
    column to its right. In this corpus the date column is written `1/ 1/2001` on some
    rows and `4/10/2001` on others, which makes a whitespace split produce 9 fields on
    some rows and 10 on others — enough to hide the structure completely.
    """
    parts = [p for p in re.split(r"\s{2,}", line.strip()) if p]
    return parts if len(parts) >= 4 else line.split()


def _is_table_row(parts: list[str], min_cols: int = 6) -> bool:
    if len(parts) < min_cols:
        return False
    structured = sum(1 for p in parts if _NUMERIC.match(p) or _LABELLED.match(p) or "/" in p)
    return structured >= max(4, len(parts) // 2)


def detect_table(body: str, min_rows: int = 200) -> TableFinding | None:
    """Find the largest contiguous run of table-shaped lines, if it is big enough to matter.

    `min_rows` is deliberately high. In this corpus the largest genuine table is 30 rows
    and the planted one is 3,600, so any threshold in between separates them cleanly and
    we are not at risk of mis-flagging real content.
    """
    lines = body.split("\n")
    offsets: list[int] = []
    pos = 0
    for line in lines:
        offsets.append(pos)
        pos += len(line) + 1

    best: tuple[int, int] | None = None
    run_start: int | None = None
    run_len = 0
    for i, line in enumerate(lines):
        if _is_table_row(_split_row(line)):
            if run_start is None:
                run_start = i
                run_len = 0
            run_len += 1
        else:
            if run_start is not None and (best is None or run_len > best[1] - best[0]):
                best = (run_start, run_start + run_len)
            run_start = None
            run_len = 0
    if run_start is not None and (best is None or run_len > best[1] - best[0]):
        best = (run_start, run_start + run_len)

    if best is None or (best[1] - best[0]) < min_rows:
        return None

    first, last = best
    rows = [_split_row(lines[i]) for i in range(first, last)]
    width = max(len(r) for r in rows)
    start = offsets[first]
    end = offsets[last - 1] + len(lines[last - 1])

    generated, proof, distinct = _prove_generated(rows, width)
    return TableFinding(
        row_count=len(rows), column_count=width, start=start, end=end,
        generated=generated, proof=proof, distinct_values=distinct,
    )


def _prove_generated(rows: list[list[str]], width: int) -> tuple[bool, list[str], dict[str, int]]:
    """Test whether every column is an exact function of the row index.

    Real operational data is not. Placeholder data generated by a loop is. Three
    signatures, and we require at least two *linear* columns plus three signals in total,
    so no single coincidence can trip it:

    * **linear** — a numeric column, or the numeric part of a labelled one like
      `METER-000007`, that is exactly `b + a*n` for every row with `a != 0`;
    * **periodic** — values repeating on a cycle far shorter than the row count, the
      signature of a generator walking a fixed list;
    * **constant** — one value throughout.
    """
    proof: list[str] = []
    distinct: dict[str, int] = {}
    linear_cols = 0
    periodic_cols = 0
    constant_cols = 0

    for col in range(width):
        values = [r[col] for r in rows if len(r) > col]
        if len(values) < len(rows) * 0.9:
            continue
        uniq = len(set(values))
        distinct[f"col{col}"] = uniq

        nums: list[Fraction] | None = []
        for v in values:
            if _NUMERIC.match(v):
                nums.append(Fraction(v.replace(",", "").lstrip("+")))
            else:
                m = _LABELLED.match(v)
                if m:
                    nums.append(Fraction(int(m.group(2))))
                else:
                    nums = None
                    break

        if nums and len(nums) >= 3:
            step = nums[1] - nums[0]
            if step != 0 and all(nums[i] - nums[i - 1] == step for i in range(1, len(nums))):
                linear_cols += 1
                proof.append(
                    f"column {col}: exactly arithmetic across all {len(nums)} rows — "
                    f"value = {nums[0]} + {step}*n, zero deviation"
                )
                continue
            modular = _modular_linear(nums)
            if modular is not None:
                stride, modulus, wraps = modular
                linear_cols += 1
                proof.append(
                    f"column {col}: modular arithmetic — value = {stride}*n mod {modulus} "
                    f"across all {len(nums)} rows ({wraps} wraps, and only "
                    f"{len({nums[i] - nums[i - 1] for i in range(1, len(nums))})} distinct "
                    f"first differences where real data would have thousands)"
                )
                continue

        if uniq == 1:
            constant_cols += 1
            proof.append(f"column {col}: constant {values[0]!r} for all {len(values)} rows")
            continue

        period = _find_period(values)
        if period is not None:
            periodic_cols += 1
            proof.append(
                f"column {col}: repeats with period {period} across {len(values)} rows "
                f"({len(values) // period} identical cycles)"
            )

    signals = linear_cols + periodic_cols + constant_cols
    generated = linear_cols >= 2 and signals >= 3
    if generated:
        proof.insert(0, (
            f"{linear_cols} of {width} columns are exact arithmetic sequences in the row "
            f"index, {periodic_cols} repeat on a fixed cycle and {constant_cols} are "
            f"constant. Real operational data is not shaped like this. Treated as "
            f"placeholder content: quotable as evidence of the format and of the workflow "
            f"around it, never used to derive a quantity."
        ))
    return generated, proof, distinct


def _modular_linear(nums: list[Fraction]) -> tuple[Fraction, Fraction, int] | None:
    """Detect `stride*n mod modulus`, the shape a counter takes when it is allowed to wrap.

    The tell is the first-difference distribution: a wrapping counter has exactly two
    distinct differences — the stride, and `stride - modulus` at each wrap — across
    thousands of rows, where a real measured quantity would have thousands of distinct
    differences. We require the stride to account for the overwhelming majority of steps
    and every remaining step to imply the *same* modulus.
    """
    diffs = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
    if len(diffs) < 50:
        return None
    counts: dict[Fraction, int] = {}
    for d in diffs:
        counts[d] = counts.get(d, 0) + 1
    if not 2 <= len(counts) <= 3:
        return None
    stride, stride_count = max(counts.items(), key=lambda kv: kv[1])
    if stride <= 0 or stride_count < len(diffs) * 0.9:
        return None

    moduli = {stride - d for d, _ in counts.items() if d != stride}
    if len(moduli) != 1:
        return None
    modulus = next(iter(moduli))
    if modulus <= stride:
        return None
    # Confirm the whole column really is the modular sequence.
    base = nums[0]
    for n, value in enumerate(nums):
        if (base + stride * n) % modulus != value % modulus:
            return None
    return stride, modulus, len(diffs) - stride_count


def _find_period(values: list[str]) -> int | None:
    """Smallest period with at least two full cycles such that the column repeats exactly."""
    n = len(values)
    if n < 4:
        return None
    first = values[0]
    for p in range(1, n // 2 + 1):
        if values[p] != first or n % p:
            continue
        if all(values[i] == values[i % p] for i in range(p, n)):
            return p
    return None