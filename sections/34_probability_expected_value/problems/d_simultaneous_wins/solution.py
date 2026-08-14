import sys

MOD = 1_000_000_007


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    probability_sum = 0
    answer = 0

    for index in range(data[0]):
        p, q = data[1 + 2 * index:3 + 2 * index]
        probability = p * pow(q, MOD - 2, MOD) % MOD

        answer = (
            answer + probability * probability_sum
        ) % MOD
        probability_sum = (
            probability_sum + probability
        ) % MOD

    print(answer)


if __name__ == "__main__":
    main()
