from patterns.Match import Match


class Literal(Match):
    def __init__(self, chars, rest=None):
        super().__init__(rest)
        self.chars = chars

    def __eq__(self, other):
        return super().__eq__(other) and (
                self.chars == other.chars
        )

    def _match(self, text, start):
        end = start + len(self.chars)
        if text[start:end] != self.chars:
            return None
        return self.rest._match(text, end)
