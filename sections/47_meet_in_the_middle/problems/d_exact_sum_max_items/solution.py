import sys


def enumerate_states(values: list[int]) -> list[tuple[int, int]]:
    states = [(0, 0)]
    for value in values:
        states.extend((total + value, count + 1) for total, count in states[:])
    return states


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, target = data[0], data[1]
    values = data[2 : 2 + n]
    middle = n // 2
    left_states = enumerate_states(values[:middle])
    right_states = enumerate_states(values[middle:])

    best_right_count: dict[int, int] = {}
    for total, count in right_states:
        previous = best_right_count.get(total, -1)
        if count > previous:
            best_right_count[total] = count

    answer = -1
    for total, count in left_states:
        other_count = best_right_count.get(target - total)
        if other_count is not None:
            answer = max(answer, count + other_count)
    print(answer)


if __name__ == "__main__":
    main()
