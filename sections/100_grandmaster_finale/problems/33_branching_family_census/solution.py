"""Weighted plane trees: Newton iteration on T = x * phi(T)."""
import sys

MOD = 998244353
_CTX = None


def _decimal_context():
    global _CTX
    if _CTX is None:
        import decimal
        _CTX = decimal.Context(prec=decimal.MAX_PREC, Emax=decimal.MAX_EMAX, Emin=decimal.MIN_EMIN)
    return _CTX


def multiply(a, b, limit=None):
    """Product of coefficient lists modulo MOD, truncated to `limit` terms.

    Large products pack coefficients into decimal digits and let libmpdec's
    number-theoretic-transform multiplication do the work."""
    if not a or not b:
        return []
    if limit is not None:
        a = a[:limit]
        b = b[:limit]
    length = len(a) + len(b) - 1
    if min(len(a), len(b)) <= 40:
        out = [0] * length
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    out[i + j] += x * y
        out = [v % MOD for v in out]
    else:
        import decimal
        ctx = _decimal_context()
        A = decimal.Decimal("".join(format(x, "024d") for x in reversed(a)))
        B = decimal.Decimal("".join(format(x, "024d") for x in reversed(b)))
        text = str(ctx.multiply(A, B)).rjust(length * 24, "0")
        top = len(text)
        out = [int(text[top - (i + 1) * 24: top - i * 24]) % MOD for i in range(length)]
    return out[:limit] if limit is not None else out


def inverse(a, n):
    """First n coefficients of 1/a (a[0] != 0)."""
    g = [pow(a[0], MOD - 2, MOD)]
    m = 1
    while m < n:
        m *= 2
        t = multiply(a[:m], g, m)
        t = [(-x) % MOD for x in t]
        t[0] = (t[0] + 2) % MOD
        g = multiply(g, t, m)
    return g[:n]


def log(a, n):
    """First n coefficients of log(a) with a[0] = 1."""
    if n == 1:
        return [0]
    da = [a[i] * i % MOD for i in range(1, min(len(a), n))]
    q = multiply(da, inverse(a, n), n - 1)
    q += [0] * (n - 1 - len(q))
    inv = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        inv[i] = (MOD - (MOD // i) * inv[MOD % i] % MOD) % MOD
    return [0] + [q[i - 1] * inv[i] % MOD for i in range(1, n)]


def exp(a, n):
    """First n coefficients of exp(a) with a[0] = 0."""
    g = [1]
    m = 1
    while m < n:
        m *= 2
        lg = log(g + [0] * (m - len(g)), m)
        t = [((a[i] if i < len(a) else 0) - lg[i]) % MOD for i in range(m)]
        t[0] = (t[0] + 1) % MOD
        g = multiply(g, t, m)
    return g[:n]


def main():
    data = list(map(int, sys.stdin.read().split()))
    N, D = data[0], data[1]
    c = [x % MOD for x in data[2:3 + D]]
    dc = [s * c[s] % MOD for s in range(1, D + 1)]  # coefficients of phi'

    def horner(coef, T, m):
        acc = [coef[-1]]
        for s in range(len(coef) - 2, -1, -1):
            acc = multiply(acc, T, m) if len(acc) > 1 or acc[0] else [0]
            acc += [0] * (1 - len(acc))
            acc[0] = (acc[0] + coef[s]) % MOD
        return acc + [0] * (m - len(acc))

    total = N + 1
    T = [0, c[0]]
    m = 2
    while m < total:
        m = min(2 * m, total)
        T = T + [0] * (m - len(T))
        P = horner(c, T, m)
        Q = horner(dc, T, m) if dc else [0] * m
        F = [(T[i] - (P[i - 1] if i else 0)) % MOD for i in range(m)]
        Fp = [((1 if i == 0 else 0) - (Q[i - 1] if i else 0)) % MOD for i in range(m)]
        step = multiply(F, inverse(Fp, m), m)
        step += [0] * (m - len(step))
        T = [(T[i] - step[i]) % MOD for i in range(m)]
    T += [0] * (total - len(T))
    print(" ".join(str(T[n]) for n in range(1, N + 1)))


if __name__ == "__main__":
    main()
