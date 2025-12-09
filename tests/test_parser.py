from lnre.tokenizer import Tokenizer
from lnre.parser import Parser


def test_parser_emits_instructions():
    tokenizer = Tokenizer()
    parser = Parser()

    tokens = tokenizer.tokenize("signal.open")
    instructions = parser.parse(tokens)

    assert len(instructions) > 0
