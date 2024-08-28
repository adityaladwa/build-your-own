import json
import sys

from bs4 import NavigableString, BeautifulSoup

import z_if
import z_loop
import z_num
import z_var

HANDLERS = {
    "z-if": z_if,
    "z-loop": z_loop,
    "z-num": z_num,
    "z-var": z_var
}


class Env:
    def __init__(self, initial):
        self.stack = [initial.copy()]

    def push(self, frame):
        self.stack.append(frame)

    def pop(self):
        self.stack.pop()

    def find(self, name):
        for frame in reversed(self.stack):
            if name in frame:
                return frame[name]
        return None


class Visitor:
    def __init__(self, root):
        self.root = root

    def walk(self, node=None):
        if node is None:
            node = self.root
        if self.open(node):
            for child in node.children:
                self.walk(child)
        self.close(node)

    def open(self, node):
        raise NotImplementedError("open")

    def close(self, node):
        raise NotImplementedError("close")


class Expander(Visitor):
    def __init__(self, root, variables):
        super().__init__(root)
        self.env = Env(variables)
        self.handlers = HANDLERS
        self.result = []

    def open(self, node):
        if isinstance(node, NavigableString):
            self.output(node.string)
            return False
        elif self.hasHandler(node):
            return self.getHandler(node).open(self, node)
        else:
            self.showTag(node, False)
            return True

    def close(self, node):
        if isinstance(node, NavigableString):
            return
        elif self.hasHandler(node):
            self.getHandler(node).close(self, node)
        else:
            self.showTag(node, True)

    def hasHandler(self, node):
        return any(
            name in self.handlers for name in node.attrs
        )

    def getHandler(self, node):
        possible = [
            name for name in node.attrs if name in self.handlers
        ]
        assert len(possible) == 1, "Should be exactly one handler"
        return self.handlers[possible[0]]

    def showTag(self, node, closing):
        if closing:
            self.output(f"</{node.name}>")
            return
        self.output(f"<{node.name}")
        for name in node.attrs:
            if not name.startswith("z-"):
                self.output(f'{name}="{node.attrs[name]}"')
        self.output(">")

    def output(self, text):
        self.result.append("UNDEF" if text is None else text)

    def getResult(self):
        return "".join(self.result)


# data = {"names": ["Alice", "Bob", "Charlie"]}
#
# dom = read_html("template.html")
# expander = Expander(dom, data)
# expander.walk()
# print(expander.result)


def main():
    with open(sys.argv[1], "r") as reader:
        variables = json.load(reader)
    with open(sys.argv[2], "r") as reader:
        doc = BeautifulSoup(reader.read(), "html.parser")
        template = doc.find("html")

    expander = Expander(template, variables)
    expander.walk()
    print(expander.getResult())


if __name__ == "__main__":
    main()
