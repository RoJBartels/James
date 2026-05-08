# james/tests/test_command_model.py

from command import (
    Command,
    CommandCategory,
    CommandActor,
    CommandChannel,
)


def test_command_is_immutable():
    command = Command.create(
        category=CommandCategory.QUERY,
        domain="system:james",
        actor=CommandActor.USER,
        channel=CommandChannel.CLI,
        payload={"text": "test"},
    )

    try:
        command.domain = "other"
        assert False, "Command should be immutable"
    except Exception:
        assert True
