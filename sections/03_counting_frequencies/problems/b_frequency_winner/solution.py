"""Reference solution for B. Frequency Winner."""

from collections import Counter
import sys


def winner(values: list[int]) -> tuple[int, int]:
    freq = Counter(values)
    best_value = values[0]
    best_count = -1
    for value, count in freq.items():
        if count > best_count or (count == best_count and value < best_value):
            best_value = value
            best_count = count
    return best_value, best_count


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
        value, count = winner(values)
        out.append(f"{value} {count}")
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

