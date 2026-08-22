import argparse,random
from pathlib import Path
def case(r):
 n=r.randint(1,30);k=r.randint(0,n);a=''.join(r.choice('abc?') for _ in range(n));b=''.join(r.choice('abc?') for _ in range(n));z=[d for d in range(n) if sum(a[i]!='?' and b[(i+d)%n]!='?' and a[i]!=b[(i+d)%n] for i in range(n))<=k];return f'{n} {k}\n{a}\n{b}\n',str(len(z))+'\n'+' '.join(map(str,z))+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--count',type=int,default=25);p.add_argument('--seed',type=int,default=1);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);r=random.Random(a.seed)
 for i in range(a.count):x,y=case(r);z=a.out_dir/f'case{i:03d}';z.with_suffix('.in').write_text(x);z.with_suffix('.out').write_text(y)
if __name__=='__main__':main()
