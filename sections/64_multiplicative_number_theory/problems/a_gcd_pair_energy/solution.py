import sys

MOD = 1_000_000_007


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, k = data[:2]
    values = data[2 : 2 + n]
    maximum = max(values)
    frequency = [0] * (maximum + 1)
    for value in values:
        frequency[value] += 1

    divisible = [0] * (maximum + 1)
    for d in range(1, maximum + 1):
        divisible[d] = sum(frequency[d::d])

    jordan = [0] + [pow(d, k, MOD) for d in range(1, maximum + 1)]
    for d in range(1, maximum + 1):
        contribution = jordan[d]
        for multiple in range(2 * d, maximum + 1, d):
            jordan[multiple] = (jordan[multiple] - contribution) % MOD

    answer = 0
    for d in range(1, maximum + 1):
        count = divisible[d]
        pairs = count * (count - 1) // 2
        answer = (answer + jordan[d] * pairs) % MOD
    print(answer)


if __name__ == "__main__":
    main()
