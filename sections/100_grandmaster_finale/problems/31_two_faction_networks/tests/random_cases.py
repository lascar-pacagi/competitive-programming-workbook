import argparse
import itertools
import random
from pathlib import Path

MOD = 998244353


def brute(n):
    """Connected bipartite labelled graphs on n vertices, by enumeration."""
    pairs = list(itertools.combinations(range(n), 2))
    count = 0
    for mask in range(1 << len(pairs)):
        adj = [[] for _ in range(n)]
        for i, (u, v) in enumerate(pairs):
            if mask >> i & 1:
                adj[u].append(v)
                adj[v].append(u)
        colour = [-1] * n
        colour[0] = 0
        stack = [0]
        ok = True
        seen = 1
        while stack and ok:
            v = stack.pop()
            for w in adj[v]:
                if colour[w] < 0:
                    colour[w] = 1 - colour[v]
                    seen += 1
                    stack.append(w)
                elif colour[w] == colour[v]:
                    ok = False
                    break
        if ok and seen == n:
            count += 1
    return count


def formula(N):
    """Independent O(N^2) recurrence: subtract the disconnected part."""
    from math import comb
    b = [sum(comb(n, k) * 2 ** (k * (n - k)) for k in range(n + 1)) for n in range(N + 1)]
    c = [0] * (N + 1)  # connected 2-coloured graphs
    for n in range(1, N + 1):
        # graphs whose component of vertex 1 has size m
        c[n] = b[n] - sum(comb(n - 1, m - 1) * c[m] * b[n - m] for m in range(1, n))
    return [c[n] // 2 % MOD for n in range(1, N + 1)]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=25)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for i in range(args.count):
        N = rng.randint(1, 60)
        stem = args.out_dir / f"case{i:03d}"
        stem.with_suffix(".in").write_text(f"{N}\n")
        stem.with_suffix(".out").write_text(" ".join(map(str, formula(N))) + "\n")


if __name__ == "__main__":
    main()
