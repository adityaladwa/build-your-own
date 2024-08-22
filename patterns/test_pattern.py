import unittest
from Any import Any
from Literal import Literal
from Either import Either


class TestPatterns(unittest.TestCase):
    def test_any_matches_empty(self):
        # /*/ matches ""
        assert Any().match("")

    def test_any_matches_entire_string(self):
        # /*/ matches "abc"
        assert Any().match("abc")

    def test_any_matches_as_prefix(self):
        # /*def/ matches "abcdef"
        assert Any(Literal("def")).match("abcdef")

    def test_any_matches_as_suffix(self):
        # /abc*/ matches "abcdef"
        assert Literal("abc", Any()).match("abcdef")

    def test_any_matches_interior(self):
        # /a*c/ matches "abc"
        assert Literal("a", Any(Literal("c"))).match("abc")

    def test_literal_match_entire_string(self):
        # /abc/ matches "abc"
        assert Literal("abc").match("abc")

    def test_literal_substring_alone_no_match(self):
        # /ab/ doesn't match "abc"
        assert not Literal("ab").match("abc")

    def test_literal_superstring_no_match(selfself):
        # /abc/ doesn't match "ab"
        assert not Literal("abc").match("ab")

    def test_literal_followed_by_literal_match(self):
        # /a/+/b/ matches "ab"
        assert Literal("a", Literal("b")).match("ab")

    def test_literal_followed_by_literal_no_match(self):
        # /a/+/b/ doesn't match "ac"
        assert not Literal("a", Literal("b")).match("ac")

    def test_either_two_literals_first(self):
        # /{a,b}/ matches "a"
        assert Either(Literal("a"), Literal("b")).match("a")

    def test_either_two_literals_not_both(self):
        # /{a,b}/ doesn't match "ab"
        assert not Either(Literal("a"), Literal("b")).match("ab")

    def test_either_followed_by_literal_match(self):
        # /{a,b}c/ matches "ac"
        assert Either(Literal("a"), Literal("b"), Literal("c")).match("ac")

    def test_either_followed_by_literal_no_match(self):
        # /{a,b}c/ doesn't match "ax"
        assert not Either(Literal("a"), Literal("b"), Literal("c")).match("ax")


if __name__ == "__main__":
    unittest.main()
