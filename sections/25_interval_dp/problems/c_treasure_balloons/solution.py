import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    a = [1] + data[1:1 + n] + [1]
    dp = [[0] * (n + 2) for _ in range(n + 2)]
    for length in range(1, n + 1):
        for l in range(1, n - length + 2):
            r = l + length - 1
            best = 0
            for k in range(l, r + 1):
                cand = dp[l][k - 1] + dp[k + 1][r] + a[l - 1] * a[k] * a[r + 1]
                if cand > best:
                    best = cand
            dp[l][r] = best
    print(dp[1][n])


if __name__ == "__main__":
    main()

