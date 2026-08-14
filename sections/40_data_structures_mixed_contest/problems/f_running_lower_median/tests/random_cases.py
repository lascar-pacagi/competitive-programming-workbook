import argparse,bisect,random
from pathlib import Path
def main():
    p=argparse.ArgumentParser();p.add_argument("--count",type=int,required=True);p.add_argument("--seed",type=int,required=True);p.add_argument("--out-dir",type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);rng=random.Random(a.seed)
    for z in range(a.count):
        n=rng.randint(1,100);values=[rng.randint(-100,100) for _ in range(n)];ordered=[];out=[]
        for x in values:bisect.insort(ordered,x);out.append(str(ordered[(len(ordered)-1)//2]))
        stem=a.out_dir/f"case{z:03d}";stem.with_suffix(".in").write_text(f"{n}\n"+" ".join(map(str,values))+"\n");stem.with_suffix(".out").write_text(" ".join(out)+"\n")
if __name__=="__main__":main()
