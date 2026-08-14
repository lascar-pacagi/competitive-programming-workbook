import argparse,random
from pathlib import Path
def main():
    p=argparse.ArgumentParser();p.add_argument("--count",type=int,required=True);p.add_argument("--seed",type=int,required=True);p.add_argument("--out-dir",type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);rng=random.Random(a.seed)
    for z in range(a.count):
        n=rng.randint(1,60);x=[rng.randint(-30,30)for _ in range(n)];m=[rng.randint(-20,20)for _ in range(n)];fee=[rng.randint(-20,20)for _ in range(n)];dp=[0]*n
        for i in range(1,n):dp[i]=fee[i]+min(dp[j]+m[j]*x[i]for j in range(i))
        lines=[str(n)," ".join(map(str,x))," ".join(map(str,m))," ".join(map(str,fee))];stem=a.out_dir/f"case{z:03d}";stem.with_suffix(".in").write_text("\n".join(lines)+"\n");stem.with_suffix(".out").write_text(f"{dp[-1]}\n")
if __name__=="__main__":main()
