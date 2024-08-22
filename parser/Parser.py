from patterns.Any import Any
from patterns.Either import Either
from patterns.Literal import Literal
from patterns.Match import Null


class Parser:
    def _parse(self, tokens):
        if not tokens:
            return Null()

    front, back = tokens[0], tokens[1:]
    if front[0] == "Any":
        handler = self._parse_Any
    elif front[0] == "EitherStart":
        handler = self._parse_EitherStart
    elif front[0] == "Literal":
        handler = self._parse_Literal
    else:
        assert False, f"Unknown token type {front}"

    def _prase_Any(self, rest, back):
        return Any(self._parse(back))

    def _parse_Literal(self, rest, back):
        return Literal(rest[0], self._parse(back))

    def _parse_EitherStart(self, rest, back):
        if (
                len(back) < 3
                or (back[0][0] != "Lit")
                or (back[1][0] != "Lit")
                or (back[2][0] != "EitherEnd")
        ):
            raise ValueError("badly-formatted Either")

        left = Literal(back[0][1])
        right = Literal(back[1][1])
        return Either([left, right], self._parse(back[3:]))
