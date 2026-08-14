import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    value = [1] + data[1:] + [1]
    dp = [[0] * (n + 2) for _ in range(n + 2)]

    for gap in range(2, n + 2):
        for left in range(n + 2 - gap):
            right = left + gap
            dp[left][right] = max(
                dp[left][last] + dp[last][right]
                + value[left] * value[last] * value[right]
                for last in range(left + 1, right)
            )

    print(dp[0][n + 1])


if __name__ == "__main__":
    main()
