from typing import Dict

from command import (
    Command,
    CommandActor,
    CommandCategory,
    CommandChannel,
)


class CLICommandAdapter:
    """
    Übersetzt rohe CLI-Eingaben in deklarative Commands.
    Kein Kernel-Wissen. Kein State-Zugriff.
    """

    def from_raw_input(self, raw_input: str) -> Command:
        """
        Minimaler, deterministischer Adapter.
        Keine Magie. Keine Heuristik.
        """

        normalized = raw_input.strip()

        # Minimalregel: alles ist erstmal eine Query
        payload: Dict[str, str] = {
            "text": normalized
        }

        return Command.create(
            category=CommandCategory.QUERY,
            domain="system:james",
            actor=CommandActor.USER,
            channel=CommandChannel.CLI,
            payload=payload,
            metadata={
                "raw_input": raw_input
            },
        )
