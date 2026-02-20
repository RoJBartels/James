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