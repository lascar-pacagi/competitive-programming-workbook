import argparse
import random
from pathlib import Path

MOD = 998244353


def brute_cycles(W, N):
    """Count Hamiltonian cycles of the W x N grid by direct search."""
    cells = W * N
    if cells < 4 or W < 2 or N < 2:
        return 0

    def neighbours(v):
        r, c = divmod(v, W)
        if r > 0:
            yield v - W
        if r + 1 < N:
            yield v + W
        if c > 0:
            yield v - 1
        if c + 1 < W:
            yield v + 1

    adj = [list(neighbours(v)) for v in range(cells)]
    seen = [False] * cells
    seen[0] = True
    count = 0

    def dfs(v, depth):
        nonlocal count
        if depth == cells:
            if 0 in adj[v]:
                count += 1
            return
        for w in adj[v]:
            if not seen[w]:
                seen[w] = True
                dfs(w, depth + 1)
                seen[w] = False

    dfs(0, 1)
    return count // 2  # each cycle is found in both directions


def partner(st, k):
    step = 1 if st[k] == 1 else -1
    depth = 0
    t = k
    while True:
        if st[t] == 1:
            depth += step
        elif st[t] == 2:
            depth -= step
        if depth == 0:
            return t
        t += step


def row_transfer(W, start):
    """Process one full row from boundary profile `start` (tuple of W+1 plugs).
    Returns (dict of next boundary profiles -> count, closed-cycle count)."""
    if start[W]:
        return {}, 0
    cur = {(0,) + start[:W]: 1}
    closed = 0
    for j in range(W):
        nxt = {}
        for st, c in cur.items():
            L, U = st[j], st[j + 1]
            s = list(st)
            s[j] = s[j + 1] = 0
            outs = []
            if not L and not U:
                if j + 1 < W:
                    s2 = s[:]
                    s2[j], s2[j + 1] = 1, 2
                    outs.append(s2)
            elif not L or not U:
                x = L or U
                s2 = s[:]
                s2[j] = x
                outs.append(s2)
                if j + 1 < W:
                    s2 = s[:]
                    s2[j + 1] = x
                    outs.append(s2)
            elif L == 1 and U == 1:
                s[partner(st, j + 1)] = 1
                outs.append(s)
            elif L == 2 and U == 2:
                s[partner(st, j)] = 2
                outs.append(s)
            elif L == 2:
                outs.append(s)
            elif j + 1 == W and not any(s):
                closed += c
            for s2 in outs:
                key = tuple(s2)
                nxt[key] = nxt.get(key, 0) + c
        cur = nxt
    return cur, closed


def matrix_cycles(W, N):
    """Independent transfer-matrix power: a_N = close^T T^(N-1) start."""
    zero = tuple([0] * (W + 1))
    index = {zero: 0}
    order = [zero]
    rows = []
    closes = []
    i = 0
    while i < len(order):
        nxt, closed = row_transfer(W, order[i])
        for key in nxt:
            if key not in index:
                index[key] = len(order)
                order.append(key)
        rows.append({index[k]: v % MOD for k, v in nxt.items()})
        closes.append(closed % MOD)
        i += 1
    S = len(order)
    T = [[0] * S for _ in range(S)]  # T[b][a]: from a to b
    for a, row in enumerate(rows):
        for b, v in row.items():
            T[b][a] = (T[b][a] + v) % MOD

    def mat_mul(X, Y):
        Yt = list(zip(*Y))
        return [[sum(x * y for x, y in zip(r, col)) % MOD for col in Yt] for r in X]

    vec = [1] + [0] * (S - 1)
    e = N - 1
    P = T
    while e:
        if e & 1:
            vec = [sum(P[r][c] * vec[c] for c in range(S)) % MOD for r in range(S)]
        P = mat_mul(P, P)
        e >>= 1
    return sum(c * v for c, v in zip(closes, vec)) % MOD


def make_case(rng):
    if rng.random() < 0.5:
        W = rng.randint(1, 5)
        N = rng.randint(1, max(1, 20 // W))
        answer = brute_cycles(W, N) % MOD
    else:
        W = rng.randint(1, 5)
        N = rng.choice([rng.randint(1, 60), rng.randint(1, 10**18)])
        answer = matrix_cycles(W, N)
    return f"{W} {N}\n", f"{answer}\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=25)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for i in range(args.count):
        case_input, case_output = make_case(rng)
        stem = args.out_dir / f"case{i:03d}"
        stem.with_suffix(".in").write_text(case_input)
        stem.with_suffix(".out").write_text(case_output)


if __name__ == "__main__":
    main()
