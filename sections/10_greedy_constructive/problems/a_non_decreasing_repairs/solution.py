"""Reference solution for A. Non-Decreasing Repairs."""

import sys


def solve_case(a: list[int]) -> int:
    cost = 0
    need = a[0]
    for x in a[1:]:
        if x < need:
            cost += need - x
        else:
            need = x
    return cost


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
        out.append(str(solve_case(a)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

