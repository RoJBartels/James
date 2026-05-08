# james/tests/test_kernel_with_debug_logger.py

from core import JamesKernel
from core.handlers import (
    command_ingress_handler,
    command_validation_handler,
    router_handler,
    debug_command_logger,
)
from command import (
    Command,
    CommandCategory,
    CommandActor,
    CommandChannel,
)


def test_kernel_pipeline_with_debug_logger_is_state_safe():
    kernel = JamesKernel()
    kernel.register_command_handler(command_ingress_handler)
    kernel.register_command_handler(command_validation_handler)
    kernel.register_command_handler(router_handler)
    kernel.register_command_handler(debug_command_logger)

    before = kernel.snapshot()

    command = Command.create(
        category=CommandCategory.QUERY,
        domain="system:james",
        actor=CommandActor.USER,
        channel=CommandChannel.CLI,
        payload={"text": "status"},
    )

    kernel.handle_command(command)
    after = kernel.snapshot()

    assert before == after
