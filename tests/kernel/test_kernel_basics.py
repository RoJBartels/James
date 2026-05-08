# james/tests/test_kernel_basics.py

from core import JamesKernel
from command import (
    Command,
    CommandCategory,
    CommandActor,
    CommandChannel,
)


def test_kernel_handles_command_without_crash():
    kernel = JamesKernel()

    command = Command.create(
        category=CommandCategory.QUERY,
        domain="system:james",
        actor=CommandActor.USER,
        channel=CommandChannel.CLI,
        payload={"text": "test"},
    )

    kernel.handle_command(command)


def test_state_is_stable_on_command():
    kernel = JamesKernel()
    before = kernel.snapshot()

    command = Command.create(
        category=CommandCategory.QUERY,
        domain="system:james",
        actor=CommandActor.USER,
        channel=CommandChannel.CLI,
        payload={"text": "status"},
    )

    kernel.handle_command(command)
    after = kernel.snapshot()

    assert before == after
