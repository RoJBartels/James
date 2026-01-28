from typing import Any

from command import Command, CommandActor, CommandCategory, CommandChannel
from core.state import KernelState
from core.errors import InvalidCommandError


def command_validation_handler(command: Command, state: KernelState) -> None:
    """
    Formale, strukturielle Validierung eines Commands.

    - keine Semantik
    - keine Policies
    - keine State-Änderung
    """

    # ---- Pflichtfelder vorhanden ----
    if command.id is None:
        raise InvalidCommandError("Command.id must be set")

    if not isinstance(command.category, CommandCategory):
        raise InvalidCommandError("Command.category must be CommandCategory")

    if not isinstance(command.actor, CommandActor):
        raise InvalidCommandError("Command.actor must be CommandActor")

    if not isinstance(command.channel, CommandChannel):
        raise InvalidCommandError("Command.channel must be CommandChannel")

    # ---- Domain ----
    if not isinstance(command.domain, str):
        raise InvalidCommandError("Command.domain must be a string")

    if command.domain.strip() == "":
        raise InvalidCommandError("Command.domain must not be empty")

    # ---- Payload ----
    if not isinstance(command.payload, dict):
        raise InvalidCommandError("Command.payload must be a dict")

    # Payload muss JSON-ähnlich sein (flach geprüft)
    for key, value in command.payload.items():
        if not isinstance(key, str):
            raise InvalidCommandError("Command.payload keys must be strings")
        _assert_json_compatible(value, path=f"payload.{key}")

    # ---- Metadata (optional, aber wirkungslos) ----
    if command.metadata is not None:
        if not isinstance(command.metadata, dict):
            raise InvalidCommandError("Command.metadata must be a dict or None")

        for key in command.metadata.keys():
            if not isinstance(key, str):
                raise InvalidCommandError("Command.metadata keys must be strings")


def _assert_json_compatible(value: Any, path: str) -> None:
    """
    Minimaler JSON-Kompatibilitätscheck.
    Keine Tiefen-Semantik, nur Struktur.
    """
    if value is None:
        return
    if isinstance(value, (str, int, float, bool)):
        return
    if isinstance(value, list):
        for i, item in enumerate(value):
            _assert_json_compatible(item, f"{path}[{i}]")
        return
    if isinstance(value, dict):
        for k, v in value.items():
            if not isinstance(k, str):
                raise InvalidCommandError(f"{path} dict keys must be strings")
            _assert_json_compatible(v, f"{path}.{k}")
        return

    raise InvalidCommandError(f"{path} contains non-JSON-compatible value")
