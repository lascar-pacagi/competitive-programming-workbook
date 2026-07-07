import sys


def main() -> None:
    s = sys.stdin.readline().strip()
    if not s:
        return
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):
        for l in range(n - length + 1):
            r = l + length - 1
            if s[l] == s[r]:
                dp[l][r] = dp[l + 1][r - 1] if l + 1 <= r - 1 else 0
            else:
                dp[l][r] = 1 + min(dp[l + 1][r], dp[l][r - 1])
    print(dp[0][n - 1])


if __name__ == "__main__":
    main()

