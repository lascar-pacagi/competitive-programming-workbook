import argparse,random
from pathlib import Path
def main():
    p=argparse.ArgumentParser();p.add_argument("--count",type=int,required=True);p.add_argument("--seed",type=int,required=True);p.add_argument("--out-dir",type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);rng=random.Random(a.seed)
    for z in range(a.count):
        s="".join(rng.choice("abcd") for _ in range(rng.randint(1,80)));q=rng.randint(1,100);lines=[s,str(q)];out=[]
        for _ in range(q):
            i,j=rng.randrange(len(s)),rng.randrange(len(s));k=0
            while i+k<len(s) and j+k<len(s) and s[i+k]==s[j+k]:k+=1
            lines.append(f"{i+1} {j+1}");out.append(str(k))
        stem=a.out_dir/f"case{z:03d}";stem.with_suffix(".in").write_text("\n".join(lines)+"\n");stem.with_suffix(".out").write_text("\n".join(out)+"\n")
if __name__=="__main__":main()
