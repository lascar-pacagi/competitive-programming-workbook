import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    p, d = data[0], data[1]
    f = [c % p for c in data[2:3 + d]]
    while f and f[-1] == 0:
        f.pop()
    if not f:
        print(p)  # the zero polynomial vanishes everywhere
        return
    if len(f) == 1:
        print(0)
        return
    # Make f monic.
    lead_inv = pow(f[-1], p - 2, p)
    f = [c * lead_inv % p for c in f]
    m = len(f) - 1
    slot = (2 * p.bit_length() + m.bit_length() + 8 + 3) // 4  # hex digits per coefficient

    def mul(a, b):
        """Polynomial product modulo p by Kronecker substitution."""
        if not a or not b:
            return []
        length = len(a) + len(b) - 1
        fmt = "0%dx" % slot
        A = int("".join(format(x, fmt) for x in reversed(a)), 16)
        B = int("".join(format(x, fmt) for x in reversed(b)), 16)
        text = format(A * B, "x").rjust(length * slot, "0")
        top = len(text)
        return [int(text[top - (i + 1) * slot: top - i * slot], 16) % p for i in range(length)]

    def series_inverse(a, n):
        g = [pow(a[0], p - 2, p)]
        k = 1
        while k < n:
            k *= 2
            t = mul(a[:k], g)[:k]
            t = [(-x) % p for x in t]
            t[0] = (t[0] + 2) % p
            g = mul(g, t)[:k]
        return g[:n]

    rev_f = f[::-1]
    inv_rev = series_inverse(rev_f, max(1, m))

    def reduce(A):
        """A mod f via a reversed-series quotient (Barrett for polynomials)."""
        while A and A[-1] == 0:
            A.pop()
        n = len(A) - 1
        if n < m:
            return A + [0] * (m - len(A))
        qlen = n - m + 1
        q_rev = mul(A[::-1][:qlen], inv_rev[:qlen])[:qlen]
        q_rev += [0] * (qlen - len(q_rev))
        Q = q_rev[::-1]
        prod = mul(Q, f)
        return [(A[i] - prod[i]) % p for i in range(m)]

    # h = x^p mod f by square-and-multiply.
    h = [1] + [0] * (m - 1) if m > 0 else []
    for bit in bin(p)[2:]:
        h = reduce(mul(h, h))
        if bit == "1":
            h = reduce([0] + h)  # multiply by x
    # gcd(f, x^p - x) has exactly the distinct roots of f as its roots.
    g = h[:] + [0] * max(0, 2 - len(h))
    g[1] = (g[1] - 1) % p
    a, b = f[:], g
    while b and b[-1] == 0:
        b.pop()
    while b:
        # a <- a mod b
        inv_lead = pow(b[-1], p - 2, p)
        a = a[:]
        db = len(b) - 1
        for i in range(len(a) - 1, db - 1, -1):
            c = a[i] * inv_lead % p
            if c:
                shift = i - db
                for j in range(db + 1):
                    a[shift + j] = (a[shift + j] - c * b[j]) % p
        a = a[:db]
        while a and a[-1] == 0:
            a.pop()
        a, b = b, a
    print(len(a) - 1)


if __name__ == "__main__":
    main()
