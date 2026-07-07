import sys
from collections import defaultdict


def spf_table(n: int) -> list[int]:
    spf = list(range(n + 1))
    if n >= 1:
        spf[1] = 1
    for p in range(2, n + 1):
        if spf[p] == p and p * p <= n:
            for x in range(p * p, n + 1, p):
                if spf[x] == x:
                    spf[x] = p
    return spf


def prime_factors(x: int, spf: list[int]) -> list[int]:
    factors = []
    while x > 1:
        p = spf[x]
        factors.append(p)
        while x % p == 0:
            x //= p
    return factors


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    arr = data[1 : 1 + n]
    spf = spf_table(max(arr))
    seen = defaultdict(int)
    answer = 0
    for idx, x in enumerate(arr):
        factors = prime_factors(x, spf)
        share = 0
        m = len(factors)
        for mask in range(1, 1 << m):
            prod = 1
            bits = 0
            for i, p in enumerate(factors):
                if (mask >> i) & 1:
                    prod *= p
                    bits += 1
            share += seen[prod] if bits % 2 else -seen[prod]
        answer += idx - share
        for mask in range(1, 1 << m):
            prod = 1
            for i, p in enumerate(factors):
                if (mask >> i) & 1:
                    prod *= p
            seen[prod] += 1
    print(answer)


if __name__ == "__main__":
    main()
