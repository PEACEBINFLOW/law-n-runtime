from __future__ import annotations

from typing import Any


class RuntimeInspector:
    """
    Read-only view into LNRE state for debugging and cognition tooling.
    """

    def __init__(self, runtime: Any) -> None:
        self.runtime = runtime

    def snapshot(self) -> dict:
        return {
            "ip": self.runtime.ip,
            "state_keys": list(self.runtime.state.keys()),
            "instruction_count": len(self.runtime.instructions),
        }
