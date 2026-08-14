import sys


MOD = 1_000_000_007


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    queries = data[1:]
    maximum = max(queries)

    divisor_count = [0] * (maximum + 1)
    expectation_sum = [0] * (maximum + 1)
    expectation = [0] * (maximum + 1)

    for divisor in range(1, maximum + 1):
        if divisor > 1:
            expectation[divisor] = (
                1
                + expectation_sum[divisor]
                * pow(divisor_count[divisor], MOD - 2, MOD)
            ) % MOD

        for multiple in range(2 * divisor, maximum + 1, divisor):
            divisor_count[multiple] += 1
            expectation_sum[multiple] += expectation[divisor]
            expectation_sum[multiple] %= MOD

    print("\n".join(str(expectation[value]) for value in queries))


if __name__ == "__main__":
    main()
