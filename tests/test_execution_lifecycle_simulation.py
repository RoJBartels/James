from datetime import datetime

from core import JamesKernel
from core.events import (
    ExecutionRequested,
    ExecutionStarted,
    ExecutionFinished,
)


def test_single_execution_lifecycle_simulation_fl1():
    kernel = JamesKernel()

    # 1️⃣ Requested
    kernel.handle_event(
        ExecutionRequested("req1", datetime.now())
    )

    # 2️⃣ Started
    kernel.handle_event(
        ExecutionStarted("exec1", datetime.now())
    )

    # 3️⃣ Finished
    kernel.handle_event(
        ExecutionFinished("exec1", datetime.now(), success=True)
    )

    # In Feature-Level 1:
    # No transition is active → no state mutation
    assert kernel.state.running_jobs == []


def test_multiple_sequential_executions_fl1():
    kernel = JamesKernel()

    # Execution A
    kernel.handle_event(
        ExecutionRequested("reqA", datetime.now())
    )
    kernel.handle_event(
        ExecutionStarted("execA", datetime.now())
    )
    kernel.handle_event(
        ExecutionFinished("execA", datetime.now(), success=True)
    )

    # Execution B
    kernel.handle_event(
        ExecutionRequested("reqB", datetime.now())
    )
    kernel.handle_event(
        ExecutionStarted("execB", datetime.now())
    )
    kernel.handle_event(
        ExecutionFinished("execB", datetime.now(), success=False)
    )

    # Still no mutation in FL1
    assert kernel.state.running_jobs == []


def test_interleaved_execution_events_fl1():
    """
    Simulates partially overlapping execution events.
    Even though logically inconsistent,
    FL1 must remain stable and non-mutating.
    """

    kernel = JamesKernel()

    kernel.handle_event(
        ExecutionStarted("exec1", datetime.now())
    )

    kernel.handle_event(
        ExecutionStarted("exec2", datetime.now())
    )

    kernel.handle_event(
        ExecutionFinished("exec1", datetime.now(), success=True)
    )

    # No mutation allowed in FL1
    assert kernel.state.running_jobs == []
    
    
def test_execution_lifecycle_fl2():
    kernel = JamesKernel()
    kernel.state.feature_level = 2

    kernel.handle_event(
        ExecutionStarted("exec1", datetime.now())
    )

    assert kernel.state.running_jobs == ["exec1"]

    kernel.handle_event(
        ExecutionFinished("exec1", datetime.now(), success=True)
    )

    assert kernel.state.running_jobs == []
    
def test_parallel_execution_lifecycle_fl2():
    kernel = JamesKernel()
    kernel.state.feature_level = 2

    kernel.handle_event(
        ExecutionStarted("execA", datetime.now())
    )

    kernel.handle_event(
        ExecutionStarted("execB", datetime.now())
    )

    assert set(kernel.state.running_jobs) == {"execA", "execB"}

    kernel.handle_event(
        ExecutionFinished("execA", datetime.now(), success=True)
    )

    assert kernel.state.running_jobs == ["execB"]