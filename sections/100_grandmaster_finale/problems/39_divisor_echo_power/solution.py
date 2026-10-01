import sys

MOD = 998244353


def main():
    data = sys.stdin.buffer.read().split()
    N, k = int(data[0]), int(data[1]) % MOD
    f = [0] + [int(x) % MOD for x in data[2:2 + N]]
    # Omega(n): number of prime factors counted with multiplicity.
    omega = [0] * (N + 1)
    for p in range(2, N + 1):
        if omega[p] == 0:
            pk = p
            while pk <= N:
                for m in range(pk, N + 1, pk):
                    omega[m] += 1
                pk *= p
    inv = [0, 1] + [0] * 64
    for i in range(2, 66):
        inv[i] = pow(i, MOD - 2, MOD)
    # D(h)(n) = Omega(n) h(n) is a derivation of Dirichlet convolution, so
    # g = f^k satisfies f * D(g) = k g * D(f).  Reading this at n isolates
    # Omega(n) g(n) in terms of g(d), d | n, d < n.
    weight = [k * omega[m] % MOD * f[m] % MOD for m in range(N + 1)]  # k Omega(m) f(m)
    acc = [0] * (N + 1)
    g = [0] * (N + 1)
    g[1] = 1
    for d in range(1, N + 1):
        if d > 1:
            g[d] = acc[d] % MOD * inv[omega[d]] % MOD
        gd = g[d]
        if not gd or 2 * d > N:
            continue
        od = omega[d]
        top = N // d
        # contribution to n = d*m for m = 2..top: g(d) f(m) (k Omega(m) - Omega(d));
        # sums stay exact (Python integers) and are reduced when g(n) is read.
        acc[2 * d::d] = [x + gd * (w - od * fm) for x, w, fm in zip(acc[2 * d::d], weight[2:top + 1], f[2:top + 1])]
    sys.stdout.write(" ".join(map(str, g[1:])) + "\n")


if __name__ == "__main__":
    main()
