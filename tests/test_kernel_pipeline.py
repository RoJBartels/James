# james/tests/test_kernel_pipeline.py

from core.kernel import JamesKernel
from core.handlers import (
    command_ingress_handler,
    command_validation_handler,
    router_handler,
)
from command import (
    Command,
    CommandCategory,
    CommandActor,
    CommandChannel,
)


def test_full_command_pipeline_runs_without_side_effects():
    kernel = JamesKernel()
    kernel.register_command_handler(command_ingress_handler)
    kernel.register_command_handler(command_validation_handler)
    kernel.register_command_handler(router_handler)

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
