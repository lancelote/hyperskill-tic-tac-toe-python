def running(number: str) -> list[float]:
    return [
        (int(number[i - 1]) + int(number[i])) / 2
        for i in range(1, len(number))
    ]


def main() -> None:
    number = input()
    print(running(number))


if __name__ == "__main__":
    main()
