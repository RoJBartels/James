# james/routing/router.py

from command.command import Command

from routing.routing_result import RoutingResult
from routing.routing_status import RoutingStatus
from routing.rules import ROUTING_RULES


def route(command: Command) -> RoutingResult:
    """
    Deterministischer FL1-Router.

    Verantwortlich ausschließlich für:

        (category, domain)
            →
        capability_space

    Der Router:
    - kennt keinen State
    - kennt keine Policies
    - kennt keine Tools
    - aktiviert keine Capabilities
    - erzeugt keine Events
    """

    # --------------------------------------------------------------
    # Validation
    # --------------------------------------------------------------

    if not _is_valid_command(command):
        return RoutingResult(
            capability_space=(),
            routing_status=RoutingStatus.INVALID,
        )

    # --------------------------------------------------------------
    # Rule Lookup
    # --------------------------------------------------------------

    rule_key = (
        command.category,
        command.domain,
    )

    capability_space = ROUTING_RULES.get(rule_key)

    # --------------------------------------------------------------
    # Unsupported
    # --------------------------------------------------------------

    if capability_space is None:
        return RoutingResult(
            capability_space=(),
            routing_status=RoutingStatus.UNSUPPORTED,
        )

    # --------------------------------------------------------------
    # Resolvable
    # --------------------------------------------------------------

    return RoutingResult(
        capability_space=capability_space,
        routing_status=RoutingStatus.RESOLVABLE,
    )


def _is_valid_command(command: Command) -> bool:
    """
    Minimale strukturelle FL1-Validierung.

    Keine Policies.
    Keine Governance.
    Keine Payload-Semantik.
    """

    if command.category is None:
        return False

    if not command.domain:
        return False

    return True