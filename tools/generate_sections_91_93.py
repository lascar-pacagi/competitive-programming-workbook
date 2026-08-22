"""Generate Sections 91--93: 64-bit computational number theory."""
from __future__ import annotations
import json
import textwrap
import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CPP_STUB = '''#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // TODO: solve the problem.
    return 0;
}
'''
PY_STUB = '''import sys


def main() -> None:
    # TODO: solve the problem.
    pass


if __name__ == "__main__":
    main()
'''

SECTIONS = {
    91: ("primality_integer_factorization", "Primality And Integer Factorization"),
    92: ("discrete_logs_modular_roots", "Discrete Logarithms And Modular Roots"),
    93: ("master_computational_number_theory_mixed", "Master Computational Number Theory Mixed Contest"),
}
TIME_LIMITS = {
    "dlog_prime": 60,
    "dlog_general": 60,
    "powerroot": 25,
    "affine_log": 25,
}
PROBLEMS = {
    91: [
        ("a_prime_or_composite", "Prime Or Composite", "prime"),
        ("b_complete_factorization", "Complete Factorization", "factor"),
        ("c_large_totient", "Large Totient", "totient"),
        ("d_large_divisor_statistics", "Large Divisor Statistics", "divstats"),
    ],
    92: [
        ("a_smallest_primitive_root", "Smallest Primitive Root", "primitive"),
        ("b_prime_discrete_log", "Prime Discrete Log", "dlog_prime"),
        ("c_general_discrete_log", "General Discrete Log", "dlog_general"),
        ("d_modular_square_roots", "Modular Square Roots", "sqrt"),
    ],
    93: [
        ("a_largest_prime_fragment", "Largest Prime Fragment", "largest"),
        ("b_carmichael_clock", "Carmichael Clock", "carmichael"),
        ("c_multiplicative_order", "Multiplicative Order", "order"),
        ("d_power_congruence", "Power Congruence", "powerroot"),
        ("e_quadratic_residue_archive", "Quadratic Residue Archive", "sqrt_batch"),
        ("f_affine_exponent_meeting", "Affine Exponent Meeting", "affine_log"),
    ],
}

STATEMENTS = {
"prime": """For each of `q <= 100000` unsigned integers `n < 2^64`, print `PRIME` or `COMPOSITE`. Values below two are composite.\n\nInput starts with `q`, followed by one number per line.\n\nSample input\n```text\n4\n1\n2\n561\n1000000007\n```\nSample output\n```text\nCOMPOSITE\nPRIME\nCOMPOSITE\nPRIME\n```""",
"factor": """Factor each positive unsigned integer `n < 2^64`. Print its prime factors in nondecreasing order, with repetitions. For `n=1`, print `1`. There are at most 200 queries.\n\nSample input\n```text\n3\n1\n60\n1000000016000000063\n```\nSample output\n```text\n1\n2 2 3 5\n1000000007 1000000009\n```""",
"totient": """For each positive `n < 2^64`, print Euler's totient `phi(n)`: the count of integers in `[1,n]` coprime to `n`. At most 200 queries.\n\nSample input\n```text\n3\n1\n36\n1000000007\n```\nSample output\n```text\n1\n12\n1000000006\n```""",
"divstats": """For each positive `n < 2^64`, print two values: its number of positive divisors and the sum of those divisors modulo `1000000007`. At most 200 queries.\n\nSample input\n```text\n2\n12\n36\n```\nSample output\n```text\n6 28\n9 91\n```""",
"primitive": """For each prime `p < 2^63`, print the smallest positive primitive root modulo `p`. A primitive root has multiplicative order `p-1`. Define the answer for `p=2` as `1`. At most 100 queries.\n\nSample input\n```text\n3\n2\n7\n17\n```\nSample output\n```text\n1\n3\n3\n```""",
"dlog_prime": """For prime `p < 2^63` and integers `a,b` in `[0,p)`, print the smallest `x >= 0` satisfying `a^x = b (mod p)`, or `-1`. There are at most 100 queries and `p <= 10^12`.\n\nSample input\n```text\n2\n13 2 8\n7 3 5\n```\nSample output\n```text\n3\n5\n```""",
"dlog_general": """For each `1 <= a,b < m <= 10^12`, print the smallest `x >= 0` with `a^x = b (mod m)`, or `-1`. The base need not be coprime to the modulus. At most 100 queries.\n\nSample input\n```text\n3\n2 8 12\n4 2 14\n3 5 7\n```\nSample output\n```text\n3\n2\n5\n```""",
"sqrt": """For each odd prime `p < 2^63` and `0 <= a < p`, print all solutions of `x^2 = a (mod p)` in increasing order, or `NONE`. Print one value when both roots coincide. At most 1000 queries.\n\nSample input\n```text\n3\n7 2\n7 3\n11 0\n```\nSample output\n```text\n3 4\nNONE\n0\n```""",
"largest": """For each `1 < n < 2^64`, print its largest prime factor. At most 200 queries.\n\nSample input\n```text\n3\n12\n97\n1000000016000000063\n```\nSample output\n```text\n3\n97\n1000000009\n```""",
"carmichael": """For each positive `n < 2^64`, print the Carmichael value `lambda(n)`, the smallest positive `L` such that `a^L = 1 (mod n)` for every `a` coprime to `n`. Define `lambda(1)=1`. At most 200 queries.\n\nSample input\n```text\n3\n1\n8\n15\n```\nSample output\n```text\n1\n2\n4\n```""",
"order": """Given coprime `a,n` with `1 <= a < n < 2^63`, print the multiplicative order of `a` modulo `n`. At most 100 queries.\n\nSample input\n```text\n2\n2 9\n3 7\n```\nSample output\n```text\n6\n6\n```""",
"powerroot": """For odd prime `p <= 10^12`, let `g` be its smallest primitive root. Given `k > 0` and `a` in `[1,p)`, print the smallest `y >= 0` satisfying `(g^y)^k = a (mod p)`, or `-1`. At most 50 queries.\n\nSample input\n```text\n2\n7 2 2\n7 2 3\n```\nSample output\n```text\n1\n-1\n```""",
"sqrt_batch": """An odd prime `p < 2^63` is fixed. For each query value `a`, print the smaller modular square root of `a`, or `-1` if none exists. `q <= 100000`.\n\nSample input\n```text\n7 3\n2\n3\n4\n```\nSample output\n```text\n3\n-1\n2\n```""",
"affine_log": """For prime `p <= 10^12`, find the smallest `t >= 0` such that `a^(u*t+v) = b (mod p)`, where `a,b` are nonzero and `u,v >= 0`, or print `-1`. At most 50 queries.\n\nSample input\n```text\n2\n13 2 8 1 0\n13 2 8 2 0\n```\nSample output\n```text\n3\n-1\n```""",
}

PY_CORE = r'''import sys,math,random
MR_BASES=(2,325,9375,28178,450775,9780504,1795265022)
def is_prime(n):
 if n<2:return False
 for p in (2,3,5,7,11,13,17,19,23,29,31,37):
  if n%p==0:return n==p
 d=n-1;s=0
 while d%2==0:s+=1;d//=2
 for a in MR_BASES:
  if a%n==0:continue
  x=pow(a,d,n)
  if x in (1,n-1):continue
  for _ in range(s-1):
   x=x*x%n
   if x==n-1:break
  else:return False
 return True
_rng=random.Random(712367821)
def rho(n):
 if n%2==0:return 2
 if n%3==0:return 3
 while True:
  c=_rng.randrange(1,n);x=_rng.randrange(0,n);y=x;d=1
  while d==1:
   x=(x*x+c)%n;y=(y*y+c)%n;y=(y*y+c)%n;d=math.gcd(abs(x-y),n)
  if d!=n:return d
def factor(n):
 out=[];stack=[n]
 while stack:
  x=stack.pop()
  if x==1:continue
  if is_prime(x):out.append(x)
  else:d=rho(x);stack.extend((d,x//d))
 out.sort();return out
def groups(n):
 result=[]
 for p in factor(n):
  if result and result[-1][0]==p:result[-1]=(p,result[-1][1]+1)
  else:result.append((p,1))
 return result
def phi(n):
 answer=n
 for p,_ in groups(n):answer=answer//p*(p-1)
 return answer
def lcm(a,b):return a//math.gcd(a,b)*b
def carmichael(n):
 answer=1
 for p,e in groups(n):
  part=(1<<(e-2)) if p==2 and e>=3 else (p-1)*p**(e-1)
  answer=lcm(answer,part)
 return answer
def primitive_root(p):
 if p==2:return 1
 primes=[q for q,_ in groups(p-1)];g=2
 while any(pow(g,(p-1)//q,p)==1 for q in primes):g+=1
 return g
def bsgs(a,b,m):
 a%=m;b%=m
 if m==1:return 0
 size=math.isqrt(m)+1;baby={};value=1
 for j in range(size):
  baby.setdefault(value,j);value=value*a%m
 step=pow(pow(a,size,m),-1,m);value=b
 best=None
 for i in range(size+1):
  if value in baby:
   candidate=i*size+baby[value]
   if best is None or candidate<best:best=candidate
  value=value*step%m
 return best
def discrete_log(a,b,m):
 a%=m;b%=m
 if b==1%m:return 0
 added=0;scale=1
 while True:
  g=math.gcd(a,m)
  if g==1:break
  if b%g:return None
  m//=g;b//=g;scale=scale*(a//g)%m;added+=1
  if scale==b:return added
  if m==1:return added
 target=b*pow(scale,-1,m)%m
 tail=bsgs(a%m,target,m)
 return None if tail is None else added+tail
def tonelli(a,p):
 a%=p
 if a==0:return 0
 if pow(a,(p-1)//2,p)!=1:return None
 if p%4==3:return pow(a,(p+1)//4,p)
 q=p-1;s=0
 while q%2==0:s+=1;q//=2
 z=2
 while pow(z,(p-1)//2,p)!=p-1:z+=1
 c=pow(z,q,p);x=pow(a,(q+1)//2,p);t=pow(a,q,p);m=s
 while t!=1:
  i=1;value=t*t%p
  while value!=1:value=value*value%p;i+=1
  b=pow(c,1<<(m-i-1),p);x=x*b%p;t=t*b*b%p;c=b*b%p;m=i
 return x
def order(a,n):
 value=carmichael(n)
 for p,_ in groups(value):
  while value%p==0 and pow(a,value//p,n)==1:value//=p
 return value
def linear_smallest(a,b,m):
 g=math.gcd(a,m)
 if b%g:return None
 mod=m//g
 return (b//g)*pow(a//g,-1,mod)%mod if mod>1 else 0
'''

def py_solution(kind):
 body={
 'prime':"print('\\n'.join('PRIME' if is_prime(n) else 'COMPOSITE' for n in d[1:]))",
 'factor':"print('\\n'.join('1' if n==1 else ' '.join(map(str,factor(n))) for n in d[1:]))",
 'totient':"print('\\n'.join(str(phi(n)) for n in d[1:]))",
 'divstats':"""out=[]
 for n in d[1:]:
  count=1;total=1
  for p,e in groups(n):count*=e+1;total=total*sum(pow(p,i,1000000007) for i in range(e+1))%1000000007
  out.append(f'{count} {total}')
 print('\\n'.join(out))""",
 'primitive':"print('\\n'.join(str(primitive_root(p)) for p in d[1:]))",
 'dlog_prime':"""out=[]
 for i in range(1,len(d),3):
  p,a,b=d[i:i+3];x=discrete_log(a,b,p);out.append(str(-1 if x is None else x))
 print('\\n'.join(out))""",
 'dlog_general':"""out=[]
 for i in range(1,len(d),3):
  a,b,m=d[i:i+3];x=discrete_log(a,b,m);out.append(str(-1 if x is None else x))
 print('\\n'.join(out))""",
 'sqrt':"""out=[]
 for i in range(1,len(d),2):
  p,a=d[i:i+2];x=tonelli(a,p)
  if x is None:out.append('NONE')
  else:
   roots=sorted({x,(p-x)%p});out.append(' '.join(map(str,roots)))
 print('\\n'.join(out))""",
 'largest':"print('\\n'.join(str(max(factor(n))) for n in d[1:]))",
 'carmichael':"print('\\n'.join(str(carmichael(n)) for n in d[1:]))",
 'order':"""out=[]
 for i in range(1,len(d),2):out.append(str(order(d[i],d[i+1])))
 print('\\n'.join(out))""",
 'powerroot':"""out=[]
 for i in range(1,len(d),3):
  p,k,a=d[i:i+3];g=primitive_root(p);target=discrete_log(g,a,p);y=linear_smallest(k,target,p-1);out.append(str(-1 if y is None else y))
 print('\\n'.join(out))""",
 'sqrt_batch':"""p,q=d[:2];out=[]
 for a in d[2:]:
  x=tonelli(a,p);out.append(str(-1 if x is None else min(x,p-x)))
 print('\\n'.join(out))""",
 'affine_log':"""out=[]
 for i in range(1,len(d),5):
  p,a,b,u,v=d[i:i+5];x=discrete_log(a,b,p)
  if x is None:out.append('-1');continue
  t=linear_smallest(u,(x-v)%order(a,p),order(a,p));out.append(str(-1 if t is None else t))
 print('\\n'.join(out))""",
 }[kind]
 body=textwrap.dedent(body).strip()
 lines=body.splitlines()
 if len(lines)>1 and lines[1].startswith(' '):
  lines=[lines[0]]+[line[1:] if line.startswith(' ') else line for line in lines[1:]]
 body='\n'.join(lines)
 return PY_CORE+'def main():\n d=list(map(int,sys.stdin.buffer.read().split()))\n'+textwrap.indent(body,' ')+'\nif __name__==\'__main__\':main()\n'

CPP_CORE = r'''#include <bits/stdc++.h>
using namespace std;using u64=uint64_t;using u128=__uint128_t;using i128=__int128_t;
u64 mul(u64 a,u64 b,u64 m){return(u128)a*b%m;}u64 power(u64 a,u64 e,u64 m){u64 r=1%m;for(;e;e>>=1,a=mul(a,a,m))if(e&1)r=mul(r,a,m);return r;}
bool prime(u64 n){if(n<2)return false;for(u64 p:{2,3,5,7,11,13,17,19,23,29,31,37})if(n%p==0)return n==p;u64 d=n-1,s=0;while(!(d&1))d>>=1,++s;for(u64 a:{2,325,9375,28178,450775,9780504,1795265022}){if(a%n==0)continue;u64 x=power(a,d,n);if(x==1||x==n-1)continue;bool witness=true;for(u64 r=1;r<s;r++){x=mul(x,x,n);if(x==n-1){witness=false;break;}}if(witness)return false;}return true;}
mt19937_64 rng(712367821);u64 rho(u64 n){if(n%2==0)return 2;if(n%3==0)return 3;while(true){u64 c=rng()%(n-1)+1,x=rng()%n,y=x,d=1;while(d==1){x=(u128(mul(x,x,n))+c)%n;y=(u128(mul(y,y,n))+c)%n;y=(u128(mul(y,y,n))+c)%n;d=gcd(x>y?x-y:y-x,n);}if(d!=n)return d;}}
vector<u64> factor(u64 n){vector<u64>out,st={n};while(!st.empty()){u64 x=st.back();st.pop_back();if(x==1)continue;if(prime(x))out.push_back(x);else{u64 d=rho(x);st.push_back(d);st.push_back(x/d);}}sort(out.begin(),out.end());return out;}vector<pair<u64,int>>groups(u64 n){vector<pair<u64,int>>g;for(u64 p:factor(n))if(!g.empty()&&g.back().first==p)g.back().second++;else g.push_back({p,1});return g;}
u64 phi(u64 n){u64 r=n;for(auto[p,e]:groups(n))r=r/p*(p-1);return r;}u64 lcm64(u64 a,u64 b){return a/gcd(a,b)*b;}u64 lambda(u64 n){u64 r=1;for(auto[p,e]:groups(n)){u64 z;if(p==2&&e>=3)z=1ULL<<(e-2);else{z=p-1;for(int i=1;i<e;i++)z*=p;}r=lcm64(r,z);}return r;}
u64 primitive(u64 p){if(p==2)return 1;vector<u64>q;for(auto[x,e]:groups(p-1))q.push_back(x);for(u64 g=2;;g++){bool ok=true;for(u64 x:q)if(power(g,(p-1)/x,p)==1){ok=false;break;}if(ok)return g;}}
long long invmod(long long a,long long m){long long b=m;i128 x=1,y=0;while(b){long long q=a/b,t=a%b;a=b;b=t;i128 z=x-(i128)q*y;x=y;y=z;}x%=m;if(x<0)x+=m;return(long long)x;}
optional<u64>bsgs(u64 a,u64 b,u64 m){if(m==1)return 0;u64 z=sqrtl((long double)m)+1;while((u128)z*z<m)z++;unordered_map<u64,u64>baby;u64 value=1;for(u64 j=0;j<z;j++){if(!baby.count(value))baby[value]=j;value=mul(value,a,m);}u64 step=invmod(power(a,z,m),m);value=b;optional<u64>best;for(u64 i=0;i<=z;i++){auto it=baby.find(value);if(it!=baby.end()){u64 candidate=i*z+it->second;if(!best||candidate<*best)best=candidate;}value=mul(value,step,m);}return best;}
optional<u64>dlog(u64 a,u64 b,u64 m){a%=m;b%=m;if(b==1%m)return 0;u64 added=0,scale=1;while(true){u64 g=gcd(a,m);if(g==1)break;if(b%g)return{};m/=g;b/=g;scale=mul(scale,a/g,m);added++;if(scale==b)return added;if(m==1)return added;}u64 target=mul(b,invmod(scale,m),m);auto tail=bsgs(a%m,target,m);if(!tail)return{};return added+*tail;}
optional<u64>tonelli(u64 a,u64 p){a%=p;if(a==0)return 0;if(power(a,(p-1)/2,p)!=1)return{};if(p%4==3)return power(a,(p+1)/4,p);u64 q=p-1,s=0;while(!(q&1))q>>=1,++s;u64 z=2;while(power(z,(p-1)/2,p)!=p-1)z++;u64 c=power(z,q,p),x=power(a,(q+1)/2,p),t=power(a,q,p),m=s;while(t!=1){u64 i=1,v=mul(t,t,p);while(v!=1)v=mul(v,v,p),i++;u64 h=power(c,1ULL<<(m-i-1),p);x=mul(x,h,p);t=mul(t,mul(h,h,p),p);c=mul(h,h,p);m=i;}return x;}
u64 order(u64 a,u64 n){u64 r=lambda(n);for(auto[p,e]:groups(r))while(r%p==0&&power(a,r/p,n)==1)r/=p;return r;}
optional<u64>linear(u64 a,u64 b,u64 m){u64 g=gcd(a,m);if(b%g)return{};u64 mod=m/g;if(mod==1)return 0;return mul((b/g)%mod,invmod((a/g)%mod,mod),mod);}
'''

def cpp_solution(kind):
 bodies={
 'prime':r'''int q;cin>>q;while(q--){u64 n;cin>>n;cout<<(prime(n)?"PRIME":"COMPOSITE")<<'\n';}''',
 'factor':r'''int q;cin>>q;while(q--){u64 n;cin>>n;if(n==1){cout<<"1\n";continue;}auto f=factor(n);for(int i=0;i<(int)f.size();i++)cout<<f[i]<<" \n"[i+1==(int)f.size()];}''',
 'totient':r'''int q;cin>>q;while(q--){u64 n;cin>>n;cout<<phi(n)<<'\n';}''',
 'divstats':r'''int q;cin>>q;const u64 M=1000000007;while(q--){u64 n;cin>>n;u64 cnt=1,sum=1;for(auto[p,e]:groups(n)){cnt*=e+1;u64 term=1,cur=1;for(int i=1;i<=e;i++)cur=mul(cur,p%M,M),term=(term+cur)%M;sum=mul(sum,term,M);}cout<<cnt<<' '<<sum<<'\n';}''',
 'primitive':r'''int q;cin>>q;while(q--){u64 p;cin>>p;cout<<primitive(p)<<'\n';}''',
 'dlog_prime':r'''int q;cin>>q;while(q--){u64 p,a,b;cin>>p>>a>>b;auto x=dlog(a,b,p);if(x)cout<<*x<<'\n';else cout<<"-1\n";}''',
 'dlog_general':r'''int q;cin>>q;while(q--){u64 a,b,m;cin>>a>>b>>m;auto x=dlog(a,b,m);if(x)cout<<*x<<'\n';else cout<<"-1\n";}''',
 'sqrt':r'''int q;cin>>q;while(q--){u64 p,a;cin>>p>>a;auto x=tonelli(a,p);if(!x){cout<<"NONE\n";continue;}u64 y=(p-*x)%p;if(*x==y)cout<<*x<<'\n';else cout<<min(*x,y)<<' '<<max(*x,y)<<'\n';}''',
 'largest':r'''int q;cin>>q;while(q--){u64 n;cin>>n;cout<<factor(n).back()<<'\n';}''',
 'carmichael':r'''int q;cin>>q;while(q--){u64 n;cin>>n;cout<<lambda(n)<<'\n';}''',
 'order':r'''int q;cin>>q;while(q--){u64 a,n;cin>>a>>n;cout<<order(a,n)<<'\n';}''',
 'powerroot':r'''int q;cin>>q;while(q--){u64 p,k,a;cin>>p>>k>>a;u64 g=primitive(p);auto target=dlog(g,a,p);auto y=linear(k,*target,p-1);if(y)cout<<*y<<'\n';else cout<<"-1\n";}''',
 'sqrt_batch':r'''u64 p;int q;cin>>p>>q;while(q--){u64 a;cin>>a;auto x=tonelli(a,p);if(x)cout<<min(*x,p-*x)<<'\n';else cout<<"-1\n";}''',
 'affine_log':r'''int q;cin>>q;while(q--){u64 p,a,b,u,v;cin>>p>>a>>b>>u>>v;auto x=dlog(a,b,p);if(!x){cout<<"-1\n";continue;}u64 ord=order(a,p);auto t=linear(u,(*x+ord-v%ord)%ord,ord);if(t)cout<<*t<<'\n';else cout<<"-1\n";}''',
 }[kind]
 return CPP_CORE+'int main(){ios::sync_with_stdio(false);cin.tie(nullptr);'+bodies+'}\n'

LESSONS={91:r'''---
title: "Section 91 — Primality And Integer Factorization"
format: pdf
geometry: margin=1.75cm
---

# Beyond the last sieve cell

This lesson derives A--C. Problem D is editorial-only.

# A. Deterministic Miller--Rabin for 64 bits

For odd `n`, write `n-1 = d * 2^s` with odd `d`. If `n` is prime, Fermat plus repeated squaring forces `a^d` either to be `1`, or to reach `-1` before reaching `1`. A base that violates this is a compositeness witness.

One base only gives a probabilistic statement. For every unsigned 64-bit input, the fixed bases

```text
2, 325, 9375, 28178, 450775, 9780504, 1795265022
```

are a proven deterministic witness set. This is a bounded-domain theorem, not a pattern that may be extended to arbitrary integers.

In C++, multiply residues with unsigned 128-bit arithmetic before reducing. Python integers already expand. Trial-divide a few tiny primes first: it removes edge cases and accelerates common composites.

# B. Pollard--rho factor discovery

Iterate `x <- x*x+c mod n`. Modulo an unknown prime factor, the sequence eventually cycles. Floyd's two-speed pointers make `gcd(|x-y|,n)` reveal a nontrivial shared factor when the two positions first coincide modulo that factor.

The attempt can return `n`; restart with new `c` and seed. A discovered divisor need not be prime. Recursively split both pieces until Miller--Rabin certifies every leaf, then sort. The invariant is multiplicative: the product of values on the work stack and accepted leaves is always the original number.

# C. Multiplicative functions after factorization

From `n = product p^e`, Euler's function is obtained once per distinct prime:

```text
phi(n) = n * product (p-1)/p.
```

Perform `answer = answer/p*(p-1)` in that order, so the intermediate division is exact. This separates two concerns cleanly: randomized factor discovery and deterministic evaluation from the certified prime multiset.

# How to find it

When a bounded sieve is impossible, ask whether the task needs all primes up to a limit or only the factors of a few individual integers. The second shape suggests primality certification plus recursive splitting. Always state the integer domain before selecting witness bases or a multiplication method.

# Exercises

A--C develop the primality/factorization pipeline. D transfers the factor multiset to two new multiplicative statistics.
''',92:r'''---
title: "Section 92 — Discrete Logarithms And Modular Roots"
format: pdf
geometry: margin=1.75cm
---

# Invert exponentiation by exposing group structure

This lesson derives A--C. Problem D is editorial-only.

# A. Primitive roots of a prime

The nonzero residues modulo prime `p` form a cyclic group of order `p-1`. A candidate `g` has full order exactly when

```text
g^((p-1)/q) != 1 mod p
```

for every distinct prime divisor `q` of `p-1`. If its order were proper, it would divide `(p-1)/q` for some missing prime factor; conversely any proper divisor misses one such factor. Factor `p-1`, then test candidates upward to obtain the smallest root.

# B. Baby-step--giant-step

Write an exponent as `x=i*m+j`, with `m` near `sqrt(modulus)`. Store baby powers `a^j`. Walk giant values `b*(a^m)^(-i)` until one matches. The equality is exactly `a^(im+j)=b`. Retaining the first baby index and minimizing candidates returns the smallest exponent.

Time and memory are both `O(sqrt(m))`. This is a meet-in-the-middle algorithm: split one long unknown exponent into two short coordinates.

# C. When the inverse does not exist

If `g=gcd(a,m)>1`, every positive power of `a` is divisible by `g`. Therefore `b` must also be divisible by `g`; otherwise no solution exists. Divide the modulus and target by `g`, record one forced exponent, and update the accumulated scale. Repeat until base and reduced modulus are coprime, then use BSGS on the adjusted target.

Check `x=0` and the accumulated scale at every reduction. Those early solutions are precisely what a careless coprime-only derivation loses.

# Recognition guide

First identify the algebraic domain: a prime-field multiplicative group, a smaller subgroup, or a non-group monoid containing nonunits. Group algorithms require inverses; a gcd reduction is not an optimization but the bridge that makes those inverses legal.

# Exercises

A--C cover group generators, meet-in-the-middle logarithms, and non-coprime reduction. D asks for square roots through the two-adic structure of `p-1`.
''',93:r'''---
title: "Section 93 — Master Computational Number Theory Mixed Contest"
format: pdf
geometry: margin=1.75cm
---

# Contest contract

Six original problems combine the tools of Sections 91--92.

| Problem | Main structure |
|---|---|
| A | certified leaves of Pollard--rho recursion |
| B | prime-power Carmichael values joined by LCM |
| C | factor and reduce a candidate group exponent |
| D | primitive-root coordinates plus a linear congruence |
| E | repeated Tonelli--Shanks queries |
| F | discrete log followed by an affine congruence |

The important habit is to separate layers. First discover or certify the group order. Then translate exponentiation into a congruence. Only after that solve the remaining linear arithmetic.

# Exercises

A--F form the complete mixed contest.
'''}

NOTES={
'prime':('Decompose `n-1` into an odd part and powers of two, then test the deterministic 64-bit witness set.','For prime inputs the strong Fermat chain condition holds for every base. The cited bounded witness theorem guarantees every composite below `2^64` fails at least one selected base.','`O(log n)` modular multiplications per base.'),
'factor':('Use Miller--Rabin as the stopping certificate and Pollard--rho only to split composite work items.','Each split preserves the product invariant. Every accepted leaf is prime, so termination yields exactly a prime factorization; sorting fixes the output order.','Expected roughly `O(n^(1/4))` per difficult factor discovery, with small memory.'),
'totient':('Factor first and apply the prime reduction once per distinct factor.','Inclusion--exclusion over divisibility by the distinct prime factors gives `n product (1-1/p)`.','Expected factorization time plus `O(number of prime factors)`.'),
'divstats':('For each prime power independently choose an exponent from zero through `e`.','Unique factorization makes these choices bijective with divisors. Counts multiply, and distributivity makes the geometric sums multiply.','Expected factorization time.'),
'primitive':('Factor `p-1` and reject a candidate if removing any distinct prime factor from the exponent makes it one.','The order divides `p-1`; it is proper exactly when it divides `(p-1)/q` for some prime divisor `q`.','Factorization plus `O(number tested * omega(p-1) log p)`.'),
'dlog_prime':('Meet baby exponents and giant exponent blocks.','A table match is algebraically equivalent to the target power equation, and every exponent has one such split.','`O(sqrt(p))` time and memory.'),
'dlog_general':('Strip common gcd factors until modular inverses become legal, then run BSGS on the adjusted equation.','Each stripping step is necessary and equivalent after accounting for its forced base factor; the final coprime equation is handled exhaustively by BSGS.','`O(log m + sqrt(m))` expected time and `O(sqrt(m))` memory.'),
'sqrt':('Use Euler classification, split `p-1=q*2^s`, and cancel the two-power discrepancy with a known nonresidue.','Tonelli--Shanks maintains `x squared = a*t` and moves `t` into successively smaller two-power subgroups until `t=1`.','`O(log squared p)` modular operations.'),
'largest':('Factor completely; the sorted final certified leaf is the answer.','Every leaf is prime and their product is the input, so no prime divisor is omitted.','Expected Pollard--rho factorization time.'),
'carmichael':('Compute the exponent of each prime-power unit group, then take their LCM.','CRT decomposes the unit group into prime-power components; an exponent works globally exactly when it is a multiple of every component exponent.','Expected factorization time.'),
'order':('Start from Carmichael lambda and repeatedly divide prime factors while the power remains one.','The true order divides lambda. A division is retained exactly when the smaller candidate is still a multiple of the order.','Two factorizations plus logarithmic exponentiation checks.'),
'powerroot':('Use the smallest primitive root to convert the power equation to `k*y = log_g(a) mod p-1`.','The primitive-root coordinate is bijective on nonzero residues, and the linear-congruence solver returns precisely its smallest exponent solution.','Factorization plus `O(sqrt(p))` time.'),
'sqrt_batch':('Apply Tonelli--Shanks independently and normalize the two roots by taking the smaller.','Every nonzero quadratic residue has exactly the pair `x,p-x`; zero has one root.','`O(q log squared p)` operations.'),
'affine_log':('Take a discrete log inside the subgroup generated by `a`, find its order, then solve the affine exponent congruence modulo that order.','Powers of `a` agree exactly when exponents agree modulo its order, so the final linear congruence is necessary and sufficient.','Factorization plus BSGS per query.')}

SAMPLES={'prime':('4\n1\n2\n561\n1000000007\n','COMPOSITE\nPRIME\nCOMPOSITE\nPRIME\n'),'factor':('3\n1\n60\n1000000016000000063\n','1\n2 2 3 5\n1000000007 1000000009\n'),'totient':('3\n1\n36\n1000000007\n','1\n12\n1000000006\n'),'divstats':('2\n12\n36\n','6 28\n9 91\n'),'primitive':('3\n2\n7\n17\n','1\n3\n3\n'),'dlog_prime':('2\n13 2 8\n7 3 5\n','3\n5\n'),'dlog_general':('3\n2 8 12\n4 2 14\n3 5 7\n','3\n2\n5\n'),'sqrt':('3\n7 2\n7 3\n11 0\n','3 4\nNONE\n0\n'),'largest':('3\n12\n97\n1000000016000000063\n','3\n97\n1000000009\n'),'carmichael':('3\n1\n8\n15\n','1\n2\n4\n'),'order':('2\n2 9\n3 7\n','6\n6\n'),'powerroot':('2\n7 2 2\n7 2 3\n','1\n-1\n'),'sqrt_batch':('7 3\n2\n3\n4\n','3\n-1\n2\n'),'affine_log':('2\n13 2 8 1 0\n13 2 8 2 0\n','3\n-1\n')}
EDGE_CASES={'prime':('3\n18446744073709551557\n18446744073709551615\n18446744073709551556\n','PRIME\nCOMPOSITE\nCOMPOSITE\n'),'factor':('1\n18446744073709551615\n','3 5 17 257 641 65537 6700417\n')}

def format_python(source):
 return ast.unparse(ast.parse(source))+'\n'

def format_cpp(source):
 """Small deterministic layout pass for generated, comment-free C++."""
 lines=[];current='';indent=0;paren=0;quote=None;escaped=False
 def flush():
  nonlocal current
  text=current.strip()
  if text:lines.append('    '*indent+text)
  current=''
 for ch in source:
  if quote:
   current+=ch
   if escaped:escaped=False
   elif ch=='\\':escaped=True
   elif ch==quote:quote=None
   continue
  if ch in ('"',"'"):quote=ch;current+=ch
  elif ch=='(':paren+=1;current+=ch
  elif ch==')':paren-=1;current+=ch
  elif ch=='{' and paren==0:
   current=current.rstrip()+' {';flush();indent+=1
  elif ch=='}' and paren==0:
   flush();indent=max(0,indent-1);current='}';flush()
  elif ch==';' and paren==0:
   current+=';';flush()
  elif ch=='\n':flush()
  else:current+=ch
 flush();return '\n'.join(lines)+'\n'

def editorial(section):
 out=[f'---\ntitle: "Section {section} Editorial — {SECTIONS[section][1]}"\nformat: pdf\ngeometry: margin=1.6cm\nfontsize: 9pt\n---\n']
 for i,(slug,title,kind) in enumerate(PROBLEMS[section]):
  idea,proof,complexity=NOTES[kind]
  out.append(f'''# {chr(65+i)}. {title}\n\n## How to find it\n\n{idea}\n\n## Correctness\n\n{proof}\n\n## Complexity\n\n{complexity}\n\n## C++\n\n```cpp\n{{{{< include problems/{slug}/solution.cpp >}}}}\n```\n\n## Python\n\n```python\n{{{{< include problems/{slug}/solution.py >}}}}\n```\n''')
 return '\n'.join(out)

def generate():
 for section,(directory,title) in SECTIONS.items():
  base=ROOT/'sections'/f'{section:02d}_{directory}';base.mkdir(parents=True,exist_ok=True);(base/'lesson.qmd').write_text(LESSONS[section]);(base/'editorial.qmd').write_text(editorial(section));links=[];checks=[]
  for slug,name,kind in PROBLEMS[section]:
   links.append(f'- [{name}](problems/{slug}/README.md)');checks.append(f'- [ ] [{name}](problems/{slug}/README.md)');p=base/'problems'/slug;p.mkdir(parents=True,exist_ok=True);tests=p/'tests';tests.mkdir(exist_ok=True);(p/'README.md').write_text(f'# {name}\n\n{STATEMENTS[kind]}\n');(p/'solve.cpp').write_text(CPP_STUB);(p/'solve.py').write_text(PY_STUB);(p/'solution.cpp').write_text(format_cpp(cpp_solution(kind)));(p/'solution.py').write_text(format_python(py_solution(kind)));(p/'manifest.json').write_text(json.dumps({'title':name,'checker':'tokens','time_limit_seconds':TIME_LIMITS.get(kind,15)})+'\n');x,y=SAMPLES[kind];(tests/'sample1.in').write_text(x);(tests/'sample1.out').write_text(y)
   if kind in EDGE_CASES:
    x,y=EDGE_CASES[kind];(tests/'edge64.in').write_text(x);(tests/'edge64.out').write_text(y)
   (tests/'random_cases.py').write_text(f'''import subprocess,sys\nfrom pathlib import Path\nROOT=Path(__file__).resolve().parents[5]\nraise SystemExit(subprocess.call([sys.executable,str(ROOT/"tools"/"computational_number_theory_random.py"),"{kind}",*sys.argv[1:]]))\n''')
  note='The lesson derives A--C; D is editorial-only.' if section<93 else 'Exactly six new problems form the mixed contest.';(base/'README.md').write_text(f'# Section {section}: {title}\n\n{note}\n\n## Problems\n\n'+'\n'.join(links)+'\n');(base/'PRACTICE.md').write_text(f'# Section {section} Practice\n\n'+'\n'.join(checks)+'\n');names=',\n        '.join(repr(x[0]) for x in PROBLEMS[section]);(base/'check.py').write_text(f'''from pathlib import Path\nimport sys\nROOT=Path(__file__).resolve().parents[2]\nsys.path.insert(0,str(ROOT))\nfrom tools.section_checker import run_section_checks\nSECTION=Path(__file__).resolve().parent\nPROBLEMS=[SECTION/"problems"/x for x in (\n        {names},\n)]\nif __name__=="__main__":raise SystemExit(run_section_checks({section},PROBLEMS,ROOT))\n''')
if __name__=='__main__':generate()
