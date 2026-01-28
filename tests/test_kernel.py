# james/tests/test_kernel.py
from core.kernel import JamesKernel
from core.events import UserCommand


def test_kernel_handles_event_without_crash():
    kernel = JamesKernel()
    kernel.handle_event(UserCommand("test"))


def test_state_is_stable():
    kernel = JamesKernel()
    snapshot = kernel.snapshot()
    assert snapshot["feature_level"] == 0
    assert snapshot["autonomy_level"] == 0
