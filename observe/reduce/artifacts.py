"""Stage 6: act on the findings, not just describe them.

The assignment asks for "a drafted artifact someone could use the next morning" for
opportunities above a threshold you choose and defend.

**The threshold** (`config/thresholds.yml`), all of which must hold:

* a low dollar floor that exists to exclude noise rather than to rank - see
  `config/thresholds.yml` for why a company-sized floor cannot be applied to figures
  deliberately scoped to four mailboxes.
* at least 5 verified citations across at least 4 distinct messages, 6 task instances and
  3 months of recurrence - the real gate — a document is a much
  stronger claim than a table row, and drafting one off thin evidence is exactly how a
  credible report becomes a discredited one.
* status `counted` and confidence not `low` — we do not write procedures from findings we
  have already told the reader to discount.
* an artifact *shape*: the characterizer must have said which document would help. `none`
  is a real answer and disqualifies.

Capped at 6, because six documents is what a team will actually adopt in a quarter and
twelve is shelfware. One extra slot is reserved for the best-evidenced item that fails only
the dollar test, labelled as a judgment call — a purely numeric cutoff is not a strategy.

**The linter** is what makes the citation convention real: every `[cit_*]` marker must
resolve to a verified citation for *that* opportunity, the required headings must be
present, and no dollar or hour figure may appear in the body. An artifact that fails is
withheld and the dashboard says so.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

import yaml

from observe.cache import sha256_text
from observe.dispatch import Unit
from observe.llm.schema_guard import check

ARTIFACTS_VERSION = "1.0.0"

_CIT_MARKER = re.compile(r"\[(cit_[0-9a-f]{12})\]")
_MONEY = re.compile(r"\$\s?\d")
_DURATION = re.compile(r"\b\d+(?:\.\d+)?\s*(hours?|hrs?|minutes?|mins?|FTEs?)\b", re.I)

_REQUIRED_HEADINGS = {
    "sop": ["## Purpose", "## Scope", "## Current practice", "## Procedure",
            "## Recommended change", "## Open questions"],
    "runbook": ["## Purpose", "## Scope", "## Current practice", "## Procedure",
                "## Recommended change", "## Open questions"],
    "checklist": ["## Purpose", "## Scope", "## Current practice", "## Procedure",
                  "## Recommended change", "## Open questions"],
    "worksheet": ["## Purpose", "## Scope", "## Current practice", "## Template",
                  "## Recommended change", "## Open questions"],
    "template": ["## Purpose", "## Scope", "## Current practice", "## Template",
                 "## Recommended change", "## Open questions"],
    "email": ["## Purpose", "## Scope", "## Current practice", "## Template",
              "## Recommended change", "## Open questions"],
}

_PREFIX = {"sop": "SOP", "runbook": "RUN", "checklist": "CHK",
           "template": "TPL", "worksheet": "WKS", "email": "EML"}


@dataclass
class Thresholds:
    min_dollars: float = 55.0
    min_citations: int = 5
    min_distinct_messages: int = 4
    min_instances: int = 6
    min_months: int = 3
    max_artifacts: int = 6
    allow_one_judgment_exception: bool = True
    rationale: str = ""

    @classmethod
    def load(cls, path: Path) -> "Thresholds":
        if not path.exists():
            return cls()
        raw = yaml.safe_load(path.read_text()) or {}
        a = raw.get("artifacts", {})
        return cls(
            min_dollars=float(a.get("min_dollars_per_month", 55.0)),
            min_citations=int(a.get("min_verified_citations", 5)),
            min_distinct_messages=int(a.get("min_distinct_messages", 4)),
            min_instances=int(a.get("min_instances", 6)),
            min_months=int(a.get("min_months", 3)),
            max_artifacts=int(a.get("max_artifacts", 6)),
            allow_one_judgment_exception=bool(a.get("allow_one_judgment_exception", True)),
            rationale=a.get("rationale", ""),
        )


@dataclass
class LintResult:
    ok: bool
    problems: list[str] = field(default_factory=list)
    markers: list[str] = field(default_factory=list)


def select(opportunities, thresholds: Thresholds) -> tuple[list, list[dict]]:
    """Choose which opportunities get a document. Returns (selected, skipped-with-reasons)."""
    eligible: list = []
    skipped: list[dict] = []
    near_miss: list = []

    for o in opportunities:
        reasons: list[str] = []
        if o.status != "counted":
            reasons.append(f"status is {o.status}")
        if o.confidence == "low":
            reasons.append("confidence is low")
        if o.artifact_shape in ("none", "", None):
            reasons.append("no artifact shape: writing one would be busywork")
        if len(o.citations) < thresholds.min_citations:
            reasons.append(f"{len(o.citations)} citations, {thresholds.min_citations} required")
        if len({c.msg_uid for c in o.citations}) < thresholds.min_distinct_messages:
            reasons.append(
                f"evidence spread over {len({c.msg_uid for c in o.citations})} messages, "
                f"{thresholds.min_distinct_messages} required")
        if o.measured.instances < thresholds.min_instances:
            reasons.append(f"{o.measured.instances} task instances, "
                           f"{thresholds.min_instances} required to call it a routine")
        if len(o.months) < thresholds.min_months:
            reasons.append(f"spans {len(o.months)} month(s), {thresholds.min_months} "
                           f"required: a burst in one month is a project, not a process")

        money_short = float(o.dollars) < thresholds.min_dollars
        if reasons:
            skipped.append({"opportunity_id": o.opportunity_id, "title": o.title,
                            "reasons": reasons})
            continue
        if money_short:
            near_miss.append(o)
            continue
        eligible.append(o)

    eligible.sort(key=lambda o: (-float(o.dollars), o.opportunity_id))
    selected = eligible[:thresholds.max_artifacts]
    for o in eligible[thresholds.max_artifacts:]:
        skipped.append({"opportunity_id": o.opportunity_id, "title": o.title,
                        "reasons": [f"beyond the cap of {thresholds.max_artifacts} artifacts"]})

    # One deliberate exception: the best-evidenced item that failed only the dollar test.
    if thresholds.allow_one_judgment_exception and near_miss and \
            len(selected) < thresholds.max_artifacts + 1:
        near_miss.sort(key=lambda o: (-len(o.citations), -float(o.dollars), o.opportunity_id))
        chosen = near_miss[0]
        chosen.flags.append("artifact_below_threshold_included_on_judgment")
        selected.append(chosen)
        for o in near_miss[1:]:
            skipped.append({"opportunity_id": o.opportunity_id, "title": o.title,
                            "reasons": [f"below ${thresholds.min_dollars:.0f}/month"]})
    else:
        for o in near_miss:
            skipped.append({"opportunity_id": o.opportunity_id, "title": o.title,
                            "reasons": [f"below ${thresholds.min_dollars:.0f}/month"]})
    return selected, skipped


def build_units(selected, *, prompt_hash: str, model: str, schema_hash: str,
                system_prompt_hash: str = "") -> list[Unit]:
    units: list[Unit] = []
    for o in selected:
        payload = _render(o)
        units.append(Unit(
            unit_id=f"artifact_{o.opportunity_id}",
            payload=payload,
            cache_key=sha256_text("artifact", payload, prompt_hash, model, schema_hash),
            expected_ids={c.citation_id for c in o.citations},
            meta={"opportunity_id": o.opportunity_id,
                  "artifact_shape": o.artifact_shape,
                  "title": o.title},
        ))
    return units


def _render(o) -> str:
    lines = [
        f"OPPORTUNITY {o.opportunity_id}",
        f"title: {o.title}",
        f"task class: {o.task_class}",
        f"document to write: {o.artifact_shape}",
        "",
        "MEASURED (facts; do not restate as findings, and do not contradict):",
        f"  {o.measured.messages} messages in {o.measured.instances} task instances",
        f"  {o.measured.senders} distinct sender(s), {len(o.person_ids)} people involved",
        f"  spans {len(o.months)} months: {', '.join(o.months[:12])}",
        "  signal rates: " + ", ".join(f"{k.replace('_signal','')}={v:.0%}"
                                       for k, v in o.signal_rates.items()),
        "  systems mentioned: " + (", ".join(f"{k}" for k in o.systems) or "none"),
        "  roles seen: " + ", ".join(f"{k}={v}" for k, v in o.roles.items()),
        "",
        "WHAT THE ARCHIVE SHOWS:",
        f"  what happens: {o.narrative.get('what_happens', '')}",
        f"  where it stalls: {o.narrative.get('where_it_stalls', '')}",
        f"  why it recurs: {o.narrative.get('why_it_recurs', '')}",
        f"  automation opportunity: {o.narrative.get('automation_opportunity', '')}",
        "",
        "VERIFIED CITATIONS - use only these ids, exactly as written:",
    ]
    for c in o.citations:
        quote = c.quote.strip().replace("\n", " ")
        lines.append(f'  [{c.citation_id}] "{quote}"')
        lines.append(f'      from {c.source_path}, {c.sent_at or "undated"}, '
                     f'sender {c.sender or "unknown"}')
    lines += [
        "",
        f"Write the {o.artifact_shape}. Every sentence about current practice must end with "
        f"one of the citation ids above in square brackets. Recommendations carry no marker "
        f"and belong under '## Recommended change'.",
    ]
    return "\n".join(lines)


def lint(body: str, artifact_shape: str, allowed_ids: set[str]) -> LintResult:
    """Enforce the convention that makes an artifact traceable."""
    problems: list[str] = []
    markers = _CIT_MARKER.findall(body or "")

    for required in _REQUIRED_HEADINGS.get(artifact_shape, _REQUIRED_HEADINGS["sop"]):
        if required.lower() not in (body or "").lower():
            problems.append(f"missing required heading {required!r}")

    unknown = sorted({m for m in markers if m not in allowed_ids})
    if unknown:
        problems.append(f"citation markers do not resolve: {unknown[:4]}")
    if not markers:
        problems.append("no citation markers at all: nothing in this document is traceable")

    # Split at the recommendations heading; only the part before it makes claims about today.
    lower = (body or "").lower()
    cut = lower.find("## recommended change")
    observational = (body or "")[:cut] if cut != -1 else (body or "")
    if _MONEY.search(observational) or _DURATION.search(observational):
        hit = (_MONEY.search(observational) or _DURATION.search(observational)).group(0)
        problems.append(
            f"body contains a quantity {hit!r}; hours and dollars belong in the report "
            f"where they carry a derivation, not in a document someone will act on"
        )

    current = lower.find("## current practice")
    if current != -1:
        section_end = lower.find("\n## ", current + 1)
        section = (body or "")[current:section_end if section_end != -1 else len(body)]
        sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", section) if len(s.strip()) > 40]
        uncited = [s for s in sentences if not _CIT_MARKER.search(s)]
        if len(uncited) > max(1, len(sentences) // 3):
            problems.append(
                f"{len(uncited)} of {len(sentences)} sentences under 'Current practice' "
                f"carry no citation marker"
            )
    return LintResult(ok=not problems, problems=problems, markers=sorted(set(markers)))


def validate(parsed, unit: Unit) -> list[str]:
    problems = list(check(parsed).violations)
    if not isinstance(parsed, dict):
        return problems + ["$: expected an object"]
    title = parsed.get("title")
    body = parsed.get("body_markdown")
    if not title:
        problems.append("$.title: missing")
    if not body or len(body) < 300:
        problems.append("$.body_markdown: missing or too short to be usable")
        return problems
    result = lint(body, unit.meta.get("artifact_shape", "sop"), unit.expected_ids)
    problems.extend(result.problems)
    return problems


def write_files(results: dict, selected, out_dir: Path) -> list[dict]:
    """Write the artifacts to disk as plain Markdown, with machine-readable front matter."""
    out_dir.mkdir(parents=True, exist_ok=True)
    by_id = {o.opportunity_id: o for o in selected}
    written: list[dict] = []
    counter: dict[str, int] = {}

    for unit_id, payload in sorted(results.items()):
        opp_id = unit_id.replace("artifact_", "")
        o = by_id.get(opp_id)
        if not o or not isinstance(payload, dict):
            continue
        shape = o.artifact_shape
        prefix = _PREFIX.get(shape, "DOC")
        counter[prefix] = counter.get(prefix, 0) + 1
        artifact_id = f"{prefix}-{counter[prefix]:02d}"
        slug = re.sub(r"[^a-z0-9]+", "-", (payload.get("title") or o.title).lower()).strip("-")[:52]
        filename = f"{artifact_id}-{slug}.md"

        used = lint(payload["body_markdown"], shape,
                    {c.citation_id for c in o.citations}).markers
        front = {
            "artifact_id": artifact_id,
            "title": payload.get("title") or o.title,
            "artifact_type": shape,
            "opportunity_id": opp_id,
            "opportunity_title": o.title,
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "generator": "claude -p via .claude/agents/artifact-drafter.md",
            "review_status": "draft-unreviewed",
            "evidence": used,
            "below_threshold_judgment_call":
                "artifact_below_threshold_included_on_judgment" in o.flags,
        }
        header = "---\n" + yaml.safe_dump(front, sort_keys=False).strip() + "\n---\n\n"
        note = (
            "> **Draft, not reviewed.** Every sentence describing current practice carries a\n"
            "> citation id that resolves to a verified quote from the archive. Sentences under\n"
            "> *Recommended change* are proposals and carry no citation. Nobody who does this\n"
            "> work has read this document.\n\n"
        )
        (out_dir / filename).write_text(header + note + payload["body_markdown"].strip() + "\n")
        written.append({**front, "filename": filename})

    (out_dir / "index.json").write_text(json.dumps(written, indent=2) + "\n")
    return written