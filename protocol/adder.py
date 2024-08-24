class Adder:
    def __init__(self, value):
        self.value = value

    def __call__(self, args):
        return args + self.value


add_3 = Adder(3)
result = add_3(8)

print(f"add4(8) = {result}")
