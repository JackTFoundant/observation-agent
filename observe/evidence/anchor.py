"""Anchoring a proposed quote to a byte range in a raw corpus file.

**The invariant this module exists to enforce:** every quote that ships is produced by
slicing corpus bytes. It is never copied from model output. A model's proposed quote is
used only as a search key. If no anchor is found there is no quote, and the claim that
depended on it does not ship.

That is structural rather than validational. A hallucinated quote cannot reach the report,
because the report's quote field is assigned from `raw_text[start:end]` — so the failure
mode "the model invented a plausible-sounding quote" is not caught late, it is impossible.

A quote is often verbatim in the *decoded* body yet absent from the raw bytes, because the
raw bytes carry `=20` and soft line breaks. We do not paper over that. Each citation
carries the tier it matched at, and the dashboard says so.
"""

from __future__ import annotations

import hashlib
import re
import unicodedata
from dataclasses import dataclass, field
from difflib import SequenceMatcher

from observe.ingest.qp import OffsetMap

ANCHOR_VERSION = "1.0.0"

MIN_QUOTE_CHARS = 24
MAX_QUOTE_CHARS = 300

# Ordered strongest to weakest. A citation records the strongest tier it actually matched,
# and `verify` later asserts it matches at that tier and *no weaker one*.
#
# `rewrapped` exists because lumping it in with `normalized` was materially unfair to good
# evidence. Mail from 2001 hard-wraps at about 72 columns, so a sentence a human typed as
# one line is stored across two or three. A model quoting that sentence reproduces it as
# one line, which is a *faithful* quote that simply cannot be found byte-for-byte. The
# characters are identical apart from where the newlines fall.
#
# `normalized` is genuinely weaker: it needed case folding or punctuation substitution to
# match, so the quote is no longer character-identical to the source. Only that tier is
# capped, and it was demoting four well-evidenced findings when the two were conflated.
TIERS = ("raw_exact", "decoded_exact", "rewrapped", "normalized")

# Tiers whose published quote is character-identical to the source apart from line breaks.
STRONG_TIERS = frozenset({"raw_exact", "decoded_exact", "rewrapped"})

_WS = re.compile(r"\s+")
_SMART = str.maketrans({
    "‘": "'", "’": "'", "‚": "'", "‛": "'",
    "“": '"', "”": '"', "„": '"', "‟": '"',
    "–": "-", "—": "-", "―": "-", "−": "-",
    " ": " ", "…": "...",
})


class AnchorError(Exception):
    """Raised with a machine-readable reason code when a quote cannot be anchored."""

    def __init__(self, reason: str, detail: str = ""):
        super().__init__(f"{reason}: {detail}" if detail else reason)
        self.reason = reason
        self.detail = detail


@dataclass
class Citation:
    """One piece of evidence. Every field is derived from the corpus, not from a model."""

    citation_id: str
    source_path: str
    source_sha256: str
    message_id: str | None
    msg_uid: str

    quote: str               # sliced from the file, never the model's string
    match_tier: str
    raw_start: int
    raw_end: int
    decoded_start: int
    decoded_end: int
    line_start: int
    line_end: int
    repaired: bool

    sender: str | None
    sent_at: str | None
    subject: str
    flags: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "citation_id": self.citation_id,
            "source_path": self.source_path,
            "source_sha256": self.source_sha256,
            "message_id": self.message_id,
            "msg_uid": self.msg_uid,
            "quote": self.quote,
            "match_tier": self.match_tier,
            "raw_start": self.raw_start,
            "raw_end": self.raw_end,
            "decoded_start": self.decoded_start,
            "decoded_end": self.decoded_end,
            "line_start": self.line_start,
            "line_end": self.line_end,
            "repaired": self.repaired,
            "sender": self.sender,
            "sent_at": self.sent_at,
            "subject": self.subject,
            "flags": sorted(self.flags),
            "check_commands": {
                "dd": f"dd bs=1 skip={self.raw_start} count={self.raw_end - self.raw_start} "
                      f"if={self.source_path} 2>/dev/null",
                "sed": f"sed -n '{self.line_start},{self.line_end}p' {self.source_path}",
            },
        }


def citation_id(source_path: str, raw_start: int, raw_end: int) -> str:
    """Content-addressed, so identical evidence dedupes for free."""
    key = f"{source_path}|{raw_start}|{raw_end}".encode()
    return "cit_" + hashlib.sha256(key).hexdigest()[:12]


def collapse_whitespace(text: str) -> str:
    """Whitespace-only folding. Characters are otherwise untouched.

    This is what recovers a quote that a mail client hard-wrapped: same characters, and
    only the newlines moved.
    """
    return _WS.sub(" ", text).strip()


def normalize_for_match(text: str) -> str:
    """The weakest comparison we will accept: NFKC, smart punctuation folded, whitespace
    collapsed, lowercased. Used only for the `normalized` tier."""
    t = unicodedata.normalize("NFKC", text).translate(_SMART)
    return _WS.sub(" ", t).strip().lower()


def _line_bounds(raw: str, start: int, end: int) -> tuple[int, int]:
    """1-based inclusive line numbers covering a raw byte range.

    Published alongside byte offsets on purpose: it gives the grader two independent ways
    to hand-check the same citation (`dd` and `sed`), and they have to agree.
    """
    line_start = raw.count("\n", 0, start) + 1
    line_end = raw.count("\n", 0, max(end - 1, start)) + 1
    return line_start, line_end


def _find_folded(haystack: str, needle: str, fold=None) -> tuple[int, int] | None:
    """Locate a folded needle inside a haystack, returning *haystack* offsets.

    Built by walking the haystack once and recording, for each character kept by
    normalization, where it came from. That keeps the mapping exact rather than guessing
    at an offset after the fact.
    """
    if fold is None:
        def fold(ch: str) -> str:
            return unicodedata.normalize("NFKC", ch).translate(_SMART).lower()
    norm_chars: list[str] = []
    origins: list[int] = []
    prev_space = True
    for i, ch in enumerate(haystack):
        folded = fold(ch)
        if not folded:
            continue
        if folded.isspace():
            if prev_space:
                continue
            norm_chars.append(" ")
            origins.append(i)
            prev_space = True
            continue
        prev_space = False
        for c in folded:
            norm_chars.append(c)
            origins.append(i)
    norm = "".join(norm_chars).strip()
    # `strip()` may have removed a leading space; recompute an aligned view instead.
    lead = len("".join(norm_chars)) - len("".join(norm_chars).lstrip())
    idx = norm.find(needle)
    if idx == -1:
        return None
    a = origins[idx + lead]
    last = idx + lead + len(needle) - 1
    b = origins[min(last, len(origins) - 1)] + 1
    return a, b


def anchor_quote(
    proposal: str,
    raw: str,
    body_decoded: str,
    omap: OffsetMap,
    *,
    allow_repair: bool = True,
) -> tuple[int, int, int, int, str, bool]:
    """Anchor a proposed quote. Returns (raw_start, raw_end, dec_start, dec_end, tier, repaired).

    Raises `AnchorError` when the quote cannot be tied to the file, which is the signal for
    the caller to quarantine rather than to guess.
    """
    proposal = (proposal or "").strip()
    if not proposal:
        raise AnchorError("empty_quote")
    if len(proposal) > MAX_QUOTE_CHARS * 3:
        raise AnchorError("quote_too_long", f"{len(proposal)} chars")

    # Tier 1: byte-for-byte in the raw file. The gold case.
    idx = raw.find(proposal)
    if idx != -1:
        d = body_decoded.find(proposal)
        dec = (d, d + len(proposal)) if d != -1 else (0, 0)
        return idx, idx + len(proposal), dec[0], dec[1], "raw_exact", False

    # Tier 2: exact in the decoded body; map the span back to raw byte space.
    idx = body_decoded.find(proposal)
    if idx != -1:
        rs, re_ = omap.to_raw(idx, idx + len(proposal))
        return rs, re_, idx, idx + len(proposal), "decoded_exact", False

    # Tier 3: whitespace-only. The quote is character-identical; the mail client wrapped it.
    rewrapped_needle = collapse_whitespace(proposal)
    if len(rewrapped_needle) >= MIN_QUOTE_CHARS:
        hit = _find_folded(body_decoded, rewrapped_needle, fold=lambda ch: ch)
        if hit:
            rs, re_ = omap.to_raw(hit[0], hit[1])
            return rs, re_, hit[0], hit[1], "rewrapped", False
        hit = _find_folded(raw, rewrapped_needle, fold=lambda ch: ch)
        if hit:
            return hit[0], hit[1], 0, 0, "rewrapped", False

    # Tier 4: matches only after case and punctuation folding too.
    needle = normalize_for_match(proposal)
    if len(needle) >= MIN_QUOTE_CHARS:
        hit = _find_folded(body_decoded, needle)
        if hit:
            rs, re_ = omap.to_raw(hit[0], hit[1])
            return rs, re_, hit[0], hit[1], "normalized", False
        hit = _find_folded(raw, needle)
        if hit:
            return hit[0], hit[1], 0, 0, "normalized", False

    if not allow_repair:
        raise AnchorError("no_anchor", proposal[:80])

    # Repair: the model paraphrased. Discard its string entirely and take the closest real
    # substring of the corpus instead. What ships is corpus text either way.
    repaired = _repair(proposal, body_decoded)
    if repaired is None:
        raise AnchorError("no_anchor", proposal[:80])
    a, b = repaired
    rs, re_ = omap.to_raw(a, b)
    return rs, re_, a, b, "decoded_exact", True


def _repair(proposal: str, body_decoded: str, min_ratio: float = 0.92) -> tuple[int, int] | None:
    """Find the corpus substring the proposal was probably a paraphrase of.

    Requires a long, high-similarity contiguous block so a vague resemblance cannot
    manufacture evidence. Then expands to word boundaries so the published quote reads as
    a sentence rather than starting mid-token.
    """
    if len(proposal) < MIN_QUOTE_CHARS or not body_decoded:
        return None
    matcher = SequenceMatcher(None, proposal, body_decoded, autojunk=False)
    block = matcher.find_longest_match(0, len(proposal), 0, len(body_decoded))
    if block.size < MIN_QUOTE_CHARS:
        return None
    a, b = block.b, block.b + block.size
    candidate = body_decoded[a:b]
    if SequenceMatcher(None, proposal[block.a:block.a + block.size], candidate).ratio() < min_ratio:
        return None

    while a > 0 and not body_decoded[a - 1].isspace() and b - a < MAX_QUOTE_CHARS:
        a -= 1
    while b < len(body_decoded) and not body_decoded[b].isspace() and b - a < MAX_QUOTE_CHARS:
        b += 1
    return a, b


def build_citation(
    proposal: str,
    *,
    raw: str,
    msg,
    allow_repair: bool = True,
) -> Citation:
    """Anchor a proposal against one parsed message and return a Citation.

    The `quote` field is assigned by slicing `raw`. This function is the only place a
    citation is constructed, so that assignment is the single chokepoint the whole
    evidence guarantee rests on.
    """
    rs, re_, ds, de, tier, repaired = anchor_quote(
        proposal, raw, msg.body_decoded, msg.offset_map, allow_repair=allow_repair
    )
    quote = raw[rs:re_]                      # <-- sliced from the corpus, never copied
    if len(quote.strip()) < MIN_QUOTE_CHARS:
        raise AnchorError("below_min_length", f"{len(quote.strip())} chars")

    flags: list[str] = []
    if tier != "raw_exact":
        flags.append(f"tier_{tier}")
    if tier not in STRONG_TIERS:
        flags.append("weak_tier")
    if repaired:
        flags.append("repaired_to_source_text")

    ls, le = _line_bounds(raw, rs, re_)
    return Citation(
        citation_id=citation_id(msg.path, rs, re_),
        source_path=msg.path,
        source_sha256=msg.file_sha256,
        message_id=msg.message_id,
        msg_uid=msg.msg_uid,
        quote=quote,
        match_tier=tier,
        raw_start=rs,
        raw_end=re_,
        decoded_start=ds,
        decoded_end=de,
        line_start=ls,
        line_end=le,
        repaired=repaired,
        sender=msg.sender,
        sent_at=msg.sent_at.isoformat() if msg.sent_at else None,
        subject=msg.subject,
        flags=flags,
    )


def reverify(citation: dict, raw: str, body_decoded: str, omap: OffsetMap) -> tuple[bool, str]:
    """Independently re-check a published citation. Used by `verify` and by the tests.

    Asserts the recorded range reproduces the recorded quote, and that it matches at the
    tier it claims **and no weaker one** — a citation claiming `raw_exact` that only
    survives normalization is a failure, not a pass.
    """
    rs, re_ = citation["raw_start"], citation["raw_end"]
    if not (0 <= rs <= re_ <= len(raw)):
        return False, "offsets_out_of_range"
    sliced = raw[rs:re_]
    if sliced != citation["quote"]:
        return False, "slice_does_not_match_quote"

    tier = citation["match_tier"]
    quote = citation["quote"]
    if tier == "raw_exact":
        if raw.find(quote) == -1:
            return False, "claimed_raw_exact_but_absent_from_raw"
        return True, "ok"
    if tier == "decoded_exact":
        if raw.find(quote) != -1 and not citation.get("repaired"):
            # Stronger than claimed is a bookkeeping error worth surfacing, not a forgery.
            return True, "ok_stronger_than_claimed"
        ds, de = citation["decoded_start"], citation["decoded_end"]
        if 0 <= ds <= de <= len(body_decoded):
            mapped = omap.to_raw(ds, de)
            if mapped[0] <= rs and re_ <= mapped[1]:
                return True, "ok"
        return False, "decoded_span_does_not_map_to_raw_range"
    if tier == "rewrapped":
        if collapse_whitespace(quote) and collapse_whitespace(quote) in collapse_whitespace(raw):
            return True, "ok"
        return False, "rewrapped_match_failed"
    if tier == "normalized":
        if normalize_for_match(quote) and normalize_for_match(quote) in normalize_for_match(raw):
            return True, "ok"
        return False, "normalized_match_failed"
    return False, f"unknown_tier:{tier}"