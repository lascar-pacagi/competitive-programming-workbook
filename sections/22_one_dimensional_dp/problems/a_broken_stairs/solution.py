import sys


MOD = 1_000_000_007


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, b = data[0], data[1]
    broken = [False] * (n + 1)
    for x in data[2:2 + b]:
        broken[x] = True
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        if broken[i]:
            continue
        dp[i] = dp[i - 1]
        if i >= 2:
            dp[i] = (dp[i] + dp[i - 2]) % MOD
    print(dp[n] % MOD)


if __name__ == "__main__":
    main()

