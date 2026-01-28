# james/core/handlers/debug_logger.py

from command import Command
from core.events import Event
from core.state import KernelState


def debug_command_logger(command: Command, state: KernelState) -> None:
    """
    Debug logger for Commands (user/system intents).

    Observes:
    - incoming Command
    - current state snapshot

    Must not modify state.
    """
    print("[DEBUG][COMMAND]")
    print(command)
    print("[DEBUG][STATE SNAPSHOT]")
    print(state.snapshot())


def debug_event_logger(event: Event, state: KernelState) -> None:
    """
    Debug logger for Events (facts that occurred).

    Observes:
    - emitted Event
    - current state snapshot

    Must not modify state.
    """
    print("[DEBUG][EVENT]")
    print(event)
    print("[DEBUG][STATE SNAPSHOT]")
    print(state.snapshot())
