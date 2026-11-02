"""Small cases checked by an independent exhaustive oracle."""
import argparse
import itertools
import random
from collections import deque
from fractions import Fraction
from pathlib import Path

def expected(text):
    it=iter(map(int,text.split()))
    n,m=next(it),next(it)
    costs=[next(it) for _ in range(n)]
    edges=[(next(it)-1,next(it)-1,next(it)) for _ in range(m)]
    best=Fraction(0)
    for mask in range(1,1<<n):
        reward=sum(w for u,v,w in edges if mask>>u&1 and mask>>v&1)
        cost=sum(c for i,c in enumerate(costs) if mask>>i&1)
        best=max(best,Fraction(reward,cost))
    return f'{best.numerator} {best.denominator}\n'

def case(rng):
    n=rng.randint(1,8)
    costs=[rng.randint(1,6) for _ in range(n)]
    edges=[(u+1,v+1,rng.randint(0,30)) for u in range(n) for v in range(u+1,n) if rng.random()<.5]
    return f'{n} {len(edges)}\n'+' '.join(map(str,costs))+'\n'+''.join(f'{u} {v} {w}\n' for u,v,w in edges)

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
