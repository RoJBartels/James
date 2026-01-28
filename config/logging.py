# james/config/logging.py

from dataclasses import dataclass

@dataclass(frozen=True)
class LoggingConfig:
    log_commands: bool = False
    log_events: bool = False
