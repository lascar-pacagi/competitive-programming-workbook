import sys


MOD = 1_000_000_007


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, k = data
    dp = [0] * (k + 1)
    dp[0] = 1
    for people in range(1, n + 1):
        for teams in range(min(people, k), 0, -1):
            dp[teams] = (dp[teams - 1] + teams * dp[teams]) % MOD
        dp[0] = 0
    print(dp[k])


if __name__ == "__main__":
    main()
