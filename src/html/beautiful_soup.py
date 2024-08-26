from bs4 import BeautifulSoup, NavigableString, Tag
import yaml

html_doc = """<html>
<body>
<h1>Title</h1>
<p>paragraph</p>
</body>
</html>"""

html = """<html>
  <head>
    <title>Software Design by Example</title>
  </head>
  <body>
    <h1>Main Title</h1>
    <p>introductory paragraph</p>
    <ul>
      <li>first item</li>
      <li>second item is <em>emphasized</em></li>
    </ul>
  </body>
</html>
"""


def display(node):
    if isinstance(node, NavigableString):
        print(f"string: {repr(node.text)}")
        return
    if isinstance(node, Tag):
        print(f"tag: {node.name} {node.attrs}")
        return
    else:
        print(f"node: {node.name}")
        for child in node.children:
            display(child)


def display_attrs(node):
    if isinstance(node, Tag):
        print(f"node: {node.name} {node.attrs}")
        for child in node:
            display(child)


def recurse(node, catalog):
    assert isinstance(node, Tag)

    if node.name not in catalog:
        catalog[node.name] = set()

    for child in node.children:
        if isinstance(child, Tag):
            catalog[node.name].add(child.name)
            recurse(child, catalog)


class Visitor:
    def visit(self, node):
        if isinstance(node, NavigableString):
            self._text(node)
        elif isinstance(node, Tag):
            self._tag_enter(node)
            for child in node:
                self.visit(child)
            self._tag_exit(node)

    def _tag_enter(self, node):
        pass

    def _tag_exit(self, node):
        pass

    def _text(self, node):
        pass


class Catalog(Visitor):
    def __init__(self):
        super().__init__()
        self.catalog = {}

    def _tag_enter(self, node):
        if node.name not in self.catalog:
            self.catalog[node.name] = set()
        for child in node:
            if isinstance(child, Tag):
                self.catalog[node.name].add(child.name)


class Check(Visitor):
    def __init__(self, manifest):
        super().__init__()
        self.manifest = manifest
        self.problems = {}

    def _tag_enter(self, node):
        actual = {child.name for child in node if isinstance(child, Tag)}
        errors = actual - self.manifest.get(node.name, set())
        if errors:
            errors |= self.problems.get(node.name, set())
            self.problems[node.name] = errors


# doc = BeautifulSoup(html_doc, 'html.parser')
# display(doc)

# doc = BeautifulSoup(html, 'html.parser')
# recurse(doc)


def read_manifest(filename):
    with open(filename, "r") as reader:
        result = yaml.load(reader, Loader=yaml.FullLoader)
        for key in result:
            result[key] = set(result[key])
        return result


manifest = read_manifest("manifest.yml")

with open("example.html", "r") as reader:
    text = reader.read()
doc = BeautifulSoup(text, "html.parser")

checker = Check(manifest)
checker.visit(doc.html)
for key, value in checker.problems.items():
    print(f"{key}: {', '.join(sorted(value))}")
