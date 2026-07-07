"""Reference solution for B. Minimum Split Limit."""

import sys


def groups_needed(a: list[int], limit: int) -> int:
    groups = 1
    current = 0
    for x in a:
        if current + x <= limit:
            current += x
        else:
            groups += 1
            current = x
    return groups


def solve_case(a: list[int], d: int) -> int:
    lo = max(a)
    hi = sum(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if groups_needed(a, mid) <= d:
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
        d = data[idx + 1]
        idx += 2
        a = data[idx:idx + n]
        idx += n
        out.append(str(solve_case(a, d)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

