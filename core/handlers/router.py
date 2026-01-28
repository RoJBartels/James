# james/core/handlers/router.py

from command import Command
from core.state import KernelState


def router_handler(command: Command, state: KernelState) -> None:
    """
    Router-Skeleton.

    Aktuelle Verantwortung:
    - existiert als semantischer Ankerpunkt
    - empfängt formal valide Commands
    - trifft KEINE Entscheidungen

    Zukünftig:
    - Ableitung von Intent / Capabilities
    - Weitergabe an Planner / Executor
    """

    # absichtlich leer
    # kein Routing
    # keine Heuristik
    # keine Events
    return
