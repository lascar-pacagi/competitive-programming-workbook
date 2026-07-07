"""Reference solution for C. Point Coverage."""

import sys


def solve_case(intervals: list[tuple[int, int]], queries: list[int]) -> list[int]:
    events: list[tuple[int, int, int]] = []
    for l, r in intervals:
        events.append((l, 0, -1))
        events.append((r, 2, -1))
    for idx, x in enumerate(queries):
        events.append((x, 1, idx))
    events.sort()

    active = 0
    ans = [0] * len(queries)
    for _, kind, idx in events:
        if kind == 0:
            active += 1
        elif kind == 1:
            ans[idx] = active
        else:
            active -= 1
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
        intervals: list[tuple[int, int]] = []
        for _ in range(n):
            l = data[idx]
            r = data[idx + 1]
            idx += 2
            intervals.append((l, r))
        queries = data[idx:idx + q]
        idx += q
        out.append(" ".join(map(str, solve_case(intervals, queries))))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

