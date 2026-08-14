import collections
import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, k = data[:2]
    cost = data[2:]
    dp = [0] * n
    candidates = collections.deque([0])
    dp[0] = cost[0]

    for i in range(1, n):
        while candidates[0] < i - k:
            candidates.popleft()

        dp[i] = cost[i] + dp[candidates[0]]

        while candidates and dp[candidates[-1]] >= dp[i]:
            candidates.pop()
        candidates.append(i)

    print(dp[-1])


if __name__ == "__main__":
    main()
