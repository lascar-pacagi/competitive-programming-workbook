import argparse,random
from pathlib import Path
def case(r):
 s=''.join(r.choice('abc') for _ in range(r.randint(1,13)));a=sorted({s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1)});q=r.randint(1,25);ks=[r.randint(1,len(a)+5) for _ in range(q)];return s+'\n'+str(q)+'\n'+'\n'.join(map(str,ks))+'\n','\n'.join(a[k-1] if k<=len(a) else '-1' for k in ks)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--count',type=int,default=25);p.add_argument('--seed',type=int,default=1);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);r=random.Random(a.seed)
 for i in range(a.count):x,y=case(r);z=a.out_dir/f'case{i:03d}';z.with_suffix('.in').write_text(x);z.with_suffix('.out').write_text(y)
if __name__=='__main__':main()
