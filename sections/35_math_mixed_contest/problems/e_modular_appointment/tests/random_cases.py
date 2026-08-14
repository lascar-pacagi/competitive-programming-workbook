import argparse,math,random
from pathlib import Path
def main():
    p=argparse.ArgumentParser();p.add_argument("--count",type=int,required=True);p.add_argument("--seed",type=int,required=True);p.add_argument("--out-dir",type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);rng=random.Random(a.seed)
    for z in range(a.count):
        q=rng.randint(1,30);lines=[str(q)];out=[]
        for _ in range(q):
            aa,m=rng.randint(1,100),rng.randint(1,100);b,c=rng.randint(0,100),rng.randint(0,100);lines.append(f"{aa} {b} {c} {m}")
            ans=next((x for x in range(m) if (aa*x+c-b)%m==0),-1);out.append(str(ans))
        stem=a.out_dir/f"case{z:03d}";stem.with_suffix(".in").write_text("\n".join(lines)+"\n");stem.with_suffix(".out").write_text("\n".join(out)+"\n")
if __name__=="__main__":main()
