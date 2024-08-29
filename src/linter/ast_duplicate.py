import ast
from collections import Counter


class FindDuplicateKeys(ast.NodeVisitor):
    def visit_Dict(self, node):
        seen = Counter()
        for key in node.keys:
            if isinstance(key, ast.Constant):
                seen[key.value] += 1

        problems = {k for (k, v) in seen.items() if v > 1}
        self.report(problems, node)
        self.generic_visit(node)

    def report(self, problems, node):
        if problems:
            msg = ", ".join(p for p in problems)
            print(f"Duplicate key(s) {{{msg}}} at {node.lineno}")


with open("duplicate.py", "r") as reader:
    source = reader.read()

tree = ast.parse(source)

duplicate = FindDuplicateKeys()

duplicate.visit(tree)
