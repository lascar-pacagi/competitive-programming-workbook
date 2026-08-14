import argparse,random
from pathlib import Path
def main():
    p=argparse.ArgumentParser();p.add_argument("--count",type=int,required=True);p.add_argument("--seed",type=int,required=True);p.add_argument("--out-dir",type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);rng=random.Random(a.seed)
    for z in range(a.count):
        pattern="".join(rng.choice("abc") for _ in range(rng.randint(1,20)));text="".join(rng.choice("abc") for _ in range(rng.randint(1,40)));out=[]
        for i in range(len(text)):
            k=0
            while k<len(pattern) and i+k<len(text) and pattern[k]==text[i+k]:k+=1
            out.append(str(k))
        stem=a.out_dir/f"case{z:03d}";stem.with_suffix(".in").write_text(pattern+"\n"+text+"\n");stem.with_suffix(".out").write_text(" ".join(out)+"\n")
if __name__=="__main__":main()
