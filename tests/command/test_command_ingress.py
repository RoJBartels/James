# james/tests/test_command_ingress.py

from command import (
    Command,
    CommandCategory,
    CommandActor,
    CommandChannel,
)
from core.handlers import command_ingress_handler
from core.state import KernelState


def test_command_ingress_does_not_modify_state():
    state = KernelState()
    before = state.snapshot()

    command = Command.create(
        category=CommandCategory.QUERY,
        domain="system:james",
        actor=CommandActor.USER,
        channel=CommandChannel.CLI,
        payload={"text": "test"},
    )

    command_ingress_handler(command, state)

    after = state.snapshot()
    assert before == after
