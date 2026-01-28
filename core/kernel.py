# james/core/kernel.py
from typing import Callable, List
from .state import KernelState
from .events import Event
from command import Command

CommandHandler = Callable[[Command, KernelState], None]
EventHandler = Callable[[Event, KernelState], None]

class JamesKernel:
    def __init__(self, initial_state: KernelState | None = None):
        self.state = initial_state or KernelState()

        self._command_handlers: List[
            CommandHandler
        ] = []

        self._event_handlers: List[
            EventHandler
        ] = []

    # -------- Registration --------

    def register_command_handler(self, handler) -> None:
        self._command_handlers.append(handler)

    def register_event_handler(self, handler) -> None:
        self._event_handlers.append(handler)

    # -------- Entry Points --------

    def handle_command(self, command: Command) -> None:
        """
        Entry point for user/system intent.
        Commands may be ignored or rejected.
        """
        for handler in self._command_handlers:
            handler(command, self.state)

    def handle_event(self, event: Event) -> None:
        """
        Entry point for internal/system facts.
        Events are always processed.
        """
        for handler in self._event_handlers:
            handler(event, self.state)

    # -------- Introspection --------

    def snapshot(self) -> dict:
        return self.state.snapshot()
