import bisect
import sys

class Fenwick:

    def __init__(self, size: int) -> None:
        self.bit = [0] * (size + 1)

    def add(self, index: int, delta: int) -> None:
        while index < len(self.bit):
            self.bit[index] += delta
            index += index & -index

    def prefix_sum(self, index: int) -> int:
        total = 0
        while index:
            total += self.bit[index]
            index -= index & -index
        return total

def main() -> None:
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    pointer = 0
    n = int(tokens[pointer])
    q = int(tokens[pointer + 1])
    pointer += 2
    initial = tokens[pointer:pointer + n]
    salary = [0] + [int(value) for value in initial]
    pointer += n
    operations: list[tuple[bytes, int, int]] = []
    coords = salary[1:]
    for _ in range(q):
        kind = tokens[pointer]
        first = int(tokens[pointer + 1])
        second = int(tokens[pointer + 2])
        pointer += 3
        operations.append((kind, first, second))
        if kind == b'!':
            coords.append(second)
    coords = sorted(set(coords))
    bit = Fenwick(len(coords))

    def rank_of(value: int) -> int:
        return bisect.bisect_left(coords, value) + 1
    for value in salary[1:]:
        bit.add(rank_of(value), 1)
    output: list[str] = []
    for kind, first, second in operations:
        if kind == b'!':
            employee, new_salary = (first, second)
            bit.add(rank_of(salary[employee]), -1)
            salary[employee] = new_salary
            bit.add(rank_of(new_salary), 1)
        else:
            low, high = (first, second)
            before_low = bisect.bisect_left(coords, low)
            through_high = bisect.bisect_right(coords, high)
            answer = (
                bit.prefix_sum(through_high)
                - bit.prefix_sum(before_low)
            )
            output.append(str(answer))
    print('\n'.join(output))
if __name__ == '__main__':
    main()
