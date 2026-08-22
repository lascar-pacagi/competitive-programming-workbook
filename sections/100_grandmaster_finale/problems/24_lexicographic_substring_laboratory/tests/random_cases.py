import argparse,random
from pathlib import Path
def case(r):
 n=r.randint(1,24);s=''.join(r.choice('abc') for _ in range(n));q=r.randint(1,30);qs=[];ans=[]
 for _ in range(q):
  l=r.randint(1,n);h=r.randint(l,n);k=r.randint(1,h-l+1);a=sorted(range(l-1,h),key=lambda x:s[x:]);x=a[k-1];v=0
  if k<len(a):
   y=a[k]
   while x+v<n and y+v<n and s[x+v]==s[y+v]:v+=1
  qs.append((l,h,k));ans.append(f'{x+1} {v}')
 return s+'\n'+str(q)+'\n'+''.join(f'{a} {b} {c}\n' for a,b,c in qs),'\n'.join(ans)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--count',type=int,default=25);p.add_argument('--seed',type=int,default=1);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);r=random.Random(a.seed)
 for i in range(a.count):x,y=case(r);z=a.out_dir/f'case{i:03d}';z.with_suffix('.in').write_text(x);z.with_suffix('.out').write_text(y)
if __name__=='__main__':main()
