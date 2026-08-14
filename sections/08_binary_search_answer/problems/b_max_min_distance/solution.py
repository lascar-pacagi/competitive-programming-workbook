"""Reference solution for B. Maximum Minimum Distance."""

import sys


def can_place(pos: list[int], k: int, dist: int) -> bool:
    count = 1
    last = pos[0]
    for x in pos[1:]:
        if x - last >= dist:
            count += 1
            last = x
            if count >= k:
                return True
    return False


def solve_case(pos: list[int], k: int) -> int:
    lo = 0
    hi = pos[-1] - pos[0] + 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if can_place(pos, k, mid):
            lo = mid
        else:
            hi = mid
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
        k = data[idx + 1]
        idx += 2
        pos = data[idx:idx + n]
        idx += n
        out.append(str(solve_case(pos, k)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
