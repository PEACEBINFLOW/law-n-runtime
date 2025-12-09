from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class Token:
    type: str
    value: str
    line: int
    column: int


class Tokenizer:
    """
    Minimal placeholder tokenizer for LAW-N syntax.
    """

    def tokenize(self, source: str) -> List[Token]:
        # TODO: implement real tokenization
        # For now, split on whitespace as placeholder.
        tokens: List[Token] = []
        for i, part in enumerate(source.split()):
            tokens.append(Token(type="WORD", value=part, line=1, column=i))
        return tokens
