class Lit:
    def __init__(self, chars, rest=None):
        self.chars = chars
        self.rest = rest

    def match(self, text, start=0):
        end = start + len(self.chars)
        if text[start:end] != self.chars:
            return False
        if self.rest:
            return self.rest.match(text, end)
        return end == len(text)


def test_literal_match_entire_string():
    # /abc/ matches "abc"
    assert Lit("abc").match("abc")


def test_literal_substring_alone_no_match():
    # /ab/ doesn't match "abc"
    assert not Lit("ab").match("abc")


def test_literal_superstring_no_match():
    # /abc/ doesn't match "ab"
    assert not Lit("abc").match("ab")


def test_literal_followed_by_literal_match():
    # /a/+/b/ matches "ab"
    assert Lit("a", Lit("b")).match("ab")


def test_literal_followed_by_literal_no_match():
    # /a/+/b/ doesn't match "ac"
    assert not Lit("a", Lit("b")).match("ac")


test_literal_match_entire_string()
test_literal_substring_alone_no_match()
test_literal_superstring_no_match()
test_literal_followed_by_literal_match()
test_literal_followed_by_literal_no_match()
