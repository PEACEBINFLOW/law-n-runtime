from __future__ import annotations

from dataclasses import dataclass
from typing import Any, List


@dataclass
class Instruction:
    op: str
    args: List[Any]


class BytecodeBuilder:
    """
    Utility for constructing LAW-N bytecode sequences from parsed AST.
    """

    def __init__(self) -> None:
        self.instructions: List[Instruction] = []

    def emit(self, op: str, *args: Any) -> None:
        self.instructions.append(Instruction(op=op, args=list(args)))

    def build(self) -> List[Instruction]:
        return self.instructions
