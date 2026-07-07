import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    cap_a = next(it)
    cap_b = next(it)
    items = [(next(it), next(it)) for _ in range(n)]
    dp = [[0] * (cap_b + 1) for _ in range(cap_a + 1)]
    for weight, value in items:
        for a in range(cap_a, -1, -1):
            for b in range(cap_b, -1, -1):
                cur = dp[a][b]
                if a + weight <= cap_a:
                    dp[a + weight][b] = max(dp[a + weight][b], cur + value)
                if b + weight <= cap_b:
                    dp[a][b + weight] = max(dp[a][b + weight], cur + value)
    print(max(max(row) for row in dp))


if __name__ == "__main__":
    main()
