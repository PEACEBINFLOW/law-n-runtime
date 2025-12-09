from __future__ import annotations

from typing import List, Any

from .tokenizer import Token
from .bytecode import BytecodeBuilder


class Parser:
    """
    Placeholder LAW-N parser: converts tokens into bytecode using simple mapping.
    """

    def parse(self, tokens: List[Token]) -> List[Any]:
        builder = BytecodeBuilder()

        # TODO: real grammar rules
        # For now, treat each token as a NO-OP instruction placeholder.
        for token in tokens:
            builder.emit("NOOP", token.value)

        return builder.build()
