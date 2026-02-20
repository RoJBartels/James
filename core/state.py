# james/core/state.py
from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class KernelState:
    """
    Explicit, mutable system state.

    May only be modified by the Kernel
    as part of validated Kernel-Transitions.
    """

    active_project: Optional[str] = None
    active_task: Optional[str] = None

    feature_level: int = 1
    autonomy_level: int = 0

    permissions: List[str] = field(default_factory=list)
    running_jobs: List[str] = field(default_factory=list)

    sandbox_mode: bool = False

    def snapshot(self) -> dict:
        """
        Serialize current state for logging / tests.
        """
        return self.__dict__.copy()
