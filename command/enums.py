from enum import Enum


class CommandCategory(str, Enum):
    QUERY = "query"
    PLANNING = "planning"
    ACTION = "action"
    CONTROL = "control"
    CONTEXT = "context"


class CommandActor(str, Enum):
    USER = "user"
    ADMIN = "admin"
    SYSTEM = "system"


class CommandChannel(str, Enum):
    CLI = "cli"
    UI = "ui"
    VOICE = "voice"
    API = "api"
