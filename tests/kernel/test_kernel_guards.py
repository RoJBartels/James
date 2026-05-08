import pytest
from datetime import datetime

from core import JamesKernel
from core.events import (
    ExecutionRequested,
    ExecutionStarted,
    ExecutionFinished,
)


def test_feature_level_guard_blocks_in_fl1():
    kernel = JamesKernel()

    event = ExecutionStarted("exec1", datetime.now())
    result = kernel._guard_feature_level(event)

    assert result.allowed is False
    assert result.reason == "feature_level_blocked"


def test_state_consistency_execution_started_duplicate():
    kernel = JamesKernel()
    kernel.state.running_jobs.append("exec1")

    event = ExecutionStarted("exec1", datetime.now())
    result = kernel._guard_state_consistency(event)

    assert result.allowed is False
    assert result.reason == "execution_already_running"


def test_state_consistency_execution_finished_not_running():
    kernel = JamesKernel()

    event = ExecutionFinished("exec1", datetime.now(), success=True)
    result = kernel._guard_state_consistency(event)

    assert result.allowed is False
    assert result.reason == "execution_not_running"


def test_state_consistency_execution_requested_allowed():
    kernel = JamesKernel()

    event = ExecutionRequested("req1", datetime.now())
    result = kernel._guard_state_consistency(event)

    assert result.allowed is True


def test_invariant_duplicate_running_jobs_detected():
    kernel = JamesKernel()
    kernel.state.running_jobs = ["exec1", "exec1"]

    event = ExecutionStarted("exec2", datetime.now())
    result = kernel._guard_invariants(event)

    assert result.allowed is False
    assert result.reason == "duplicate_running_jobs_detected"