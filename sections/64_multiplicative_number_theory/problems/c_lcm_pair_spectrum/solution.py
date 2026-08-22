import sys

MOD = 1_000_000_007


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, maximum = data[:2]
    frequency = [0] * (maximum + 1)
    for value in data[2 : 2 + n]:
        frequency[value] += 1

    inside = [0] * (maximum + 1)
    for divisor in range(1, maximum + 1):
        amount = frequency[divisor]
        if amount:
            for multiple in range(divisor, maximum + 1, divisor):
                inside[multiple] += amount

    exact = [count * (count - 1) // 2 % MOD for count in inside]
    for divisor in range(1, maximum + 1):
        contribution = exact[divisor]
        for multiple in range(2 * divisor, maximum + 1, divisor):
            exact[multiple] = (exact[multiple] - contribution) % MOD
    print(*exact[1:])


if __name__ == "__main__":
    main()
