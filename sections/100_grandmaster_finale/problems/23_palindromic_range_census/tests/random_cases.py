import argparse,random
from pathlib import Path
def case(r):
 n=r.randint(1,18);s=''.join(r.choice('abc') for _ in range(n));seen=set();iv=[]
 for e in range(n):
  for st in range(e+1):
   x=s[st:e+1]
   if x==x[::-1] and x not in seen:seen.add(x);iv.append((st+1,e+1))
 q=r.randint(1,25);qs=[];ans=[]
 for _ in range(q):l=r.randint(1,n);h=r.randint(l,n);qs.append((l,h));ans.append(str(sum(l<=a and b<=h for a,b in iv)))
 return s+'\n'+str(q)+'\n'+''.join(f'{l} {h}\n' for l,h in qs),'\n'.join(ans)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--count',type=int,default=25);p.add_argument('--seed',type=int,default=1);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);r=random.Random(a.seed)
 for i in range(a.count):x,y=case(r);z=a.out_dir/f'case{i:03d}';z.with_suffix('.in').write_text(x);z.with_suffix('.out').write_text(y)
if __name__=='__main__':main()
