import sys

MOD = 1_000_000_007


def main():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    rows = [data[2 + i].decode() for i in range(n)]
    grid = [[ch == "1" for ch in row] for row in rows]
    if m > n:  # keep the shorter side as the free variables
        grid = [list(col) for col in zip(*grid)]
        n, m = m, n
    # Every press is an affine function of the first-row presses: an integer
    # whose bits 0..m-1 are coefficients and bit m is the constant.
    const = 1 << m
    prev = [0] * m
    cur = [1 << c for c in range(m)]
    for r in range(n - 1):
        lamp = grid[r]
        nxt = [0] * m
        for c in range(m):
            # lamp (r, c) must end off; only press (r+1, c) can still change it
            v = prev[c] ^ cur[c]
            if c:
                v ^= cur[c - 1]
            if c + 1 < m:
                v ^= cur[c + 1]
            if lamp[c]:
                v ^= const
            nxt[c] = v
        prev, cur = cur, nxt
    # The last row of lamps gives m equations in the m first-row variables.
    eqs = []
    lamp = grid[n - 1]
    for c in range(m):
        v = prev[c] ^ cur[c]
        if c:
            v ^= cur[c - 1]
        if c + 1 < m:
            v ^= cur[c + 1]
        if lamp[c]:
            v ^= const
        eqs.append(v)
    # Gaussian elimination over GF(2).
    rank = 0
    for bit in range(m):
        mask = 1 << bit
        pivot = next((i for i in range(rank, m) if eqs[i] & mask), -1)
        if pivot < 0:
            continue
        eqs[rank], eqs[pivot] = eqs[pivot], eqs[rank]
        pv = eqs[rank]
        for i in range(m):
            if i != rank and eqs[i] & mask:
                eqs[i] ^= pv
        rank += 1
    if any(e == const for e in eqs[rank:]):
        print(0)
    else:
        print(pow(2, m - rank, MOD))


if __name__ == "__main__":
    main()
