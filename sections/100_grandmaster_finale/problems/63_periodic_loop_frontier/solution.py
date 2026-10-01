import sys

MOD = 998244353
SLOT = 20  # hex digits per packed coefficient in Kronecker multiplication


def pack(a):
    return int("".join(format(x, "020x") for x in reversed(a)), 16) if a else 0


def multiply(a, b):
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


def nth_term(seq, index):
    """seq satisfies a linear recurrence; return its term at `index`."""
    if index < len(seq):
        return seq[index]
    Q = berlekamp_massey(seq)
    L = len(Q) - 1
    if L == 0:
        return 0
    P = multiply(seq[:L], Q)[:L]
    while index:
        Qm = [x if i % 2 == 0 else (MOD - x) % MOD for i, x in enumerate(Q)]
        U = multiply(P, Qm)
        V = multiply(Q, Qm)
        P = U[index & 1::2]
        Q = V[0::2]
        index >>= 1
        if not P:
            return 0
    return P[0] * pow(Q[0], MOD - 2, MOD) % MOD


def cycle_counts(W):
    """Yield (a_N, number of distinct row-boundary profiles so far) for N=1,2,..

    A profile stores W+1 plugs in 2-bit fields (0 none, 1 '(' , 2 ')').
    Field j is the left plug of cell j and field j+1 its upper plug.
    """
    top_shift = 2 * W
    full = (1 << (2 * (W + 1))) - 1

    def partner(st, k):
        if (st >> (2 * k)) & 3 == 1:
            depth = 0
            t = k
            while True:
                v = (st >> (2 * t)) & 3
                if v == 1:
                    depth += 1
                elif v == 2:
                    depth -= 1
                    if depth == 0:
                        return t
                t += 1
        depth = 0
        t = k
        while True:
            v = (st >> (2 * t)) & 3
            if v == 2:
                depth += 1
            elif v == 1:
                depth -= 1
                if depth == 0:
                    return t
            t -= 1

    cur = {0: 1}
    seen = {0}
    while True:
        nxt = {}
        for st, c in cur.items():
            if st >> top_shift:
                continue
            ns = (st << 2) & full
            nxt[ns] = (nxt.get(ns, 0) + c) % MOD
        cur = nxt
        closed = 0
        for j in range(W):
            sj = 2 * j
            sk = sj + 2
            clear = ~(15 << sj)
            last = j + 1 == W
            nxt = {}
            get = nxt.get
            for st, c in cur.items():
                L = (st >> sj) & 3
                U = (st >> sk) & 3
                base = st & clear
                if not L and not U:
                    if not last:
                        key = base | (1 << sj) | (2 << sk)
                        nxt[key] = (get(key, 0) + c) % MOD
                elif not L or not U:
                    x = L | U
                    key = base | (x << sj)
                    nxt[key] = (get(key, 0) + c) % MOD
                    if not last:
                        key = base | (x << sk)
                        nxt[key] = (get(key, 0) + c) % MOD
                elif L == 1 and U == 1:
                    p = partner(st, j + 1)
                    key = (base & ~(3 << (2 * p))) | (1 << (2 * p))
                    nxt[key] = (get(key, 0) + c) % MOD
                elif L == 2 and U == 2:
                    p = partner(st, j)
                    key = (base & ~(3 << (2 * p))) | (2 << (2 * p))
                    nxt[key] = (get(key, 0) + c) % MOD
                elif L == 2:
                    nxt[base] = (get(base, 0) + c) % MOD
                elif last and base == 0:
                    closed = (closed + c) % MOD  # the single cycle closes here
            cur = nxt
        seen.update(cur.keys())
        yield closed, len(seen)


def main():
    W, N = map(int, sys.stdin.read().split())
    seq = []
    for value, profiles in cycle_counts(W):
        seq.append(value)
        if len(seq) > N or len(seq) >= 2 * profiles + 8:
            break
    print(nth_term(seq, N - 1))


if __name__ == "__main__":
    main()
