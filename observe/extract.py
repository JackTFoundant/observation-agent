"""Stage 1: per-message extraction.

The only stage where a model sees message text. Everything about the payload is shaped to
keep a worker's context window small and its job narrow:

* only the sender's own words (trailer stripping already removed quoted history);
* a hard per-message character cap, so one pathological message cannot eat a batch;
* headers reduced to the few fields that help classification.

The 350 KB message is the reason the cap exists. Its body is a machine-generated table
(proven in `observe.classify`), so the cap keeps the prose and discards the rows, with a
one-line note in their place saying what was removed and why.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from observe.cache import sha256_text
from observe.classify import Classification, detect_table
from observe.dispatch import Unit
from observe.llm.schema_guard import check_extraction_batch

EXTRACT_VERSION = "1.1.0"

MAX_CHARS_PER_MESSAGE = 1600
BATCH_SIZE = 24


@dataclass
class MessageCard:
    """The reduced view of a message that a worker sees."""

    msg_uid: str
    date: str
    sender: str
    recipients: str
    folder: str
    subject: str
    text: str
    notes: list[str]

    def render(self) -> str:
        head = (
            f"--- MESSAGE {self.msg_uid}\n"
            f"date: {self.date}\n"
            f"from: {self.sender}\n"
            f"to: {self.recipients}\n"
            f"folder: {self.folder}\n"
            f"subject: {self.subject}\n"
        )
        for note in self.notes:
            head += f"note: {note}\n"
        return head + "text:\n" + self.text + "\n"


def _short_addr(addr: str | None) -> str:
    if not addr:
        return "(none)"
    return addr.split("@")[0] if addr.endswith("@enron.com") else addr


def build_card(msg, cls: Classification) -> MessageCard:
    """Reduce one parsed message to the smallest useful view."""
    text = msg.novel_text.strip()
    notes: list[str] = []

    if len(text) > MAX_CHARS_PER_MESSAGE:
        table = detect_table(msg.body_decoded)
        if table is not None and table.generated:
            # Keep the prose before the table; drop the generated rows entirely.
            prose = msg.body_decoded[:table.start].strip()
            text = prose[:MAX_CHARS_PER_MESSAGE]
            notes.append(
                f"a {table.row_count}-row table was removed here: it is machine-generated "
                f"placeholder data (columns are exact functions of the row index), so no "
                f"quantity may be taken from it. The prose above is genuine."
            )
        else:
            head = text[: int(MAX_CHARS_PER_MESSAGE * 0.75)]
            tail = text[-int(MAX_CHARS_PER_MESSAGE * 0.2):]
            text = f"{head}\n[... {len(msg.novel_text) - len(head) - len(tail)} characters omitted ...]\n{tail}"
            notes.append("long message truncated in the middle")

    recipients = ", ".join(_short_addr(a) for a in (msg.recipients + msg.cc)[:6])
    if len(msg.recipients) + len(msg.cc) > 6:
        recipients += f" (+{len(msg.recipients) + len(msg.cc) - 6} more)"

    if "no_usable_date" in msg.flags:
        notes.append("this message has no usable date")
    if cls.category == "automated":
        notes.append("sender looks automated")

    return MessageCard(
        msg_uid=msg.msg_uid,
        date=msg.sent_at.strftime("%Y-%m-%d %a") if msg.sent_at else "unknown",
        sender=_short_addr(msg.sender),
        recipients=recipients or "(none)",
        folder=(msg.path.rsplit("/", 1)[0].replace("corpus/", "")),
        subject=msg.subject or "(no subject)",
        text=text or "(empty)",
        notes=notes,
    )


MESSAGE_STAGE = "extract_message"


def message_cards(
    messages,
    classifications: dict[str, Classification],
    *,
    prompt_hash: str,
    model: str,
    schema_hash: str,
) -> list[tuple[str, MessageCard, str]]:
    """Every message that should reach a model, with its own content-addressed cache key."""
    cards: list[tuple[str, MessageCard, str]] = []
    for m in messages:
        cls = classifications[m.msg_uid]
        if not cls.send_to_model:
            continue
        card = build_card(m, cls)
        key = sha256_text(
            "extract", m.file_sha256, str(m.novel_end), card.render(),
            prompt_hash, model, schema_hash, EXTRACT_VERSION,
        )
        cards.append((m.msg_uid, card, key))
    return cards


def build_units(
    cards: list[tuple[str, MessageCard, str]],
    *,
    batch_size: int = BATCH_SIZE,
) -> list[Unit]:
    """Batch the (uncached) message cards for dispatch.

    Batches are a transport detail, not a unit of work. The unit of work is one message,
    cached under its own key — see `message_cards`. Batching per-message-cached work means
    a changed batch boundary invalidates nothing: dedup got more conservative partway
    through this build, the survivor set changed, every batch boundary moved, and with a
    batch-keyed cache that alone would have thrown away 2,400 completed extractions.

    It is also what makes an interrupted run resume mid-batch rather than redoing it.
    """
    units: list[Unit] = []
    for i in range(0, len(cards), batch_size):
        chunk = cards[i:i + batch_size]
        units.append(_unit_from_chunk(chunk, f"extract_{i // batch_size:04d}"))
    return units


def _unit_from_chunk(chunk: list[tuple[str, MessageCard, str]], unit_id: str) -> Unit:
    payload = (
        f"Classify the following {len(chunk)} messages. Return one object per message.\n\n"
        + "\n".join(card.render() for _uid, card, _k in chunk)
    )
    return Unit(
        unit_id=unit_id,
        payload=payload,
        cache_key=sha256_text(*[k for _u, _c, k in chunk]),
        expected_ids={uid for uid, _c, _k in chunk},
        meta={"cards": chunk},
    )


def split_unit(unit: Unit) -> list[Unit]:
    """Bisect a batch that keeps failing, to isolate the message causing it."""
    chunk = unit.meta.get("cards") or []
    if len(chunk) < 2:
        return [unit]
    mid = len(chunk) // 2
    return [
        _unit_from_chunk(chunk[:mid], f"{unit.unit_id}a"),
        _unit_from_chunk(chunk[mid:], f"{unit.unit_id}b"),
    ]


def validate(parsed, unit: Unit) -> list[str]:
    """Reject a response that smuggles in a quantity, omits messages, or invents ids."""
    result = check_extraction_batch(parsed, unit.expected_ids)
    return result.violations


def load_schema(root: Path) -> tuple[dict, str]:
    """Load the extraction schema and its hash.

    `$schema` is stripped before the schema goes to the CLI: it rejects the draft-2020-12
    meta-schema URI outright ("no schema with key or ref ..."). The declaration stays in
    the file on disk so editors and JSON tooling still understand it. The hash is taken
    over the file text, so the cache key tracks what we wrote, not what we sent.
    """
    text = (root / "schemas/extraction.schema.json").read_text()
    schema = json.loads(text)
    schema.pop("$schema", None)
    return schema, sha256_text(text)


def load_system_prompt(root: Path) -> str:
    """Assemble the worker's entire context window from the `.claude/` files on disk.

    Read here rather than passed via `--agent` so the window is exactly these bytes, with
    no dependence on the CLAUDE.md that happens to sit in the runner's home directory.
    """
    agent = (root / ".claude/agents/message-extractor.md").read_text()
    skill = (root / ".claude/skills/enron-email-forensics/SKILL.md").read_text()
    agent = _strip_frontmatter(agent)
    skill = _strip_frontmatter(skill)
    return (
        "You are a batch extraction worker in a deterministic pipeline. You return JSON "
        "only.\n\n" + agent + "\n\n---\n\n# Domain reference\n\n" + skill
    )


def _strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4:].lstrip()
    return text