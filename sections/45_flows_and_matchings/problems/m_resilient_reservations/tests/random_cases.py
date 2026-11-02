"""Small cases checked by an independent exhaustive oracle."""
import argparse
import itertools
import random
from collections import deque
from fractions import Fraction
from pathlib import Path

def expected(text):
    it=iter(map(int,text.split()))
    n,m,e=next(it),next(it),next(it)
    adj=[[] for _ in range(n)]
    for _ in range(e):adj[next(it)-1].append(next(it)-1)
    def feasible(cancelled):
        def assign(u,used):
            if u==n:return True
            return any(not ((used|cancelled)>>v&1) and assign(u+1,used|(1<<v)) for v in adj[u])
        return assign(0,0)
    first_bad=m+1
    for mask in range(1<<m):
        if mask.bit_count()<first_bad and not feasible(mask):first_bad=mask.bit_count()
    return str(first_bad-1)+'\n'

def case(rng):
    n,m=rng.randint(1,4),rng.randint(1,6)
    es=[(u+1,v+1) for u in range(n) for v in range(m) if rng.random()<.6]
    rng.shuffle(es)
    return f'{n} {m} {len(es)}\n'+''.join(f'{u} {v}\n' for u,v in es)

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
