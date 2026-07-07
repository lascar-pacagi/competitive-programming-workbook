"""Reference solution for C. Bounded Sum Sequence."""

import sys


def construct(n: int, m: int, s: int) -> str:
    if s < n or s > n * m:
        return "IMPOSSIBLE"
    ans: list[int] = []
    remaining = s
    for pos in range(n):
        left = n - pos - 1
        x = max(1, remaining - left * m)
        ans.append(x)
        remaining -= x
    return " ".join(map(str, ans))


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
        s = data[idx + 2]
        idx += 3
        out.append(construct(n, m, s))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

