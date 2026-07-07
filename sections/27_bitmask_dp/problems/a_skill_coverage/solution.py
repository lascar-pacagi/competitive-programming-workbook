import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    full = (1 << n) - 1
    offers: list[tuple[int, int]] = []
    for _ in range(m):
        cost = next(it)
        k = next(it)
        mask = 0
        for _ in range(k):
            skill = next(it) - 1
            mask |= 1 << skill
        offers.append((cost, mask))

    inf = 10**30
    dp = [inf] * (1 << n)
    dp[0] = 0
    for cost, offer in offers:
        new_dp = dp[:]
        for mask in range(1 << n):
            candidate = dp[mask] + cost
            merged = mask | offer
            if candidate < new_dp[merged]:
                new_dp[merged] = candidate
        dp = new_dp

    print(-1 if dp[full] >= inf else dp[full])


if __name__ == "__main__":
    main()
