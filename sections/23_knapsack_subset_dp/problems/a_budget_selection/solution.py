import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    w = next(it)
    dp = [0] * (w + 1)
    for _ in range(n):
        cost = next(it)
        value = next(it)
        if cost > w:
            continue
        for cap in range(w, cost - 1, -1):
            cand = dp[cap - cost] + value
            if cand > dp[cap]:
                dp[cap] = cand
    print(max(dp))


if __name__ == "__main__":
    main()

