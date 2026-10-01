"""Connected bipartite labelled graphs: log of the 2-coloured-graph EGF."""
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
    N = int(sys.stdin.read().split()[0])
    zeta = pow(3, (MOD - 1) // 8, MOD)  # primitive 8th root of unity
    s = (zeta + pow(zeta, MOD - 2, MOD)) % MOD  # s^2 = 2
    s_inv = pow(s, MOD - 2, MOD)
    fact = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact = [1] * (N + 1)
    inv_fact[N] = pow(fact[N], MOD - 2, MOD)
    for i in range(N, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD
    # 2^{k(n-k)} = s^{n^2} s^{-k^2} s^{-(n-k)^2}
    a = [pow(s_inv, k * k % (MOD - 1), MOD) * inv_fact[k] % MOD for k in range(N + 1)]
    B = multiply(a, a, N + 1)
    B = [B[n] * pow(s, n * n % (MOD - 1), MOD) % MOD for n in range(N + 1)]
    C = log(B, N + 1)
    half = (MOD + 1) // 2
    print(" ".join(str(C[n] * fact[n] % MOD * half % MOD) for n in range(1, N + 1)))


if __name__ == "__main__":
    main()
