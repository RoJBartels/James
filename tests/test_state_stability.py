from core.kernel import JamesKernel
from command import (
    Command,
    CommandCategory,
    CommandActor,
    CommandChannel,
)


def test_state_is_unchanged_by_command():
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
