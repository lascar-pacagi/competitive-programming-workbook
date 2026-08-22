import argparse,random
from pathlib import Path
def case(r):
 n=r.randint(1,11);k=r.randint(1,n);a=[r.randint(0,9) for _ in range(n)];inf=10**30;dp=[[inf]*(k+1) for _ in range(n+1)];dp[0][0]=0;s=[0]
 for x in a:s.append(s[-1]+x)
 for i in range(1,n+1):
  for c in range(1,min(i,k)+1):dp[i][c]=min(dp[j][c-1]+(s[i]-s[j])**2 for j in range(c-1,i))
 return f"{n} {k}\n"+' '.join(map(str,a))+'\n',f"{dp[n][k]}\n"
def main():
 p=argparse.ArgumentParser();p.add_argument('--count',type=int,default=25);p.add_argument('--seed',type=int,default=1);p.add_argument('--out-dir',type=Path,required=True);z=p.parse_args();z.out_dir.mkdir(parents=True,exist_ok=True);r=random.Random(z.seed)
 for i in range(z.count):a,b=case(r);s=z.out_dir/f"case{i:03d}";s.with_suffix('.in').write_text(a);s.with_suffix('.out').write_text(b)
if __name__=='__main__':main()
