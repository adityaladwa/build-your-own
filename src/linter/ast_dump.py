import ast

with open("sample.py", "r") as reader:
    source = reader.read()

tree = ast.parse(source)
print(ast.dump(tree, indent=4))
