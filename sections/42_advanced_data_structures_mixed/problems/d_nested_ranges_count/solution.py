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
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    ranges = [(data[2 * i + 1], data[2 * i + 2], i) for i in range(n)]
    rights = sorted({right for _, right, _ in ranges})
    ranges.sort(key=lambda interval: (interval[0], -interval[1]))

    def rank_of(right: int) -> int:
        return bisect.bisect_left(rights, right) + 1

    contains = [0] * n
    contained_by = [0] * n

    bit = Fenwick(len(rights))
    processed = 0
    start = 0
    while start < n:
        end = start + 1
        while end < n and ranges[end][:2] == ranges[start][:2]:
            end += 1
        group_size = end - start
        rank = rank_of(ranges[start][1])
        base = processed - bit.prefix_sum(rank - 1)
        for _, _, index in ranges[start:end]:
            contained_by[index] = base + group_size - 1
        bit.add(rank, group_size)
        processed += group_size
        start = end

    bit = Fenwick(len(rights))
    end = n
    while end:
        start = end - 1
        while start > 0 and ranges[start - 1][:2] == ranges[end - 1][:2]:
            start -= 1
        group_size = end - start
        rank = rank_of(ranges[start][1])
        base = bit.prefix_sum(rank)
        for _, _, index in ranges[start:end]:
            contains[index] = base + group_size - 1
        bit.add(rank, group_size)
        end = start

    print(" ".join(map(str, contains)))
    print(" ".join(map(str, contained_by)))


if __name__ == "__main__":
    main()
