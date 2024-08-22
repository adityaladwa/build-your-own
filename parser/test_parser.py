import unittest

from Tokeniser import Tokeniser


class TokeniserTest(unittest.TestCase):

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
