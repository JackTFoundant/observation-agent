"""Quoted-printable decoding that remembers where every output character came from.

Every citation this system publishes is a byte range into a raw corpus file. A quote is
often verbatim in the *decoded* body but absent from the raw bytes, because the raw bytes
carry `=20` soft-encodings and `=\\n` soft line breaks. So we cannot use `quopri`: we need
the decode *and* a map back to raw byte space.

Two invariants hold everywhere downstream:

1. Raw text is `raw_bytes.decode("latin-1")`. That is lossless and one character is one
   byte, so a character offset into raw text *is* a byte offset into the file.
2. Decoded text is likewise a latin-1 view of the decoded byte sequence, so the same
   "one char is one byte" property holds on both sides of the map.

The map is a list of spans rather than a per-character index because a 350 KB message
would otherwise cost a 350 K-element list. Identity runs are long, and only `=XX`, soft
line breaks and CRLF pairs break one.

CRLF collapsing happens in the same pass as the escape decoding rather than as a second
pass over the result. Composing two offset maps is possible but loses granularity wherever
one map's span straddles several of the other's, which silently mis-anchors quotes; one
pass has no such failure mode.
"""

from __future__ import annotations

from bisect import bisect_right
from dataclasses import dataclass

HEXDIGITS = frozenset("0123456789abcdefABCDEF")


@dataclass(frozen=True)
class Span:
    """One run of the decode. `out_len == raw_len` for untouched text."""

    out_start: int
    out_len: int
    raw_start: int
    raw_len: int

    @property
    def out_end(self) -> int:
        return self.out_start + self.out_len

    @property
    def raw_end(self) -> int:
        return self.raw_start + self.raw_len

    @property
    def is_identity(self) -> bool:
        return self.out_len == self.raw_len

    def as_tuple(self) -> tuple[int, int, int, int]:
        return (self.out_start, self.out_len, self.raw_start, self.raw_len)


class OffsetMap:
    """Maps decoded-text offsets back to raw-file byte offsets.

    `raw_base` lets a body be decoded on its own while still reporting offsets into the
    whole file: the body starts at some offset and the map carries it.
    """

    __slots__ = ("spans", "_out_starts", "out_len", "raw_base")

    def __init__(self, spans: list[Span], out_len: int, raw_base: int = 0):
        self.spans = spans or [Span(0, 0, 0, 0)]
        self.out_len = out_len
        self.raw_base = raw_base
        self._out_starts = [s.out_start for s in self.spans]

    @classmethod
    def identity(cls, length: int, raw_base: int = 0) -> "OffsetMap":
        return cls([Span(0, length, 0, length)], length, raw_base)

    @classmethod
    def from_tuples(cls, tuples, out_len: int, raw_base: int = 0) -> "OffsetMap":
        return cls([Span(*t) for t in tuples], out_len, raw_base)

    def to_raw(self, out_start: int, out_end: int) -> tuple[int, int]:
        """Map a decoded half-open range to a raw half-open byte range.

        Snaps outward to span boundaries, so a range beginning inside a `=20` still yields
        a raw range that fully contains the bytes that produced it. Never returns a range
        narrower than the characters asked for.
        """
        out_start = max(0, min(out_start, self.out_len))
        out_end = max(out_start, min(out_end, self.out_len))

        start_span = self._span_covering(out_start)
        if start_span.is_identity:
            raw_start = start_span.raw_start + (out_start - start_span.out_start)
        else:
            raw_start = start_span.raw_start

        if out_end == out_start:
            return (self.raw_base + raw_start, self.raw_base + raw_start)

        end_span = self._span_covering(out_end - 1)
        if end_span.is_identity:
            raw_end = end_span.raw_start + (out_end - end_span.out_start)
        else:
            raw_end = end_span.raw_end

        return (self.raw_base + raw_start, self.raw_base + max(raw_end, raw_start))

    def _span_covering(self, out_pos: int) -> Span:
        idx = bisect_right(self._out_starts, out_pos) - 1
        if idx < 0:
            return self.spans[0]
        # Zero-width output spans (dropped soft line breaks) share an out_start with the
        # span that follows; walk forward so we anchor on text rather than on a break.
        while self.spans[idx].out_len == 0 and idx + 1 < len(self.spans):
            idx += 1
        return self.spans[idx]

    def serializable(self) -> list[tuple[int, int, int, int]]:
        return [s.as_tuple() for s in self.spans]


class _SpanWriter:
    """Accumulates spans, merging contiguous identity runs so the map stays compact."""

    __slots__ = ("spans",)

    def __init__(self) -> None:
        self.spans: list[Span] = []

    def add(self, out_start: int, out_len: int, raw_start: int, raw_len: int) -> None:
        if self.spans and out_len == raw_len and out_len:
            prev = self.spans[-1]
            if prev.is_identity and prev.out_end == out_start and prev.raw_end == raw_start:
                self.spans[-1] = Span(
                    prev.out_start, prev.out_len + out_len, prev.raw_start, prev.raw_len + raw_len
                )
                return
        self.spans.append(Span(out_start, out_len, raw_start, raw_len))


def decode_qp(raw: str, raw_base: int = 0, collapse_crlf: bool = True) -> tuple[str, OffsetMap]:
    """Decode quoted-printable text, returning the decoded text and an offset map.

    Deliberately lenient, because this corpus came off a real 2002 mail server. A bare `=`
    not followed by two hex digits or a line break is kept as a literal `=` rather than
    raising, and that includes a `=` at the very end of the input: the spec would call
    that a soft break, but keeping it literal makes the decode stable under slicing, which
    is what the citation layer needs. Being strict here would lose real messages.
    """
    out: list[str] = []
    writer = _SpanWriter()
    out_pos = 0
    i = 0
    n = len(raw)
    run_raw = run_out = run_len = 0

    def flush() -> None:
        nonlocal run_len
        if run_len:
            writer.add(run_out, run_len, run_raw, run_len)
            run_len = 0

    def literal(ch: str, raw_idx: int) -> None:
        nonlocal run_len, run_raw, run_out, out_pos
        if run_len == 0:
            run_raw = raw_idx
            run_out = out_pos
        out.append(ch)
        run_len += 1
        out_pos += 1

    while i < n:
        ch = raw[i]

        if ch == "\r" and collapse_crlf and i + 1 < n and raw[i + 1] == "\n":
            flush()
            out.append("\n")
            writer.add(out_pos, 1, i, 2)
            out_pos += 1
            i += 2
            continue

        if ch != "=":
            literal(ch, i)
            i += 1
            continue

        # A '=' introduces either a soft line break or a hex escape.
        if i + 2 < n and raw[i + 1] == "\r" and raw[i + 2] == "\n":
            flush()
            writer.add(out_pos, 0, i, 3)
            i += 3
            continue
        if i + 1 < n and raw[i + 1] == "\n":
            flush()
            writer.add(out_pos, 0, i, 2)
            i += 2
            continue
        if i + 2 < n and raw[i + 1] in HEXDIGITS and raw[i + 2] in HEXDIGITS:
            flush()
            decoded = chr(int(raw[i + 1:i + 3], 16))
            if decoded == "\r" and collapse_crlf:
                # `=0D=0A` should collapse like a literal CRLF pair.
                if raw[i + 3:i + 6].lower() == "=0a":
                    out.append("\n")
                    writer.add(out_pos, 1, i, 6)
                    out_pos += 1
                    i += 6
                    continue
            out.append(decoded)
            writer.add(out_pos, 1, i, 3)
            out_pos += 1
            i += 3
            continue

        # Not a valid escape. Keep the '=' as literal text.
        literal(ch, i)
        i += 1

    flush()
    return "".join(out), OffsetMap(writer.spans, out_pos, raw_base)


def identity_decode(raw: str, raw_base: int = 0, collapse_crlf: bool = True) -> tuple[str, OffsetMap]:
    """Pass-through for 7bit/8bit bodies, so callers get one uniform interface.

    Still collapses CRLF, because line-ending noise otherwise leaks into every quote
    comparison downstream. When there are no CRLFs this is a single-span map.
    """
    if not collapse_crlf or "\r\n" not in raw:
        return raw, OffsetMap.identity(len(raw), raw_base)

    out: list[str] = []
    writer = _SpanWriter()
    out_pos = 0
    i = 0
    n = len(raw)
    run_raw = run_out = run_len = 0

    def flush() -> None:
        nonlocal run_len
        if run_len:
            writer.add(run_out, run_len, run_raw, run_len)
            run_len = 0

    while i < n:
        if raw[i] == "\r" and i + 1 < n and raw[i + 1] == "\n":
            flush()
            out.append("\n")
            writer.add(out_pos, 1, i, 2)
            out_pos += 1
            i += 2
            continue
        if run_len == 0:
            run_raw = i
            run_out = out_pos
        out.append(raw[i])
        run_len += 1
        out_pos += 1
        i += 1
    flush()
    return "".join(out), OffsetMap(writer.spans, out_pos, raw_base)


def decode_body(
    raw: str, transfer_encoding: str | None, raw_base: int = 0
) -> tuple[str, OffsetMap]:
    """Dispatch on the message's Content-Transfer-Encoding.

    base64 is deliberately *not* decoded: a base64 body is an attachment payload, not
    prose a human typed, so there is nothing in it worth quoting. Returning it untouched
    keeps offsets honest and lets the noise classifier drop it.
    """
    enc = (transfer_encoding or "").strip().lower()
    if enc == "quoted-printable":
        return decode_qp(raw, raw_base)
    return identity_decode(raw, raw_base)
