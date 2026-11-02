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
    a = [next(it) for _ in range(n)]
    b = [next(it) for _ in range(m)]
    es = [(next(it) - 1, next(it) - 1, next(it)) for _ in range(e)]
    best = 0
    def visit(k, total):
        nonlocal best
        if k == len(es):
            best = max(best, total)
            return
        u, v, c = es[k]
        for x in range(min(a[u], b[v], c) + 1):
            a[u] -= x; b[v] -= x
            visit(k + 1, total + x)
            a[u] += x; b[v] += x
    visit(0, 0)
    return str(best) + '\n'

def case(rng):
    n, m = rng.randint(1, 3), rng.randint(1, 3)
    pairs = [(u + 1, v + 1) for u in range(n) for v in range(m)]
    rng.shuffle(pairs)
    pairs = pairs[:rng.randint(0, min(6, len(pairs)))]
    a = [rng.randint(0, 3) for _ in range(n)]
    b = [rng.randint(0, 3) for _ in range(m)]
    return f'{n} {m} {len(pairs)}\n' + ' '.join(map(str, a)) + '\n' + ' '.join(map(str, b)) + '\n' + ''.join(f'{u} {v} {rng.randint(0, 2)}\n' for u, v in pairs)

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
