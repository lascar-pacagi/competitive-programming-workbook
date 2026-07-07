"""Reference solution for A. Minimum Adjacent Gap."""

import sys


def min_gap(values: list[int]) -> int:
    values.sort()
    return min(values[i] - values[i - 1] for i in range(1, len(values)))


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
        values = data[idx:idx + n]
        idx += n
        out.append(str(min_gap(values)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

