import argparse,random
from pathlib import Path
def case(r):
 s=''.join(r.choice('abc') for _ in range(r.randint(1,25)));a=0
 for i in range(len(s)):
  for j in range(i+1,len(s)):
   k=0
   while j+k<len(s) and s[i+k]==s[j+k]:k+=1
   a+=k
 return s+'\n',f'{a}\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--count',type=int,default=25);p.add_argument('--seed',type=int,default=1);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);r=random.Random(a.seed)
 for i in range(a.count):x,y=case(r);z=a.out_dir/f'case{i:03d}';z.with_suffix('.in').write_text(x);z.with_suffix('.out').write_text(y)
if __name__=='__main__':main()
