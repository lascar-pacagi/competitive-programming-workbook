import argparse,itertools,random
from pathlib import Path
def main():
    p=argparse.ArgumentParser();p.add_argument("--count",type=int,required=True);p.add_argument("--seed",type=int,required=True);p.add_argument("--out-dir",type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);rng=random.Random(a.seed)
    for z in range(a.count):
        n=rng.randint(1,18);v=[rng.randint(-30,30)for _ in range(n)];total=sum(v);best=min(abs(total-2*sum(v[i]for i in range(n)if mask>>i&1))for mask in range(1<<n));stem=a.out_dir/f"case{z:03d}";stem.with_suffix(".in").write_text(f"{n}\n"+" ".join(map(str,v))+"\n");stem.with_suffix(".out").write_text(f"{best}\n")
if __name__=="__main__":main()
