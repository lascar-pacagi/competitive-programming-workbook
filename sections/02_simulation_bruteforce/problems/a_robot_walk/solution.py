"""Reference solution for A. Robot Walk."""

from __future__ import annotations

import sys


def solve_case(s: str) -> tuple[int, int, int]:
    x = 0
    y = 0
    best = 0
    for ch in s:
        if ch == "U":
            y += 1
        elif ch == "D":
            y -= 1
        elif ch == "L":
            x -= 1
        else:
            x += 1
        best = max(best, abs(x) + abs(y))
    return x, y, best


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    t = int(data[0])
    out: list[str] = []
    for i in range(1, t + 1):
        x, y, best = solve_case(data[i].decode())
        out.append(f"{x} {y} {best}")
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

