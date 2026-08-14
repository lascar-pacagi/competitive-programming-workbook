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
    coefficients = Fenwick(n + 1)
    weighted_coefficients = Fenwick(n + 1)

    def add_range(left: int, right: int, delta: int) -> None:
        coefficients.add(left, delta)
        coefficients.add(right + 1, -delta)
        weighted_coefficients.add(left, delta * left)
        weighted_coefficients.add(right + 1, -delta * (right + 1))

    def prefix_sum(position: int) -> int:
        return (position + 1) * coefficients.sum(position) - weighted_coefficients.sum(position)

    index = 2
    output: list[str] = []
    for _ in range(q):
        operation = data[index]
        left = data[index + 1]
        right = data[index + 2]
        index += 3
        if operation == 1:
            delta = data[index]
            index += 1
            add_range(left, right, delta)
        else:
            output.append(str(prefix_sum(right) - prefix_sum(left - 1)))
    sys.stdout.write("\n".join(output) + ("\n" if output else ""))


if __name__ == "__main__":
    main()
