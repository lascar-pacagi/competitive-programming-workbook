import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    profit = [[next(it) for _ in range(n)] for _ in range(n)]
    total = 1 << n
    neg = -10**30
    dp = [neg] * total
    dp[0] = 0

    for mask in range(total):
        worker = mask.bit_count()
        if worker == n or dp[mask] == neg:
            continue
        for job in range(n):
            if not (mask >> job) & 1:
                nxt = mask | (1 << job)
                value = dp[mask] + profit[worker][job]
                if value > dp[nxt]:
                    dp[nxt] = value

    print(dp[total - 1])


if __name__ == "__main__":
    main()
