import sys


MOD = 1_000_000_007


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    weight = data[1:]
    total = sum(weight)

    subset_sum = [0] * (1 << n)
    answer = 0
    for mask in range(1, 1 << n):
        least_bit = mask & -mask
        bit = least_bit.bit_length() - 1
        subset_sum[mask] = subset_sum[mask ^ least_bit] + weight[bit]
        term = total * pow(subset_sum[mask], MOD - 2, MOD) % MOD
        answer += term if mask.bit_count() & 1 else -term

    print(answer % MOD)


if __name__ == "__main__":
    main()
