from typing import Callable, List
from .state import KernelState
from .events import (
    Event,
    ExecutionRequested,
    ExecutionStarted,
    ExecutionFinished,
)
from command import Command

#-------------------------------------------------------------------
# GuardResult Class as a simple wrapper for guard outcomes
#-------------------------------------------------------------------
from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class GuardResult:
    allowed: bool
    reason: Optional[str] = None
    
#-------------------------------------------------------------------
# Type Aliases for Handlers
#-------------------------------------------------------------------

CommandHandler = Callable[[Command, KernelState], None]
EventHandler = Callable[[Event, KernelState], None]

#-------------------------------------------------------------------
# JamesKernel Class Definition
#-------------------------------------------------------------------

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
        g1 = self._guard_feature_level(event)
        if not g1.allowed:
            return

        # G2: State-Consistency Guard
        g2 = self._guard_state_consistency(event)
        if not g2.allowed:
            return

        # G3: Invariant Guard
        g3 = self._guard_invariants(event)
        if not g3.allowed:
            return

        # Transition (NOOP in Feature-Level 1)
        return

    def _transition_execution_started(
        self, event: ExecutionStarted
    ) -> None:
        # G1: Feature-Level Guard
        g1 = self._guard_feature_level(event)
        if not g1.allowed:
            return

        # G2: State-Consistency Guard
        g2 = self._guard_state_consistency(event)
        if not g2.allowed:
            return

        # G3: Invariant Guard
        g3 = self._guard_invariants(event)
        if not g3.allowed:
            return

        self.state.running_jobs.append(event.execution_id)

    def _transition_execution_finished(
        self, event: ExecutionFinished
    ) -> None:
        # G1: Feature-Level Guard
        g1 = self._guard_feature_level(event)
        if not g1.allowed:
            return

        # G2: State-Consistency Guard
        g2 = self._guard_state_consistency(event)
        if not g2.allowed:
            return

        # G3: Invariant Guard
        g3 = self._guard_invariants(event)
        if not g3.allowed:
            return

        # NOOP
        return

    # ------------------------------------------------------------------
    # Guards (Defensive Layer – Semantics + Structured for Future Activation)
    # ------------------------------------------------------------------

    def _guard_feature_level(self, event: Event) -> GuardResult:
        """
        G1 – Feature-Level Guard

        In Feature-Level 1:
        - Execution transitions are defined
        - but not yet activated
        - all transitions are disabled (NOOP)
        """
        
        if isinstance(event, ExecutionStarted):
            if self.state.feature_level >= 2:
                return GuardResult(allowed=True)
            return GuardResult(
                allowed=False,
                reason="feature_level_blocked"
            )

        if isinstance(event, ExecutionFinished):
            if self.state.feature_level >= 2:
                return GuardResult(allowed=True)
            return GuardResult(
                allowed=False,
                reason="feature_level_blocked"
            )

        return GuardResult(
            allowed=False,
            reason="feature_level_blocked"
        )


    def _guard_state_consistency(self, event: Event) -> GuardResult:
        """
        G2 – State-Consistency Guard

        Ensures event logically fits current state.
        No mutation allowed, but logical validity is checked.
        """

        # ExecutionStarted:
        # execution_id must not already be running
        if isinstance(event, ExecutionStarted):
            if event.execution_id in self.state.running_jobs:
                return GuardResult(
                    allowed=False,
                    reason="execution_already_running"
                )
            return GuardResult(allowed=True)

        # ExecutionFinished:
        # execution_id must currently be running
        if isinstance(event, ExecutionFinished):
            if event.execution_id not in self.state.running_jobs:
                return GuardResult(
                    allowed=False,
                    reason="execution_not_running"
                )
            return GuardResult(allowed=True)

        # ExecutionRequested:
        # no state relation in FL1
        if isinstance(event, ExecutionRequested):
            return GuardResult(allowed=True)

        return GuardResult(
            allowed=False,
            reason="unsupported_event_for_transition"
        )


    def _guard_invariants(self, event: Event) -> GuardResult:
        """
        G3 – Invariant Guard

        Protects hard system invariants.
        """

        # Invariant example:
        # running_jobs must not contain duplicates
        if len(self.state.running_jobs) != len(set(self.state.running_jobs)):
            return GuardResult(
                allowed=False,
                reason="duplicate_running_jobs_detected"
            )

        # No additional invariants defined yet
        return GuardResult(allowed=True)

    # ------------------------------------------------------------------
    # Introspection
    # ------------------------------------------------------------------

    def snapshot(self) -> dict:
        return self.state.snapshot()
