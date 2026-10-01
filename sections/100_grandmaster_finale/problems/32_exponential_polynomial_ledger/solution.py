import sys

MOD = 998244353


def main():
    n, r, d = map(int, sys.stdin.read().split())
    r %= MOD
    if n == 0:
        print(0)
        return
    if r == 0:
        print(1 if d == 0 else 0)  # only the term i = 0 survives, and 0^0 = 1
        return
    m = d + 2  # sample points 0..d+1
    # i^d for i = 0..m via a linear sieve (powers only at primes).
    pw = [0] * (m + 1)
    pw[0] = 1 if d == 0 else 0
    if m >= 1:
        pw[1] = 1
    primes = []
    composite = bytearray(m + 1)
    for i in range(2, m + 1):
        if not composite[i]:
            primes.append(i)
            pw[i] = pow(i, d, MOD)
        for p in primes:
            if i * p > m:
                break
            composite[i * p] = 1
            pw[i * p] = pw[i] * pw[p] % MOD
            if i % p == 0:
                break
    # Prefix sums S(k) = sum_{i<k} r^i i^d for k = 0..m.
    S = [0] * (m + 1)
    rp = 1
    for i in range(m):
        S[i + 1] = (S[i] + rp * pw[i]) % MOD
        rp = rp * r % MOD
    fact = [1] * (m + 2)
    for i in range(1, m + 2):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact = [1] * (m + 2)
    inv_fact[m + 1] = pow(fact[m + 1], MOD - 2, MOD)
    for i in range(m + 1, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD

    def interpolate(values, x):
        """Value at x of the polynomial through (i, values[i]), i = 0..k-1."""
        k = len(values)
        x %= MOD
        pre = [1] * (k + 1)
        for i in range(k):
            pre[i + 1] = pre[i] * (x - i) % MOD
        suf = [1] * (k + 1)
        for i in range(k - 1, -1, -1):
            suf[i] = suf[i + 1] * (x - i) % MOD
        total = 0
        for i in range(k):
            term = values[i] * pre[i] % MOD * suf[i + 1] % MOD * inv_fact[i] % MOD * inv_fact[k - 1 - i] % MOD
            total += -term if (k - 1 - i) & 1 else term
        return total % MOD

    if r == 1:
        # sum_{i<n} i^d is a polynomial of degree d + 1 in n.
        print(interpolate(S[:d + 2], n))
        return
    # S(k) = r^k G(k) + c with deg G <= d.  The (d+1)-th finite difference of
    # G vanishes, which pins down c; then interpolate G at n.
    r_inv = pow(r, MOD - 2, MOD)
    t = [0] * (d + 2)
    rk = 1
    for i in range(d + 2):
        t[i] = S[i] * rk % MOD
        rk = rk * r_inv % MOD
    num = 0
    for i in range(d + 2):
        w = fact[d + 1] * inv_fact[i] % MOD * inv_fact[d + 1 - i] % MOD
        num += -w * t[i] if (d + 1 - i) & 1 else w * t[i]
    c = num % MOD * pow(pow((r_inv - 1) % MOD, d + 1, MOD), MOD - 2, MOD) % MOD
    G = []
    rk = 1
    for i in range(d + 1):
        G.append((t[i] - c * rk) % MOD)
        rk = rk * r_inv % MOD
    print((pow(r, n % (MOD - 1), MOD) * interpolate(G, n) + c) % MOD)


if __name__ == "__main__":
    main()
