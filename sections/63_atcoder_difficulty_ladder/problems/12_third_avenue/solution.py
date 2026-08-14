import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    target, k = data[:2]
    coins = data[2:2 + k]

    inf = target + 1
    dp = [inf] * (target + 1)
    dp[0] = 0
    for amount in range(1, target + 1):
        for coin in coins:
            if coin <= amount and dp[amount - coin] != inf:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    print(-1 if dp[target] == inf else dp[target])


if __name__ == "__main__":
    main()
