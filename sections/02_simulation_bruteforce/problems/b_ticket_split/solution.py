"""Reference solution for B. Ticket Split."""

import sys


def find_split(n: int, s: int, a: int, b: int, c: int) -> tuple[int, int, int] | None:
    for x in range(n + 1):
        for y in range(n - x + 1):
            z = n - x - y
            if a * x + b * y + c * z == s:
                return x, y, z
    return None


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n, s, a, b, c = data[idx:idx + 5]
        idx += 5
        ans = find_split(n, s, a, b, c)
        if ans is None:
            out.append("-1")
        else:
            out.append(f"{ans[0]} {ans[1]} {ans[2]}")
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

