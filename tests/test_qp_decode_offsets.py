"""The offset map is load-bearing: every published citation is a byte range it produced.

The property that matters is not "decode is correct" but "the map never lies": for any
decoded substring, the raw range it maps to must fully contain the bytes that produced it.
"""

from __future__ import annotations

import quopri

from hypothesis import given, settings
from hypothesis import strategies as st

from observe.ingest.qp import OffsetMap, decode_body, decode_qp, identity_decode


def test_identity_text_is_unchanged_and_maps_one_to_one():
    raw = "Please confirm the nomination change for HPL by 9:00 am tomorrow."
    out, omap = decode_qp(raw)
    assert out == raw
    start = raw.index("nomination")
    rs, re_ = omap.to_raw(start, start + len("nomination"))
    assert raw[rs:re_] == "nomination"


def test_soft_line_break_is_dropped_and_span_maps_across_it():
    raw = "Total East deliveries averaged 452 MMBtu/d=\nfor the week."
    out, omap = decode_qp(raw)
    assert out == "Total East deliveries averaged 452 MMBtu/dfor the week."
    # A quote spanning the dropped break must map to a raw range containing the break.
    start = out.index("452")
    end = out.index("for the week") + len("for the week")
    rs, re_ = omap.to_raw(start, end)
    assert "=\n" in raw[rs:re_]
    assert raw[rs:re_].startswith("452")
    assert raw[rs:re_].endswith("for the week")


def test_hex_escape_decodes_and_maps_to_three_raw_bytes():
    raw = "Enron=20North=20America"
    out, omap = decode_qp(raw)
    assert out == "Enron North America"
    start = out.index("North")
    rs, re_ = omap.to_raw(start, start + len("North"))
    assert raw[rs:re_] == "North"
    # The space itself occupies three raw bytes.
    sp = out.index(" ")
    rs, re_ = omap.to_raw(sp, sp + 1)
    assert raw[rs:re_] == "=20"


def test_tab_escape_from_real_corpus_shape():
    raw = "=09Enron North America Corp.=20\n=09From:  Eric Bass"
    out, _ = decode_qp(raw)
    assert out == "\tEnron North America Corp. \n\tFrom:  Eric Bass"


def test_bare_equals_is_kept_literal_rather_than_raising():
    # Real 2002 mail. A strict decoder would lose the message.
    raw = "variance = 580 on every row"
    out, omap = decode_qp(raw)
    assert out == raw
    rs, re_ = omap.to_raw(0, len(raw))
    assert raw[rs:re_] == raw


def test_trailing_equals_is_kept_literal_so_the_decode_is_slice_stable():
    # The spec would call this a soft break, but dropping it makes decoding unstable under
    # slicing, which breaks re-verification of a citation that ends near it.
    raw = "confirm back to me by close of business Thursday="
    out, omap = decode_qp(raw)
    assert out == raw
    assert omap.to_raw(0, len(out)) == (0, len(raw))


def test_empty_input():
    out, omap = decode_qp("")
    assert out == ""
    assert omap.to_raw(0, 0) == (0, 0)


def test_raw_base_offsets_report_into_the_whole_file():
    raw = "pull your own meters out of this"
    _, omap = decode_qp(raw, raw_base=1000)
    rs, re_ = omap.to_raw(0, len(raw))
    assert (rs, re_) == (1000, 1000 + len(raw))


def test_identity_decode_matches_decode_qp_on_plain_text():
    raw = "Here is a list of the 66 physical deals that were zeroed out"
    a, ma = identity_decode(raw)
    b, mb = decode_qp(raw)
    assert a == b
    assert ma.to_raw(5, 20) == mb.to_raw(5, 20)


def test_crlf_is_collapsed_in_the_same_pass_and_the_map_stays_correct():
    raw = "line one\r\nline two\r\nline three"
    out, omap = decode_qp(raw)
    assert out == "line one\nline two\nline three"
    start = out.index("line two")
    rs, re_ = omap.to_raw(start, start + len("line two"))
    assert raw[rs:re_] == "line two"


def test_crlf_collapse_interleaved_with_qp_escapes():
    # The case that made a two-pass, map-composing implementation mis-anchor: a span in
    # the newline pass straddles several spans of the escape pass.
    raw = "Transwestern=20deliveries\r\nwere=20933=20MMBtu/d"
    out, omap = decode_qp(raw)
    assert out == "Transwestern deliveries\nwere 933 MMBtu/d"
    for needle in ("933", "MMBtu/d", "were", "deliveries", "Transwestern"):
        start = out.index(needle)
        rs, re_ = omap.to_raw(start, start + len(needle))
        assert raw[rs:re_] == needle, needle


def test_crlf_collapse_in_identity_path():
    raw = "Team,\r\n\r\nPasting the full month position below"
    out, omap = identity_decode(raw)
    assert out == "Team,\n\nPasting the full month position below"
    start = out.index("Pasting")
    rs, re_ = omap.to_raw(start, start + len("Pasting the full month position below"))
    assert raw[rs:re_] == "Pasting the full month position below"


def test_encoded_crlf_pair_collapses():
    out, _ = decode_qp("first=0D=0Asecond")
    assert out == "first\nsecond"


def test_decode_body_dispatches_on_transfer_encoding():
    raw = "Enron=20North"
    assert decode_body(raw, "quoted-printable")[0] == "Enron North"
    assert decode_body(raw, "7bit")[0] == raw
    assert decode_body(raw, None)[0] == raw
    # base64 is left untouched on purpose: an attachment payload has nothing quotable.
    assert decode_body("VGhpcyBpcyBhbiBhdHRhY2htZW50", "base64")[0] == "VGhpcyBpcyBhbiBhdHRhY2htZW50"


def test_offset_map_identity_constructor():
    omap = OffsetMap.identity(10, raw_base=7)
    assert omap.to_raw(2, 5) == (9, 12)


# ---------------------------------------------------------------------------
# The property test. This is the one that actually protects the citation layer.
# ---------------------------------------------------------------------------

qp_fragments = st.sampled_from(
    [
        "=20", "=09", "=3D", "=\n", "=\r\n", "=E9", "=2E",
        "hello", " world", "\n", "\r\n", "Enron", "HPL", "nomination",
        "=", "==", "=2", "=ZZ", "\t", "452 MMBtu/d", ".", "confirm",
    ]
)


@given(st.lists(qp_fragments, min_size=0, max_size=60))
@settings(max_examples=400, deadline=None)
def test_property_decoded_substring_always_maps_to_containing_raw_range(fragments):
    raw = "".join(fragments)
    out, omap = decode_qp(raw)

    # The map covers exactly the decoded text.
    assert omap.out_len == len(out)

    # Spans tile the output in order, without gaps or overlaps.
    cursor = 0
    for span in omap.spans:
        assert span.out_start == cursor
        cursor += span.out_len
    assert cursor == len(out)

    # For every decoded window, re-slicing the raw text at the mapped range must recover
    # a string that still decodes to something containing the window. That is the
    # guarantee the dashboard highlight and `verify` both depend on.
    for start in range(0, len(out), max(1, len(out) // 9 or 1)):
        for width in (1, 5, 17):
            end = min(start + width, len(out))
            if end <= start:
                continue
            rs, re_ = omap.to_raw(start, end)
            assert 0 <= rs <= re_ <= len(raw)
            redecoded, _ = decode_qp(raw[rs:re_])
            assert out[start:end] in redecoded, (
                f"window {out[start:end]!r} not recoverable from raw[{rs}:{re_}]={raw[rs:re_]!r}"
            )


@given(st.lists(qp_fragments, min_size=0, max_size=40))
@settings(max_examples=200, deadline=None)
def test_property_decode_agrees_with_quopri_on_wellformed_input(fragments):
    """Where `quopri` and we both apply, we must agree. Divergence is only permitted on
    the malformed escapes we deliberately keep literal."""
    raw = "".join(fragments)
    if any(bad in raw for bad in ("=ZZ", "==", "=2\n")) or raw.endswith(("=", "=2")):
        return
    # CRLF collapsing is ours, not quopri's, so compare the escape logic alone.
    mine, _ = decode_qp(raw, collapse_crlf=False)
    theirs = quopri.decodestring(raw.encode("latin-1")).decode("latin-1")
    assert mine == theirs


@given(st.lists(qp_fragments, min_size=1, max_size=40), st.integers(min_value=0, max_value=5000))
@settings(max_examples=150, deadline=None)
def test_property_raw_base_is_a_pure_shift(fragments, base):
    raw = "".join(fragments)
    _, m0 = decode_qp(raw)
    _, mb = decode_qp(raw, raw_base=base)
    a = m0.to_raw(0, m0.out_len)
    b = mb.to_raw(0, mb.out_len)
    assert (b[0] - base, b[1] - base) == a
