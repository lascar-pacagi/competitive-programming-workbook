import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    values = data[1:]

    # Each pair is (minimum, number of suffixes having that minimum).
    stack: list[tuple[int, int]] = []
    ending_sum = 0
    answer = 0

    for value in values[:n]:
        ways = 1
        while stack and stack[-1][0] >= value:
            old_value, old_ways = stack.pop()
            ending_sum -= old_value * old_ways
            ways += old_ways

        stack.append((value, ways))
        ending_sum += value * ways
        answer += ending_sum

    print(answer)


if __name__ == "__main__":
    main()
