"""Reference solution for A. Complete Window."""

import sys


def solve_case(a: list[int], m: int) -> int:
    freq = [0] * (m + 1)
    have = 0
    best = len(a) + 1
    left = 0
    for right, value in enumerate(a):
        if 1 <= value <= m:
            if freq[value] == 0:
                have += 1
            freq[value] += 1
        while have == m:
            best = min(best, right - left + 1)
            old = a[left]
            if 1 <= old <= m:
                freq[old] -= 1
                if freq[old] == 0:
                    have -= 1
            left += 1
    return -1 if best == len(a) + 1 else best


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n = data[idx]
        m = data[idx + 1]
        idx += 2
        a = data[idx:idx + n]
        idx += n
        out.append(str(solve_case(a, m)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

