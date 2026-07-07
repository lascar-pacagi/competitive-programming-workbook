"""Reference solution for B. Until Threshold."""

import sys


def steps_to_threshold(x: int, y: int) -> int:
    steps = 0
    while x < y:
        x = 2 * x + 1
        steps += 1
    return steps


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    out: list[str] = []
    idx = 1
    for _ in range(t):
        x = data[idx]
        y = data[idx + 1]
        idx += 2
        out.append(str(steps_to_threshold(x, y)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

