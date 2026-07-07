"""Reference solution for B. Rescue Boats."""

import sys


def solve_case(weights: list[int], limit: int) -> int:
    weights.sort()
    left = 0
    right = len(weights) - 1
    boats = 0
    while left <= right:
        if weights[left] + weights[right] <= limit:
            left += 1
        right -= 1
        boats += 1
    return boats


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
        weights = data[idx:idx + n]
        idx += n
        out.append(str(solve_case(weights, limit)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

