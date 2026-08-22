import argparse,random
from pathlib import Path
def case(r):
 n=r.randint(1,22);s=''.join(r.choice('abc') for _ in range(n));q=r.randint(1,25);qs=[];ans=[]
 for _ in range(q):
  p=''.join(r.choice('abc') for _ in range(r.randint(1,6)));k=r.randint(1,8);a=[i+1 for i in range(n-len(p)+1) if s[i:i+len(p)]==p];qs.append((p,k));ans.append(str(a[k-1] if len(a)>=k else -1))
 return s+'\n'+str(q)+'\n'+''.join(f'{p} {k}\n' for p,k in qs),'\n'.join(ans)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--count',type=int,default=25);p.add_argument('--seed',type=int,default=1);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);r=random.Random(a.seed)
 for i in range(a.count):x,y=case(r);z=a.out_dir/f'case{i:03d}';z.with_suffix('.in').write_text(x);z.with_suffix('.out').write_text(y)
if __name__=='__main__':main()
