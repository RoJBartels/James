#james/main.py
from core import JamesKernel
from core.handlers import (
    command_ingress_handler,
    command_validation_handler,
    router_handler,
    debug_command_logger,
    debug_event_logger,
)
from ui.cli.main import run_cli
from config.logging import LoggingConfig


def main() -> None:
    kernel = JamesKernel()

    logging_cfg = LoggingConfig(
        log_commands=True,
        log_events=False,
    )

    # ---- Command pipeline ----
    kernel.register_command_handler(command_ingress_handler)
    kernel.register_command_handler(command_validation_handler)
    kernel.register_command_handler(router_handler)

    if logging_cfg.log_commands:
        kernel.register_command_handler(debug_command_logger)

    # ---- Event pipeline ----
    if logging_cfg.log_events:
        kernel.register_event_handler(debug_event_logger)

    run_cli(kernel)


if __name__ == "__main__":
    main()
