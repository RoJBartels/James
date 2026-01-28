from core.kernel import JamesKernel
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
