import math
import sys

MOD = 1_000_000_007


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    previous = []
    answer = 0

    for x in data[1:1 + n]:
        current = [(x, 1)]
        for g, count in previous:
            next_gcd = math.gcd(g, x)
            if current[-1][0] == next_gcd:
                current[-1] = (next_gcd, current[-1][1] + count)
            else:
                current.append((next_gcd, count))
        answer = (answer + sum(g * count for g, count in current)) % MOD
        previous = current

    print(answer)


if __name__ == "__main__":
    main()
