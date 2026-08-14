import argparse, random
from pathlib import Path
MOD=1_000_000_007
def slow(l,r):
    a,b=0,1;s=0
    for i in range(r+1):
        if i>=l:s=(s+a)%MOD
        a,b=b,(a+b)%MOD
    return s
def main():
    p=argparse.ArgumentParser();p.add_argument('--count',type=int,required=True);p.add_argument('--seed',type=int,required=True);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);g=random.Random(a.seed)
    for c in range(a.count):
        if c==0:qs=[(0,0)]*200000;ans=[0]*200000
        else:
            qs=[]
            for _ in range(g.randint(1,30)):
                l=g.randint(0,30);qs.append((l,g.randint(l,40)))
            ans=[slow(l,r) for l,r in qs]
        z=a.out_dir/f'case{c:03d}';z.with_suffix('.in').write_text(str(len(qs))+'\n'+'\n'.join(f'{l} {r}' for l,r in qs)+'\n');z.with_suffix('.out').write_text('\n'.join(map(str,ans))+'\n')
if __name__=='__main__':main()
