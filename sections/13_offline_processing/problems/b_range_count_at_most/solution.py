"""Reference solution for B. Range Count At Most."""

import sys


class Fenwick:
    def __init__(self, n: int) -> None:
        self.bit = [0] * (n + 1)

    def add(self, idx: int, delta: int) -> None:
        while idx < len(self.bit):
            self.bit[idx] += delta
            idx += idx & -idx

    def sum(self, idx: int) -> int:
        total = 0
        while idx > 0:
            total += self.bit[idx]
            idx -= idx & -idx
        return total

    def range_sum(self, left: int, right: int) -> int:
        return self.sum(right) - self.sum(left - 1)


def solve_case(a: list[int], queries: list[tuple[int, int, int]]) -> list[int]:
    values = sorted((value, pos) for pos, value in enumerate(a, start=1))
    ordered = sorted((x, l, r, idx) for idx, (l, r, x) in enumerate(queries))
    bit = Fenwick(len(a))
    ans = [0] * len(queries)
    ptr = 0
    for x, l, r, idx in ordered:
        while ptr < len(values) and values[ptr][0] <= x:
            _, pos = values[ptr]
            bit.add(pos, 1)
            ptr += 1
        ans[idx] = bit.range_sum(l, r)
    return ans


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n = data[idx]
        q = data[idx + 1]
        idx += 2
        a = data[idx:idx + n]
        idx += n
        queries: list[tuple[int, int, int]] = []
        for _ in range(q):
            l = data[idx]
            r = data[idx + 1]
            x = data[idx + 2]
            idx += 3
            queries.append((l, r, x))
        out.extend(map(str, solve_case(a, queries)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

