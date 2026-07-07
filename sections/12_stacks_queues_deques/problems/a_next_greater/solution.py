"""Reference solution for A. Next Greater."""

import sys


def solve_case(a: list[int]) -> list[int]:
    ans = [-1] * len(a)
    stack: list[int] = []
    for i in range(len(a) - 1, -1, -1):
        while stack and stack[-1] <= a[i]:
            stack.pop()
        if stack:
            ans[i] = stack[-1]
        stack.append(a[i])
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
        idx += 1
        a = data[idx:idx + n]
        idx += n
        out.append(" ".join(map(str, solve_case(a))))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

