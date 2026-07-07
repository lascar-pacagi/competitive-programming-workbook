import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, k = data[0], data[1]
    h = data[2:2 + n]
    inf = 10**30
    dp = [inf] * n
    dp[0] = 0
    for i in range(1, n):
        best = inf
        start = max(0, i - k)
        hi = h[i]
        for j in range(start, i):
            cand = dp[j] + abs(h[j] - hi)
            if cand < best:
                best = cand
        dp[i] = best
    print(dp[-1])


if __name__ == "__main__":
    main()

