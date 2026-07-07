import sys


MOD = 1_000_000_007


def main() -> None:
    input = sys.stdin.readline
    first = input().split()
    if not first:
        return
    n, m = map(int, first)
    grid = [input().strip() for _ in range(n)]
    dp = [[0] * m for _ in range(n)]
    if grid[0][0] == ".":
        dp[0][0] = 1
    for r in range(n):
        for c in range(m):
            if grid[r][c] == "#":
                dp[r][c] = 0
                continue
            if r:
                dp[r][c] = (dp[r][c] + dp[r - 1][c]) % MOD
            if c:
                dp[r][c] = (dp[r][c] + dp[r][c - 1]) % MOD
    print(dp[n - 1][m - 1])


if __name__ == "__main__":
    main()

