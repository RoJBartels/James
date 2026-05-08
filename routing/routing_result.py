# james/routing/routing_result.py

from dataclasses import dataclass
from typing import Tuple

from routing.routing_status import RoutingStatus


@dataclass(frozen=True)
class RoutingResult:
    """
    Deterministisches Ergebnis des semantischen Routers.

    Beschreibt ausschließlich:
    - capability_space
    - routing_status

    Keine Governance.
    Keine Tool-Bindung.
    Keine Capability-Aktivierung.
    """

    capability_space: Tuple[str, ...]
    routing_status: RoutingStatus