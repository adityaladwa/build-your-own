from src.layout_engine.ease_mode import Block, Col, Row
from src.layout_engine.placed import PlacedCol, PlacedBlock
from src.layout_engine.render import RenderedCol, RenderedBlock, render
from src.layout_engine.wrapped import WrappedRow, WrappedBlock


def test_lays_out_a_grid_of_rows_of_columns():
    fixture = Col(
        Row(Block(1, 2), Block(3, 4)),
        Row(Block(5, 6), Col(
            Block(7, 8), Block(9, 10)
        ))
    )

    assert fixture.get_width() == 14
    assert fixture.get_height() == 22


def test_places_a_col_of_two_blocks():
    fixture = PlacedCol(
        PlacedBlock(1, 1),
        PlacedBlock(2, 4)
    )
    fixture.place(0, 0)
    assert fixture.report() == [
        "col",
        0, 0, 2, 5,
        ["block", 0, 0, 1, 1],
        ["block", 0, 1, 2, 5],
    ]


def test_renders_a_column_of_two_blocks():
    fixture = RenderedCol(
        RenderedBlock(1, 1),
        RenderedBlock(2, 4)
    )
    fixture.place(0, 0)
    actual = render(fixture)
    expected = "\n".join(["ba", "cc", "cc", "cc", "cc"])
    print(actual)
    assert actual == expected


def test_wrap_a_row_of_two_blocks_that_do_not_fit_on_one_row():
    fixture = WrappedRow(3, WrappedBlock(2, 1), WrappedBlock(2, 1))
    wrapped = fixture.wrap()
    wrapped.place(0, 0)
    assert wrapped.report() == [
        "row",
        0, 0, 2, 2,
        [
            "col",
            0, 0, 2, 2,
            ["row", 0, 0, 2, 1, ["block", 0, 0, 2, 1]],
            ["row", 0, 1, 2, 2, ["block", 0, 1, 2, 2]],
        ],
    ]
