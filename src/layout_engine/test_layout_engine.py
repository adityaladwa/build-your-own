from src.layout_engine.ease_mode import Block, Col, Row
from src.layout_engine.placed import PlacedCol, PlacedBlock


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
