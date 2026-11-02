"""Small cases checked by an independent exhaustive oracle."""
import argparse
import itertools
import random
from collections import deque
from fractions import Fraction
from pathlib import Path

def expected(text):
    it = iter(map(int, text.split()))
    n, m, e = next(it), next(it), next(it)
    adj = [[] for _ in range(n)]
    for _ in range(e):
        u, v, d = next(it) - 1, next(it) - 1, next(it)
        adj[u].append((v, d))
    best = None
    def visit(u, used, limit):
        nonlocal best
        if u == n:
            best = limit if best is None else min(best, limit)
            return
        for v, d in adj[u]:
            if not (used >> v & 1):
                visit(u + 1, used | (1 << v), max(limit, d))
    visit(0, 0, 0)
    return str(-1 if best is None else best) + '\n'

def case(rng):
    n, m = rng.randint(1, 5), rng.randint(1, 5)
    edges = [(u + 1, v + 1, rng.randint(0, 12)) for u in range(n) for v in range(m) if rng.random() < .55]
    rng.shuffle(edges)
    return f'{n} {m} {len(edges)}\n' + ''.join(f'{u} {v} {d}\n' for u, v, d in edges)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--count', type=int, required=True)
    parser.add_argument('--seed', type=int, required=True)
    parser.add_argument('--out-dir', type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for index in range(args.count):
        text = case(rng)
        stem = args.out_dir / f'random{index:03d}'
        stem.with_suffix('.in').write_text(text)
        stem.with_suffix('.out').write_text(expected(text))


if __name__ == '__main__':
    main()
