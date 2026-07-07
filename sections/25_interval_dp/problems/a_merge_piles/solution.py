import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    a = data[1:1 + n]
    pref = [0]
    for x in a:
        pref.append(pref[-1] + x)

    def total(l: int, r: int) -> int:
        return pref[r + 1] - pref[l]

    inf = 10**30
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):
        for l in range(0, n - length + 1):
            r = l + length - 1
            best = inf
            add = total(l, r)
            for k in range(l, r):
                cand = dp[l][k] + dp[k + 1][r] + add
                if cand < best:
                    best = cand
            dp[l][r] = best
    print(dp[0][n - 1])


if __name__ == "__main__":
    main()

