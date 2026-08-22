import sys

MOD = 1_000_000_007


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    q = data[0]
    queries = [(data[i], data[i + 1]) for i in range(1, 2 * q + 1, 2)]
    maximum = max((min(a, b) for a, b in queries), default=1)

    mu = [0] * (maximum + 1)
    primes = []
    composite = [False] * (maximum + 1)
    mu[1] = 1
    for value in range(2, maximum + 1):
        if not composite[value]:
            primes.append(value)
            mu[value] = -1
        for prime in primes:
            product = value * prime
            if product > maximum:
                break
            composite[product] = True
            if value % prime == 0:
                mu[product] = 0
                break
            mu[product] = -mu[value]

    prefix = [0] * (maximum + 1)
    for value in range(1, maximum + 1):
        prefix[value] = prefix[value - 1] + mu[value]

    answers = []
    for a, b in queries:
        answer = 0
        left = 1
        limit = min(a, b)
        while left <= limit:
            qa = a // left
            qb = b // left
            right = min(limit, a // qa, b // qb)
            answer += (prefix[right] - prefix[left - 1]) * qa * qb
            left = right + 1
        answers.append(str(answer % MOD))
    print("\n".join(answers))


if __name__ == "__main__":
    main()
