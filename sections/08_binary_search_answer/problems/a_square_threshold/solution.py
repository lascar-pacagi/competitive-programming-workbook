"""Reference solution for A. Square Threshold."""

import sys


def ceil_sqrt(n: int) -> int:
    lo = 0
    hi = 1_000_000_000
    while lo < hi:
        mid = (lo + hi) // 2
        if mid * mid >= n:
            hi = mid
        else:
            lo = mid + 1
    return lo


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    out = [str(ceil_sqrt(data[i])) for i in range(1, t + 1)]
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

