import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    full = (1 << n) - 1
    cheapest_for_mask: dict[int, int] = {}
    for _ in range(m):
        cost = next(it)
        k = next(it)
        mask = 0
        for _ in range(k):
            skill = next(it) - 1
            mask |= 1 << skill
        previous = cheapest_for_mask.get(mask)
        if previous is None or cost < previous:
            cheapest_for_mask[mask] = cost

    # An offer that costs no less and covers a subset of another offer can
    # never appear in an optimum. Removing it keeps the worst-case DP within
    # the exercise's Python time budget.
    raw_offers = list(cheapest_for_mask.items())
    offers = [
        (cost, mask)
        for mask, cost in raw_offers
        if not any(
            other_mask != mask
            and (mask | other_mask) == other_mask
            and other_cost <= cost
            for other_mask, other_cost in raw_offers
        )
    ]

    inf = 10**30
    dp = [inf] * (1 << n)
    dp[0] = 0
    for cost, offer in offers:
        new_dp = dp[:]
        for mask, value in enumerate(dp):
            if value == inf:
                continue
            candidate = value + cost
            merged = mask | offer
            if candidate < new_dp[merged]:
                new_dp[merged] = candidate
        dp = new_dp

    print(-1 if dp[full] >= inf else dp[full])


if __name__ == "__main__":
    main()
