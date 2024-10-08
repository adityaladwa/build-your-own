def sign(value):
    if value < 0:
        return -1
    else:
        return 1


def test_sign_negative():
    assert sign(-3) == -1


def test_sign_positive():
    assert sign(19) == 1


def test_sign_zero():
    assert sign(0) == 1


def test_sign_error():
    assert sign(1) == 1


def run_tests():
    results = {
        "pass": 0,
        "fail": 0,
        "error": 0
    }
    for (name, func) in globals().items():
        if not name.startswith("test_"): continue
        try:
            func()
            results["pass"] += 1
        except AssertionError:
            results["fail"] += 1
        except Exception:
            results["error"] += 1

    print(f"pass {results["pass"]}")
    print(f"fail {results["fail"]}")
    print(f"error {results["error"]}")


def find_tests(prefix):
    for (name, func) in globals().items():
        if name.startswith(prefix):
            print(name, func)


run_tests()