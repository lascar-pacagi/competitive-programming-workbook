import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    days = data[1 : 1 + n]
    inf = 10**9
    dp = [0, inf, inf]  # rest, C++, Python as the previous day's action
    for available in days:
        ndp = [min(dp) + 1, inf, inf]
        if available & 1:
            ndp[1] = min(dp[0], dp[2])
        if available & 2:
            ndp[2] = min(dp[0], dp[1])
        dp = ndp
    print(min(dp))


if __name__ == "__main__":
    main()
