"""Reference solution for A. Inventory Cleanup."""

from collections import Counter
import sys


def min_deletions(values: list[int], k: int) -> int:
    freq = sorted(Counter(values).values())
    remove = max(0, len(freq) - k)
    return sum(freq[:remove])


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n = data[idx]
        k = data[idx + 1]
        idx += 2
        values = data[idx:idx + n]
        idx += n
        out.append(str(min_deletions(values, k)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

