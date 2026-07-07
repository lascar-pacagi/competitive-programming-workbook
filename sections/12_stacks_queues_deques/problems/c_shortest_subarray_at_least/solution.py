"""Reference solution for C. Shortest Subarray At Least K."""

from collections import deque
import sys


def solve_case(a: list[int], target: int) -> int:
    pref = [0]
    for x in a:
        pref.append(pref[-1] + x)

    ans = len(a) + 1
    dq: deque[int] = deque()
    for i, value in enumerate(pref):
        while dq and value - pref[dq[0]] >= target:
            ans = min(ans, i - dq.popleft())
        while dq and pref[dq[-1]] >= value:
            dq.pop()
        dq.append(i)
    return -1 if ans == len(a) + 1 else ans


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n = data[idx]
        target = data[idx + 1]
        idx += 2
        a = data[idx:idx + n]
        idx += n
        out.append(str(solve_case(a, target)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

