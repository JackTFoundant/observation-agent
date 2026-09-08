"""Parallel dispatch of headless workers, with the failure handling that makes a run
unattended.

The design goal is that nothing here ever needs a human. Every failure mode has a
predetermined response, and the run finishes with a complete report even when some of it
went wrong — a degraded, honestly-annotated report beats a crash at minute 29.

The one failure that stops the run immediately is authentication. Retrying 76 workers
against an unauthenticated CLI wastes twenty minutes to learn something the first call
already knew.
"""

from __future__ import annotations

import json
import random
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

from observe.claude_cli import WorkerError, resolve_cli, run_worker

DISPATCH_VERSION = "1.1.0"

# How many times a single unit may be re-queued after a rate limit before we give up on it.
# Generous on purpose: a throttle is transient and costs us nothing but time, whereas
# dropping the unit costs us corpus coverage. The run deadline is the real stop.
MAX_THROTTLE_RETRIES = 12


class RunDeadlineExceeded(Exception):
    pass


class AuthenticationFailed(Exception):
    pass


@dataclass
class RunLog:
    """Append-only JSONL. This *is* the run-logs deliverable."""

    path: Path
    _lock: threading.Lock = field(default_factory=threading.Lock)

    def __post_init__(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def event(self, **fields) -> None:
        """Append one event. Never raises.

        Logging must not be able to kill a run. It once did: the run directory was removed
        while a run was in flight and the resulting `FileNotFoundError` propagated out of a
        worker thread and took down twenty minutes of work. A run that cannot write its log
        should carry on and lose the log, not the opposite.
        """
        record = {"ts": round(time.time(), 3), **fields}
        line = json.dumps(record, separators=(",", ":"), default=str)
        with self._lock:
            for attempt in (1, 2):
                try:
                    with self.path.open("a") as fh:
                        fh.write(line + "\n")
                    return
                except FileNotFoundError:
                    if attempt == 1:
                        self.path.parent.mkdir(parents=True, exist_ok=True)
                        continue
                except OSError:
                    return


class AdaptiveSemaphore:
    """Concurrency that backs off on rate limits and recovers on clean completions.

    A fixed pool either wastes the budget or trips the limit; which one depends on how much
    of the subscription the grader has already spent today, which we cannot know.
    """

    def __init__(self, initial: int, floor: int = 2, ceiling: int = 12):
        self._cond = threading.Condition()
        self.limit = initial
        self.floor = floor
        self.ceiling = ceiling
        self.active = 0
        self._clean_since = time.monotonic()
        self.reductions = 0

    def acquire(self) -> None:
        with self._cond:
            while self.active >= self.limit:
                self._cond.wait(timeout=1.0)
            self.active += 1

    def release(self) -> None:
        with self._cond:
            self.active -= 1
            self._cond.notify()

    def penalize(self) -> None:
        with self._cond:
            new = max(self.floor, self.limit // 2)
            if new != self.limit:
                self.limit = new
                self.reductions += 1
            self._clean_since = time.monotonic()

    def reward(self) -> None:
        with self._cond:
            if self.limit < self.ceiling and time.monotonic() - self._clean_since > 60:
                self.limit += 1
                self._clean_since = time.monotonic()
                self._cond.notify()


@dataclass
class Unit:
    """One piece of work: a batch of messages, a cluster, an artifact."""

    unit_id: str
    payload: str
    cache_key: str
    expected_ids: set[str] = field(default_factory=set)
    meta: dict = field(default_factory=dict)


@dataclass
class DispatchOutcome:
    results: dict[str, object]
    failed: list[dict]
    cache_hits: int
    model_calls: int
    deadline_hit: bool


def dispatch(
    units: list[Unit],
    *,
    stage: str,
    system_prompt: str,
    json_schema: dict,
    validate: Callable[[object, Unit], list[str]],
    cache,
    log: RunLog,
    model: str = "sonnet",
    effort: str | None = None,
    concurrency: int = 8,
    timeout: int = 240,
    deadline_at: float | None = None,
    max_model_calls: int = 400,
    split: Callable[[Unit], list[Unit]] | None = None,
) -> DispatchOutcome:
    """Run every unit, using the cache where possible.

    `validate` returns a list of problems; a non-empty list means the response is rejected
    and retried. `split` lets a failing batch be bisected — one pathological message
    otherwise poisons its whole batch, and bisection isolates it in two extra calls instead
    of losing twenty-five extractions.
    """
    results: dict[str, object] = {}
    failed: list[dict] = []
    cli = resolve_cli()
    sem = AdaptiveSemaphore(concurrency)
    calls = 0
    calls_lock = threading.Lock()
    stop = threading.Event()
    auth_error: list[str] = []

    # Cache pass first, so the log shows honestly how much work was skipped.
    pending: list[Unit] = []
    cached = cache.get_many(stage, [u.cache_key for u in units])
    for u in units:
        if u.cache_key in cached:
            results[u.unit_id] = cached[u.cache_key]
        else:
            pending.append(u)
    log.event(stage=stage, event="cache_pass", cached=len(cached), pending=len(pending))

    def budget_ok() -> bool:
        nonlocal calls
        with calls_lock:
            if calls >= max_model_calls:
                return False
            calls += 1
            return True

    def attempt_unit(unit: Unit, depth: int = 0) -> None:
        if stop.is_set():
            return
        if deadline_at and time.monotonic() > deadline_at:
            stop.set()
            return

        last: dict | None = None
        attempt = 0
        throttles = 0
        # A rate limit does not consume a content attempt.
        #
        # The first cold run lost two whole batches - 48 messages, 2% of the corpus - to
        # rate limiting, because a throttle was counted as one of three attempts and the
        # backoff was capped at 40s. But a throttle is transient and is not the unit's
        # fault, whereas malformed JSON is and deserves to give up. Conflating them meant
        # the run silently covered 98% of a corpus it claimed to read in full.
        #
        # So throttles get their own budget and a much longer backoff, and the only thing
        # that finally stops them is the run deadline - at which point the coverage gap is
        # reported loudly rather than absorbed.
        while attempt < 3 and throttles <= MAX_THROTTLE_RETRIES:
            if stop.is_set():
                return
            if deadline_at and time.monotonic() > deadline_at:
                stop.set()
                return
            attempt += 1
            if not budget_ok():
                failed.append({"unit_id": unit.unit_id, "kind": "budget",
                               "detail": f"max_model_calls={max_model_calls} reached"})
                log.event(stage=stage, unit_id=unit.unit_id, event="budget_exhausted")
                return

            prompt = system_prompt
            if attempt > 1 and last:
                prompt = (
                    system_prompt
                    + "\n\n## Your previous response was rejected\n"
                    + "\n".join(f"- {v}" for v in last.get("problems", [])[:8])
                    + "\n\nReturn only valid JSON matching the schema, covering every "
                      "message id you were given exactly once."
                )

            sem.acquire()
            try:
                res = run_worker(
                    unit.payload,
                    system_prompt=prompt,
                    model=model,
                    json_schema=json_schema,
                    effort=effort if attempt == 1 else "medium",
                    timeout=timeout,
                    cli=cli,
                    attempt=attempt,
                )
            except WorkerError as e:
                sem.release()
                if e.kind == "auth":
                    auth_error.append(e.detail)
                    stop.set()
                    log.event(stage=stage, unit_id=unit.unit_id, event="auth_failed", detail=e.detail)
                    return
                if e.kind == "rate_limit":
                    sem.penalize()
                    throttles += 1
                    attempt -= 1          # a throttle is not a content failure
                    # Capped well below the old 180s. The adaptive semaphore already
                    # halves concurrency on a throttle, so a long sleep on top is a double
                    # penalty: 13 throttles once cost 29 minutes of cumulative sleep and
                    # starved every later stage. Retry often, sleep briefly, let the
                    # semaphore do the throttling.
                    backoff = min(45, 8 * (2 ** min(throttles, 3))) + random.uniform(0, 5)
                    log.event(stage=stage, unit_id=unit.unit_id, event="rate_limited",
                              throttle=throttles, new_limit=sem.limit,
                              backoff_s=round(backoff, 1))
                    time.sleep(backoff)
                    last = {"problems": [f"rate limited: {e.detail}"]}
                    continue
                log.event(stage=stage, unit_id=unit.unit_id, event="worker_error",
                          kind=e.kind, attempt=attempt, detail=e.detail[:300])
                cache.record_failure(stage, unit.unit_id, e.kind, e.detail, attempt)
                last = {"problems": [f"{e.kind}: {e.detail}"]}
                time.sleep(random.uniform(1, 4))
                continue
            else:
                sem.release()
                sem.reward()

            problems = validate(res.parsed, unit)
            if not problems:
                cache.put(stage, unit.cache_key, res.parsed, unit_id=unit.unit_id,
                          model=res.model, duration_ms=res.duration_ms)
                results[unit.unit_id] = res.parsed
                log.event(stage=stage, unit_id=unit.unit_id, event="ok", attempt=attempt,
                          duration_ms=res.duration_ms, model=res.model,
                          payload_chars=len(unit.payload))
                return

            log.event(stage=stage, unit_id=unit.unit_id, event="rejected", attempt=attempt,
                      problems=problems[:5])
            cache.record_failure(stage, unit.unit_id, "validation", "; ".join(problems), attempt)
            last = {"problems": problems}

            # After the second rejection, bisect rather than keep asking the same question
            # — but only when the problems look *localized*. A rejection that names most
            # of the batch is a systematic fault (a bad schema, a guard bug), and bisecting
            # it just multiplies one wasted call into a dozen. Splitting is for isolating
            # a single pathological message, which is what it costs two calls to find.
            localized = len(problems) <= max(2, len(unit.expected_ids) // 2)
            if attempt == 2 and split and depth < 2 and localized:
                halves = split(unit)
                if len(halves) > 1:
                    log.event(stage=stage, unit_id=unit.unit_id, event="bisect",
                              parts=[h.unit_id for h in halves])
                    for h in halves:
                        attempt_unit(h, depth + 1)
                    return

        kind = "throttled_out" if throttles > MAX_THROTTLE_RETRIES else "exhausted"
        failed.append({
            "unit_id": unit.unit_id,
            "kind": kind,
            "throttles": throttles,
            "expected_ids": sorted(unit.expected_ids),
            "detail": "; ".join((last or {}).get("problems", ["unknown"]))[:500],
        })
        log.event(stage=stage, unit_id=unit.unit_id, event="failed_permanently",
                  kind=kind, throttles=throttles, units_lost=len(unit.expected_ids))

    with ThreadPoolExecutor(max_workers=max(sem.ceiling, concurrency)) as pool:
        futures = [pool.submit(attempt_unit, u) for u in pending]
        for f in as_completed(futures):
            f.result()

    if auth_error:
        raise AuthenticationFailed(auth_error[0])

    deadline_hit = bool(deadline_at and time.monotonic() > deadline_at)
    if deadline_hit:
        log.event(stage=stage, event="deadline_reached",
                  completed=len(results), total=len(units))

    return DispatchOutcome(
        results=results,
        failed=failed,
        cache_hits=len(cached),
        model_calls=calls,
        deadline_hit=deadline_hit,
    )