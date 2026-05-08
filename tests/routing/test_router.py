# tests/routing/test_router.py

from command.command import Command
from command.enums import (
    CommandCategory,
    CommandActor,
    CommandChannel,
)

from routing.router import route
from routing.routing_status import RoutingStatus


def test_query_system_is_resolvable():

    command = Command.create(
        category=CommandCategory.QUERY,
        domain="system",
        actor=CommandActor.USER,
        channel=CommandChannel.CLI,
        payload={},
    )

    result = route(command)

    assert result.routing_status == RoutingStatus.RESOLVABLE

    assert result.capability_space == (
        "system_status",
        "system_info",
    )

def test_unsupported_route():

    command = Command.create(
        category=CommandCategory.CONTROL,
        domain="research",
        actor=CommandActor.USER,
        channel=CommandChannel.CLI,
        payload={},
    )

    result = route(command)

    assert result.routing_status == RoutingStatus.UNSUPPORTED

    assert result.capability_space == ()

def test_invalid_command_missing_domain():

    command = Command.create(
        category=CommandCategory.QUERY,
        domain="",
        actor=CommandActor.USER,
        channel=CommandChannel.CLI,
        payload={},
    )

    result = route(command)

    assert result.routing_status == RoutingStatus.INVALID

    assert result.capability_space == ()

def test_routing_is_deterministic():

    command = Command.create(
        category=CommandCategory.QUERY,
        domain="research",
        actor=CommandActor.USER,
        channel=CommandChannel.CLI,
        payload={},
    )

    result_1 = route(command)
    result_2 = route(command)

    assert result_1 == result_2