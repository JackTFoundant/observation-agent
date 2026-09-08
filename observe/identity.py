"""Resolving the same human across the several identifiers they appear under.

Enron's export writes one person many ways: `daren.farmer@enron.com`, `j..farmer@enron.com`
(a doubled dot where a middle initial was), and inside an X.500 distinguished name as
`Farmer, Daren J. </O=ENRON/OU=NA/CN=RECIPIENTS/CN=Dfarmer>`. Without resolution, every
per-person count and every participant-overlap signal downstream is garbage.

Union-find over co-occurrence evidence rather than a model call, because "are these the
same person" is a question with a right answer that we can derive from the headers, and a
model would guess. The evidence is deliberately conservative: we merge on a display name
that appears with two addresses, or on an X.500 CN that matches an address's local part.
Similar names alone are never enough — `mark.mcclure` and `mark.mccoy` are two people.
"""

from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import dataclass, field

IDENTITY_VERSION = "1.0.0"

_NAME_CLEAN = re.compile(r"[^a-z ]+")
_X500 = re.compile(r"^x500:(.+)$")


class UnionFind:
    def __init__(self) -> None:
        self.parent: dict[str, str] = {}

    def add(self, x: str) -> None:
        self.parent.setdefault(x, x)

    def find(self, x: str) -> str:
        self.add(x)
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[x] != root:            # path compression
            self.parent[x], x = root, self.parent[x]
        return root

    def union(self, a: str, b: str) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            # Deterministic winner so runs are reproducible.
            lo, hi = sorted((ra, rb))
            self.parent[hi] = lo


@dataclass
class Person:
    person_id: str
    canonical_address: str
    addresses: list[str] = field(default_factory=list)
    display_names: list[str] = field(default_factory=list)
    message_count: int = 0

    @property
    def label(self) -> str:
        if self.display_names:
            return sorted(self.display_names, key=lambda s: (-len(s), s))[0]
        return self.canonical_address


def _clean_display(name: str) -> str:
    """`Farmer, Daren </O=ENRON/...>` -> `farmer daren`."""
    name = name.split("</")[0].split("<")[0]
    name = _NAME_CLEAN.sub(" ", name.lower())
    return " ".join(sorted(w for w in name.split() if len(w) > 1))


def _local_part(addr: str) -> str:
    return addr.split("@", 1)[0] if "@" in addr else addr


def _name_tokens_from_address(addr: str) -> set[str]:
    return {t for t in re.split(r"[._\-]+", _local_part(addr)) if len(t) > 1}


def resolve(messages) -> tuple[dict[str, str], dict[str, Person]]:
    """Return (address -> person_id, person_id -> Person).

    Only header evidence is used, and only two merge rules, both of which require the
    corpus itself to link the identifiers:

    1. A cleaned display name (`X-From`) observed with two different addresses.
    2. An X.500 pseudo-address whose CN is a recognisable abbreviation of a real address's
       local part (`cn=dfarmer` <- `daren.farmer`).
    """
    uf = UnionFind()
    display_to_addrs: dict[str, set[str]] = defaultdict(set)
    addr_displays: dict[str, set[str]] = defaultdict(set)
    all_addrs: set[str] = set()
    counts: dict[str, int] = defaultdict(int)

    for m in messages:
        for addr in m.all_participants:
            uf.add(addr)
            all_addrs.add(addr)
        if m.sender:
            counts[m.sender] += 1
            if m.sender_display:
                key = _clean_display(m.sender_display)
                if key and " " in key:              # require at least two name words
                    display_to_addrs[key].add(m.sender)
                    addr_displays[m.sender].add(m.sender_display.split("</")[0].strip())

    # Rule 1: one display name, several addresses.
    for _key, addrs in display_to_addrs.items():
        addrs = sorted(addrs)
        for other in addrs[1:]:
            uf.union(addrs[0], other)

    # Rule 2: X.500 CN abbreviates a real address.
    real = [a for a in all_addrs if "@" in a]
    real_index: dict[str, list[str]] = defaultdict(list)
    for a in real:
        toks = _name_tokens_from_address(a)
        for t in toks:
            real_index[t].append(a)

    for a in all_addrs:
        m = _X500.match(a)
        if not m:
            continue
        cn = m.group(1).lower()
        # `dfarmer` -> initial 'd' + surname 'farmer'
        best: str | None = None
        for surname_len in range(len(cn) - 1, 2, -1):
            surname = cn[-surname_len:]
            initial = cn[:len(cn) - surname_len]
            if len(initial) > 2:
                continue
            for cand in real_index.get(surname, []):
                toks = _name_tokens_from_address(cand)
                if surname in toks and (not initial or any(t.startswith(initial) for t in toks)):
                    best = cand
                    break
            if best:
                break
        if best:
            uf.union(best, a)

    # Build people, preferring a real @-address as the canonical form.
    groups: dict[str, list[str]] = defaultdict(list)
    for a in all_addrs:
        groups[uf.find(a)].append(a)

    address_to_person: dict[str, str] = {}
    people: dict[str, Person] = {}
    for _root, addrs in sorted(groups.items()):
        addrs = sorted(addrs)
        with_at = [a for a in addrs if "@" in a and not a.startswith("x500:")]
        canonical = min(with_at, key=lambda a: (len(a), a)) if with_at else addrs[0]
        pid = "p_" + re.sub(r"[^a-z0-9]+", "_", canonical).strip("_")[:40]
        displays: set[str] = set()
        total = 0
        for a in addrs:
            displays |= addr_displays.get(a, set())
            total += counts.get(a, 0)
        person = Person(
            person_id=pid,
            canonical_address=canonical,
            addresses=addrs,
            display_names=sorted(displays)[:6],
            message_count=total,
        )
        people[pid] = person
        for a in addrs:
            address_to_person[a] = pid
    return address_to_person, people