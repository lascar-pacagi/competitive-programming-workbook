import sys


class Fenwick:
    def __init__(self, size: int) -> None:
        self.size = size
        self.bit = [0] * (size + 1)

    def add(self, index: int, delta: int) -> None:
        while index <= self.size:
            self.bit[index] += delta
            index += index & -index

    def sum(self, index: int) -> int:
        result = 0
        while index > 0:
            result += self.bit[index]
            index -= index & -index
        return result


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, q = data[0], data[1]
    values = data[2 : 2 + n]
    offset = 2 + n
    queries = []
    for query_index in range(q):
        left, right = data[offset], data[offset + 1]
        offset += 2
        queries.append((right, left, query_index))
    queries.sort()

    bit = Fenwick(n)
    last_position: dict[int, int] = {}
    answers = [0] * q
    processed_right = 0

    for right, left, query_index in queries:
        while processed_right < right:
            value = values[processed_right]
            position = processed_right + 1
            previous = last_position.get(value)
            if previous is not None:
                bit.add(previous, -1)
            bit.add(position, 1)
            last_position[value] = position
            processed_right += 1
        answers[query_index] = bit.sum(right) - bit.sum(left - 1)

    sys.stdout.write("\n".join(map(str, answers)) + "\n")


if __name__ == "__main__":
    main()
