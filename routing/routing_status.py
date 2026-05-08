# james/routing/routing_status.py

from enum import Enum


class RoutingStatus(str, Enum):
    """
    Deterministischer Routing-Status.

    Beschreibt ausschließlich das Ergebnis
    der semantischen Routing-Auflösung.

    Keine Governance.
    Keine Policies.
    Keine Execution-Entscheidungen.
    """

    RESOLVABLE = "resolvable"
    UNSUPPORTED = "unsupported"
    INVALID = "invalid"