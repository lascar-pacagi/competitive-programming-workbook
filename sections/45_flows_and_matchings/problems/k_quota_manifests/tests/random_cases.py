"""Small cases checked by an independent exhaustive oracle."""
import argparse
import itertools
import random
from collections import deque
from fractions import Fraction
from pathlib import Path

def expected(text):
    it = iter(map(int,text.split()))
    n,m,e,total = next(it),next(it),next(it),next(it)
    rows = [(next(it),next(it)) for _ in range(n)]
    cols = [(next(it),next(it)) for _ in range(m)]
    es = [(next(it)-1,next(it)-1,next(it)) for _ in range(e)]
    for amounts in itertools.product(*(range(c+1) for u,v,c in es)):
        if sum(amounts)!=total:continue
        a,b=[0]*n,[0]*m
        for (u,v,c),x in zip(es,amounts):a[u]+=x;b[v]+=x
        if all(lo<=x<=hi for x,(lo,hi) in zip(a,rows)) and all(lo<=x<=hi for x,(lo,hi) in zip(b,cols)):
            return 'YES\n'
    return 'NO\n'

def case(rng):
    n,m=rng.randint(1,3),rng.randint(1,3)
    pairs=[(u+1,v+1) for u in range(n) for v in range(m)]
    rng.shuffle(pairs);pairs=pairs[:rng.randint(0,min(6,len(pairs)))]
    bounds=[]
    for _ in range(n+m):
        x,y=rng.randint(0,3),rng.randint(0,3)
        bounds.append((min(x,y),max(x,y)))
    return f'{n} {m} {len(pairs)} {rng.randint(0,8)}\n'+''.join(f'{a} {b}\n' for a,b in bounds)+''.join(f'{u} {v} {rng.randint(0,2)}\n' for u,v in pairs)

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
