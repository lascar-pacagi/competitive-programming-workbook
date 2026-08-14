import sys


MOD = 1_000_000_007


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    values = data[1:]
    maximum = max(values)

    frequency = [0] * (maximum + 1)
    for value in values:
        frequency[value] += 1

    powers = [1] * (n + 1)
    for i in range(1, n + 1):
        powers[i] = 2 * powers[i - 1] % MOD

    exact = [0] * (maximum + 1)
    for divisor in range(maximum, 0, -1):
        divisible_count = 0
        remove = 0
        for multiple in range(divisor, maximum + 1, divisor):
            divisible_count += frequency[multiple]
            if multiple != divisor:
                remove += exact[multiple]
        exact[divisor] = (powers[divisible_count] - 1 - remove) % MOD

    print(exact[1])


if __name__ == "__main__":
    main()
