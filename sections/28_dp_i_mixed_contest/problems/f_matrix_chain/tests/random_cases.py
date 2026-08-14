import argparse,random
from functools import lru_cache
from pathlib import Path
def main():
    p=argparse.ArgumentParser();p.add_argument("--count",type=int,required=True);p.add_argument("--seed",type=int,required=True);p.add_argument("--out-dir",type=Path,required=True);a=p.parse_args()
    a.out_dir.mkdir(parents=True,exist_ok=True);rng=random.Random(a.seed)
    for z in range(a.count):
        n=rng.randint(1,9);d=[rng.randint(1,20) for _ in range(n+1)]
        @lru_cache(None)
        def f(l,r):
            if l==r:return 0
            return min(f(l,k)+f(k+1,r)+d[l]*d[k+1]*d[r+1] for k in range(l,r))
        stem=a.out_dir/f"case{z:03d}";stem.with_suffix(".in").write_text(f"{n}\n"+" ".join(map(str,d))+"\n");stem.with_suffix(".out").write_text(f"{f(0,n-1)}\n")
if __name__=="__main__":main()
