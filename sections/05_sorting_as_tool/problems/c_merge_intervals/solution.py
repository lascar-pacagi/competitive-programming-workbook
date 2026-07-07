"""Reference solution for C. Merge Intervals."""

import sys


def merge(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    intervals.sort()
    merged: list[tuple[int, int]] = []
    for l, r in intervals:
        if not merged or l > merged[-1][1] + 1:
            merged.append((l, r))
        else:
            old_l, old_r = merged[-1]
            merged[-1] = (old_l, max(old_r, r))
    return merged


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
        merged = merge(intervals)
        out.append(str(len(merged)))
        out.extend(f"{l} {r}" for l, r in merged)
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

