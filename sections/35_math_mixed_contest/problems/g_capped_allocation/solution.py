import sys


MOD = 1_000_000_007


def choose_small_k(top: int, k: int, inverse_factorial: int) -> int:
    if top < k or top < 0:
        return 0
    numerator = 1
    for i in range(1, k + 1):
        numerator = numerator * (top - i + 1) % MOD
    return numerator * inverse_factorial % MOD


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, target = data[:2]
    cap = data[2:]

    subset_count = 1 << n
    factorial = 1
    for i in range(1, n):
        factorial = factorial * i % MOD
    inverse_factorial = pow(factorial, MOD - 2, MOD)
    shifted_sum = [0] * subset_count
    answer = 0
    for mask in range(subset_count):
        if mask:
            least_bit = mask & -mask
            bit = least_bit.bit_length() - 1
            shifted_sum[mask] = shifted_sum[mask ^ least_bit] + cap[bit] + 1

        remaining = target - shifted_sum[mask]
        ways = choose_small_k(
            remaining + n - 1,
            n - 1,
            inverse_factorial,
        )
        answer += -ways if mask.bit_count() & 1 else ways

    print(answer % MOD)


if __name__ == "__main__":
    main()
