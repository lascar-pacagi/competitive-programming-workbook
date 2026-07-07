"""Reference solution for C. Minimum Capacity."""

import sys


def days_needed(weights: list[int], capacity: int) -> int:
    days = 1
    cur = 0
    for w in weights:
        if cur + w <= capacity:
            cur += w
        else:
            days += 1
            cur = w
    return days


def solve_case(weights: list[int], days: int) -> int:
    lo = max(weights)
    hi = sum(weights)
    while lo < hi:
        mid = (lo + hi) // 2
        if days_needed(weights, mid) <= days:
            hi = mid
        else:
            lo = mid + 1
    return lo


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n = data[idx]
        days = data[idx + 1]
        idx += 2
        weights = data[idx:idx + n]
        idx += n
        out.append(str(solve_case(weights, days)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

