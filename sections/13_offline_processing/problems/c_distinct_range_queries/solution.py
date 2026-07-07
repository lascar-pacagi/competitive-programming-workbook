"""Reference solution for C. Distinct Range Queries."""

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


def solve_case(a: list[int], queries: list[tuple[int, int]]) -> list[int]:
    ordered = sorted((r, l, idx) for idx, (l, r) in enumerate(queries))
    bit = Fenwick(len(a))
    last: dict[int, int] = {}
    ans = [0] * len(queries)
    ptr = 0
    for r, l, idx in ordered:
        while ptr < r:
            ptr += 1
            value = a[ptr - 1]
            if value in last:
                bit.add(last[value], -1)
            bit.add(ptr, 1)
            last[value] = ptr
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
        queries: list[tuple[int, int]] = []
        for _ in range(q):
            l = data[idx]
            r = data[idx + 1]
            idx += 2
            queries.append((l, r))
        out.extend(map(str, solve_case(a, queries)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

