"""Reference solution for A. Value Counts."""

from collections import Counter
import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n = data[idx]
        q = data[idx + 1]
        idx += 2
        freq = Counter(data[idx:idx + n])
        idx += n
        for _ in range(q):
            x = data[idx]
            idx += 1
            out.append(str(freq.get(x, 0)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

