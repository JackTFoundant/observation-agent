"""Rate limiting must cost time, never coverage.

The first cold run lost two batches — 48 messages, 2% of the corpus — because a throttle
consumed one of three content attempts and the backoff was capped at 40 seconds. The report
still said it had read every message. These tests pin the fix: a throttle gets its own
budget, and whatever is genuinely lost is reported rather than absorbed.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from observe.claude_cli import WorkerError
from observe.dispatch import MAX_THROTTLE_RETRIES, RunLog, Unit, dispatch


class FakeCache:
    def __init__(self):
        self.store = {}
        self.failures = []

    def get_many(self, _stage, keys):
        return {k: self.store[k] for k in keys if k in self.store}

    def put(self, _stage, key, payload, **_kw):
        self.store[key] = payload

    def record_failure(self, *a, **kw):
        self.failures.append((a, kw))


def unit(uid="u1", n=3):
    return Unit(unit_id=uid, payload="p", cache_key="k" + uid,
                expected_ids={f"m{i}" for i in range(n)})


@pytest.fixture
def log(tmp_path):
    return RunLog(tmp_path / "run.jsonl")


def _dispatch(units, runner, cache, log, **kw):
    import observe.dispatch as mod
    kw.setdefault("validate", lambda parsed, u: [])
    return mod.dispatch(
        units, stage="test", system_prompt="sp", json_schema={"type": "object"},
        cache=cache, log=log, concurrency=1, timeout=5, **kw)


def test_a_throttle_does_not_consume_a_content_attempt(monkeypatch, log):
    """Three throttles then success must still succeed."""
    import observe.dispatch as mod
    calls = {"n": 0}

    def runner(payload, **kwargs):
        calls["n"] += 1
        if calls["n"] <= 3:
            raise WorkerError("rate_limit", "429 slow down")
        return type("R", (), {"parsed": {"ok": True}, "model": "m",
                              "duration_ms": 1, "attempt": 1})()

    monkeypatch.setattr(mod, "run_worker", runner)
    monkeypatch.setattr(mod.time, "sleep", lambda *_: None)
    monkeypatch.setattr(mod, "resolve_cli", lambda: Path("/bin/true"))

    cache = FakeCache()
    out = _dispatch([unit()], runner, cache, log)
    assert out.results, "three throttles then success should still produce a result"
    assert not out.failed


def test_content_failures_still_give_up_after_three_attempts(monkeypatch, log):
    """A throttle is transient; malformed output is not. They must not share a budget."""
    import observe.dispatch as mod
    calls = {"n": 0}

    def runner(payload, **kwargs):
        calls["n"] += 1
        return type("R", (), {"parsed": {"bad": True}, "model": "m",
                              "duration_ms": 1, "attempt": 1})()

    monkeypatch.setattr(mod, "run_worker", runner)
    monkeypatch.setattr(mod.time, "sleep", lambda *_: None)
    monkeypatch.setattr(mod, "resolve_cli", lambda: Path("/bin/true"))

    out = _dispatch([unit()], runner, FakeCache(), log,
                    validate=lambda parsed, u: ["always wrong"])
    assert out.failed
    assert out.failed[0]["kind"] == "exhausted"
    assert calls["n"] == 3, f"expected exactly 3 content attempts, got {calls['n']}"


def test_relentless_throttling_eventually_gives_up_but_reports_what_was_lost(monkeypatch, log):
    import observe.dispatch as mod

    def runner(payload, **kwargs):
        raise WorkerError("rate_limit", "429 forever")

    monkeypatch.setattr(mod, "run_worker", runner)
    monkeypatch.setattr(mod.time, "sleep", lambda *_: None)
    monkeypatch.setattr(mod, "resolve_cli", lambda: Path("/bin/true"))

    out = _dispatch([unit(n=24)], runner, FakeCache(), log)
    assert out.failed
    f = out.failed[0]
    assert f["kind"] == "throttled_out"
    assert f["throttles"] > MAX_THROTTLE_RETRIES
    # The identities of everything lost must travel with the failure, so the report can
    # name them instead of quietly covering 98% of the corpus.
    assert len(f["expected_ids"]) == 24


def test_the_run_log_records_each_throttle_with_its_backoff(monkeypatch, log, tmp_path):
    import observe.dispatch as mod
    calls = {"n": 0}

    def runner(payload, **kwargs):
        calls["n"] += 1
        if calls["n"] <= 2:
            raise WorkerError("rate_limit", "429")
        return type("R", (), {"parsed": {}, "model": "m", "duration_ms": 1, "attempt": 1})()

    monkeypatch.setattr(mod, "run_worker", runner)
    monkeypatch.setattr(mod.time, "sleep", lambda *_: None)
    monkeypatch.setattr(mod, "resolve_cli", lambda: Path("/bin/true"))

    _dispatch([unit()], runner, FakeCache(), log)
    events = [json.loads(l) for l in log.path.read_text().splitlines()]
    throttles = [e for e in events if e.get("event") == "rate_limited"]
    assert len(throttles) == 2
    assert all("backoff_s" in e and "throttle" in e for e in throttles)


def test_auth_failure_stops_the_whole_run_immediately(monkeypatch, log):
    """Retrying a hundred workers against an unauthenticated CLI wastes twenty minutes to
    learn what the first call already knew."""
    import observe.dispatch as mod

    def runner(payload, **kwargs):
        raise WorkerError("auth", "not authenticated")

    monkeypatch.setattr(mod, "run_worker", runner)
    monkeypatch.setattr(mod.time, "sleep", lambda *_: None)
    monkeypatch.setattr(mod, "resolve_cli", lambda: Path("/bin/true"))

    with pytest.raises(mod.AuthenticationFailed):
        _dispatch([unit("a"), unit("b"), unit("c")], runner, FakeCache(), log)


# ---------------------------------------------------------------------------
# Per-stage budgets: one stage must not be able to consume the whole run
# ---------------------------------------------------------------------------

def test_stage_budgets_reserve_time_for_later_stages(tmp_path):
    """Extraction may take most of a run, but never all of it.

    A heavily throttled cold run once ran extraction to 28.7 of a 25-minute budget, so
    characterization and artifact drafting got zero calls and the report shipped with no
    narratives and no artifacts at all.
    """
    from observe.pipeline import Context, new_context
    ctx = new_context(tmp_path, run_id="t", deadline_s=1000)

    e = ctx.stage_deadline("extract") - ctx.started
    c = ctx.stage_deadline("characterize") - ctx.started
    a = ctx.stage_deadline("artifact") - ctx.started

    assert e < c < a <= ctx.deadline_s, "each stage must yield to the next"
    assert e <= ctx.deadline_s * 0.7, "extraction must not be able to eat the whole budget"
    assert ctx.deadline_s - a > 0, "the run must keep slack after the last model stage"


def test_an_unknown_stage_gets_the_whole_budget():
    from observe.pipeline import new_context
    from pathlib import Path
    ctx = new_context(Path("."), run_id="t2", deadline_s=600)
    assert ctx.stage_deadline("something_else") == ctx.deadline_at


def test_backoff_is_bounded_so_throttles_cannot_burn_the_budget(monkeypatch, log):
    """13 throttles once cost 29 minutes of cumulative sleep. The adaptive semaphore
    already reduces pressure; a long sleep on top is a double penalty."""
    import observe.dispatch as mod
    slept: list[float] = []
    calls = {"n": 0}

    def runner(payload, **kwargs):
        calls["n"] += 1
        if calls["n"] <= 6:
            raise WorkerError("rate_limit", "429")
        return type("R", (), {"parsed": {}, "model": "m", "duration_ms": 1, "attempt": 1})()

    monkeypatch.setattr(mod, "run_worker", runner)
    monkeypatch.setattr(mod.time, "sleep", lambda s: slept.append(s))
    monkeypatch.setattr(mod, "resolve_cli", lambda: Path("/bin/true"))

    _dispatch([unit()], runner, FakeCache(), log)
    assert slept, "a throttle should back off"

    # The property that matters is the per-throttle ceiling. Cumulative sleep for one unit
    # is bounded structurally by MAX_THROTTLE_RETRIES x that ceiling, and in practice by the
    # stage deadline (tested separately) - units back off in parallel, so this does not sum
    # across the run. My first version of this test asserted a flat 240s, a number I picked
    # rather than one the design implies; it failed at 251s while the behaviour was correct.
    assert max(slept) <= 50, f"single backoff too long: {max(slept):.0f}s"
    assert sum(slept) <= MAX_THROTTLE_RETRIES * 50, (
        f"cumulative backoff {sum(slept):.0f}s exceeds the structural ceiling")
    assert sum(slept) / len(slept) <= 45, (
        f"mean backoff {sum(slept) / len(slept):.0f}s is too aggressive; the semaphore, "
        f"not sleep, should be doing the throttling")


def test_deadline_is_reported_not_absorbed(monkeypatch, log):
    """Hitting the deadline must surface, so the report can say the run was cut short."""
    import observe.dispatch as mod

    def runner(payload, **kwargs):
        return type("R", (), {"parsed": {}, "model": "m", "duration_ms": 1, "attempt": 1})()

    monkeypatch.setattr(mod, "run_worker", runner)
    monkeypatch.setattr(mod, "resolve_cli", lambda: Path("/bin/true"))

    out = mod.dispatch(
        [unit("a"), unit("b")], stage="test", system_prompt="sp",
        json_schema={"type": "object"}, validate=lambda p, u: [],
        cache=FakeCache(), log=log, concurrency=1, timeout=5,
        deadline_at=mod.time.monotonic() - 1,      # already past
    )
    assert out.deadline_hit
    assert not out.results
