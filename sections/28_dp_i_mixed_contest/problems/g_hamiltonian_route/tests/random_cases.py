import argparse,itertools,random
from pathlib import Path
def main():
    p=argparse.ArgumentParser();p.add_argument("--count",type=int,required=True);p.add_argument("--seed",type=int,required=True);p.add_argument("--out-dir",type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);rng=random.Random(a.seed)
    for z in range(a.count):
        n=rng.randint(2,9);w=[[-1]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i!=j and rng.random()<.65:w[i][j]=rng.randint(0,30)
        best=None
        for middle in itertools.permutations(range(1,n-1)):
            path=(0,)+middle+(n-1,);cost=0
            for x,y in zip(path,path[1:]):
                if w[x][y]<0:break
                cost+=w[x][y]
            else:best=cost if best is None else min(best,cost)
        stem=a.out_dir/f"case{z:03d}";stem.with_suffix(".in").write_text(f"{n}\n"+"\n".join(" ".join(map(str,row)) for row in w)+"\n");stem.with_suffix(".out").write_text(f"{-1 if best is None else best}\n")
if __name__=="__main__":main()
