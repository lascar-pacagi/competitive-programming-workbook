"""Reference solution for B. Sliding Window Maximum."""

from collections import deque
import sys


def solve_case(a: list[int], k: int) -> list[int]:
    dq: deque[int] = deque()
    ans: list[int] = []
    for i, x in enumerate(a):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and a[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if i + 1 >= k:
            ans.append(a[dq[0]])
    return ans


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
        a = data[idx:idx + n]
        idx += n
        out.append(" ".join(map(str, solve_case(a, k))))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

