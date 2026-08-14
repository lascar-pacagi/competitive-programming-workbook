import argparse,random
from pathlib import Path
def main():
    p=argparse.ArgumentParser();p.add_argument("--count",type=int,required=True);p.add_argument("--seed",type=int,required=True);p.add_argument("--out-dir",type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);rng=random.Random(a.seed)
    for z in range(a.count):
        n=rng.randint(1,25);k=rng.randint(1,n);arr=[rng.randint(0,8)for _ in range(n)];ps=[0]
        for x in arr:ps.append(ps[-1]+x)
        cost=[[0]*n for _ in range(n)]
        for l in range(n):
            for r in range(l,n):cost[l][r]=(ps[r+1]-ps[l])**2
        inf=10**30;dp=[[inf]*(n+1)for _ in range(k+1)];dp[0][0]=0
        for g in range(1,k+1):
            for i in range(g,n+1):dp[g][i]=min(dp[g-1][j]+cost[j][i-1]for j in range(g-1,i))
        lines=[f"{n} {k}"]+[" ".join(map(str,row))for row in cost];stem=a.out_dir/f"case{z:03d}";stem.with_suffix(".in").write_text("\n".join(lines)+"\n");stem.with_suffix(".out").write_text(f"{dp[k][n]}\n")
if __name__=="__main__":main()
