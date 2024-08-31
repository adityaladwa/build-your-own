from src.layout_engine.placed import PlacedBlock, PlacedCol, PlacedRow


def render(root):
    root.place(0, 0)
    width = root.get_width()
    height = root.get_height()
    screen = make_screen(width, height)
    draw(screen, root)
    return "\n".join("".join(ch) for ch in screen)


def make_screen(width, height):
    screen = []
    for i in range(height):
        screen.append([" "] * width)
    return screen


def draw(screen, node, fill=None):
    fill = next_fill(fill)
    node.render(screen, fill)
    if hasattr(node, "children"):
        for child in node.children:
            fill = draw(screen, child, fill)
    return fill


def next_fill(fill):
    return "a" if fill is None else chr(ord(fill) + 1)


class Renderable:
    def render(self, screen, fill):
        for ix in range(self.get_width()):
            for iy in range(self.get_height()):
                screen[self.y0 + iy][self.x0 + ix] = fill


class RenderedBlock(PlacedBlock, Renderable):
    pass


class RenderedCol(PlacedCol, Renderable):
    pass


class RenderedRow(PlacedRow, Renderable):
    pass
