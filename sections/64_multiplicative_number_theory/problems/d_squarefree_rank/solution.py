import math
import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    queries = data[1 : 1 + data[0]]
    limit = math.isqrt(3 * max(queries)) + 1

    mu = [0] * (limit + 1)
    composite = bytearray(limit + 1)
    primes: list[int] = []
    mu[1] = 1
    for value in range(2, limit + 1):
        if not composite[value]:
            primes.append(value)
            mu[value] = -1
        for prime in primes:
            product = value * prime
            if product > limit:
                break
            composite[product] = 1
            if value % prime == 0:
                mu[product] = 0
                break
            mu[product] = -mu[value]

    def count_squarefree(x: int) -> int:
        return sum(
            mu[d] * (x // (d * d))
            for d in range(1, math.isqrt(x) + 1)
        )

    answers = []
    for rank in queries:
        low, high = 1, 3 * rank
        while low < high:
            middle = (low + high) // 2
            if count_squarefree(middle) >= rank:
                high = middle
            else:
                low = middle + 1
        answers.append(str(low))
    print("\n".join(answers))


if __name__ == "__main__":
    main()
