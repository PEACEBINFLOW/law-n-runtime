from __future__ import annotations

from typing import Any, Dict, List

from .bytecode import Instruction
from .exceptions import RuntimeHalt
from .inspector import RuntimeInspector


class LNRE:
    """
    LAW-N Runtime Environment (LNRE).

    Executes LAW-N bytecode instructions in a time-aware, stateful loop.
    """

    def __init__(self) -> None:
        self.ip: int = 0               # instruction pointer
        self.instructions: List[Instruction] = []
        self.state: Dict[str, Any] = {}
        self.inspector = RuntimeInspector(self)

    def load(self, instructions: List[Instruction]) -> None:
        self.instructions = instructions
        self.ip = 0

    def step(self) -> None:
        if self.ip >= len(self.instructions):
            raise RuntimeHalt("End of instruction stream")

        instr = self.instructions[self.ip]
        self._execute_instruction(instr)
        self.ip += 1

    def run(self) -> None:
        try:
            while True:
                self.step()
        except RuntimeHalt:
            return

    def _execute_instruction(self, instr: Instruction) -> None:
        # TODO: core opcode dispatch goes here
        # Example:
        # if instr.op == "TIME_WAIT":
        #     self._op_time_wait(instr.args)
        # elif instr.op == "NSQL_EXEC":
        #     self._op_nsql_exec(instr.args)
        # ...
        pass


def main() -> None:
    # Placeholder console entrypoint
    print("LNRE runtime entrypoint (wire CLI later)")
