import argparse
import random
from pathlib import Path

MOD = 1_000_000_007


def brute(n, w, edges):
    adj = [0] * n
    for u, v in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    best, count = -1, 0
    for mask in range(1 << n):
        if any(mask >> v & 1 and adj[v] & mask for v in range(n)):
            continue
        s = sum(w[v] for v in range(n) if mask >> v & 1)
        if s > best:
            best, count = s, 1
        elif s == best:
            count += 1
    return best, count % MOD


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=25)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for i in range(args.count):
        n = rng.randint(1, 14)
        top = rng.choice([0, 1, 2, 10**9])
        w = [rng.randint(0, top) for _ in range(n)]
        p = rng.random()
        edges = [(u, v) for u in range(n) for v in range(u + 1, n) if rng.random() < p]
        if rng.random() < 0.2 and edges:
            edges.append(edges[0])  # repeated rivalry
        rng.shuffle(edges)
        stem = args.out_dir / f"case{i:03d}"
        stem.with_suffix(".in").write_text(f"{n} {len(edges)}\n{' '.join(map(str, w))}\n" + "".join(f"{u + 1} {v + 1}\n" for u, v in edges))
        stem.with_suffix(".out").write_text("%d %d\n" % brute(n, w, edges))


if __name__ == "__main__":
    main()
