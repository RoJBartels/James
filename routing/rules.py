# james/routing/rules.py

from command.enums import CommandCategory

from routing.capabilities import (
    SYSTEM_STATUS,
    SYSTEM_INFO,
    RESEARCH_MEMORY,
    RESEARCH_WEB,
    PROJECT_PLANNING,
    EXECUTION_CODE,
)

# ------------------------------------------------------------------
# Deterministische Routing-Regeln
# ------------------------------------------------------------------

# TODO:
# Replace raw domain strings with CommandDomain enum
# once command-layer refactor is completed.

ROUTING_RULES = {

    # --------------------------------------------------------------
    # Query / System
    # --------------------------------------------------------------

    (
        CommandCategory.QUERY,
        "system",
    ): (
        SYSTEM_STATUS,
        SYSTEM_INFO,
    ),

    # --------------------------------------------------------------
    # Query / Research
    # --------------------------------------------------------------

    (
        CommandCategory.QUERY,
        "research",
    ): (
        RESEARCH_MEMORY,
        RESEARCH_WEB,
    ),

    # --------------------------------------------------------------
    # Action / Execution
    # --------------------------------------------------------------

    (
        CommandCategory.ACTION,
        "execution",
    ): (
        EXECUTION_CODE,
    ),

    # --------------------------------------------------------------
    # Planning / Project
    # --------------------------------------------------------------

    (
        CommandCategory.PLANNING,
        "project",
    ): (
        PROJECT_PLANNING,
    ),
}