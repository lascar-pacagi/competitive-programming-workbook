"""Reference solution for B. Longest Bounded Window."""

import sys


def longest_window(values: list[int], limit: int) -> int:
    left = 0
    total = 0
    best = 0
    for right, value in enumerate(values):
        total += value
        while left <= right and total > limit:
            total -= values[left]
            left += 1
        best = max(best, right - left + 1)
    return best


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n = data[idx]
        limit = data[idx + 1]
        idx += 2
        values = data[idx:idx + n]
        idx += n
        out.append(str(longest_window(values, limit)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

