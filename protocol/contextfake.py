class ContextFake:
    def __init__(self, name, func=None, value=None):
        super().__init__()
        self.name = name
        self.original = None

    def __enter__(self):
        assert self.name in globals(), f"Unknown variable {self.name}"
        self.original = globals()[self.name]
        globals()[self.name] = self
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        globals()[self.name] = self.original


def subber(a, b):
    return a - b


def check_no_lasting_effect():
    assert subber(2, 3) == -1
    with ContextFake("subber", value=1234) as fake:
        assert subber(2, 3) == 1234
        assert len(fake.calls) == 1
    assert subber(2, 3) == -1
