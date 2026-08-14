from __future__ import annotations
import argparse,random
from pathlib import Path
def brute(a,k,z):
 for s in range(z+1):
  if s+k-1<=z and all(s+k-1<l or r<s for l,r in a):return s
 return -1
def main():
 p=argparse.ArgumentParser();p.add_argument('--count',type=int,required=True);p.add_argument('--seed',type=int,required=True);p.add_argument('--out-dir',type=Path,required=True);x=p.parse_args();x.out_dir.mkdir(parents=True,exist_ok=True);g=random.Random(x.seed)
 for c in range(x.count):
  if c==0:a=[(i*2,i*2) for i in range(200000)];rows=[(a,1,500000)];ans=['1']
  else:
   rows=[];ans=[]
   for _ in range(g.randint(1,7)):
    z=g.randint(0,60);a=[]
    for _ in range(g.randint(0,20)):
     l=g.randint(0,z);a.append((l,g.randint(l,z)))
    k=g.randint(1,15);rows.append((a,k,z));ans.append(str(brute(a,k,z)))
  lines=[str(len(rows))]
  for a,k,z in rows:lines.append(f'{len(a)} {k} {z}');lines.extend(f'{l} {r}' for l,r in a)
  s=x.out_dir/f'case{c:03d}';s.with_suffix('.in').write_text('\n'.join(lines)+'\n');s.with_suffix('.out').write_text('\n'.join(ans)+'\n')
if __name__=='__main__':main()
