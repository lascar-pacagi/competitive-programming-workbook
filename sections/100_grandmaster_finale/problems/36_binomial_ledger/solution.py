import sys


def factorize(m):
    out = []
    p = 2
    while p * p <= m:
        if m % p == 0:
            e = 0
            while m % p == 0:
                m //= p
                e += 1
            out.append((p, e))
        p += 1
    if m > 1:
        out.append((m, 1))
    return out


class PrimePower:
    """C(n, k) mod p^e by removing every factor p from the factorials."""

    def __init__(self, p, e):
        self.p = p
        self.e = e
        self.pe = p ** e
        pe = self.pe
        pre = [1] * (pe + 1)
        for i in range(1, pe + 1):
            pre[i] = pre[i - 1] * i % pe if i % p else pre[i - 1]
        self.pre = pre
        self.full = pre[pe]  # +-1 by Wilson's theorem for prime powers

    def unit_factorial(self, x):
        """x! with all factors p removed, modulo p^e."""
        pe, p, pre, full = self.pe, self.p, self.pre, self.full
        result = 1
        while x:
            q, r = divmod(x, pe)
            if full != 1 and q & 1:
                result = result * full % pe
            result = result * pre[r] % pe
            x //= p
        return result

    def legendre(self, x):
        p = self.p
        v = 0
        while x:
            x //= p
            v += x
        return v

    def binom(self, n, k):
        v = self.legendre(n) - self.legendre(k) - self.legendre(n - k)
        if v >= self.e:
            return 0
        pe = self.pe
        top = self.unit_factorial(n)
        bottom = self.unit_factorial(k) * self.unit_factorial(n - k) % pe
        return top * pow(bottom, -1, pe) % pe * self.p ** v % pe


def main():
    data = sys.stdin.buffer.read().split()
    m, q = int(data[0]), int(data[1])
    parts = [PrimePower(p, e) for p, e in factorize(m)]
    # CRT coefficients: x = sum r_i * M_i * (M_i^{-1} mod m_i)
    coef = []
    for part in parts:
        Mi = m // part.pe
        coef.append(Mi * pow(Mi % part.pe, -1, part.pe) % m if part.pe > 1 else 0)
    out = []
    for i in range(q):
        n = int(data[2 + 2 * i])
        k = int(data[3 + 2 * i])
        if k > n or m == 1:
            out.append(0)
            continue
        total = 0
        for part, cf in zip(parts, coef):
            total += part.binom(n, k) * cf
        out.append(total % m)
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
