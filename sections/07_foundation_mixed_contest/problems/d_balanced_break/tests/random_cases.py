from __future__ import annotations
import argparse, random, subprocess, sys
from pathlib import Path
P=Path(__file__).resolve().parents[1]
def slow(a):
 total=sum(a); left=0; best=None; pos=1
 for i in range(len(a)-1):
  left+=a[i]; d=abs(left-(total-left))
  if best is None or d<best: best,pos=d,i+1
 return f'{best} {pos}'
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--count',type=int,required=True);ap.add_argument('--seed',type=int,required=True);ap.add_argument('--out-dir',type=Path,required=True);z=ap.parse_args();r=random.Random(z.seed);z.out_dir.mkdir(parents=True,exist_ok=True)
 for c in range(z.count):
  arr=[[r.randint(-50,50) for _ in range(r.randint(2,30))] for _ in range(r.randint(1,10))]
  if c==0: arr=[[0]*200000]  # explicit scale case; the independent oracle still has a linear scan
  inp=str(len(arr))+'\n'+'\n'.join(str(len(a))+'\n'+' '.join(map(str,a)) for a in arr)+'\n';out='\n'.join(slow(a) for a in arr)+'\n';stem=f'case{c:03d}';(z.out_dir/f'{stem}.in').write_text(inp);(z.out_dir/f'{stem}.out').write_text(out)
if __name__=='__main__':main()
