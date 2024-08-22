class Match:
    def __init__(self, rest):
        self.rest = rest if rest is not None else Null()

    def __eq__(self, other):
        return (other is not None and
                self.__class__ == other.__class__ and
                self.rest == other.rest)

    def match(self, text):
        result = self._match(text, 0)
        return result == len(text)


class Null(Match):
    def __init__(self):
        self.rest = None

    def _match(self, text, start):
        return start
