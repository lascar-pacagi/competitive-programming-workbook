import argparse, random
from functools import lru_cache
from pathlib import Path
def brute(a):
    n, m = len(a), len(a[0])
    neg = -10**18
    @lru_cache(None)
    def dp(r, c, used):
        if r == n-1 and c == m-1:
            return a[r][c] if used else neg
        best = neg
        if r+1 < n:
            suffix = dp(r+1,c,used)
            if suffix != neg: best = max(best, a[r][c] + suffix)
        if c+1 < m:
            suffix = dp(r,c+1,used)
            if suffix != neg: best = max(best, a[r][c] + suffix)
        if not used and r+1 < n and c+1 < m:
            suffix = dp(r+1,c+1,1)
            if suffix != neg: best = max(best, a[r][c] + suffix)
        return best
    ans = dp(0,0,0)
    return -1 if ans == neg else ans
def main():
    p=argparse.ArgumentParser();p.add_argument("--count",type=int,required=True);p.add_argument("--seed",type=int,required=True);p.add_argument("--out-dir",type=Path,required=True);a=p.parse_args()
    a.out_dir.mkdir(parents=True,exist_ok=True);rng=random.Random(a.seed)
    for z in range(a.count):
        n,m=rng.randint(1,7),rng.randint(1,7)
        g=[[rng.randint(-9,12) for _ in range(m)] for _ in range(n)]
        stem=a.out_dir/f"case{z:03d}"
        stem.with_suffix(".in").write_text(f"{n} {m}\n"+"\n".join(" ".join(map(str,row)) for row in g)+"\n")
        stem.with_suffix(".out").write_text(f"{brute(g)}\n")
if __name__=="__main__":main()
