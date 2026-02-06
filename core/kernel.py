from typing import Callable, List
from .state import KernelState
from .events import (
    Event,
    ExecutionRequested,
    ExecutionStarted,
    ExecutionFinished,
)
from command import Command

CommandHandler = Callable[[Command, KernelState], None]
EventHandler = Callable[[Event, KernelState], None]


class JamesKernel:
    def __init__(self, initial_state: KernelState | None = None):
        self.state = initial_state or KernelState()

        self._command_handlers: List[CommandHandler] = []
        self._event_handlers: List[EventHandler] = []

    # ------------------------------------------------------------------
    # Registration
    # ------------------------------------------------------------------

    def register_command_handler(self, handler: CommandHandler) -> None:
        self._command_handlers.append(handler)

    def register_event_handler(self, handler: EventHandler) -> None:
        self._event_handlers.append(handler)

    # ------------------------------------------------------------------
    # Entry Points
    # ------------------------------------------------------------------

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
        # 1) Event handler pipeline (logging, inspection, etc.)
        for handler in self._event_handlers:
            handler(event, self.state)

        # 2) Kernel transitions (Feature-Level gated, NOOP in FL1)
        self._process_transitions(event)

    # ------------------------------------------------------------------
    # Transition Processing (Step A1)
    # ------------------------------------------------------------------

    def _process_transitions(self, event: Event) -> None:
        """
        Dispatch kernel transitions based on event type.

        NOTE:
        - Transitions are the ONLY allowed place for state mutation
        - In Feature-Level 1, all transitions are NOOP
        """
        if isinstance(event, ExecutionRequested):
            self._transition_execution_requested(event)

        elif isinstance(event, ExecutionStarted):
            self._transition_execution_started(event)

        elif isinstance(event, ExecutionFinished):
            self._transition_execution_finished(event)

        # Unknown events are intentionally ignored

    # ------------------------------------------------------------------
    # Individual Transitions (NOOP, Feature-Level 1)
    # ------------------------------------------------------------------

    def _transition_execution_requested(
        self, event: ExecutionRequested
    ) -> None:
        # G1: Feature-Level Guard
        if not self._guard_feature_level(event):
            return

        # G2: State-Consistency Guard
        if not self._guard_state_consistency(event):
            return

        # G3: Invariant Guard
        if not self._guard_invariants(event):
            return

        # Transition (NOOP in Feature-Level 1)
        return

    def _transition_execution_started(
        self, event: ExecutionStarted
    ) -> None:
        if not self._guard_feature_level(event):
            return

        if not self._guard_state_consistency(event):
            return

        if not self._guard_invariants(event):
            return

        # NOOP
        return

    def _transition_execution_finished(
        self, event: ExecutionFinished
    ) -> None:
        if not self._guard_feature_level(event):
            return

        if not self._guard_state_consistency(event):
            return

        if not self._guard_invariants(event):
            return

        # NOOP
        return

    # ------------------------------------------------------------------
    # Guards (Defensive Layer)
    # ------------------------------------------------------------------

    def _guard_feature_level(self, event: Event) -> bool:
        """
        G1 – Feature-Level Guard

        Returns True if this event is allowed to cause
        state mutation in the current feature level.
        """
        # Feature-Level 1: no transitions are active
        return False

    def _guard_state_consistency(self, event: Event) -> bool:
        """
        G2 – State-Consistency Guard

        Ensures the event is logically compatible
        with the current kernel state.
        """
        # No state changes allowed yet
        return False

    def _guard_invariants(self, event: Event) -> bool:
        """
        G3 – Invariant Guard

        Prevents violation of hard kernel invariants.
        """
        # No invariants evaluated in FL1
        return False

    # ------------------------------------------------------------------
    # Introspection
    # ------------------------------------------------------------------

    def snapshot(self) -> dict:
        return self.state.snapshot()
