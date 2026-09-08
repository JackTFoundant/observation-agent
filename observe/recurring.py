"""Recurring work discovered from headers alone, with no model involved.

Content clustering has a blind spot this module exists to close.

The clearest recurring process in this corpus is a **daily credit report**: roughly 70
messages, one per working day, subject `Credit Report--4/3/01`. Most of them have an *empty
body* — the report itself was an attachment, which the export did not preserve. So they are
classified as attachment-only acknowledgements, never reach an extractor, and the
content-clustering stage sees a fraction of them. When it ran alone, that process failed
the promotion gate on "spans 2 months" while the corpus actually shows it running for over
a year.

But the recurrence was never in the bodies. It is in the subject lines, and those are in
the raw bytes where they can be cited exactly. `Subject: Credit Report--4/3/01` repeated
across fourteen months, always from the same sender, to the same person, *is* the evidence.

So this stage groups messages by a normalized subject template and promotes a template that
recurs often enough, over long enough, with a consistent sender. It is entirely
deterministic — no model reads anything here — and it recovers exactly the processes a
body-text pipeline is structurally unable to see.

The cadence it infers is measured, not assumed: median days between consecutive instances.
"""

from __future__ import annotations

import hashlib
import re
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from statistics import median

RECURRING_VERSION = "1.0.0"

# Anything that varies per instance becomes a placeholder, so the template is what stays
# the same. Dates first, then bare numbers, so `01/21-01/25` collapses to one token.
_SUBSTITUTIONS = (
    (re.compile(r"\b\d{1,2}[/\-.]\d{1,2}(?:[/\-.]\d{2,4})?\b"), "<date>"),
    (re.compile(r"\b\d{1,2}:\d{2}\s*(?:am|pm)?\b", re.I), "<time>"),
    (re.compile(r"\b(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.?\s+\d{1,2}\b", re.I), "<date>"),
    (re.compile(r"\b(?:mon|tue|wed|thu|fri|sat|sun)[a-z]*\b", re.I), "<day>"),
    (re.compile(r"\b(?:january|february|march|april|may|june|july|august|september|october|november|december)\b", re.I), "<month>"),
    (re.compile(r"\b\d[\d,]*(?:\.\d+)?\b"), "<n>"),
    # Punctuation runs collapse: the same daily report was typed `Credit Report--4/3/01`,
    # `Credit Report - 4/4/01` and `Credit Report 4/5/01`. Treating those as three
    # different series splits one process into three that each fail the gate.
    (re.compile(r"[\s\-_.:;,|/\\]*<date>[\s\-_.:;,|/\\]*"), " <date> "),
    (re.compile(r"[\-_.:;,|]{1,}"), " "),
    (re.compile(r"\s+"), " "),
)

_MIN_INSTANCES = 8
_MIN_MONTHS = 3
_MIN_WEEKS = 3
_MIN_TEMPLATE_WORDS = 2


def subject_template(subject: str) -> str:
    """Reduce a subject to what stays constant across instances.

    `Credit Report--4/3/01` and `Credit Report--4/4/01` both become `credit report--<date>`,
    while `California Capacity Report for Week of 01/21-01/25` becomes
    `california capacity report for week of <date>-<date>`.
    """
    s = (subject or "").strip()
    # Strip reply/forward prefixes: a reply to a report is not another instance of it.
    prev = None
    while prev != s:
        prev = s
        s = re.sub(r"^\s*(?:re|fw|fwd|aw|sv)\s*:", "", s, flags=re.I).strip()
    for pattern, replacement in _SUBSTITUTIONS:
        s = pattern.sub(replacement, s)
    return s.strip().lower()


def _words(template: str) -> int:
    return len([w for w in re.split(r"[^a-z&]+", template) if len(w) > 2])


@dataclass
class RecurringSeries:
    """A subject template that recurs, proven from headers."""

    series_id: str
    template: str
    example_subject: str
    msg_uids: list[str]
    sender_person: str | None
    recipients: list[str]
    months: list[str]
    weeks: list[str]
    median_gap_days: float | None
    cadence: str
    is_reply_free: bool
    replies_excluded: int
    empty_body_share: float
    folders: list[str] = field(default_factory=list)

    @property
    def size(self) -> int:
        return len(self.msg_uids)

    def as_dict(self) -> dict:
        return {
            "series_id": self.series_id,
            "template": self.template,
            "example_subject": self.example_subject,
            "instances": self.size,
            "sender_person": self.sender_person,
            "recipients": self.recipients[:8],
            "months": self.months,
            "weeks_spanned": len(self.weeks),
            "median_gap_days": self.median_gap_days,
            "cadence": self.cadence,
            "replies_excluded": self.replies_excluded,
            "empty_body_share": round(self.empty_body_share, 3),
            "folders": self.folders,
        }


def _cadence_from_gap(gap: float | None, instances: int, months: int) -> str:
    """Name the cadence from the measured median gap between instances."""
    if gap is None:
        return "irregular"
    if gap <= 1.6:
        return "daily"
    if gap <= 4.0:
        return "several times a week"
    if gap <= 10.0:
        return "weekly"
    if gap <= 20.0:
        return "fortnightly"
    if gap <= 45.0:
        return "monthly"
    return "irregular"


def find_series(messages, address_to_person: dict[str, str]) -> list[RecurringSeries]:
    """Every recurring subject template in the corpus, promoted or not."""
    groups: dict[tuple[str, str | None], list] = defaultdict(list)
    replies_dropped: dict[tuple[str, str | None], int] = defaultdict(int)
    for m in messages:
        template = subject_template(m.subject)
        if not template or _words(template) < _MIN_TEMPLATE_WORDS:
            continue
        sender = address_to_person.get(m.sender or "", m.sender)
        if m.is_reply:
            # A reply to a report is not another instance of the report. Excluded from the
            # series rather than disqualifying it: rejecting a 17-instance weekly series
            # because two people replied to it would lose a real process.
            replies_dropped[(template, sender)] += 1
            continue
        groups[(template, sender)].append(m)

    series: list[RecurringSeries] = []
    for (template, sender), members in groups.items():
        if len(members) < 3:
            continue
        dated = sorted((m for m in members if m.sent_at), key=lambda m: m.sent_at)
        gaps = [
            (dated[i].sent_at - dated[i - 1].sent_at).total_seconds() / 86400.0
            for i in range(1, len(dated))
        ]
        gaps = [g for g in gaps if g > 0]
        med = round(median(gaps), 2) if gaps else None
        months = sorted({m.sent_at.strftime("%Y-%m") for m in dated})
        weeks = sorted({f"{m.sent_at.isocalendar()[0]}-W{m.sent_at.isocalendar()[1]:02d}"
                        for m in dated})
        recips = Counter()
        for m in members:
            recips.update(address_to_person.get(a, a) for a in m.recipients)
        empties = sum(1 for m in members if not m.novel_text.strip())

        series.append(RecurringSeries(
            series_id="ser_" + hashlib.sha256(f"{template}|{sender}".encode()).hexdigest()[:10],
            template=template,
            example_subject=Counter(m.subject for m in members).most_common(1)[0][0],
            msg_uids=[m.msg_uid for m in members],
            sender_person=sender,
            recipients=[r for r, _ in recips.most_common()],
            months=months,
            weeks=weeks,
            median_gap_days=med,
            cadence=_cadence_from_gap(med, len(members), len(months)),
            is_reply_free=True,
            replies_excluded=replies_dropped.get((template, sender), 0),
            empty_body_share=empties / len(members),
            folders=sorted({m.path.rsplit("/", 1)[0] for m in members}),
        ))

    series.sort(key=lambda s: (-s.size, s.series_id))
    return series


def promote(series: list[RecurringSeries]) -> tuple[list[RecurringSeries], list[dict]]:
    """Apply the gate. Returns (promoted, rejected-with-reasons).

    Stricter than it looks. The template must recur at least eight times, across at least
    three months *and* three distinct weeks, and must not be a reply chain — a subject
    replied to nine times in one afternoon is one conversation, not nine instances of a
    recurring task.
    """
    promoted: list[RecurringSeries] = []
    rejected: list[dict] = []
    for s in series:
        failed: list[str] = []
        if s.size < _MIN_INSTANCES:
            failed.append(f"only {s.size} instances (need {_MIN_INSTANCES})")
        if len(s.months) < _MIN_MONTHS:
            failed.append(f"spans {len(s.months)} month(s) (need {_MIN_MONTHS})")
        if len(s.weeks) < _MIN_WEEKS:
            failed.append(f"spans {len(s.weeks)} week(s) (need {_MIN_WEEKS})")
        if failed:
            rejected.append({**s.as_dict(), "failed_gates": failed})
        else:
            promoted.append(s)
    return promoted, rejected