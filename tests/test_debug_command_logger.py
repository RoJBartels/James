from command import (
    Command,
    CommandCategory,
    CommandActor,
    CommandChannel,
)
from core.handlers import debug_command_logger
from core.state import KernelState


def test_debug_command_logger_does_not_modify_state():
    state = KernelState()
    before = state.snapshot()

    command = Command.create(
        category=CommandCategory.QUERY,
        domain="system:james",
        actor=CommandActor.USER,
        channel=CommandChannel.CLI,
        payload={"text": "debug"},
    )

    debug_command_logger(command, state)

    after = state.snapshot()
    assert before == after
