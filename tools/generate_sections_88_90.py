"""Generate Sections 88--90: formal power series and transforms."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];MOD=998244353
CPP_STUB='''#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // TODO: solve the problem.
    return 0;
}
''';PY_STUB='''import sys


def main() -> None:
    # TODO: solve the problem.
    pass


if __name__ == "__main__":
    main()
'''
SECTIONS={88:("formal_power_series","Formal Power Series"),89:("polynomial_evaluation_subset_transforms","Polynomial Evaluation And Subset Transforms"),90:("master_polynomial_algebra_mixed","Master Polynomial Algebra Mixed Contest")}
PROBLEMS={88:[("a_series_inverse","Series Inverse","inverse"),("b_series_logarithm","Series Logarithm","log"),("c_series_exponential","Series Exponential","exp"),("d_series_square_root","Series Square Root","sqrt")],89:[("a_multipoint_evaluation","Multipoint Evaluation","evaluate"),("b_polynomial_interpolation","Polynomial Interpolation","interpolate"),("c_xor_convolution","XOR Convolution","xor"),("d_subset_convolution","Subset Convolution","subset")],90:[("a_rational_series","Rational Series","rational"),("b_connected_series","Connected Series","connected"),("c_archive_evaluation","Archive Evaluation","archive_eval"),("d_recover_polynomial","Recover Polynomial","recover"),("e_or_convolution","OR Convolution","orconv"),("f_disjoint_cover_counts","Disjoint Cover Counts","cover") ]}
TIME_LIMITS = {'exp': 45, 'sqrt': 30, 'interpolate': 40, 'recover': 40, 'orconv': 25}
STATEMENTS={
"inverse":"""For polynomial `A(x)` with `A[0] != 0`, print the first `n` coefficients of the unique formal series `B` satisfying `A*B = 1 (mod x^n)`. Modulus is `998244353`; `n <= 200000`.\n\nSample input\n```text\n4\n1 2 0 0\n```\nSample output\n```text\n1 998244351 4 998244345\n```""",
"log":"""Given the first `n` coefficients of `A` with `A[0]=1`, print `log(A) mod x^n` over `998244353`. `n <= 200000`.\n\nSample input\n```text\n4\n1 1 0 0\n```\nSample output\n```text\n0 1 499122176 332748118\n```""",
"exp":"""Given `A[0]=0`, print `exp(A) mod x^n` over `998244353`. `n <= 200000`.\n\nSample input\n```text\n4\n0 1 0 0\n```\nSample output\n```text\n1 1 499122177 166374059\n```""",
"sqrt":"""Given `A[0]=1` and a guarantee that a formal square root with constant coefficient `1` exists, print `B` with `B^2=A (mod x^n)`. `n <= 200000`.\n\nSample input\n```text\n4\n1 2 1 0\n```\nSample output\n```text\n1 1 0 0\n```""",
"evaluate":"""Given a polynomial of degree below `n` and `q` points, evaluate it at all points modulo `998244353`. `n,q <= 200000`.\n\nSample input\n```text\n3 3\n1 2 1\n0 1 2\n```\nSample output\n```text\n1 4 9\n```""",
"interpolate":"""Given `n` distinct points `(x_i,y_i)` modulo `998244353`, recover the unique polynomial of degree below `n`; print coefficients low degree first. `n <= 200000`.\n\nSample input\n```text\n3\n0 1\n1 4\n2 9\n```\nSample output\n```text\n1 2 1\n```""",
"xor":"""Given arrays `a,b` of length `2^k`, print their XOR convolution `c[s]=sum a[x]*b[y]` over pairs with `x XOR y=s`, modulo `998244353`. `k <= 20`.\n\nSample input\n```text\n2\n1 2 3 4\n4 3 2 1\n```\nSample output\n```text\n20 22 28 30\n```""",
"subset":"""Given functions `f,g` on all subsets of a `k`-element universe, print subset convolution `h[S]=sum_{A subset S} f[A]*g[S\\A]` where `A` and `S\\A` are disjoint. `k <= 20`.\n\nSample input\n```text\n2\n1 2 3 4\n5 6 7 8\n```\nSample output\n```text\n5 16 22 60\n```""",
"rational":"""Given numerator `P` and denominator `Q` with `Q[0]!=0`, print the first `n` coefficients of `P/Q`. Inputs provide `n`, then n coefficients of each polynomial. `n <= 200000`.\n\nSample input\n```text\n4\n1 0 0 0\n1 998244352 0 0\n```\nSample output\n```text\n1 1 1 1\n```""",
"connected":"""A formal series `A` with `A[0]=1` counts arbitrary labeled assemblies under the course's ordinary-series encoding. Print the first `n` coefficients of its connected-component series `log(A)`. `n <= 200000`.\n\nSample input\n```text\n3\n1 1 499122177\n```\nSample output\n```text\n0 1 0\n```""",
"archive_eval":"""Evaluate one polynomial at many archive keys modulo `998244353`; keys may repeat. `n,q <= 200000`.\n\nSample input\n```text\n2 4\n3 2\n0 2 2 5\n```\nSample output\n```text\n3 7 7 13\n```""",
"recover":"""Recover coefficients from distinct modular samples, as in interpolation, but points arrive in arbitrary order and may include zero. `n <= 200000`.\n\nSample input\n```text\n2\n3 7\n0 1\n```\nSample output\n```text\n1 2\n```""",
"orconv":"""For arrays indexed by `k`-bit masks, print OR convolution over pairs with `x OR y=s`, modulo `998244353`. `k <= 22`.\n\nSample input\n```text\n1\n1 2\n3 4\n```\nSample output\n```text\n3 18\n```""",
"cover":"""For each mask `S`, count weighted ordered decompositions `S=A disjoint-union B` with contribution `f[A]*g[B]`; print all answers modulo `998244353`. `k <= 20`.\n\nSample input\n```text\n2\n1 2 3 4\n5 6 7 8\n```\nSample output\n```text\n5 16 22 60\n```"""
}

# The reference programs are supplied in both languages.  These limits keep
# the Python implementations useful instead of making them ceremonial.
for key in ("evaluate", "archive_eval"):
    STATEMENTS[key] = STATEMENTS[key].replace("n,q <= 200000", "n,q <= 50000")
for key in ("interpolate", "recover"):
    STATEMENTS[key] = STATEMENTS[key].replace("n <= 200000", "n <= 50000")
for key in ("subset", "cover"):
    STATEMENTS[key] = STATEMENTS[key].replace("k <= 20", "k <= 16")

PY_CORE=r'''import sys
MOD=998244353
ROOT=3
def ntt(a,invert):
 n=len(a);j=0
 for i in range(1,n):
  bit=n>>1
  while j&bit:j^=bit;bit>>=1
  j^=bit
  if i<j:a[i],a[j]=a[j],a[i]
 length=2
 while length<=n:
  wlen=pow(ROOT,(MOD-1)//length,MOD)
  if invert:wlen=pow(wlen,MOD-2,MOD)
  half=length>>1
  for i in range(0,n,length):
   w=1
   for j in range(i,i+half):
    u=a[j];v=a[j+half]*w%MOD
    a[j]=(u+v)%MOD;a[j+half]=(u-v)%MOD;w=w*wlen%MOD
  length<<=1
 if invert:
  z=pow(n,MOD-2,MOD)
  for i in range(n):a[i]=a[i]*z%MOD
def conv(a,b,need=None):
 if not a or not b:return []
 total=len(a)+len(b)-1
 if min(len(a),len(b))<32:
  c=[0]*total
  for i,x in enumerate(a):
   for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%MOD
 else:
  size=1
  while size<total:size<<=1
  x=a+[0]*(size-len(a));y=b+[0]*(size-len(b));ntt(x,False);ntt(y,False)
  for i in range(size):x[i]=x[i]*y[i]%MOD
  ntt(x,True);c=x[:total]
 return c if need is None else c[:need]
def fps_inv(a,n):
 g=[pow(a[0],MOD-2,MOD)];size=1
 while size<n:
  size=min(size<<1,n);ag=conv(a[:size],g,size);ag += [0]*(size-len(ag));ag[0]=(2-ag[0])%MOD
  for i in range(1,size):ag[i]=(-ag[i])%MOD
  g=conv(g,ag,size);g += [0]*(size-len(g))
 return g[:n]
def derivative(a):return [i*a[i]%MOD for i in range(1,len(a))]
def integral(a):
 n=len(a)+1;inv=[0]*n
 if n>1:inv[1]=1
 for i in range(2,n):inv[i]=(MOD-(MOD//i)*inv[MOD%i])%MOD
 return [0]+[a[i-1]*inv[i]%MOD for i in range(1,n)]
def fps_log(a,n):
 r=integral(conv(derivative(a),fps_inv(a,n),n-1));return (r+[0]*n)[:n]
def fps_exp(a,n):
 g=[1];size=1
 while size<n:
  size=min(size<<1,n);lg=fps_log(g,size);delta=(a[:size]+[0]*size)[:size]
  for i in range(size):delta[i]=(delta[i]-lg[i])%MOD
  delta[0]=(delta[0]+1)%MOD;g=conv(g,delta,size);g += [0]*(size-len(g))
 return g[:n]
def fps_sqrt(a,n):
 g=[1];size=1;half=(MOD+1)//2
 while size<n:
  size=min(size<<1,n);q=conv(a[:size],fps_inv(g,size),size);q += [0]*(size-len(q));g += [0]*(size-len(g))
  g=[(g[i]+q[i])*half%MOD for i in range(size)]
 return g[:n]
def poly_mod(a,b):
 while a and a[-1]==0:a.pop()
 while b and b[-1]==0:b.pop()
 if len(a)<len(b):return a
 qn=len(a)-len(b)+1;q=conv(a[::-1][:qn],fps_inv(b[::-1],qn),qn)[::-1]
 prod=conv(q,b,len(a));r=[(a[i]-(prod[i] if i<len(prod) else 0))%MOD for i in range(len(b)-1)]
 while r and r[-1]==0:r.pop()
 return r
def product_tree(xs):
 size=1
 while size<len(xs):size<<=1
 tree=[[1] for _ in range(2*size)]
 for i,x in enumerate(xs):tree[size+i]=[(-x)%MOD,1]
 for i in range(size-1,0,-1):tree[i]=conv(tree[i<<1],tree[i<<1|1])
 return tree,size
def evaluate(a,xs,tree=None,size=None):
 if not xs:return []
 if tree is None:tree,size=product_tree(xs)
 ans=[0]*len(xs);stack=[(1,poly_mod(a[:],tree[1]))]
 while stack:
  v,r=stack.pop()
  if v>=size:
   i=v-size
   if i<len(xs):ans[i]=r[0] if r else 0
  else:
   stack.append((v<<1,poly_mod(r[:],tree[v<<1])));stack.append((v<<1|1,poly_mod(r[:],tree[v<<1|1])))
 return ans
def interpolate(xs,ys):
 tree,size=product_tree(xs);values=evaluate(derivative(tree[1]),xs,tree,size);work=[[0] for _ in range(2*size)]
 for i in range(len(xs)):work[size+i]=[ys[i]*pow(values[i],MOD-2,MOD)%MOD]
 for v in range(size-1,0,-1):
  work[v]=conv(work[v<<1],tree[v<<1|1]);other=conv(work[v<<1|1],tree[v<<1])
  if len(work[v])<len(other):work[v]+=[0]*(len(other)-len(work[v]))
  for i,x in enumerate(other):work[v][i]=(work[v][i]+x)%MOD
 return (work[1]+[0]*len(xs))[:len(xs)]
def fwt(a,kind,invert=False):
 n=len(a);length=1
 while length<n:
  for mask in range(n):
   if mask&length:
    if kind=='or':a[mask]=(a[mask]-a[mask^length])%MOD if invert else (a[mask]+a[mask^length])%MOD
    else:
     u=a[mask^length];v=a[mask];a[mask^length]=(u+v)%MOD;a[mask]=(u-v)%MOD
  length<<=1
 if kind=='xor' and invert:
  z=pow(n,MOD-2,MOD)
  for i in range(n):a[i]=a[i]*z%MOD
def subset_conv(f,g,k):
 n=1<<k;F=[[0]*n for _ in range(k+1)];G=[[0]*n for _ in range(k+1)]
 for s in range(n):c=s.bit_count();F[c][s]=f[s];G[c][s]=g[s]
 for bit in range(k):
  step=1<<bit
  for s in range(n):
   if s&step:
    t=s^step
    for c in range(k+1):F[c][s]=(F[c][s]+F[c][t])%MOD;G[c][s]=(G[c][s]+G[c][t])%MOD
 H=[[0]*n for _ in range(k+1)]
 for s in range(n):
  for c in range(k+1):H[c][s]=sum(F[i][s]*G[c-i][s] for i in range(c+1))%MOD
 for bit in range(k):
  step=1<<bit
  for s in range(n):
   if s&step:
    t=s^step
    for c in range(k+1):H[c][s]=(H[c][s]-H[c][t])%MOD
 return [H[s.bit_count()][s] for s in range(n)]
'''

def py_main(kind):
 if kind in ('inverse','log','exp','sqrt','connected'):
  fn={'inverse':'fps_inv(a,n)','log':'fps_log(a,n)','exp':'fps_exp(a,n)','sqrt':'fps_sqrt(a,n)','connected':'fps_log(a,n)'}[kind]
  return PY_CORE+f"""def main():
 d=list(map(int,sys.stdin.buffer.read().split()));n=d[0];a=d[1:1+n];print(*{fn})
if __name__=='__main__':main()
"""
 if kind=='rational':
  return PY_CORE+"""def main():
 d=list(map(int,sys.stdin.buffer.read().split()));n=d[0];p=d[1:1+n];q=d[1+n:1+2*n];ans=conv(p,fps_inv(q,n),n);print(*(ans+[0]*n)[:n])
if __name__=='__main__':main()
"""
 if kind in ('evaluate','archive_eval'):
  return PY_CORE+"""def main():
 d=list(map(int,sys.stdin.buffer.read().split()));n,q=d[:2];a=d[2:2+n];xs=d[2+n:2+n+q];print(*evaluate(a,xs))
if __name__=='__main__':main()
"""
 if kind in ('interpolate','recover'):
  return PY_CORE+"""def main():
 d=list(map(int,sys.stdin.buffer.read().split()));n=d[0];xs=d[1::2];ys=d[2::2];print(*interpolate(xs,ys))
if __name__=='__main__':main()
"""
 if kind=='orconv':
  return PY_CORE+"""from array import array
def main():
 d=array('I',map(int,sys.stdin.buffer.read().split()));k=d[0];n=1<<k;a=d[1:1+n];b=d[1+n:1+2*n];del d
 fwt(a,'or');fwt(b,'or');c=array('I',(a[i]*b[i]%MOD for i in range(n)));del a,b;fwt(c,'or',True)
 write=sys.stdout.write
 for start in range(0,n,16384):
  if start:write(' ')
  write(' '.join(map(str,c[start:start+16384])))
 write('\\n')
if __name__=='__main__':main()
"""
 if kind=='xor':
  name='xor'
  return PY_CORE+f"""def main():
 d=list(map(int,sys.stdin.buffer.read().split()));k=d[0];n=1<<k;a=d[1:1+n];b=d[1+n:1+2*n];fwt(a,'{name}');fwt(b,'{name}');c=[a[i]*b[i]%MOD for i in range(n)];fwt(c,'{name}',True);print(*c)
if __name__=='__main__':main()
"""
 return PY_CORE+"""def main():
 d=list(map(int,sys.stdin.buffer.read().split()));k=d[0];n=1<<k;f=d[1:1+n];g=d[1+n:1+2*n];print(*subset_conv(f,g,k))
if __name__=='__main__':main()
"""

CPP_CORE=r'''#include <bits/stdc++.h>
using namespace std; using ll=long long;
const int MOD=998244353,G=3;
int power(int a,int e){ll r=1;for(;e;e>>=1,a=(ll)a*a%MOD)if(e&1)r=r*a%MOD;return r;}
void ntt(vector<int>&a,bool inv){int n=a.size();for(int i=1,j=0;i<n;i++){int b=n>>1;for(;j&b;b>>=1)j^=b;j^=b;if(i<j)swap(a[i],a[j]);}for(int len=2;len<=n;len<<=1){int wlen=power(G,(MOD-1)/len);if(inv)wlen=power(wlen,MOD-2);for(int i=0;i<n;i+=len){ll w=1;for(int j=0;j<len/2;j++){int u=a[i+j],v=w*a[i+j+len/2]%MOD;a[i+j]=u+v;if(a[i+j]>=MOD)a[i+j]-=MOD;a[i+j+len/2]=u-v;if(a[i+j+len/2]<0)a[i+j+len/2]+=MOD;w=w*wlen%MOD;}}}if(inv){ll z=power(n,MOD-2);for(int&x:a)x=x*z%MOD;}}
vector<int> conv(vector<int>a,vector<int>b,int need=-1){if(a.empty()||b.empty())return{};int total=a.size()+b.size()-1;if(min(a.size(),b.size())<32){vector<int>c(total);for(int i=0;i<(int)a.size();i++)for(int j=0;j<(int)b.size();j++)c[i+j]=(c[i+j]+(ll)a[i]*b[j])%MOD;if(need>=0&&need<(int)c.size())c.resize(need);return c;}int n=1;while(n<total)n<<=1;a.resize(n);b.resize(n);ntt(a,0);ntt(b,0);for(int i=0;i<n;i++)a[i]=(ll)a[i]*b[i]%MOD;ntt(a,1);a.resize(need>=0?min(need,total):total);return a;}
vector<int> inverse(const vector<int>&a,int n){vector<int>r(1,power(a[0],MOD-2));for(int sz=2;sz/2<n;sz<<=1){int take=min(sz,n);vector<int>f(a.begin(),a.begin()+min((int)a.size(),take));auto t=conv(f,r,take);t.resize(take);t[0]=(2-t[0]+MOD)%MOD;for(int i=1;i<take;i++)if(t[i])t[i]=MOD-t[i];r=conv(r,t,take);r.resize(take);}r.resize(n);return r;}
vector<int> derivative(const vector<int>&a){vector<int>d(max(0,(int)a.size()-1));for(int i=1;i<(int)a.size();i++)d[i-1]=(ll)i*a[i]%MOD;return d;}
vector<int> integrate(const vector<int>&a){vector<int>r(a.size()+1),iv(a.size()+1);if(a.size())iv[1]=1;for(int i=2;i<(int)iv.size();i++)iv[i]=MOD-(ll)(MOD/i)*iv[MOD%i]%MOD;for(int i=1;i<(int)r.size();i++)r[i]=(ll)a[i-1]*iv[i]%MOD;return r;}
vector<int> logarithm(const vector<int>&a,int n){auto r=integrate(conv(derivative(a),inverse(a,n),n-1));r.resize(n);return r;}
vector<int> exponential(const vector<int>&a,int n){vector<int>r(1,1);for(int sz=2;sz/2<n;sz<<=1){int take=min(sz,n);auto lg=logarithm(r,take);vector<int>d(take);for(int i=0;i<take;i++)d[i]=((i<(int)a.size()?a[i]:0)-lg[i]+MOD)%MOD;d[0]++;if(d[0]>=MOD)d[0]-=MOD;r=conv(r,d,take);r.resize(take);}r.resize(n);return r;}
vector<int> square_root(const vector<int>&a,int n){vector<int>r(1,1);int half=(MOD+1)/2;for(int sz=2;sz/2<n;sz<<=1){int take=min(sz,n);vector<int>f(a.begin(),a.begin()+min((int)a.size(),take));auto q=conv(f,inverse(r,take),take);q.resize(take);r.resize(take);for(int i=0;i<take;i++)r[i]=(ll)(r[i]+q[i])*half%MOD;}r.resize(n);return r;}
void trim(vector<int>&a){while(!a.empty()&&a.back()==0)a.pop_back();}
vector<int> poly_mod(vector<int>a,vector<int>b){trim(a);trim(b);if(a.size()<b.size())return a;vector<int>orig=a;int qn=a.size()-b.size()+1;reverse(a.begin(),a.end());reverse(b.begin(),b.end());a.resize(qn);auto q=conv(a,inverse(b,qn),qn);reverse(q.begin(),q.end());reverse(b.begin(),b.end());auto p=conv(q,b);vector<int>r(b.size()-1);for(int i=0;i<(int)r.size();i++)r[i]=(orig[i]-(i<(int)p.size()?p[i]:0)+MOD)%MOD;trim(r);return r;}
struct ProductTree{int n,size;vector<int>x;vector<vector<int>>t;ProductTree(vector<int>xs):n(xs.size()),x(move(xs)){size=1;while(size<n)size<<=1;t.assign(2*size,{1});for(int i=0;i<n;i++)t[size+i]={x[i]?MOD-x[i]:0,1};for(int i=size-1;i;i--)t[i]=conv(t[i<<1],t[i<<1|1]);}
 vector<int> eval(const vector<int>&a){vector<int>ans(n);function<void(int,vector<int>)>go=[&](int v,vector<int>r){if(v>=size){int i=v-size;if(i<n)ans[i]=r.empty()?0:r[0];return;}go(v<<1,poly_mod(r,t[v<<1]));go(v<<1|1,poly_mod(r,t[v<<1|1]));};go(1,poly_mod(a,t[1]));return ans;}
 vector<int> interp(const vector<int>&y){auto val=eval(derivative(t[1]));vector<vector<int>>w(2*size,vector<int>{0});for(int i=0;i<n;i++)w[size+i]={(int)((ll)y[i]*power(val[i],MOD-2)%MOD)};for(int v=size-1;v;v--){w[v]=conv(w[v<<1],t[v<<1|1]);auto z=conv(w[v<<1|1],t[v<<1]);w[v].resize(max(w[v].size(),z.size()));for(int i=0;i<(int)z.size();i++){w[v][i]+=z[i];if(w[v][i]>=MOD)w[v][i]-=MOD;}}w[1].resize(n);return w[1];}};
void fwt(vector<int>&a,string kind,bool inv=false){int n=a.size();for(int bit=1;bit<n;bit<<=1)for(int s=0;s<n;s++)if(s&bit){if(kind=="or"){a[s]=(a[s]+(inv?MOD-a[s^bit]:a[s^bit]))%MOD;}else{int u=a[s^bit],v=a[s];a[s^bit]=u+v;if(a[s^bit]>=MOD)a[s^bit]-=MOD;a[s]=u-v;if(a[s]<0)a[s]+=MOD;}}if(kind=="xor"&&inv){ll z=power(n,MOD-2);for(int&v:a)v=v*z%MOD;}}
vector<int> subset_conv(const vector<int>&f,const vector<int>&g,int k){int n=1<<k;vector<vector<int>>F(k+1,vector<int>(n)),H=F,Gv=F;for(int s=0;s<n;s++){int c=__builtin_popcount(s);F[c][s]=f[s];Gv[c][s]=g[s];}for(int bit=0;bit<k;bit++)for(int s=0;s<n;s++)if(s>>bit&1)for(int c=0;c<=k;c++){F[c][s]+=F[c][s^(1<<bit)];if(F[c][s]>=MOD)F[c][s]-=MOD;Gv[c][s]+=Gv[c][s^(1<<bit)];if(Gv[c][s]>=MOD)Gv[c][s]-=MOD;}for(int s=0;s<n;s++)for(int c=0;c<=k;c++)for(int i=0;i<=c;i++)H[c][s]=(H[c][s]+(ll)F[i][s]*Gv[c-i][s])%MOD;for(int bit=0;bit<k;bit++)for(int s=0;s<n;s++)if(s>>bit&1)for(int c=0;c<=k;c++){H[c][s]-=H[c][s^(1<<bit)];if(H[c][s]<0)H[c][s]+=MOD;}vector<int>ans(n);for(int s=0;s<n;s++)ans[s]=H[__builtin_popcount(s)][s];return ans;}
void print(const vector<int>&a){for(int i=0;i<(int)a.size();i++)cout<<a[i]<<" \n"[i+1==(int)a.size()];}
'''

def cpp_main(kind):
 if kind in ('inverse','log','exp','sqrt','connected'):
  fn={'inverse':'inverse(a,n)','log':'logarithm(a,n)','exp':'exponential(a,n)','sqrt':'square_root(a,n)','connected':'logarithm(a,n)'}[kind]
  return CPP_CORE+f'''int main(){{ios::sync_with_stdio(false);cin.tie(nullptr);int n;cin>>n;vector<int>a(n);for(int&x:a)cin>>x;print({fn});}}
'''
 if kind=='rational':return CPP_CORE+'''int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;cin>>n;vector<int>p(n),q(n);for(int&x:p)cin>>x;for(int&x:q)cin>>x;auto a=conv(p,inverse(q,n),n);a.resize(n);print(a);}
'''
 if kind in ('evaluate','archive_eval'):return CPP_CORE+'''int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,q;cin>>n>>q;vector<int>a(n),x(q);for(int&v:a)cin>>v;for(int&v:x)cin>>v;ProductTree tree(x);print(tree.eval(a));}
'''
 if kind in ('interpolate','recover'):return CPP_CORE+'''int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;cin>>n;vector<int>x(n),y(n);for(int i=0;i<n;i++)cin>>x[i]>>y[i];ProductTree tree(x);print(tree.interp(y));}
'''
 if kind in ('xor','orconv'):
  name='xor' if kind=='xor' else 'or'
  return CPP_CORE+f'''int main(){{ios::sync_with_stdio(false);cin.tie(nullptr);int k;cin>>k;int n=1<<k;vector<int>a(n),b(n);for(int&x:a)cin>>x;for(int&x:b)cin>>x;fwt(a,"{name}");fwt(b,"{name}");for(int i=0;i<n;i++)a[i]=(ll)a[i]*b[i]%MOD;fwt(a,"{name}",true);print(a);}}
'''
 return CPP_CORE+'''int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int k;cin>>k;int n=1<<k;vector<int>a(n),b(n);for(int&x:a)cin>>x;for(int&x:b)cin>>x;print(subset_conv(a,b,k));}
'''

LESSONS={
88:r'''---
title: "Section 88 — Formal Power Series"
format: pdf
geometry: margin=1.75cm
---

# Polynomials as locally determined infinite objects

This lesson derives Problems A--C. Problem D is deliberately left for the editorial.

A formal power series is a coefficient sequence. Equality modulo `x^n` means that the first `n` coefficients agree; convergence and numerical approximation play no role. The modulus `998244353 = 119 * 2^23 + 1` supplies the roots of unity needed by NTT, so a product of length `n` costs `M(n) = O(n log n)`.

# A. Inverse: lift twice as many correct coefficients

Suppose `A G = 1 mod x^m`. Write the error as `E = 1-A G`; its first `m` coefficients vanish. Newton's update is

```text
G' = G * (2 - A*G).
```

Then `1-A G' = (1-A G)^2 = E^2`, whose first `2m` coefficients vanish. Truncate every temporary polynomial to the precision currently requested. Starting from `G[0] = inverse(A[0])`, doubling gives the answer in `O(M(n))`, because the geometric sum `M(1)+M(2)+...+M(n)` is `O(M(n))`.

# B. Logarithm: turn multiplication into addition

The formal derivative obeys the familiar product rule, so

```text
log(A)' = A' / A.
log(A)  = integral(A' * inverse(A)).
```

The constant is fixed to zero, which is why the input requires `A[0]=1`. Integration divides coefficient `i-1` by `i`; all needed integers are invertible because `n < MOD`. This pattern is useful whenever a combinatorial construction turns products into sums of connected components.

# C. Exponential: Newton on `log(G)=A`

Assume `log(G)=A mod x^m`. Correct it with

```text
G' = G * (1 - log(G) + A).
```

The parenthesis has constant coefficient one and cancels the known logarithmic error. A formal expansion shows the new error starts at degree `2m`. Begin with `G=1`, forced by `A[0]=0`, and double precision.

# How to recognize the method

First write the algebraic identity defining the unknown series. Ask whether its constant term determines a base coefficient. Next obtain a correction whose error is squared; that is the Newton signal. Finally audit every truncation: coefficients at degree at least `n` can never influence a result below degree `n`.

# Exercises

A--C build inverse, logarithm, and exponential. D asks you to transfer the same correction idea to a square root.
''',
89:r'''---
title: "Section 89 — Polynomial Evaluation And Subset Transforms"
format: pdf
geometry: margin=1.75cm
---

# Change representation until the operation is pointwise

This lesson derives Problems A--C. Problem D is editorial-only.

# A. Multipoint evaluation

For one point, Horner is linear; repeating it is quadratic. Build a product tree whose leaf `i` is `x-X_i` and whose internal polynomial is the product of its children. At a node, replace `P` by its remainder modulo the node polynomial. Both children need only the remainder modulo their own product. At a leaf the remainder is the scalar `P(X_i)`.

Fast polynomial division reverses dividend and divisor, computes a truncated series inverse, recovers the quotient, then subtracts. Across one tree level the total polynomial size is linear, so the complete algorithm costs `O(M(n) log n)`.

# B. Interpolation is the transposed product tree

Let `M(x)` be the product of all `(x-X_i)`. The Lagrange weight is

```text
w_i = Y_i / M'(X_i).
```

Distinct points ensure the denominator is nonzero. Put `w_i` at leaves. At each internal node combine

```text
left_value * right_product + right_value * left_product.
```

Induction says this is the sum of every leaf weight times all factors except its own. At the root it is exactly the interpolating polynomial.

# C. XOR convolution

The Walsh--Hadamard transform uses butterflies `(u,v) -> (u+v,u-v)`. A bit independently records whether two input bits agree or differ, so XOR convolution becomes pointwise multiplication in transformed coordinates. Applying the same butterflies again yields `n` times the input; multiply by `inverse(n)` to invert.

# A unifying question

Convolution is difficult in the original basis because outputs mix many input pairs. Search for a representation where the operation is coordinatewise: values at roots for ordinary multiplication, Walsh characters for XOR, and subset-zeta ranks for disjoint union.

# Exercises

A--C cover product trees, interpolation, and XOR transforms. D introduces ranked subset convolution without advance exposure.
''',
90:r'''---
title: "Section 90 — Master Polynomial Algebra Mixed Contest"
format: pdf
geometry: margin=1.75cm
---

# Contest contract

Six new problems combine the polynomial and transform tools of Sections 88--89.

| Problem | Main decision |
|---|---|
| A | division as multiplication by a formal inverse |
| B | logarithm extracts connected components |
| C | product-tree evaluation with repeated queries |
| D | interpolation in arbitrary input order |
| E | OR zeta transform and Möbius inversion |
| F | rank-refined subset convolution |

Do not choose a transform merely because masks or polynomials appear. State the binary operation that combines indices, then choose the transform whose characters diagonalize that operation.

# Exercises

A--F form the complete mixed contest; all are new and self-contained.
'''}

NOTES={
'inverse':('Treat the unknown coefficients as the inverse of a series and double the known precision with Newton iteration.','If `E=1-AG` vanishes below degree `m`, the update makes the new error `E^2`, which vanishes below degree `2m`.','`O(M(n))` time and `O(n)` auxiliary storage.'),
'log':('Differentiate first: the difficult operation becomes `A prime` multiplied by the already-solved inverse of `A`.','The derivative of the constructed answer equals `A prime / A`; its chosen zero constant therefore makes it the unique formal logarithm.','`O(M(n))` time and `O(n)` storage.'),
'exp':('Solve `log(G)=A` by Newton correction, doubling precision at each step.','With an error beginning at degree `m`, multiplying by `1-log(G)+A` cancels its linear part; all remaining error has degree at least `2m`.','`O(M(n))` time and `O(n)` storage.'),
'sqrt':('Apply Newton to `G squared-A=0`: average `G` with `A/G`.','Writing `G=B+e` shows the update cancels `e` and leaves only terms quadratic in `e`, hence doubles correct precision. The required constant selects the branch.','`O(M(n))` time and `O(n)` storage.'),
'evaluate':('Organize all moduli `x-X_i` in a product tree and propagate remainders.','Remainder transitivity makes each child remainder congruent to the original polynomial modulo its subtree product; at a leaf its constant is exactly the requested value.','`O(M(n+q) log q)` time and `O((n+q) log q)` aggregate polynomial storage.'),
'archive_eval':('Use one product tree; repeated keys need no special case because evaluation, unlike interpolation, permits repeated leaves.','Each leaf still receives the polynomial modulo `x-X_i`, so duplicates independently obtain the same correct value.','`O(M(n+q) log q)` time.'),
'interpolate':('Evaluate the derivative of the root product, form Lagrange weights, and merge them upward.','The root expansion is the Lagrange formula. It matches every sample value and has degree below `n`, so uniqueness proves equality.','`O(M(n) log n)` time.'),
'recover':('Input order is irrelevant: pair each ordinate with its own leaf and use the product-tree Lagrange construction.','At `X_i`, every other basis term contains `X_i-X_i`, while its own term evaluates to one.','`O(M(n) log n)` time.'),
'xor':('Use Walsh--Hadamard butterflies because XOR is addition in the vector space of bits.','Each Walsh character turns XOR into multiplication; inversion restores coefficients after pointwise products.','`O(k 2^k)` time and `O(2^k)` storage.'),
'orconv':('Use subset zeta transform: a transformed coordinate sums all submasks.','Multiplying two zeta sums counts exactly pairs whose OR is a submask; Möbius subtraction isolates pairs with OR equal to each mask.','`O(k 2^k)` time and `O(2^k)` storage.'),
'subset':('Separate values by popcount, zeta-transform every rank, convolve ranks, then Möbius-invert.','Rank equality removes overlapping pairs: if ranks add to `|S|` and both sets lie in `S`, their union is `S` exactly when they are disjoint.','`O(k squared 2^k)` time and `O(k 2^k)` storage.'),
'cover':('This is subset convolution under a story name; use ranked zeta transforms.','The rank filter and Möbius inversion leave precisely ordered disjoint pairs whose union is the output mask.','`O(k squared 2^k)` time and `O(k 2^k)` storage.'),
'rational':('Compute `Q` inverse to precision `n`, then multiply by `P` and truncate.','Multiplying the output by `Q` gives `P` modulo `x^n` by the inverse invariant, which uniquely determines the quotient prefix.','`O(M(n))` time and `O(n)` storage.'),
'connected':('The assembly product becomes an additive connected-component series under formal logarithm.','The requested encoding defines the connected series as the unique zero-constant series whose exponential is `A`; formal log is its inverse.','`O(M(n))` time and `O(n)` storage.')}

def editorial(section):
 out=[f'''---\ntitle: "Section {section} Editorial — {SECTIONS[section][1]}"\nformat: pdf\ngeometry: margin=1.55cm\nfontsize: 8.5pt\n---\n''']
 for i,(slug,title,kind) in enumerate(PROBLEMS[section]):
  idea,proof,complexity=NOTES[kind]
  out.append(f'''# {chr(65+i)}. {title}\n\n## How to find it\n\n{idea}\n\n## Correctness\n\n{proof}\n\n## Complexity\n\n{complexity}\n\n## C++\n\n```cpp\n{{{{< include problems/{slug}/solution.cpp >}}}}\n```\n\n## Python\n\n```python\n{{{{< include problems/{slug}/solution.py >}}}}\n```\n''')
 return '\n'.join(out)

SAMPLES={
'inverse':('4\n1 2 0 0\n','1 998244351 4 998244345\n'),'log':('4\n1 1 0 0\n','0 1 499122176 332748118\n'),'exp':('4\n0 1 0 0\n','1 1 499122177 166374059\n'),'sqrt':('4\n1 2 1 0\n','1 1 0 0\n'),'evaluate':('3 3\n1 2 1\n0 1 2\n','1 4 9\n'),'interpolate':('3\n0 1\n1 4\n2 9\n','1 2 1\n'),'xor':('2\n1 2 3 4\n4 3 2 1\n','20 22 28 30\n'),'subset':('2\n1 2 3 4\n5 6 7 8\n','5 16 22 60\n'),'rational':('4\n1 0 0 0\n1 998244352 0 0\n','1 1 1 1\n'),'connected':('3\n1 1 499122177\n','0 1 0\n'),'archive_eval':('2 4\n3 2\n0 2 2 5\n','3 7 7 13\n'),'recover':('2\n3 7\n0 1\n','1 2\n'),'orconv':('1\n1 2\n3 4\n','3 18\n'),'cover':('2\n1 2 3 4\n5 6 7 8\n','5 16 22 60\n')}

def generate():
 for section,(directory,title) in SECTIONS.items():
  base=ROOT/'sections'/f'{section:02d}_{directory}';base.mkdir(parents=True,exist_ok=True)
  (base/'lesson.qmd').write_text(LESSONS[section]);(base/'editorial.qmd').write_text(editorial(section));links=[];checks=[]
  for slug,name,kind in PROBLEMS[section]:
   links.append(f'- [{name}](problems/{slug}/README.md)');checks.append(f'- [ ] [{name}](problems/{slug}/README.md)');p=base/'problems'/slug;p.mkdir(parents=True,exist_ok=True);tests=p/'tests';tests.mkdir(exist_ok=True)
   limit=TIME_LIMITS.get(kind,15)
   (p/'README.md').write_text(f'# {name}\n\n{STATEMENTS[kind]}\n');(p/'solve.cpp').write_text(CPP_STUB);(p/'solve.py').write_text(PY_STUB);(p/'solution.cpp').write_text(cpp_main(kind));(p/'solution.py').write_text(py_main(kind));(p/'manifest.json').write_text(json.dumps({'title':name,'checker':'tokens','time_limit_seconds':limit})+'\n');sample_in,sample_out=SAMPLES[kind];(tests/'sample1.in').write_text(sample_in);(tests/'sample1.out').write_text(sample_out)
   (tests/'random_cases.py').write_text(f'''import subprocess,sys\nfrom pathlib import Path\nROOT=Path(__file__).resolve().parents[5]\nraise SystemExit(subprocess.call([sys.executable,str(ROOT/"tools"/"polynomial_algebra_random.py"),"{kind}",*sys.argv[1:]]))\n''')
  note='The lesson derives A--C; D is explained only in the editorial.' if section<90 else 'Exactly six new problems form the mixed contest.'
  (base/'README.md').write_text(f'# Section {section}: {title}\n\n{note}\n\n## Problems\n\n'+'\n'.join(links)+'\n');(base/'PRACTICE.md').write_text(f'# Section {section} Practice\n\n'+'\n'.join(checks)+'\n');names=',\n        '.join(repr(x[0]) for x in PROBLEMS[section])
  (base/'check.py').write_text(f'''from pathlib import Path\nimport sys\nROOT=Path(__file__).resolve().parents[2]\nsys.path.insert(0,str(ROOT))\nfrom tools.section_checker import run_section_checks\nSECTION=Path(__file__).resolve().parent\nPROBLEMS=[SECTION/"problems"/x for x in (\n        {names},\n)]\nif __name__=="__main__":raise SystemExit(run_section_checks({section},PROBLEMS,ROOT))\n''')
if __name__=='__main__':generate()
