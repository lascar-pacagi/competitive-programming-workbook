import sys


MOD = 1_000_000_007
RIGHT = 0
DOWN = 1


def main() -> None:
    input = sys.stdin.readline
    first = input().split()
    if not first:
        return
    n, m, k = map(int, first)
    grid = [input().strip() for _ in range(n)]
    if grid[0][0] == "#" or grid[n - 1][m - 1] == "#":
        print(0)
        return
    dp = [[[[0, 0] for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]
    if m > 1 and grid[0][1] == ".":
        dp[0][1][0][RIGHT] = 1
    if n > 1 and grid[1][0] == ".":
        dp[1][0][0][DOWN] = 1
    if n == 1 and m == 1:
        print(1)
        return
    for r in range(n):
        for c in range(m):
            if grid[r][c] == "#":
                continue
            for turns in range(k + 1):
                if c > 0 and grid[r][c - 1] == ".":
                    dp[r][c][turns][RIGHT] = (
                        dp[r][c][turns][RIGHT] + dp[r][c - 1][turns][RIGHT]
                    ) % MOD
                    if turns:
                        dp[r][c][turns][RIGHT] = (
                            dp[r][c][turns][RIGHT] + dp[r][c - 1][turns - 1][DOWN]
                        ) % MOD
                if r > 0 and grid[r - 1][c] == ".":
                    dp[r][c][turns][DOWN] = (
                        dp[r][c][turns][DOWN] + dp[r - 1][c][turns][DOWN]
                    ) % MOD
                    if turns:
                        dp[r][c][turns][DOWN] = (
                            dp[r][c][turns][DOWN] + dp[r - 1][c][turns - 1][RIGHT]
                        ) % MOD
    ans = 0
    for turns in range(k + 1):
        ans = (ans + dp[n - 1][m - 1][turns][RIGHT] + dp[n - 1][m - 1][turns][DOWN]) % MOD
    print(ans)


if __name__ == "__main__":
    main()

