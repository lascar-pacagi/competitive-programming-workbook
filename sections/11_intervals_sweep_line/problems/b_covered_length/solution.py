"""Reference solution for B. Covered Length."""

import sys


def solve_case(intervals: list[tuple[int, int]]) -> int:
    events: list[tuple[int, int]] = []
    for l, r in intervals:
        events.append((l, 1))
        events.append((r, -1))
    events.sort()

    active = 0
    prev = events[0][0]
    total = 0
    i = 0
    while i < len(events):
        x = events[i][0]
        if active > 0:
            total += x - prev
        while i < len(events) and events[i][0] == x:
            active += events[i][1]
            i += 1
        prev = x
    return total


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        intervals: list[tuple[int, int]] = []
        for _ in range(n):
            l = data[idx]
            r = data[idx + 1]
            idx += 2
            intervals.append((l, r))
        out.append(str(solve_case(intervals)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

