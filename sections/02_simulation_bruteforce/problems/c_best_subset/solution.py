"""Reference solution for C. Best Subset."""

import sys


def best_subset(values: list[int], limit: int) -> int:
    n = len(values)
    best = 0
    for mask in range(1 << n):
        total = 0
        for i, value in enumerate(values):
            if mask & (1 << i):
                total += value
        if total <= limit and total > best:
            best = total
    return best


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n = data[idx]
        limit = data[idx + 1]
        idx += 2
        values = data[idx:idx + n]
        idx += n
        out.append(str(best_subset(values, limit)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

