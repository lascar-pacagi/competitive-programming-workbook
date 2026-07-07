"""Reference solution for C. Best Study Streak."""

import sys


def solve(values: list[int], limit: int) -> tuple[int, int]:
    left = 0
    total = 0
    best_len = 0
    best_start = 0
    for right, value in enumerate(values):
        total += value
        while left <= right and total > limit:
            total -= values[left]
            left += 1
        length = right - left + 1
        start = left + 1
        if length > best_len or (length == best_len and length > 0 and start < best_start):
            best_len = length
            best_start = start
    return best_len, best_start


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
        length, start = solve(values, limit)
        out.append(f"{length} {start}")
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

