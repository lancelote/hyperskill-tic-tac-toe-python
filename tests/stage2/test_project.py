from textwrap import dedent

from src.stage2.project import to_grid


def test_to_grid():
    assert (
        to_grid("O_OXXO_XX")
        == dedent(
            """
        ---------
        | O _ O |
        | X X O |
        | _ X X |
        ---------
        """
        ).strip()
    )
