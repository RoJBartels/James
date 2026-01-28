# james/core/events.py
from dataclasses import dataclass
from typing import Any


class Event:
    """
    Base class for all kernel-internal events.

    Events represent facts that have occurred.
    They are created only by the Kernel.
    """
    pass


@dataclass(frozen=True)
class SystemEvent(Event):
    name: str
    payload: Any = None
