# james/tests/test_command_validation.py

import pytest

from command import (
    Command,
    CommandCategory,
    CommandActor,
    CommandChannel,
)
from core.handlers import command_validation_handler
from core.errors import InvalidCommandError
from core.state import KernelState


def test_valid_command_passes_validation():
    state = KernelState()

    command = Command.create(
        category=CommandCategory.QUERY,
        domain="system:james",
        actor=CommandActor.USER,
        channel=CommandChannel.CLI,
        payload={"text": "ok"},
    )

    command_validation_handler(command, state)


def test_invalid_command_empty_domain_fails():
    state = KernelState()

    command = Command.create(
        category=CommandCategory.QUERY,
        domain="",
        actor=CommandActor.USER,
        channel=CommandChannel.CLI,
        payload={"text": "fail"},
    )

    with pytest.raises(InvalidCommandError):
        command_validation_handler(command, state)
