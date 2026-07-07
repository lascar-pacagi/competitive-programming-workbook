import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    inf = 10**30
    prev = [inf] * m
    for r in range(n):
        cur = [inf] * m
        for c in range(m):
            x = next(it)
            if r == 0 and c == 0:
                cur[c] = x
            else:
                best = prev[c]
                if c:
                    best = min(best, cur[c - 1])
                cur[c] = best + x
        prev = cur
    print(prev[-1])


if __name__ == "__main__":
    main()

