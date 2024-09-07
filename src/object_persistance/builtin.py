import sys


def save(writer, thing):
    if isinstance(thing, bool):
        print(f"bool:{thing}", file=writer)
    elif isinstance(thing, float):
        print(f"float:{thing}", file=writer)
    elif isinstance(thing, int):
        print(f"int:{thing}", file=writer)
    elif isinstance(thing, str):
        lines = thing.splitlines()
        print(f"str:{len(lines)}", file=writer)
        for line in lines:
            print(line, file=writer)
    elif isinstance(thing, list):
        print(f"list:{len(thing)}", file=writer)
        for item in thing:
            save(writer, item)
    elif isinstance(thing, dict):
        print(f"dict:{len(thing)}", file=writer)
        for (key, value) in thing.items():
            save(writer, key)
            save(writer, value)
    else:
        raise ValueError(f"Unknown type: {type(thing)}")


def load(reader):
    line = reader.readline()[:-1]
    assert line, "Nothing to read"
    fields = line.split(":", maxsplit=1)
    assert len(fields) == 2, f"Badly formatted line: {line}"
    key, value = fields
    if key == "bool":
        names = {"True": True, "False": False}
        assert value in names, f"Unknown boolean: {value}"
        return names[value]
    elif key == "float":
        return float(value)
    elif key == "int":
        return int(value)
    elif key == "list":
        return [load(reader) for _ in range(int(value))]
    else:
        raise ValueError(f"Unknown type of thing {line}")


save(sys.stdout, [False, 3.14, "hello", {"left": 1, "right": [2, 3]}])
