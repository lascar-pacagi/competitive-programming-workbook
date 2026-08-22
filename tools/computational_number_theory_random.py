"""Independent trial-division and exhaustive oracles for Sections 91--93."""
import argparse, math, random
from pathlib import Path
MOD=1_000_000_007

def factors(n):
 out=[];p=2
 while p*p<=n:
  while n%p==0:out.append(p);n//=p
  p+=1 if p==2 else 2
 if n>1:out.append(n)
 return out
def grouped(n):
 out=[]
 for p in factors(n):
  if out and out[-1][0]==p:out[-1][1]+=1
  else:out.append([p,1])
 return out
def phi(n):
 r=n
 for p,_ in grouped(n):r=r//p*(p-1)
 return r
def order(a,n):
 x=1
 for k in range(1,phi(n)+1):
  x=x*a%n
  if x==1:return k
 raise AssertionError
def primitive(p):
 if p==2:return 1
 for g in range(2,p):
  if order(g,p)==p-1:return g
def dlog(a,b,m):
 value=1%m;seen=set()
 for x in range(2*m+2):
  if value==b%m:return x
  if value in seen:return None
  seen.add(value);value=value*a%m
 return None
def primes(limit=300):return [n for n in range(2,limit) if all(n%d for d in range(2,math.isqrt(n)+1))]
PRIMES=primes()
def one(kind,r):
 q=r.randint(1,12)
 if kind in {'prime','factor','totient','divstats','largest','carmichael'}:
  lo=2 if kind=='largest' else 1;upper=200 if kind=='carmichael' else 2_000_000;nums=[r.randint(lo,upper) for _ in range(q)];answers=[]
  for n in nums:
   fs=factors(n)
   if kind=='prime':answers.append('PRIME' if len(fs)==1 and fs[0]==n else 'COMPOSITE')
   elif kind=='factor':answers.append('1' if n==1 else ' '.join(map(str,fs)))
   elif kind=='totient':answers.append(str(phi(n)))
   elif kind=='largest':answers.append(str(max(fs)))
   elif kind=='divstats':
    count=1;total=1
    for p,e in grouped(n):count*=e+1;total=total*sum(pow(p,i,MOD) for i in range(e+1))%MOD
    answers.append(f'{count} {total}')
   else:
    lam=1
    for a in range(1,n):
     if math.gcd(a,n)==1:lam=math.lcm(lam,order(a,n))
    answers.append(str(lam))
  return f'{q}\n'+'\n'.join(map(str,nums))+'\n','\n'.join(answers)+'\n'
 if kind=='primitive':
  ps=[r.choice(PRIMES) for _ in range(q)];return f'{q}\n'+'\n'.join(map(str,ps))+'\n','\n'.join(str(primitive(p)) for p in ps)+'\n'
 if kind in {'dlog_prime','dlog_general'}:
  rows=[];ans=[]
  for _ in range(q):
   if kind=='dlog_prime':m=r.choice(PRIMES);a=r.randrange(m);b=r.randrange(m);rows.append((m,a,b))
   else:m=r.randint(2,250);a=r.randint(1,m-1);b=r.randint(1,m-1);rows.append((a,b,m))
   x=dlog(a,b,m);ans.append(str(-1 if x is None else x))
  return f'{q}\n'+''.join(' '.join(map(str,x))+'\n' for x in rows),'\n'.join(ans)+'\n'
 if kind=='sqrt':
  rows=[];ans=[]
  for _ in range(q):
   p=r.choice(PRIMES[1:]);a=r.randrange(p);roots=[x for x in range(p) if x*x%p==a];rows.append((p,a));ans.append('NONE' if not roots else ' '.join(map(str,roots)))
  return f'{q}\n'+''.join(f'{p} {a}\n' for p,a in rows),'\n'.join(ans)+'\n'
 if kind=='order':
  rows=[]
  for _ in range(q):
   n=r.randint(2,500);a=r.randrange(1,n)
   while math.gcd(a,n)>1:a=r.randrange(1,n)
   rows.append((a,n))
  return f'{q}\n'+''.join(f'{a} {n}\n' for a,n in rows),'\n'.join(str(order(a,n)) for a,n in rows)+'\n'
 if kind=='powerroot':
  rows=[];ans=[]
  for _ in range(q):
   p=r.choice(PRIMES[1:]);k=r.randint(1,30);a=r.randrange(1,p);g=primitive(p);ys=[y for y in range(p-1) if pow(pow(g,y,p),k,p)==a];rows.append((p,k,a));ans.append(str(min(ys)) if ys else '-1')
  return f'{q}\n'+''.join(f'{p} {k} {a}\n' for p,k,a in rows),'\n'.join(ans)+'\n'
 if kind=='sqrt_batch':
  p=r.choice(PRIMES[1:]);vals=[r.randrange(p) for _ in range(q)];ans=[]
  for a in vals:
   roots=[x for x in range(p) if x*x%p==a];ans.append(str(min(roots)) if roots else '-1')
  return f'{p} {q}\n'+'\n'.join(map(str,vals))+'\n','\n'.join(ans)+'\n'
 if kind=='affine_log':
  rows=[];ans=[]
  for _ in range(q):
   p=r.choice(PRIMES[1:]);a=r.randrange(1,p);b=r.randrange(1,p);u=r.randint(0,20);v=r.randint(0,20);values=[t for t in range(2*p+1) if pow(a,u*t+v,p)==b];rows.append((p,a,b,u,v));ans.append(str(min(values)) if values else '-1')
  return f'{q}\n'+''.join(' '.join(map(str,x))+'\n' for x in rows),'\n'.join(ans)+'\n'
 raise ValueError(kind)
def main():
 p=argparse.ArgumentParser();p.add_argument('kind');p.add_argument('--count',type=int,default=20);p.add_argument('--seed',type=int,default=1);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);r=random.Random(a.seed)
 for i in range(a.count):x,y=one(a.kind,r);stem=a.out_dir/f'case{i:03d}';stem.with_suffix('.in').write_text(x);stem.with_suffix('.out').write_text(y)
if __name__=='__main__':main()
