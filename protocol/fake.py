from patterns.Literal import Literal


class Fake:
    def __init__(self, func=None, value=None):
        self.calls = []
        self.func = func
        self.value = value

    def __call__(self, *args, **kwargs):
        self.calls.append((args, kwargs))
        if self.func is not None:
            return self.func(*args, **kwargs)
        return self.value


def fakeit(name, func=None, value=None):
    assert name in globals(), f"Unknown function {name}"
    fake = Fake(func, value)
    globals()[name] = fake
    return fake


def adder(a, b):
    return a + b


def test_with_real_functions():
    assert adder(3, 2) == 5


def test_with_mock_functions():
    fakeit("adder", value=99)
    assert adder(3, 2) == 99


def test_fake_records_calls():
    fake = fakeit("adder", value=99)
    assert adder(3, 2) == 99
    assert adder(3, 4) == 99
    assert fake.calls == [((3, 2), {}), ((3, 4), {})]


def test_fake_calculations_result():
    fakeit("adder", func=lambda left, right: 10 * left + right)
    assert adder(2, 3) == 23


test_with_mock_functions()
test_with_mock_functions()
test_fake_records_calls()
test_fake_calculations_result()
