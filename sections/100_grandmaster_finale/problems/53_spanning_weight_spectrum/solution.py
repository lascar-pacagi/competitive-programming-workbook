import sys

MOD = 998244353


def determinant(a):
    n = len(a)
    det = 1
    for c in range(n):
        pivot = -1
        for r in range(c, n):
            if a[r][c]:
                pivot = r
                break
        if pivot < 0:
            return 0
        if pivot != c:
            a[pivot], a[c] = a[c], a[pivot]
            det = -det
        row = a[c]
        det = det * row[c] % MOD
        inv = pow(row[c], MOD - 2, MOD)
        tail = row[c:]
        for r in range(c + 1, n):
            other = a[r]
            if other[c]:
                f = other[c] * inv % MOD
                other[c:] = [(x - f * y) % MOD for x, y in zip(other[c:], tail)]
    return det % MOD


def main():
    data = sys.stdin.buffer.read().split()
    n, m, K = int(data[0]), int(data[1]), int(data[2])
    edges = []
    for i in range(m):
        u = int(data[3 + 3 * i]) - 1
        v = int(data[4 + 3 * i]) - 1
        w = int(data[5 + 3 * i])
        if u != v:
            edges.append((u, v, w))
    D = (n - 1) * K
    values = []
    size = n - 1
    for x in range(D + 1):
        pw = [1] * (K + 1)
        for i in range(1, K + 1):
            pw[i] = pw[i - 1] * x % MOD
        lap = [[0] * size for _ in range(size)]
        for u, v, w in edges:
            t = pw[w]
            if u < size:
                lap[u][u] += t
            if v < size:
                lap[v][v] += t
            if u < size and v < size:
                lap[u][v] -= t
                lap[v][u] -= t
        lap = [[value % MOD for value in row] for row in lap]
        values.append(determinant(lap))

    # Lagrange interpolation through (i, values[i]), i = 0..D.
    master = [1]
    for i in range(D + 1):
        nxt = [0] * (len(master) + 1)
        for k, c in enumerate(master):
            nxt[k + 1] += c
            nxt[k] -= c * i
        master = [c % MOD for c in nxt]
    fact = [1] * (D + 1)
    for i in range(1, D + 1):
        fact[i] = fact[i - 1] * i % MOD
    coef = [0] * (D + 1)
    for i in range(D + 1):
        if not values[i]:
            continue
        denom = fact[i] * fact[D - i] % MOD
        if (D - i) % 2:
            denom = MOD - denom
        scale = values[i] * pow(denom, MOD - 2, MOD) % MOD
        quotient = [0] * (D + 1)
        carry = 0
        for k in range(D + 1, 0, -1):
            carry = (master[k] + carry * i) % MOD
            quotient[k - 1] = carry
        coef = [(c + scale * t) % MOD for c, t in zip(coef, quotient)]
    sys.stdout.write(" ".join(map(str, coef)) + "\n")


if __name__ == "__main__":
    main()
