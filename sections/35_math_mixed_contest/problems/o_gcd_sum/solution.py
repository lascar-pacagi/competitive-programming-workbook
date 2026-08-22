import math
import sys

MOD = 1_000_000_007


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    q = data[0]
    queries = data[1:1 + q]
    maximum = max(queries, default=1)

    phi = list(range(maximum + 1))
    for p in range(2, maximum + 1):
        if phi[p] != p:
            continue
        for multiple in range(p, maximum + 1, p):
            phi[multiple] -= phi[multiple] // p

    answers = []
    for n in queries:
        answer = 0
        for d in range(1, math.isqrt(n) + 1):
            if n % d:
                continue
            answer += d * phi[n // d]
            other = n // d
            if other != d:
                answer += other * phi[d]
        answers.append(str(answer % MOD))
    print("\n".join(answers))


if __name__ == "__main__":
    main()
