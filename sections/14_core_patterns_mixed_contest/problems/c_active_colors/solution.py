"""Reference solution for C. Active Colors."""

import sys


def solve_case(intervals: list[tuple[int, int, int]], queries: list[int]) -> list[int]:
    events: list[tuple[int, int, int, int]] = []
    for l, r, color in intervals:
        events.append((r, 0, color, -1))
        events.append((l, 1, color, -1))
    for idx, x in enumerate(queries):
        events.append((x, 2, 0, idx))
    events.sort()

    freq: dict[int, int] = {}
    distinct = 0
    ans = [0] * len(queries)
    for _, kind, color, idx in events:
        if kind == 0:
            count = freq[color] - 1
            if count == 0:
                distinct -= 1
                del freq[color]
            else:
                freq[color] = count
        elif kind == 1:
            count = freq.get(color, 0)
            if count == 0:
                distinct += 1
            freq[color] = count + 1
        else:
            ans[idx] = distinct
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
        intervals: list[tuple[int, int, int]] = []
        for _ in range(n):
            l = data[idx]
            r = data[idx + 1]
            color = data[idx + 2]
            idx += 3
            intervals.append((l, r, color))
        queries = data[idx:idx + q]
        idx += q
        out.append(" ".join(map(str, solve_case(intervals, queries))))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

