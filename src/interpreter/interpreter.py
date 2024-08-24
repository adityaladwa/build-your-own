import json
import sys


def do_add(args, env):
    assert len(args) == 2
    left = do(args[0], env)
    right = do(args[1], env)
    return left + right


def do_abs(args, env):
    assert len(args) == 1
    val = do(args[0], env)
    return abs(val)


def do_get(args, env):
    assert len(args) == 1
    assert isinstance(args[0], str)
    assert args[0] in env, f"Unknown variable {args[0]}"
    return env[args[0]]


def do_set(args, env):
    assert len(args) == 2
    assert isinstance(args[0], str)
    value = do(args[1], env)
    env[args[0]] = value
    return value


def do_seq(args, env):
    assert len(args) > 0
    for item in args:
        result = do(item, env)
    return result


def do(expr, env):
    # integer evaluate to themselves
    if isinstance(expr, int):
        return expr

    # lists trigger function calls
    assert isinstance(expr, list)
    assert expr[0] in OPS, f"Unknown operation {expr[0]}"
    func = OPS[expr[0]]
    return func(expr[1:], env)

OPS = {
    name.replace("do_", ""): func
    for (name, func) in globals().items()
    if name.startswith("do_")
}


def main():
    assert len(sys.argv) == 2, "Usage: interpreter.py filename"
    with open(sys.argv[1], "r") as reader:
        program = json.load(reader)
    result = do(program, {})
    print(f"=> {result}")


if __name__ == "__main__":
    main()
