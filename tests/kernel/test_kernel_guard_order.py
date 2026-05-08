from datetime import datetime

from core import JamesKernel
from core.kernel import GuardResult
from core.events import ExecutionStarted


# ------------------------------------------------------------------
# Tracking Kernel (Test-only)
# ------------------------------------------------------------------

class TrackingKernel(JamesKernel):
    """
    Test subclass that tracks guard invocation order.
    """

    def __init__(self):
        super().__init__()
        self.guard_trace = []

    def _guard_feature_level(self, event):
        self.guard_trace.append("G1")
        return GuardResult(allowed=True)

    def _guard_state_consistency(self, event):
        self.guard_trace.append("G2")
        return GuardResult(allowed=True)

    def _guard_invariants(self, event):
        self.guard_trace.append("G3")
        return GuardResult(allowed=True)


# ------------------------------------------------------------------
# 1️⃣ Guard Execution Order
# ------------------------------------------------------------------

def test_guard_execution_order():
    kernel = TrackingKernel()

    event = ExecutionStarted("exec1", datetime.now())
    kernel._transition_execution_started(event)

    assert kernel.guard_trace == ["G1", "G2", "G3"]


# ------------------------------------------------------------------
# 2️⃣ Short-Circuit on G1
# ------------------------------------------------------------------

def test_guard_short_circuit_on_g1():

    class KernelG1Blocks(TrackingKernel):
        def _guard_feature_level(self, event):
            self.guard_trace.append("G1")
            return GuardResult(allowed=False)

    kernel = KernelG1Blocks()

    event = ExecutionStarted("exec1", datetime.now())
    kernel._transition_execution_started(event)

    # Only G1 should run
    assert kernel.guard_trace == ["G1"]


# ------------------------------------------------------------------
# 3️⃣ Short-Circuit on G2
# ------------------------------------------------------------------

def test_guard_short_circuit_on_g2():

    class KernelG2Blocks(TrackingKernel):
        def _guard_state_consistency(self, event):
            self.guard_trace.append("G2")
            return GuardResult(allowed=False)

    kernel = KernelG2Blocks()

    event = ExecutionStarted("exec1", datetime.now())
    kernel._transition_execution_started(event)

    # G1 runs, then G2 blocks, G3 must NOT run
    assert kernel.guard_trace == ["G1", "G2"]


# ------------------------------------------------------------------
# 4️⃣ All Guards Pass (No Mutation in FL1)
# ------------------------------------------------------------------

def test_all_guards_pass_no_state_mutation():
    kernel = TrackingKernel()

    event = ExecutionStarted("exec1", datetime.now())
    kernel._transition_execution_started(event)

    # Even though all guards allow, FL1 transition is NOOP
    assert kernel.state.running_jobs == []