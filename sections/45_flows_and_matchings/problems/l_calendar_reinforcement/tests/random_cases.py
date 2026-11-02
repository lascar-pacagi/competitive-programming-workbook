"""Small cases checked by an independent exhaustive oracle."""
import argparse
import itertools
import random
from collections import deque
from fractions import Fraction
from pathlib import Path

def expected(text):
    it = iter(map(int,text.split()))
    n,p=next(it),next(it)
    cal=[(next(it),next(it),next(it)) for _ in range(p)]
    jobs=[(next(it),next(it),next(it)) for _ in range(n)]
    if any(work>r-l for l,r,work in jobs):return '-1\n'
    base=[0]*cal[-1][1]
    for l,r,c in cal:
        for day in range(l,r):base[day]=c
    options=[list(itertools.combinations(range(l,r),work)) for l,r,work in jobs]
    for extra in range(n+1):
        load=[0]*len(base)
        def assign(i):
            if i==n:return True
            for days in options[i]:
                if all(load[d]<base[d]+extra for d in days):
                    for d in days:load[d]+=1
                    if assign(i+1):return True
                    for d in days:load[d]-=1
            return False
        if assign(0):return str(extra)+'\n'
    raise AssertionError('n extra workers must suffice')

def case(rng):
    n,t=rng.randint(1,4),rng.randint(1,5)
    points=[0]+[x for x in range(1,t) if rng.random()<.6]+[t]
    text=f'{n} {len(points)-1}\n'
    for l,r in zip(points,points[1:]):text+=f'{l} {r} {rng.randint(0,2)}\n'
    for _ in range(n):
        l=rng.randrange(t);r=rng.randint(l+1,t)
        text+=f'{l} {r} {rng.randint(1,r-l+1)}\n'
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
