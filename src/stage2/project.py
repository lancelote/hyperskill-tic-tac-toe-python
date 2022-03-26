from textwrap import dedent


def to_grid(state: str) -> str:
    assert len(state) == 9, "state should be 9 symbols"

    return dedent(
        f"""
        ---------
        | {state[0]} {state[1]} {state[2]} |
        | {state[3]} {state[4]} {state[5]} |
        | {state[6]} {state[7]} {state[8]} |
        ---------
    """
    ).strip()


def main() -> None:
    state = input("Enter cells: ")
    grid = to_grid(state)
    print(grid)


if __name__ == "__main__":
    main()
