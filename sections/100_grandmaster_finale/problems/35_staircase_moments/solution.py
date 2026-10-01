import sys

MOD = 998244353
INV2 = (MOD + 1) // 2
INV6 = pow(6, MOD - 2, MOD)


def solve(a, b, c, n):
    """(F, G, H) = sums over x = 0..n of q, x*q, q*q with q = (a x + b) // c.

    Reduce a, b below c, then swap the roles of x and q (the lattice points
    under the line counted by columns instead of rows), like Euclid."""
    # Iterative version of the recursion: record frames, then unwind.
    frames = []
    while True:
        if a == 0:
            q = b // c % MOD
            n1 = (n + 1) % MOD
            base = (n1 * q % MOD, q * (n % MOD) % MOD * n1 % MOD * INV2 % MOD, n1 * q % MOD * q % MOD)
            break
        if a >= c or b >= c:
            frames.append((0, a // c, b // c, n))
            a %= c
            b %= c
            continue
        m = (a * n + b) // c
        if m == 0:
            base = (0, 0, 0)
            break
        frames.append((1, m, None, n))
        a, b, c, n = c, c - b - 1, a, m - 1
    F, G, H = base
    for kind, x, y, n in reversed(frames):
        nm = n % MOD
        s1 = nm * (nm + 1) % MOD * INV2 % MOD
        s2 = nm * (nm + 1) % MOD * (2 * nm + 1) % MOD * INV6 % MOD
        if kind == 0:
            A = x % MOD
            B = y % MOD
            f = (F + A * s1 + B * (nm + 1)) % MOD
            g = (G + A * s2 + B * s1) % MOD
            h = (H + A * A % MOD * s2 + B * B % MOD * (nm + 1) + 2 * A * B % MOD * s1
                 + 2 * B * F + 2 * A * G) % MOD
        else:
            m = x % MOD
            f = (nm * m - F) % MOD
            g = (m * nm % MOD * (nm + 1) - H - F) % MOD * INV2 % MOD
            h = (nm * m % MOD * (m + 1) - 2 * G - 2 * F - f) % MOD
        F, G, H = f, g, h
    return F, G, H


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    out = []
    for i in range(t):
        n, a, b, c = data[1 + 4 * i:5 + 4 * i]
        out.append("%d %d %d" % solve(a, b, c, n))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
