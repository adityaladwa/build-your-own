def one():
    print("One")


def two():
    print("Two")


def three():
    print("Three")


everything = [one(), two(), three()]

for func in everything:
    func()