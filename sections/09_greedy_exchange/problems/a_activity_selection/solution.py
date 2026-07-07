"""Reference solution for A. Activity Selection."""

import sys


def solve_case(intervals: list[tuple[int, int]]) -> int:
    intervals.sort(key=lambda p: (p[1], p[0]))
    count = 0
    last_end = -10**30
    for start, end in intervals:
        if start >= last_end:
            count += 1
            last_end = end
    return count


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
            start = data[idx]
            end = data[idx + 1]
            idx += 2
            intervals.append((start, end))
        out.append(str(solve_case(intervals)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

