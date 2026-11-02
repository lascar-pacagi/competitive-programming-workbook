"""Small cases checked by an independent exhaustive oracle."""
import argparse
import itertools
import random
from collections import deque
from fractions import Fraction
from pathlib import Path

def expected(text):
    it = iter(map(int, text.split()))
    n, g = next(it), next(it)
    values = [next(it) for _ in range(n)]
    groups = []
    for _ in range(g):
        kind, bonus, size = next(it), next(it), next(it)
        members = [next(it)-1 for _ in range(size)]
        groups.append((kind,bonus,members))
    best = None
    for mask in range(1<<n):
        value = sum(w for i,w in enumerate(values) if mask>>i&1)
        for kind,bonus,members in groups:
            if all((mask>>i&1)==kind for i in members):value += bonus
        best = value if best is None else max(best,value)
    return str(best)+'\n'

def case(rng):
    n, g = rng.randint(1,8), rng.randint(0,8)
    text = f'{n} {g}\n'+' '.join(str(rng.randint(-9,9)) for _ in range(n))+'\n'
    for _ in range(g):
        members = rng.sample(range(1,n+1),rng.randint(1,n))
        text += f'{rng.randrange(2)} {rng.randint(0,20)} {len(members)} '+' '.join(map(str,members))+'\n'
    return text

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
