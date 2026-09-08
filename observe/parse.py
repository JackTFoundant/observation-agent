"""Parsing raw Enron export files into messages, with byte offsets preserved throughout.

The one rule that shapes this module: **offsets must survive**. Every downstream citation
is a byte range into the original file, so nothing here is allowed to reflow, re-wrap or
re-encode text without recording where it went. That is why the body is located by index
into the raw text rather than handed to `email`'s payload machinery, which returns strings
with no provenance.

Header parsing itself *is* delegated to the stdlib. Tab-continued folded headers are the
kind of thing a hand-rolled parser gets 95% right and then quietly mangles.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from email.parser import HeaderParser
from email.utils import getaddresses, parsedate_to_datetime
from pathlib import Path

from observe.ingest.qp import OffsetMap, decode_body

PARSER_VERSION = "1.2.0"

# The body of a reply usually restates the whole thread. Only the text this author
# actually typed is worth showing a model, so we cut at the earliest trailer marker.
# Ordered by specificity; every pattern is anchored to a line start.
_TRAILER_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("outlook_original", re.compile(r"^[ \t]*-{2,}[ \t]*Original Message[ \t]*-{2,}", re.M | re.I)),
    ("outlook_reply_sep", re.compile(r"^[ \t]*-{4,}[ \t]*Forwarded Message[ \t]*-{4,}", re.M | re.I)),
    ("lotus_forward", re.compile(r"^-{4,}[ \t]*Forwarded by .{0,120}?-{4,}[ \t]*$", re.M)),
    ("lotus_header", re.compile(r"^[ \t]*={4,}[ \t]*$\n^[ \t]*Forwarded", re.M)),
    # Outlook's quoted block without the dashes: a From: line immediately followed by Sent:.
    ("outlook_from_sent", re.compile(r"^[ \t]*From:[ \t].*\r?\n[ \t]*(Sent|To|Date):[ \t]", re.M)),
    # Lotus Notes: a name line, then a date/time line, then To:/cc:.
    ("lotus_notes_block", re.compile(
        r"^[A-Z][A-Za-z.\-' ]{2,60}\r?\n\d{1,2}/\d{1,2}/\d{2,4}[ \t]+\d{1,2}:\d{2}[ \t]*(AM|PM)?\r?\n[ \t]*(To|cc):",
        re.M,
    )),
    ("underscore_rule", re.compile(r"^[ \t]*_{20,}[ \t]*$", re.M)),
    ("quoted_run", re.compile(r"^(?:>[^\n]*\r?\n){3,}", re.M)),
    ("enron_disclaimer", re.compile(
        r"^\*+\s*$\n^.{0,40}This (e-?mail|message).{0,200}(confidential|privileged)", re.M | re.I)),
)

_SUBJECT_PREFIX = re.compile(r"^(?:\s*(?:re|fw|fwd|aw|sv|tr)\s*(?:\[\d+\])?\s*:)+", re.I)
_SUBJECT_NOISE = re.compile(r"[\d/\-–—.,()\[\]]+")
_WS = re.compile(r"\s+")

# Enron addresses arrive as `j..farmer@enron.com`, `f..smith@enron.com`, and inside X.500
# distinguished names. Collapsing runs of dots is what lets identity resolution work.
_DOT_RUN = re.compile(r"\.{2,}")
_X500_CN = re.compile(r"/cn=([a-z0-9_.\-]+)>?\s*$", re.I)


@dataclass
class ParsedMessage:
    """One corpus file, parsed. All offsets are byte offsets into `path`."""

    path: str
    file_sha256: str
    file_size: int
    msg_uid: str

    message_id: str | None
    subject: str
    subject_key: str
    is_reply: bool
    sender: str | None
    sender_display: str | None
    recipients: list[str]
    cc: list[str]
    all_participants: list[str]
    folder: str | None
    origin: str | None

    sent_at: datetime | None
    date_raw: str | None
    date_usable: bool

    header_end: int
    body_raw_start: int
    body_raw_end: int
    body_decoded: str
    offset_map: OffsetMap

    novel_start: int  # offset into body_decoded
    novel_end: int
    trailer_reason: str | None

    content_type: str | None
    transfer_encoding: str | None
    is_multipart: bool

    content_hash: str
    novel_hash: str
    flags: list[str] = field(default_factory=list)

    @property
    def novel_text(self) -> str:
        return self.body_decoded[self.novel_start:self.novel_end]

    @property
    def is_ack_only(self) -> bool:
        """The body is entirely a quoted trailer: a bare forward or acknowledgement.

        Not a parse failure. These messages are real coordination overhead and counting
        them is one of the few things this corpus lets us measure exactly.
        """
        return self.trailer_reason is not None and not self.novel_text.strip()

    def novel_to_raw(self, start: int, end: int) -> tuple[int, int]:
        return self.offset_map.to_raw(self.novel_start + start, self.novel_start + end)


def read_raw(path: Path) -> tuple[str, str, int]:
    """Return (raw_text, sha256, size). Raw text is latin-1 so 1 char == 1 byte."""
    data = path.read_bytes()
    return data.decode("latin-1"), hashlib.sha256(data).hexdigest(), len(data)


def _split_header_block(raw: str) -> tuple[str, int]:
    """Find the end of the *first* header block.

    Deliberately only the first: these files embed whole forwarded messages in the body,
    complete with their own `Message-ID:` and `Date:` headers. Treating a later one as
    real would attribute a message to the wrong person on the wrong date. (Counting
    `^Message-ID:` across the corpus finds 3,269 in 3,240 files for exactly this reason.)
    """
    for sep in ("\n\n", "\r\n\r\n"):
        idx = raw.find(sep)
        if idx != -1:
            return raw[:idx], idx + len(sep)
    # No blank line at all: treat the leading run of header-shaped lines as the block.
    lines = raw.split("\n")
    end = 0
    for line in lines:
        if not re.match(r"^[A-Za-z][A-Za-z0-9\-]*:|^[ \t]", line):
            break
        end += len(line) + 1
    return raw[:end], min(end, len(raw))


def _canonical_address(addr: str) -> str:
    """Normalize an address so the same human collapses onto one key."""
    addr = addr.strip().strip("<>").strip().lower()
    if not addr:
        return ""
    m = _X500_CN.search(addr)
    if m:
        return f"x500:{m.group(1)}"
    addr = _DOT_RUN.sub(".", addr)
    addr = addr.strip(".")
    if "@" in addr:
        local, _, domain = addr.rpartition("@")
        local = _DOT_RUN.sub(".", local).strip(".")
        return f"{local}@{domain}"
    return addr


def _addresses(value: str | None) -> list[str]:
    if not value:
        return []
    out: list[str] = []
    seen: set[str] = set()
    for _name, addr in getaddresses([value.replace("\n", " ").replace("\t", " ")]):
        canon = _canonical_address(addr)
        if canon and canon not in seen:
            seen.add(canon)
            out.append(canon)
    return out


def normalize_subject_key(subject: str) -> str:
    """A thread key: strip reply prefixes, digits and punctuation, collapse whitespace.

    Digits go because "Nom for 6/12" and "Nom for 6/13" are the same recurring task, and
    that collapse is what makes a nomination thread countable as one instance rather than
    thirty.
    """
    s = subject or ""
    prev = None
    while prev != s:
        prev = s
        s = _SUBJECT_PREFIX.sub("", s).strip()
    s = _SUBJECT_NOISE.sub(" ", s)
    s = _WS.sub(" ", s).strip().lower()
    return s


def _parse_date(value: str | None) -> tuple[datetime | None, bool]:
    if not value:
        return None, False
    try:
        dt = parsedate_to_datetime(value.strip())
    except (TypeError, ValueError, IndexError, OverflowError):
        return None, False
    if dt is None:
        return None, False
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    # The archive is a 1999-2002 export. Anything outside that is a parse artifact, not a
    # date, and letting it through would stretch every coverage window it touches.
    if not (1995 <= dt.year <= 2005):
        return None, False
    return dt, True


def _locate_multipart_text(raw: str, body_start: int, content_type: str) -> tuple[int, int, str | None]:
    """For a multipart body, return the (start, end, transfer_encoding) of the first
    text/plain part, so offsets still point into the real file."""
    m = re.search(r'boundary="?([^";\s]+)"?', content_type, re.I)
    if not m:
        return body_start, len(raw), None
    marker = f"--{m.group(1)}"
    pos = body_start
    while True:
        start = raw.find(marker, pos)
        if start == -1:
            return body_start, len(raw), None
        part_hdr_start = start + len(marker)
        nxt = raw.find(marker, part_hdr_start)
        part_end = nxt if nxt != -1 else len(raw)
        part = raw[part_hdr_start:part_end]
        hdr_block, offset = _split_header_block(part.lstrip("\r\n"))
        lead = len(part) - len(part.lstrip("\r\n"))
        headers = HeaderParser().parsestr(hdr_block)
        ctype = (headers.get("Content-Type") or "text/plain").lower()
        if ctype.startswith("text/plain"):
            s = part_hdr_start + lead + offset
            return s, part_end, headers.get("Content-Transfer-Encoding")
        if nxt == -1:
            return body_start, len(raw), None
        pos = nxt


def find_trailer(text: str) -> tuple[int, str | None]:
    """Return the offset where quoted history begins, and which pattern matched."""
    best = len(text)
    reason: str | None = None
    for name, pat in _TRAILER_PATTERNS:
        m = pat.search(text)
        if m and m.start() < best:
            best = m.start()
            reason = name
    return best, reason


def make_msg_uid(path: str) -> str:
    return "m_" + hashlib.sha256(path.encode()).hexdigest()[:12]


def parse_file(path: Path, corpus_root: Path) -> ParsedMessage:
    raw, sha, size = read_raw(path)
    rel = str(path.relative_to(corpus_root.parent)) if corpus_root.parent in path.parents else str(path)
    hdr_block, body_start = _split_header_block(raw)
    headers = HeaderParser().parsestr(hdr_block)

    content_type = headers.get("Content-Type")
    transfer_encoding = headers.get("Content-Transfer-Encoding") or headers.get("Content-transfer-encoding")
    is_multipart = bool(content_type and "multipart/" in content_type.lower())

    body_end = len(raw)
    if is_multipart:
        body_start, body_end, part_enc = _locate_multipart_text(raw, body_start, content_type)
        transfer_encoding = part_enc or transfer_encoding

    body_decoded, omap = decode_body(raw[body_start:body_end], transfer_encoding, raw_base=body_start)

    novel_end, trailer_reason = find_trailer(body_decoded)
    subject = (headers.get("Subject") or "").replace("\n", " ").replace("\t", " ").strip()
    is_reply = bool(_SUBJECT_PREFIX.match(subject))

    sender_list = _addresses(headers.get("From"))
    sender = sender_list[0] if sender_list else None
    recipients = _addresses(headers.get("To"))
    cc = _addresses(headers.get("Cc"))
    bcc = _addresses(headers.get("Bcc"))

    # X-To carries display names for messages whose To: is missing entirely (bulk
    # announcements). We keep it for the noise classifier rather than as participants.
    x_to = (headers.get("X-To") or "").strip()

    participants: list[str] = []
    for a in [sender, *recipients, *cc, *bcc]:
        if a and a not in participants:
            participants.append(a)

    sent_at, date_usable = _parse_date(headers.get("Date"))

    novel = body_decoded[:novel_end]
    # The send time is part of the content hash, and it has to be.
    #
    # A genuine duplicate is one message stored twice - a sender's `sent_items` copy and a
    # recipient's `inbox` copy - and those share a Date header exactly. Two instances of a
    # recurring report do not. Without the timestamp, 48 of the 71 daily credit reports
    # collapsed into one "duplicate" group: their bodies are empty (the report was an
    # attachment) and the subject key deliberately strips the date, so every day hashed
    # identically. Dedup was deleting the most recurring process in the corpus.
    stamp = sent_at.strftime("%Y-%m-%dT%H:%M") if sent_at else f"undated:{rel}"
    content_hash = hashlib.sha256(
        f"{normalize_subject_key(subject)}|{sender or ''}|{stamp}|"
        f"{_WS.sub(' ', body_decoded).strip()}".encode()
    ).hexdigest()
    novel_hash = hashlib.sha256(
        f"{normalize_subject_key(subject)}|{sender or ''}|{stamp}|"
        f"{_WS.sub(' ', novel).strip()}".encode()
    ).hexdigest()

    flags: list[str] = []
    if not date_usable:
        flags.append("no_usable_date")
    if not recipients:
        flags.append("no_to_header")
    if is_multipart:
        flags.append("multipart")
    if not body_decoded.strip():
        flags.append("empty_body")
    if x_to and not recipients:
        flags.append("bulk_x_to")

    return ParsedMessage(
        path=rel,
        file_sha256=sha,
        file_size=size,
        msg_uid=make_msg_uid(rel),
        message_id=(headers.get("Message-ID") or "").strip() or None,
        subject=subject,
        subject_key=normalize_subject_key(subject),
        is_reply=is_reply,
        sender=sender,
        sender_display=(headers.get("X-From") or "").strip() or None,
        recipients=recipients,
        cc=cc,
        all_participants=participants,
        folder=(headers.get("X-Folder") or "").strip() or None,
        origin=(headers.get("X-Origin") or "").strip() or None,
        sent_at=sent_at,
        date_raw=(headers.get("Date") or "").strip() or None,
        date_usable=date_usable,
        header_end=body_start,
        body_raw_start=body_start,
        body_raw_end=body_end,
        body_decoded=body_decoded,
        offset_map=omap,
        novel_start=0,
        novel_end=novel_end,
        trailer_reason=trailer_reason,
        content_type=content_type,
        transfer_encoding=transfer_encoding,
        is_multipart=is_multipart,
        content_hash=content_hash,
        novel_hash=novel_hash,
        flags=flags,
    )


def iter_corpus(corpus_root: Path):
    """Every file under the corpus root, in a stable order.

    Sorted numerically where filenames are numeric, because these are bare integers with a
    trailing dot (`1.`, `10.`, `100.`) and lexicographic order would scatter them.
    """
    def sort_key(p: Path):
        stem = p.name.rstrip(".")
        return (str(p.parent), 0, int(stem)) if stem.isdigit() else (str(p.parent), 1, p.name)

    return sorted((p for p in corpus_root.rglob("*") if p.is_file()), key=sort_key)