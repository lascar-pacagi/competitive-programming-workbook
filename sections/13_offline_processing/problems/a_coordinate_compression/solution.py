"""Reference solution for A. Coordinate Compression."""

import sys


def solve_case(a: list[int]) -> list[int]:
    values = sorted(set(a))
    rank = {value: i for i, value in enumerate(values)}
    return [rank[x] for x in a]


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

