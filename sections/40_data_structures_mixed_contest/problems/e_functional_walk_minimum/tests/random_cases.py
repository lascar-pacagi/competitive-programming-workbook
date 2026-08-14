import argparse,random
from pathlib import Path
def main():
    p=argparse.ArgumentParser();p.add_argument("--count",type=int,required=True);p.add_argument("--seed",type=int,required=True);p.add_argument("--out-dir",type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);rng=random.Random(a.seed)
    for z in range(a.count):
        n,q=rng.randint(1,20),rng.randint(1,40);nxt=[rng.randrange(n) for _ in range(n)];val=[rng.randint(-20,20) for _ in range(n)];lines=[f"{n} {q}"," ".join(str(x+1) for x in nxt)," ".join(map(str,val))];out=[]
        for _ in range(q):
            start,k=rng.randrange(n),rng.randint(0,100);v=start;best=val[v]
            for _ in range(k):v=nxt[v];best=min(best,val[v])
            lines.append(f"{start+1} {k}");out.append(f"{v+1} {best}")
        stem=a.out_dir/f"case{z:03d}";stem.with_suffix(".in").write_text("\n".join(lines)+"\n");stem.with_suffix(".out").write_text("\n".join(out)+"\n")
if __name__=="__main__":main()
