import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = data[0], data[1]
    values = [data[2 + r * m:2 + (r + 1) * m] for r in range(n)]
    negative_infinity = -(1 << 62)
    dp = [[negative_infinity] * n for _ in range(n)]
    dp[0][0] = values[0][0]

    for step in range(n + m - 2):
        nxt = [[negative_infinity] * n for _ in range(n)]
        for r1 in range(n):
            c1 = step - r1
            if not 0 <= c1 < m:
                continue
            for r2 in range(n):
                c2 = step - r2
                if not 0 <= c2 < m or dp[r1][r2] == negative_infinity:
                    continue
                for down1 in (0, 1):
                    for down2 in (0, 1):
                        nr1, nr2 = r1 + down1, r2 + down2
                        nc1, nc2 = c1 + 1 - down1, c2 + 1 - down2
                        if nr1 >= n or nr2 >= n or nc1 >= m or nc2 >= m:
                            continue
                        gain = values[nr1][nc1]
                        if (nr1, nc1) != (nr2, nc2):
                            gain += values[nr2][nc2]
                        nxt[nr1][nr2] = max(nxt[nr1][nr2], dp[r1][r2] + gain)
        dp = nxt

    print(dp[n - 1][n - 1])


if __name__ == "__main__":
    main()
