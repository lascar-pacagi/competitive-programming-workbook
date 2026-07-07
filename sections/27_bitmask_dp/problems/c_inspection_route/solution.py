import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    cost = [[next(it) for _ in range(n)] for _ in range(n)]
    total = 1 << n
    full = total - 1
    inf = 10**30
    dp = [[inf] * n for _ in range(total)]
    dp[1][0] = 0

    for mask in range(total):
        if not (mask & 1):
            continue
        for last in range(n):
            cur = dp[mask][last]
            if cur >= inf:
                continue
            for nxt in range(n):
                if not (mask >> nxt) & 1:
                    new_mask = mask | (1 << nxt)
                    value = cur + cost[last][nxt]
                    if value < dp[new_mask][nxt]:
                        dp[new_mask][nxt] = value

    answer = min(dp[full][last] + cost[last][0] for last in range(n))
    print(answer)


if __name__ == "__main__":
    main()
