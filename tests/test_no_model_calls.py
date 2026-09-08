"""The guard that makes 'tests pass without invoking a model' mechanical rather than
aspirational."""

from __future__ import annotations

import pytest

from tests.conftest import ModelCallAttempted


def test_the_guard_is_installed_and_trips(model_guard_is_armed):
    with pytest.raises(ModelCallAttempted):
        model_guard_is_armed("payload", system_prompt="x")


def test_dispatch_cannot_reach_a_model():
    import observe.dispatch as dispatch
    with pytest.raises(ModelCallAttempted):
        dispatch.run_worker("payload", system_prompt="x")


def test_doctor_cannot_reach_a_model():
    import observe.claude_cli as cli
    with pytest.raises(ModelCallAttempted):
        cli.doctor()


def test_importing_the_whole_pipeline_makes_no_model_call():
    """Import-time side effects are a real way this could break."""
    import observe.cli            # noqa: F401
    import observe.pipeline       # noqa: F401
    import observe.reduce.artifacts  # noqa: F401
    import observe.reduce.render  # noqa: F401
    import observe.serve          # noqa: F401
    import observe.verify         # noqa: F401
