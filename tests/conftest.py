"""Make model calls impossible in tests, mechanically rather than by convention.

The assignment requires that "tests pass without invoking a model at all". A promise not to
call one is not the same as being unable to, so the autouse fixture below replaces the only
function in the system that shells out to the CLI with one that raises.

Any stage that would normally consult a model instead reads a frozen response from
`tests/golden/`, which doubles as a cassette of what real workers actually returned.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

GOLDEN = Path(__file__).parent / "golden"


class ModelCallAttempted(AssertionError):
    """Raised if any test path tries to reach a model."""


def _forbidden(*args, **kwargs):
    raise ModelCallAttempted(
        "a test attempted a model call. Tests must run with zero model invocations; "
        "use a frozen fixture from tests/golden/ instead."
    )


@pytest.fixture(autouse=True)
def no_model_calls(monkeypatch):
    """Block every route to a model for the duration of every test."""
    import observe.claude_cli as cli

    monkeypatch.setattr(cli, "run_worker", _forbidden, raising=True)
    monkeypatch.setattr(cli, "doctor", _forbidden, raising=True)
    # dispatch imports run_worker by name, so patch its binding too.
    import observe.dispatch as dispatch
    monkeypatch.setattr(dispatch, "run_worker", _forbidden, raising=True)
    yield


@pytest.fixture
def model_guard_is_armed():
    """Lets a test assert the guard exists and actually trips."""
    import observe.claude_cli as cli
    return cli.run_worker


@pytest.fixture
def frozen_extraction() -> dict:
    return json.loads((GOLDEN / "clean_extraction.json").read_text())


@pytest.fixture
def poisoned_extraction() -> dict:
    return json.loads((GOLDEN / "poisoned_extraction.json").read_text())


@pytest.fixture
def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]
