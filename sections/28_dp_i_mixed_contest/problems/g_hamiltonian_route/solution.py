import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    values = data[1:]
    weight = [
        values[row * n:(row + 1) * n]
        for row in range(n)
    ]

    infinity = 10**30
    mask_count = 1 << n
    dp = [[infinity] * n for _ in range(mask_count)]
    dp[1][0] = 0

    for mask in range(mask_count):
        for u in range(n):
            if dp[mask][u] == infinity:
                continue

            for v in range(n):
                if mask >> v & 1 or weight[u][v] < 0:
                    continue

                next_mask = mask | (1 << v)
                dp[next_mask][v] = min(
                    dp[next_mask][v],
                    dp[mask][u] + weight[u][v],
                )

    answer = dp[mask_count - 1][n - 1]
    print(-1 if answer == infinity else answer)


if __name__ == "__main__":
    main()
