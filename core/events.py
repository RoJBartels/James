# james/core/events.py

from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Any


class Event:
    """
    Base class for all kernel-internal events.

    Events represent facts that have occurred.
    They are immutable and carry no behavior.
    """
    pass


# ---------------------------------------------------------------------------
# Execution Lifecycle Events (Feature-Level 1)
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class ExecutionRequested(Event):
    """
    A request to start an execution has been registered.

    NOTE:
    - does NOT imply approval
    - does NOT imply execution start
    - producer not yet defined (future kernel responsibility)
    """

    request_id: str
    timestamp: datetime


@dataclass(frozen=True)
class ExecutionStarted(Event):
    """
    Execution has started.
    """

    execution_id: str
    timestamp: datetime


@dataclass(frozen=True)
class ExecutionFinished(Event):
    """
    Execution has finished and reached a terminal state.
    """

    execution_id: str
    timestamp: datetime
    success: bool
    result: Optional[Any] = None
    error: Optional[str] = None
