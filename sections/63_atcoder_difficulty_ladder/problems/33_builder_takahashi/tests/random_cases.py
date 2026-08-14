from __future__ import annotations
import argparse, random
from pathlib import Path
def brute(s):return [sum(s[i:i+l]==s[:l] for i in range(len(s)-l+1)) for l in range(1,len(s)+1)]
def main():
 p=argparse.ArgumentParser();p.add_argument('--count',type=int,required=True);p.add_argument('--seed',type=int,required=True);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);r=random.Random(a.seed)
 for k in range(a.count):
  s='a'*200000 if k==0 else ''.join(r.choice('abc') for _ in range(r.randint(1,40)))
  ans=list(range(len(s),0,-1)) if k==0 else brute(s);z=a.out_dir/f'case{k:03d}';z.with_suffix('.in').write_text(s+'\n');z.with_suffix('.out').write_text(' '.join(map(str,ans))+'\n')
if __name__=='__main__':main()
