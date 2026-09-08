"""Stages 4-5: turn clusters and series into ranked, cited, costed opportunities.

Two hard rules live here.

**Nothing ships without evidence.** Every opportunity's citations are anchored to exact
byte ranges in the raw files, and an opportunity that cannot field enough verified
citations from enough distinct threads and senders is *quarantined* — excluded from the
report body and from every dollar total, and published under "Not counted" with the reason.
Silently dropping it would leave a suspiciously tidy report, which is the thing a sceptical
reader notices first.

**No model touches a number.** Estimation consumes only counts measured from the corpus.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from pathlib import Path

from observe.estimate.model import BANDS, Measured, band_estimates, measure
from observe.evidence.anchor import STRONG_TIERS, AnchorError, Citation, build_citation
from observe.parse import read_raw

BUILD_VERSION = "1.0.0"

MIN_CITATIONS = 3
MIN_CITATION_THREADS = 2
MIN_CITATION_SENDERS = 2
MAX_CITATIONS_PER_OPPORTUNITY = 8
MAX_NORMALIZED_SHARE = 0.40


@dataclass
class Opportunity:
    opportunity_id: str
    source: str                      # "content_cluster" | "header_frequency"
    title: str
    task_class: str
    label_mechanical: str
    narrative: dict
    measured: Measured
    bands: dict
    citations: list[Citation]
    quarantined_citations: list[dict]
    member_uids: list[str]
    thread_ids: list[str]
    person_ids: list[str]
    months: list[str]
    signal_rates: dict
    systems: dict
    roles: dict
    gate_metrics: dict
    confidence: str
    artifact_shape: str
    status: str = "counted"          # "counted" | "low_confidence" | "quarantined"
    status_reason: str = ""
    flags: list[str] = field(default_factory=list)

    @property
    def dollars(self) -> Decimal:
        return self.bands["base"].dollars_per_month

    def as_dict(self) -> dict:
        return {
            "opportunity_id": self.opportunity_id,
            "source": self.source,
            "title": self.title,
            "task_class": self.task_class,
            "label_mechanical": self.label_mechanical,
            "narrative": self.narrative,
            "status": self.status,
            "status_reason": self.status_reason,
            "confidence": self.confidence,
            "artifact_shape": self.artifact_shape,
            "measured": self.measured.as_dict(),
            "gate_metrics": self.gate_metrics,
            "signal_rates": self.signal_rates,
            "systems": self.systems,
            "roles": self.roles,
            "months": self.months,
            "people": len(self.person_ids),
            "hours_per_month": {
                b: float(self.bands[b].hours_per_month.quantize(Decimal("0.1"))) for b in BANDS
            },
            "automatable_hours_per_month": {
                b: float(self.bands[b].automatable_hours_per_month.quantize(Decimal("0.1")))
                for b in BANDS
            },
            "dollars_per_month": {
                b: float(self.bands[b].dollars_per_month) for b in BANDS
            },
            "derivation": self.bands["base"].derivation,
            "citations": [c.to_dict() for c in self.citations],
            "quarantined_citations": self.quarantined_citations,
            "member_count": len(self.member_uids),
            "member_uids": self.member_uids,
            "flags": sorted(self.flags),
        }


# ---------------------------------------------------------------------------
# Citation building
# ---------------------------------------------------------------------------

def _raw_cache(corpus_root: Path):
    cache: dict[str, str] = {}

    def get(path: str) -> str:
        if path not in cache:
            # The 350KB message is in here; a small LRU keeps memory flat across 3,240 files.
            if len(cache) > 40:
                cache.clear()
            cache[path], _sha, _size = read_raw(Path(path))
        return cache[path]

    return get


def collect_citations(
    uids: list[str],
    records: dict,
    by_uid: dict,
    get_raw,
    *,
    limit: int = MAX_CITATIONS_PER_OPPORTUNITY,
) -> tuple[list[Citation], list[dict]]:
    """Anchor the proposed quotes for these messages. Returns (verified, quarantined).

    Ordered so the strongest evidence is tried first: messages the characterizer picked,
    then anything with a quote. Deduplicated by `citation_id`, which is content-addressed,
    so the same span cited twice collapses for free.
    """
    verified: list[Citation] = []
    quarantined: list[dict] = []
    seen: set[str] = set()

    for uid in uids:
        if len(verified) >= limit:
            break
        record = records.get(uid)
        msg = by_uid.get(uid)
        if not record or not msg:
            continue
        for ev in (record.get("evidence") or []):
            proposal = (ev.get("quote_proposal") or "").strip()
            if not proposal:
                continue
            try:
                raw = get_raw(msg.path)
                citation = build_citation(proposal, raw=raw, msg=msg)
            except AnchorError as e:
                quarantined.append({
                    "msg_uid": uid,
                    "source_path": msg.path,
                    "reason": e.reason,
                    "detail": e.detail[:200],
                    "proposal_preview": proposal[:160],
                })
                continue
            except OSError as e:
                quarantined.append({
                    "msg_uid": uid, "source_path": msg.path,
                    "reason": "unreadable_source", "detail": str(e)[:200],
                    "proposal_preview": proposal[:160],
                })
                continue
            if citation.citation_id in seen:
                continue
            seen.add(citation.citation_id)
            verified.append(citation)
            if len(verified) >= limit:
                break
    return verified, quarantined


def subject_citation(msg, get_raw) -> Citation | None:
    """Cite a message's `Subject:` header line itself.

    This is what makes the header-frequency findings checkable. For a recurring report
    whose body is an empty attachment stub, the subject line *is* the evidence that the
    report was produced that day, and it sits in the raw bytes like any other quote.
    """
    raw = get_raw(msg.path)
    for line in raw.split("\n"):
        if line.startswith("Subject:") and len(line.strip()) >= 24:
            try:
                return build_citation(line.rstrip("\r"), raw=raw, msg=msg, allow_repair=False)
            except AnchorError:
                return None
    return None


# ---------------------------------------------------------------------------
# Claim gates
# ---------------------------------------------------------------------------

def evaluate_claim(citations: list[Citation], metrics: dict) -> tuple[str, str, list[str]]:
    """Decide whether an opportunity may be counted. Returns (status, reason, flags)."""
    flags: list[str] = []
    threads = {c.msg_uid for c in citations}
    senders = {c.sender for c in citations if c.sender}

    if len(citations) < MIN_CITATIONS:
        return ("quarantined",
                f"only {len(citations)} verified citation(s); {MIN_CITATIONS} required",
                flags)
    if len(threads) < MIN_CITATION_THREADS:
        return ("quarantined",
                f"all evidence comes from {len(threads)} message(s); "
                f"{MIN_CITATION_THREADS} required so one thread cannot look like a pattern",
                flags)
    if len(senders) < MIN_CITATION_SENDERS and metrics.get("messages", 0) < 15:
        return ("quarantined",
                f"evidence from {len(senders)} sender and only {metrics.get('messages', 0)} "
                f"messages", flags)

    # Only the genuinely weak tier is capped. A `rewrapped` citation is character-identical
    # to the source apart from where the mail client put the newlines.
    normalized = sum(1 for c in citations if c.match_tier not in STRONG_TIERS)
    if normalized / len(citations) > MAX_NORMALIZED_SHARE:
        flags.append("majority_normalized_citations")
        return ("low_confidence",
                f"{normalized} of {len(citations)} citations matched only after whitespace "
                f"and punctuation normalization", flags)

    if not any(c.match_tier in STRONG_TIERS for c in citations):
        flags.append("no_strong_citation")
        return ("low_confidence",
                "no citation is character-identical to its source", flags)

    if metrics.get("coherence") == "incoherent":
        flags.append("characterizer_called_it_incoherent")
        return ("low_confidence",
                "the cluster was judged incoherent when described, so the grouping is "
                "probably an artefact", flags)

    return ("counted", "", flags)


def confidence_of(citations: list[Citation], metrics: dict, coherence: str) -> str:
    raw_exact = sum(1 for c in citations if c.match_tier in STRONG_TIERS)
    if (coherence == "tight" and raw_exact >= 3 and metrics.get("senders", 0) >= 2
            and metrics.get("months", 0) >= 4):
        return "high"
    if coherence == "incoherent" or raw_exact == 0:
        return "low"
    return "medium"


# ---------------------------------------------------------------------------
# Assembly
# ---------------------------------------------------------------------------

def build_from_clusters(clusters, characterizations: dict, records: dict, corpus,
                        config_path: Path, get_raw) -> list[Opportunity]:
    out: list[Opportunity] = []
    for c in clusters:
        if not c.gate.passed:
            continue
        narrative = characterizations.get(c.cluster_id) or {}
        members = [records[u] for u in c.member_uids if u in records]
        if not members:
            continue

        ordered = list(narrative.get("key_evidence_uids") or []) + [
            u for u in c.exemplar_uids if u not in (narrative.get("key_evidence_uids") or [])
        ] + [u for u in c.member_uids if u not in c.exemplar_uids]
        citations, quarantined = collect_citations(ordered, records, corpus.by_uid, get_raw)

        measured = measure(members, set(c.thread_ids))
        bands = band_estimates(measured, c.task_class, config_path)
        metrics = {**c.gate.metrics, "coherence": narrative.get("coherence", "mixed")}
        status, reason, flags = evaluate_claim(citations, metrics)

        out.append(Opportunity(
            opportunity_id=c.cluster_id,
            source="content_cluster",
            title=narrative.get("title") or c.label,
            task_class=c.task_class,
            label_mechanical=c.label,
            narrative={
                "what_happens": narrative.get("what_happens", ""),
                "where_it_stalls": narrative.get("where_it_stalls", ""),
                "why_it_recurs": narrative.get("why_it_recurs", ""),
                "automation_opportunity": narrative.get("automation_opportunity", ""),
                "coherence": narrative.get("coherence", "mixed"),
            },
            measured=measured,
            bands=bands,
            citations=citations,
            quarantined_citations=quarantined,
            member_uids=c.member_uids,
            thread_ids=c.thread_ids,
            person_ids=c.person_ids,
            months=c.months,
            signal_rates=c.signal_rates,
            systems=c.systems,
            roles=c.roles,
            gate_metrics=c.gate.metrics,
            confidence=confidence_of(citations, c.gate.metrics,
                                     narrative.get("coherence", "mixed")),
            artifact_shape=narrative.get("artifact_recommendation", "none"),
            status=status,
            status_reason=reason,
            flags=flags,
        ))
    return out


def build_from_series(series, corpus, config_path: Path, get_raw,
                      characterizations: dict | None = None) -> list[Opportunity]:
    """Header-frequency findings, cited by their own subject lines.

    These need no model to have been discovered, and their evidence is unusually strong:
    the same subject line, from the same person, on a measured cadence, quotable verbatim
    from the raw bytes.
    """
    out: list[Opportunity] = []
    characterizations = characterizations or {}
    for s in series:
        msgs = [corpus.by_uid[u] for u in s.msg_uids if u in corpus.by_uid]
        if not msgs:
            continue
        msgs.sort(key=lambda m: (m.sent_at is None, m.sent_at or 0))

        citations: list[Citation] = []
        quarantined: list[dict] = []
        seen: set[str] = set()
        # Spread the cited instances across the series rather than taking the first few,
        # so the citations themselves demonstrate the recurrence.
        step = max(1, len(msgs) // MAX_CITATIONS_PER_OPPORTUNITY)
        for m in msgs[::step]:
            if len(citations) >= MAX_CITATIONS_PER_OPPORTUNITY:
                break
            try:
                cit = subject_citation(m, get_raw)
            except OSError:
                cit = None
            if cit is None:
                quarantined.append({
                    "msg_uid": m.msg_uid, "source_path": m.path,
                    "reason": "subject_line_too_short_to_cite",
                    "detail": "", "proposal_preview": (m.subject or "")[:160],
                })
                continue
            if cit.citation_id in seen:
                continue
            seen.add(cit.citation_id)
            citations.append(cit)

        members = [{
            "msg_uid": m.msg_uid,
            "thread_id": m.msg_uid,             # each instance is its own task instance
            "person_ids": sorted({corpus.address_to_person.get(a, a)
                                  for a in m.all_participants}),
            "month": m.sent_at.strftime("%Y-%m") if m.sent_at else None,
            "sender_person": corpus.address_to_person.get(m.sender or "", m.sender),
            "rework_signal": False,
            "waiting_signal": False,
            "manual_transfer_signal": s.empty_body_share > 0.5,
            "evidence": [],
        } for m in msgs]

        measured = measure(members, {m.msg_uid for m in msgs})
        bands = band_estimates(measured, "recurring_report", config_path)
        metrics = {
            "messages": len(msgs), "distinct_content": len(msgs),
            "senders": 1, "threads": len(msgs), "months": len(s.months),
            "weeks": len(s.weeks), "folders": len(s.folders),
            "people": len({p for m in members for p in m["person_ids"]}),
            "coherence": "tight",
        }
        status, reason, flags = evaluate_claim(citations, metrics)
        narrative = characterizations.get(s.series_id) or {}

        out.append(Opportunity(
            opportunity_id=s.series_id,
            source="header_frequency",
            title=narrative.get("title") or f'"{s.example_subject}" produced {s.cadence}',
            task_class="recurring_report",
            label_mechanical=s.template,
            narrative={
                "what_happens": narrative.get("what_happens") or (
                    f'The same message, "{s.example_subject}", is produced and sent '
                    f'{s.cadence} by one person to {len(s.recipients)} recipient(s). '
                    f'{s.size} instances span {len(s.months)} months and {len(s.weeks)} '
                    f'distinct weeks, with a median gap of {s.median_gap_days} days. '
                    + (f'{s.empty_body_share:.0%} of them carry no message body at all, '
                       f'meaning the content was an attachment assembled outside the mail '
                       f'system. ' if s.empty_body_share > 0.2 else "")
                ),
                "where_it_stalls": narrative.get("where_it_stalls") or (
                    "This series was discovered from headers alone, so the corpus shows "
                    "that it happened on a cadence but not what it cost to produce. The "
                    "bodies are unavailable."
                ),
                "why_it_recurs": narrative.get("why_it_recurs") or (
                    f"A fixed {s.cadence} reporting obligation to a standing distribution "
                    f"list."
                ),
                "automation_opportunity": narrative.get("automation_opportunity") or (
                    "A scheduled job that assembles the same figures from their sources "
                    "and sends them to the standing list on the same cadence."
                ),
                "coherence": "tight",
                "cadence": s.cadence,
                "median_gap_days": s.median_gap_days,
                "discovery_note": (
                    "Discovered deterministically from subject lines, with no model "
                    "involved. Content clustering could not see this process because the "
                    f"bodies are empty in {s.empty_body_share:.0%} of instances."
                ),
            },
            measured=measured,
            bands=bands,
            citations=citations,
            quarantined_citations=quarantined,
            member_uids=[m.msg_uid for m in msgs],
            thread_ids=[m.msg_uid for m in msgs],
            person_ids=sorted({p for m in members for p in m["person_ids"]}),
            months=s.months,
            signal_rates={"manual_transfer_signal": 1.0 if s.empty_body_share > 0.5 else 0.0},
            systems={"email": len(msgs)},
            roles={"status_report": len(msgs)},
            gate_metrics=metrics,
            confidence=confidence_of(citations, metrics, "tight"),
            artifact_shape=narrative.get("artifact_recommendation", "email"),
            status=status,
            status_reason=reason,
            flags=flags + ["discovered_from_headers"],
        ))
    return out


def rank(opportunities: list[Opportunity]) -> list[Opportunity]:
    """Counted first, by base dollars. Deterministic tie-break on id so runs match."""
    order = {"counted": 0, "low_confidence": 1, "quarantined": 2}
    return sorted(
        opportunities,
        key=lambda o: (order.get(o.status, 3), -o.dollars, o.opportunity_id),
    )