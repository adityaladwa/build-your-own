def original(value):
    print(f"original: {value}")


def logging(func, label):
    def __inner(value):
        print(f"++ {label}")
        func(value)
        print(f"-- {label}")

    return __inner


original = logging(original, "original")
original("hello")


def wrap(func):
    def __inner(*args):
        print("before call")
        func(*args)
        print("after call")

    return __inner


@wrap
def original(message):
    print(f"original: {message}")


original("example")
