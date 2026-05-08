# james/tests/test_router_handler.py

from command import (
    Command,
    CommandCategory,
    CommandActor,
    CommandChannel,
)
from core.handlers import router_handler
from core.state import KernelState


def test_router_does_not_modify_state():
    state = KernelState()
    before = state.snapshot()

    command = Command.create(
        category=CommandCategory.QUERY,
        domain="system:james",
        actor=CommandActor.USER,
        channel=CommandChannel.CLI,
        payload={"text": "route me"},
    )

    router_handler(command, state)

    after = state.snapshot()
    assert before == after
