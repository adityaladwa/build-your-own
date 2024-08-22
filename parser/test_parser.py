import unittest

from Tokeniser import Tokeniser
from parser.Parser import Parser
from patterns.Either import Either
from patterns.Literal import Literal


class ParserPackageTests(unittest.TestCase):

    def test_tok_empty_string(self):
        assert Tokeniser().tok("") == []

    def test_tok_any_either(self):
        assert Tokeniser().tok("*{abc,def}") == [
            ["Any"],
            ["EitherStart"],
            ["Literal", "abc"],
            ["Literal", "def"],
            ["EitherEnd"]
        ]

    def test_parse_either_two_lit(self):
        tokens = Tokeniser().tok("{abc,def}")
        assert Parser()._parse(tokens) == Either(
            Literal("abc"), Literal("def")
        )
