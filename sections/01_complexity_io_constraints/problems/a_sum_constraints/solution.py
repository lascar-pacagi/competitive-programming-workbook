"""Reference solution for A. Sum Under Constraints."""

import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    t = next(it)
    out: list[str] = []
    for _ in range(t):
        n = next(it)
        total = 0
        for _ in range(n):
            total += next(it)
        out.append(str(total))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

