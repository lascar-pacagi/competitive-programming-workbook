import sys
from math import isqrt

MOD = 1000000007


def main():
    N = int(sys.stdin.read().split()[0])
    sq = isqrt(N)
    sieve = bytearray([1]) * (sq + 1)
    primes = []
    for i in range(2, sq + 1):
        if sieve[i]:
            primes.append(i)
            sieve[i * i::i] = bytearray(len(range(i * i, sq + 1, i)))

    # Lucy DP over the distinct values N // i (kept exact; Python ints are
    # unbounded, and reduction happens at the end).
    vals = []
    i = 1
    while i <= N:
        v = N // i
        vals.append(v)
        i = N // v + 1
    small = [0] * (sq + 2)
    large = [0] * (sq + 2)
    for idx, v in enumerate(vals):
        if v <= sq:
            small[v] = idx
        else:
            large[N // v] = idx
    count = [v - 1 for v in vals]
    total = [v * (v + 1) // 2 - 1 for v in vals]
    for p in primes:
        p2 = p * p
        if p2 > N:
            break
        base = small[p - 1]
        pc = count[base]
        ps = total[base]
        for idx, v in enumerate(vals):
            if v < p2:
                break
            w = v // p
            k = small[w] if w <= sq else large[N // w]
            count[idx] -= count[k] - pc
            total[idx] -= p * (total[k] - ps)
    # Prime part: f(p) = p - 1 for odd p, f(2) = 3.
    prime_f = [((s - c + 2) % MOD if v >= 2 else 0) for v, s, c in zip(vals, total, count)]

    def pf(v):
        if v < 2:
            return 0
        return prime_f[small[v] if v <= sq else large[N // v]]

    sys.setrecursionlimit(10000)
    prime_count = len(primes)

    def S(v, j):
        pj = primes[j - 1] if j else 1
        if v < 2 or pj >= v:
            return 0
        result = pf(v) - pf(pj)
        k = j
        while k < prime_count:
            p = primes[k]
            if p * p > v:
                break
            pe = p
            e = 1
            while pe * p <= v:
                result += (p ^ e) * S(v // pe, k + 1) + (p ^ (e + 1))
                pe *= p
                e += 1
            k += 1
        return result % MOD

    print((S(N, 0) + 1) % MOD)


if __name__ == "__main__":
    main()
