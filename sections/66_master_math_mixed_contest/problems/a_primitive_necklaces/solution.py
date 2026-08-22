import math
import sys

MOD = 1_000_000_007


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    queries = [tuple(data[i : i + 2]) for i in range(1, 2 * data[0] + 1, 2)]
    maximum = max(n for n, _ in queries)
    mu = [0] * (maximum + 1)
    composite = bytearray(maximum + 1)
    primes: list[int] = []
    mu[1] = 1
    for value in range(2, maximum + 1):
        if not composite[value]:
            primes.append(value)
            mu[value] = -1
        for prime in primes:
            product = value * prime
            if product > maximum:
                break
            composite[product] = 1
            if value % prime == 0:
                mu[product] = 0
                break
            mu[product] = -mu[value]

    output = []
    for n, colors in queries:
        primitive_words = 0
        for divisor in range(1, math.isqrt(n) + 1):
            if n % divisor:
                continue
            primitive_words += mu[divisor] * pow(colors, n // divisor, MOD)
            other = n // divisor
            if other != divisor:
                primitive_words += mu[other] * pow(colors, n // other, MOD)
        answer = primitive_words % MOD * pow(n, MOD - 2, MOD) % MOD
        output.append(str(answer))
    print("\n".join(output))


if __name__ == "__main__":
    main()
