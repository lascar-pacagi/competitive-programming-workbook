"""Small cases checked by an independent exhaustive oracle."""
import argparse
import itertools
import random
from collections import deque
from fractions import Fraction
from pathlib import Path

def expected(text):
    it = iter(map(int, text.split()))
    n, m, k, q = next(it), next(it), next(it), next(it)
    costs = [next(it) for _ in range(n)]
    starts = [next(it) - 1 for _ in range(k)]
    targets = {next(it) - 1 for _ in range(q)}
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = next(it) - 1, next(it) - 1
        adj[u].append(v)
    candidates = [v for v in range(n) if costs[v] >= 0 and v not in starts and v not in targets]
    best = None
    for mask in range(1 << len(candidates)):
        closed = {v for i, v in enumerate(candidates) if mask >> i & 1}
        seen = set(starts)
        queue = list(starts)
        for u in queue:
            for v in adj[u]:
                if v not in closed and v not in seen:
                    seen.add(v); queue.append(v)
        if seen.isdisjoint(targets):
            value = sum(costs[v] for v in closed)
            best = value if best is None else min(best, value)
    return str(-1 if best is None else best) + '\n'

def case(rng):
    n = rng.randint(2, 8)
    order = list(range(n)); rng.shuffle(order)
    k = rng.randint(1, min(2, n - 1))
    q = rng.randint(1, min(2, n - k))
    starts, targets = order[:k], order[k:k+q]
    edges = [(u, v) for u in range(n) for v in range(n) if u != v and rng.random() < .22]
    costs = [rng.choice([-1, 0, 1, 3, 8]) for _ in range(n)]
    return f'{n} {len(edges)} {k} {q}\n' + ' '.join(map(str, costs)) + '\n' + ' '.join(str(v+1) for v in starts) + '\n' + ' '.join(str(v+1) for v in targets) + '\n' + ''.join(f'{u+1} {v+1}\n' for u,v in edges)

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
