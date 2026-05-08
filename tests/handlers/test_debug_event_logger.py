from core.events import SystemEvent
from core.handlers import debug_event_logger
from core.state import KernelState


def test_debug_event_logger_does_not_modify_state():
    state = KernelState()
    before = state.snapshot()

    event = SystemEvent(name="test-event", payload={"x": 1})
    debug_event_logger(event, state)

    after = state.snapshot()
    assert before == after
