def get_running_sum(number_str: str) -> list[int]:
    current = 0
    running_sum = []

    for digit_str in number_str:
        current += int(digit_str)
        running_sum.append(current)

    return running_sum


def main() -> None:
    number_str = input()
    print(get_running_sum(number_str))


if __name__ == '__main__':
    main()
