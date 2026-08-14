import sys


def line(values: list[int], left: int, right: int) -> int:
    two_back = one_back = 0
    for index in range(left, right + 1):
        two_back, one_back = one_back, max(one_back, two_back + values[index])
    return one_back


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    values = data[1:]
    if len(values) == 1:
        print(max(0, values[0]))
    else:
        print(max(line(values, 0, len(values) - 2), line(values, 1, len(values) - 1)))


if __name__ == "__main__":
    main()
