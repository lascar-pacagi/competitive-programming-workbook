import sys


MOD = 1_000_000_007


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, target = data[:2]
    values = data[2:2 + n]

    factors = []
    remaining = target
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            exponent = 0
            while remaining % prime == 0:
                remaining //= prime
                exponent += 1
            factors.append((prime, exponent))
        prime += 1
    if remaining > 1:
        factors.append((remaining, 1))

    mask_count = 1 << len(factors)
    frequency = [0] * mask_count
    for value in values:
        if target % value:
            continue
        mask = 0
        copy = value
        for bit, (prime, target_exponent) in enumerate(factors):
            exponent = 0
            while copy % prime == 0:
                copy //= prime
                exponent += 1
            if exponent == target_exponent:
                mask |= 1 << bit
        frequency[mask] += 1

    dp = [0] * mask_count
    dp[0] = 1
    for type_mask, count in enumerate(frequency):
        if count == 0:
            continue
        nonempty_ways = (pow(2, count, MOD) - 1) % MOD
        next_dp = dp.copy()
        for mask, ways in enumerate(dp):
            combined = mask | type_mask
            next_dp[combined] += ways * nonempty_ways
            next_dp[combined] %= MOD
        dp = next_dp

    full_mask = mask_count - 1
    answer = dp[full_mask]
    if full_mask == 0:
        answer -= 1
    print(answer % MOD)


if __name__ == "__main__":
    main()
