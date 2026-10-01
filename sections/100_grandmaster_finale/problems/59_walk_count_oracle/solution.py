import sys

MOD = 998244353
SLOT = 20  # hex digits per packed coefficient (80 bits > log2(n * MOD^2))


def pack(a):
    return int("".join(format(x, "020x") for x in reversed(a)), 16) if a else 0


def multiply(a, b):
    """Polynomial product modulo MOD by Kronecker substitution."""
    if not a or not b:
        return []
    length = len(a) + len(b) - 1
    text = format(pack(a) * pack(b), "x").rjust(length * SLOT, "0")
    top = len(text)
    return [int(text[top - (i + 1) * SLOT: top - i * SLOT], 16) % MOD for i in range(length)]


def berlekamp_massey(s):
    C = [1]
    B = [1]
    L = 0
    m = 1
    b = 1
    for i in range(len(s)):
        d = 0
        for j in range(L + 1):
            d += C[j] * s[i - j]
        d %= MOD
        if d == 0:
            m += 1
            continue
        T = C[:]
        coef = d * pow(b, MOD - 2, MOD) % MOD
        if len(C) < len(B) + m:
            C.extend([0] * (len(B) + m - len(C)))
        for j, x in enumerate(B):
            C[j + m] = (C[j + m] - coef * x) % MOD
        if 2 * L <= i:
            L = i + 1 - L
            B = T
            b = d
            m = 1
        else:
            m += 1
    return C[:L + 1]


def main():
    data = sys.stdin.buffer.read().split()
    n, m, N, s, t = int(data[0]), int(data[1]), int(data[2]), int(data[3]) - 1, int(data[4]) - 1
    edges = [(int(data[5 + 2 * i]) - 1, int(data[6 + 2 * i]) - 1) for i in range(m)]
    edges.sort()
    terms = 2 * n + 2
    seq = []
    cur = [0] * n
    cur[s] = 1
    for _ in range(terms):
        seq.append(cur[t])
        nxt = [0] * n
        for u, v in edges:
            nxt[v] += cur[u]
        cur = [x % MOD for x in nxt]
    if N < terms:
        print(seq[N])
        return
    Q = berlekamp_massey(seq)
    L = len(Q) - 1
    if L == 0:
        print(0)
        return
    P = multiply(seq[:L], Q)[:L]
    while N:
        Qm = [x if i % 2 == 0 else (MOD - x) % MOD for i, x in enumerate(Q)]
        U = multiply(P, Qm)
        V = multiply(Q, Qm)
        P = U[N & 1::2]
        Q = V[0::2]
        N >>= 1
        if not P:
            print(0)
            return
    print(P[0] * pow(Q[0], MOD - 2, MOD) % MOD)


if __name__ == "__main__":
    main()
