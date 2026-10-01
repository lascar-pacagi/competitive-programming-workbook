import math
import random
import sys

_rng = random.Random(20261001)


def is_prime(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def rho(n):
    if n % 2 == 0:
        return 2
    while True:
        c = _rng.randrange(1, n)
        y = _rng.randrange(n)
        g = 1
        q = 1
        r = 1
        x = y
        ys = y
        while g == 1:
            x = y
            for _ in range(r):
                y = (y * y + c) % n
            k = 0
            while k < r and g == 1:
                ys = y
                for _ in range(min(128, r - k)):
                    y = (y * y + c) % n
                    q = q * abs(x - y) % n
                g = math.gcd(q, n)
                k += 128
            r *= 2
        if g == n:
            g = 1
            while g == 1:
                ys = (ys * ys + c) % n
                g = math.gcd(abs(x - ys), n)
        if g != n:
            return g


def factor(n, out):
    if n == 1:
        return
    if is_prime(n):
        out[n] = out.get(n, 0) + 1
        return
    for p in (2, 3, 5, 7, 11, 13):
        if n % p == 0:
            out[p] = out.get(p, 0) + 1
            factor(n // p, out)
            return
    d = rho(n)
    factor(d, out)
    factor(n // d, out)


def fib_matrix_power(e, mod):
    """[[1,1],[1,0]]^e modulo mod, as (a, b, c, d)."""
    ra, rb, rc, rd = 1, 0, 0, 1
    a, b, c, d = 1, 1, 1, 0
    while e:
        if e & 1:
            ra, rb, rc, rd = (ra * a + rb * c) % mod, (ra * b + rb * d) % mod, (rc * a + rd * c) % mod, (rc * b + rd * d) % mod
        a, b, c, d = (a * a + b * c) % mod, (a * b + b * d) % mod, (c * a + d * c) % mod, (c * b + d * d) % mod
        e >>= 1
    return ra, rb, rc, rd


def period_prime_power(p, e):
    """Order of the Fibonacci matrix modulo p^e.

    p^(e-1) * L is a multiple of it, with L = p - 1, 2(p + 1), or 20 for p = 5
    by the Frobenius action on the roots of x^2 - x - 1; strip prime factors
    while the matrix power is still the identity."""
    mod = p ** e
    if p == 5:
        base = 20
    elif p % 5 in (1, 4):
        base = p - 1
    else:
        base = 2 * (p + 1)
    fac = {}
    factor(base, fac)
    if e > 1:
        fac[p] = fac.get(p, 0) + e - 1
    L = base * p ** (e - 1)
    for r in fac:
        while L % r == 0 and fib_matrix_power(L // r, mod) == (1, 0, 0, 1):
            L //= r
    return L


def main():
    data = sys.stdin.read().split()
    q = int(data[0])
    out = []
    for i in range(q):
        m = int(data[1 + i])
        fac = {}
        factor(m, fac)
        answer = 1
        for p, e in fac.items():
            L = period_prime_power(p, e)
            answer = answer // math.gcd(answer, L) * L
        out.append(answer)
    print("\n".join(map(str, out)))


if __name__ == "__main__":
    main()
