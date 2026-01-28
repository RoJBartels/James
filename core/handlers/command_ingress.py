# james/core/handlers/command_ingress.py

from command import Command
from core.state import KernelState


def command_ingress_handler(command: Command, state: KernelState) -> None:
    """
    Reiner Ingress-Handler für Commands.

    Aufgaben:
    - bestätigt den Eintritt eines Commands in den Kernel
    - keine Interpretation
    - keine Validierung
    - keine State-Änderung
    """

    # absichtlich leer
    # späterer Erweiterungspunkt für:
    # - Logging
    # - Tracing
    # - Audit
    return
