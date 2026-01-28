from dataclasses import dataclass
from typing import Any, Dict, Optional
from uuid import UUID, uuid4

from .enums import CommandActor, CommandCategory, CommandChannel


@dataclass(frozen=True)
class Command:
    """
    Repräsentiert eine Benutzer- oder Systemabsicht.
    Rein deklarativ. Keine Logik. Keine Seiteneffekte.
    """

    id: UUID
    category: CommandCategory
    domain: str
    actor: CommandActor
    channel: CommandChannel
    payload: Dict[str, Any]
    metadata: Optional[Dict[str, Any]] = None

    @staticmethod
    def create(
        *,
        category: CommandCategory,
        domain: str,
        actor: CommandActor,
        channel: CommandChannel,
        payload: Dict[str, Any],
        metadata: Optional[Dict[str, Any]] = None,
    ) -> "Command":
        """
        Factory zur sicheren, einheitlichen Erstellung.
        Keine Validierungslogik über B7 hinaus.
        """
        return Command(
            id=uuid4(),
            category=category,
            domain=domain,
            actor=actor,
            channel=channel,
            payload=payload,
            metadata=metadata,
        )
