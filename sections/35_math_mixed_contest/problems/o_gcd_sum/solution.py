import sys

MOD = 1_000_000_007


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    queries = data[1:1 + data[0]]
    maximum = max(queries, default=1)
    # Smallest-prime-factor sieve from section 31.
    smallest = list(range(maximum + 1))
    p = 2
    while p * p <= maximum:
        if smallest[p] == p:
            for multiple in range(p * p, maximum + 1, p):
                if smallest[multiple] == multiple:
                    smallest[multiple] = p
        p += 1

    power = [1] * (maximum + 1)
    answer = [0] * (maximum + 1)
    answer[1] = 1
    for value in range(2, maximum + 1):
        p = smallest[value]
        rest = value // p
        if rest % p:
            power[value] = p
            answer[value] = (2 * p - 1) * answer[rest]
        else:
            previous_power = power[rest]
            power[value] = previous_power * p
            answer[value] = (p * answer[rest]
                + (p - 1) * previous_power * answer[rest // previous_power])
    print("\n".join(str(answer[value] % MOD) for value in queries))


if __name__ == "__main__":
    main()
