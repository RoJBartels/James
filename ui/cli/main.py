# james/ui/cli/main.py
from core.kernel import JamesKernel
from ui.cli import CLICommandAdapter


def run_cli(kernel: JamesKernel) -> None:
    adapter = CLICommandAdapter()

    while True:
        raw = input("> ")

        if raw.strip() in {"exit", "quit"}:
            break

        command = adapter.from_raw_input(raw)
        kernel.handle_command(command)

