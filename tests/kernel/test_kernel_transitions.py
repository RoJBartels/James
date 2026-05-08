from datetime import datetime

from core import JamesKernel
from core.events import (
    ExecutionStarted,
    ExecutionFinished,
)


def test_execution_started_does_not_mutate_state_in_fl1():
    kernel = JamesKernel()

    event = ExecutionStarted("exec1", datetime.now())
    kernel.handle_event(event)

    assert kernel.state.running_jobs == []


def test_execution_finished_does_not_mutate_state_in_fl1():
    kernel = JamesKernel()
    kernel.state.running_jobs.append("exec1")

    event = ExecutionFinished("exec1", datetime.now(), success=True)
    kernel.handle_event(event)

    # Still unchanged because G1 blocks
    assert kernel.state.running_jobs == ["exec1"]
    
def test_execution_started_mutates_state_in_fl2():
    kernel = JamesKernel()
    kernel.state.feature_level = 2

    kernel.handle_event(
        ExecutionStarted("exec1", datetime.now())
    )

    assert kernel.state.running_jobs == ["exec1"]
    
def test_duplicate_execution_started_blocked_in_fl2():
    kernel = JamesKernel()
    kernel.state.feature_level = 2

    kernel.handle_event(
        ExecutionStarted("exec1", datetime.now())
    )

    kernel.handle_event(
        ExecutionStarted("exec1", datetime.now())
    )

    # Still only one entry
    assert kernel.state.running_jobs == ["exec1"]
    
def test_parallel_execution_started_allowed_in_fl2():
    kernel = JamesKernel()
    kernel.state.feature_level = 2

    kernel.handle_event(
        ExecutionStarted("exec1", datetime.now())
    )

    kernel.handle_event(
        ExecutionStarted("exec2", datetime.now())
    )

    assert set(kernel.state.running_jobs) == {"exec1", "exec2"}
    
def test_running_jobs_order_is_append_order():
    kernel = JamesKernel()
    kernel.state.feature_level = 2

    kernel.handle_event(
        ExecutionStarted("execA", datetime.now())
    )

    kernel.handle_event(
        ExecutionStarted("execB", datetime.now())
    )

    assert kernel.state.running_jobs == ["execA", "execB"]
    
def test_execution_finished_without_start_blocked_fl2():
    kernel = JamesKernel()
    kernel.state.feature_level = 2

    kernel.handle_event(
        ExecutionFinished("exec1", datetime.now(), success=True)
    )

    assert kernel.state.running_jobs == []