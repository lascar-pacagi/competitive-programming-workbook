"""Small cases checked by an independent exhaustive oracle."""
import argparse
import itertools
import random
from collections import deque
from fractions import Fraction
from pathlib import Path

def expected(text):
    it = iter(map(int, text.split()))
    n, m = next(it), next(it)
    costs = [(next(it), next(it)) for _ in range(n)]
    edges = [(next(it)-1, next(it)-1, next(it)) for _ in range(m)]
    best = min(sum(costs[i][mask >> i & 1] for i in range(n)) +
               sum(p for u,v,p in edges if not (mask >> u & 1) and mask >> v & 1)
               for mask in range(1 << n))
    return str(best) + '\n'

def case(rng):
    n = rng.randint(1, 9)
    costs = [(rng.randint(0, 15), rng.randint(0, 15)) for _ in range(n)]
    edges = [(u+1,v+1,rng.randint(0,20)) for u in range(n) for v in range(n) if u != v and rng.random()<.25]
    return f'{n} {len(edges)}\n' + ''.join(f'{a} {b}\n' for a,b in costs) + ''.join(f'{u} {v} {c}\n' for u,v,c in edges)

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
