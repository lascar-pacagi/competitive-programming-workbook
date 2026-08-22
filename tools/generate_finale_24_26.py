"""Generate Section 100 problems 24--26."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT/'sections/100_grandmaster_finale/problems'
SC='#include <bits/stdc++.h>\nusing namespace std;\nint main(){ios::sync_with_stdio(false);cin.tie(nullptr);/* TODO */}\n';SP='def main(): pass  # TODO\nif __name__=="__main__":main()\n'

R24=r'''# Lexicographic Substring Laboratory

For query `(l,r,k)`, consider the suffixes of `s` starting at positions
`l..r`, sorted lexicographically. Print the starting position of the `k`-th
suffix and its LCP with the next suffix in that restricted order. For the last
suffix print LCP `0`.

## Input
```text
s
q
q lines: l r k
```
Lowercase `s`; `1 <= |s|,q <= 200000`; `1 <= l <= r <= |s|`, `1 <= k <= r-l+1`.

## Sample input
```text
banana
3
1 6 2
2 5 2
3 3 1
```
## Sample output
```text
4 3
2 0
3 0
```
'''
C24=r'''#include <bits/stdc++.h>
using namespace std;struct N{int l=0,r=0,z=0;};int main(){ios::sync_with_stdio(false);cin.tie(nullptr);string s;if(!(cin>>s))return 0;int n=s.size();vector<int>sa(n),rk(n),nr(n);iota(sa.begin(),sa.end(),0);for(int i=0;i<n;i++)rk[i]=s[i];for(int k=1;;k*=2){sort(sa.begin(),sa.end(),[&](int a,int b){return pair(rk[a],a+k<n?rk[a+k]:-1)<pair(rk[b],b+k<n?rk[b+k]:-1);});nr[sa[0]]=0;for(int i=1;i<n;i++)nr[sa[i]]=nr[sa[i-1]]+(pair(rk[sa[i-1]],sa[i-1]+k<n?rk[sa[i-1]+k]:-1)<pair(rk[sa[i]],sa[i]+k<n?rk[sa[i]+k]:-1));rk=nr;if(rk[sa.back()]==n-1)break;}vector<int>h(n);for(int i=0,k=0;i<n;i++){int x=rk[i];if(!x)continue;int j=sa[x-1];while(i+k<n&&j+k<n&&s[i+k]==s[j+k])k++;h[x]=k;if(k)k--;}int K=1;while((1<<K)<=n)K++;vector<vector<int>>st(K,vector<int>(n));st[0]=h;for(int z=1;z<K;z++)for(int i=0;i+(1<<z)<=n;i++)st[z][i]=min(st[z-1][i],st[z-1][i+(1<<(z-1))]);auto lcp=[&](int a,int b){if(a==b)return n-sa[a];if(a>b)swap(a,b);a++;int z=31-__builtin_clz(b-a+1);return min(st[z][a],st[z][b-(1<<z)+1]);};vector<N>tr(1);function<int(int,int,int,int)>add=[&](int o,int l,int r,int x){int u=tr.size();tr.push_back(tr[o]);tr[u].z++;if(l<r){int m=(l+r)/2;if(x<=m)tr[u].l=add(tr[o].l,l,m,x);else tr[u].r=add(tr[o].r,m+1,r,x);}return u;};vector<int>root(n+1);for(int i=0;i<n;i++)root[i+1]=add(root[i],0,n-1,rk[i]);function<int(int,int,int,int,int)>kth=[&](int a,int b,int l,int r,int k){if(l==r)return l;int z=tr[tr[b].l].z-tr[tr[a].l].z,m=(l+r)/2;return k<=z?kth(tr[a].l,tr[b].l,l,m,k):kth(tr[a].r,tr[b].r,m+1,r,k-z);};int q;cin>>q;while(q--){int l,r,k;cin>>l>>r>>k;int a=kth(root[l-1],root[r],0,n-1,k);cout<<sa[a]+1<<' ';if(k==r-l+1)cout<<0;else{int b=kth(root[l-1],root[r],0,n-1,k+1);cout<<lcp(a,b);}cout<<'\n';}}
'''
P24=r'''import sys
def main():
 d=sys.stdin.buffer.read().split();s=d[0];n=len(s);sa=list(range(n));rank=list(s);k=1
 while True:
  sa.sort(key=lambda i:(rank[i],rank[i+k] if i+k<n else -1));nr=[0]*n
  for j in range(1,n):nr[sa[j]]=nr[sa[j-1]]+((rank[sa[j-1]],rank[sa[j-1]+k] if sa[j-1]+k<n else -1)<(rank[sa[j]],rank[sa[j]+k] if sa[j]+k<n else -1))
  rank=nr
  if rank[sa[-1]]==n-1:break
  k*=2
 h=[0]*n;k=0
 for i in range(n):
  x=rank[i]
  if x:
   j=sa[x-1]
   while i+k<n and j+k<n and s[i+k]==s[j+k]:k+=1
   h[x]=k;k=max(0,k-1)
 size=1
 while size<n:size*=2
 seg=[n*2]*(2*size);seg[size:size+n]=h
 for i in range(size-1,0,-1):seg[i]=min(seg[i*2],seg[i*2+1])
 def lcp(a,b):
  if a==b:return n-sa[a]
  if a>b:a,b=b,a
  a+=1;v=n*2;a+=size;b+=size+1
  while a<b:
   if a&1:v=min(v,seg[a]);a+=1
   if b&1:b-=1;v=min(v,seg[b])
   a//=2;b//=2
  return v
 levels=max(1,(n-1).bit_length());prefs=[];zeros=[];cur=rank
 for bit in range(levels-1,-1,-1):
  pref=[0];z=[];o=[]
  for x in cur:
   iszero=not (x>>bit&1);pref.append(pref[-1]+iszero);(z if iszero else o).append(x)
  prefs.append(pref);zeros.append(len(z));cur=z+o
 def kth(l,r,k):
  value=0
  for lev,bit in enumerate(range(levels-1,-1,-1)):
   p=prefs[lev];zl=p[l];zr=p[r];cnt=zr-zl
   if k<=cnt:l=zl;r=zr
   else:k-=cnt;value|=1<<bit;l=zeros[lev]+l-zl;r=zeros[lev]+r-zr
  return value
 q=int(d[1]);out=[];at=2
 for _ in range(q):
  l=int(d[at])-1;r=int(d[at+1]);k=int(d[at+2]);at+=3;a=kth(l,r,k);v=0 if k==r-l else lcp(a,kth(l,r,k+1));out.append(f'{sa[a]+1} {v}')
 print('\n'.join(out))
if __name__=='__main__':main()
'''
G24=r'''import argparse,random
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
'''

R25=r'''# Dynamic Pattern Ledger

There are `n` lowercase patterns, initially inactive. Operations are `+ i`
(activate), `- i` (deactivate), and `? text`. Activation commands are valid.
For a query, print the total number of occurrences of active patterns in
`text`; overlapping occurrences and equal patterns with different indices are
counted separately.

## Input
```text
n q
n patterns
q operations
```
Total pattern and query-text length is at most `400000`; `n,q <= 200000`.

## Sample input
```text
3 6
a
aba
ba
+ 1
+ 2
? ababa
- 1
+ 3
? ababa
```
## Sample output
```text
5
4
```
'''
C25=r'''#include <bits/stdc++.h>
using namespace std;struct N{array<int,26>to{};int f=0;vector<int>ch;N(){to.fill(0);}};int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,q;if(!(cin>>n>>q))return 0;vector<N>t(1);vector<int>end(n);for(int i=0;i<n;i++){string s;cin>>s;int v=0;for(char x:s){int c=x-'a';if(!t[v].to[c])t[v].to[c]=t.size(),t.emplace_back();v=t[v].to[c];}end[i]=v;}queue<int>qu;for(int c=0;c<26;c++)if(t[0].to[c])qu.push(t[0].to[c]);while(!qu.empty()){int v=qu.front();qu.pop();t[t[v].f].ch.push_back(v);for(int c=0;c<26;c++)if(t[v].to[c])t[t[v].to[c]].f=t[t[v].f].to[c],qu.push(t[v].to[c]);else t[v].to[c]=t[t[v].f].to[c];}int T=t.size(),tm=0;vector<int>in(T),out(T),it(T);vector<pair<int,int>>st={{0,0}};while(!st.empty()){int v=st.back().first,&i=st.back().second;if(i==0)in[v]=++tm;if(i<(int)t[v].ch.size())st.push_back({t[v].ch[i++],0});else out[v]=tm,st.pop_back();}vector<long long>bit(T+2);auto add=[&](int x,int z){for(;x<(int)bit.size();x+=x&-x)bit[x]+=z;};auto get=[&](int x){long long z=0;for(;x;x-=x&-x)z+=bit[x];return z;};while(q--){char op;cin>>op;if(op=='?'){string s;cin>>s;int v=0;long long ans=0;for(char x:s)v=t[v].to[x-'a'],ans+=get(in[v]);cout<<ans<<'\n';}else{int i;cin>>i;int z=op=='+'?1:-1,v=end[i-1];add(in[v],z);add(out[v]+1,-z);}}}
'''
P25=r'''import sys,collections
def main():
 d=sys.stdin.buffer.read().split();n=int(d[0]);q=int(d[1]);to=[{}];fail=[0];ends=[];at=2
 for s in d[at:at+n]:
  v=0
  for c in s:
   if c not in to[v]:to[v][c]=len(to);to.append({});fail.append(0)
   v=to[v][c]
  ends.append(v)
 at+=n;qq=collections.deque(to[0].values());order=[0]
 while qq:
  v=qq.popleft();order.append(v)
  for c,u in to[v].items():
   f=fail[v]
   while f and c not in to[f]:f=fail[f]
   fail[u]=to[f].get(c,0);qq.append(u)
 child=[[] for _ in to]
 for v in range(1,len(to)):child[fail[v]].append(v)
 tin=[0]*len(to);tout=[0]*len(to);tm=0;st=[(0,0)]
 while st:
  v,i=st[-1]
  if i==0:tm+=1;tin[v]=tm
  if i<len(child[v]):st[-1]=(v,i+1);st.append((child[v][i],0))
  else:tout[v]=tm;st.pop()
 bit=[0]*(len(to)+2)
 def add(x,z):
  while x<len(bit):bit[x]+=z;x+=x&-x
 def get(x):
  z=0
  while x:z+=bit[x];x-=x&-x
  return z
 out=[]
 for _ in range(q):
  op=d[at];x=d[at+1];at+=2
  if op==b'?':
   v=0;ans=0
   for c in x:
    while v and c not in to[v]:v=fail[v]
    v=to[v].get(c,0);ans+=get(tin[v])
   out.append(str(ans))
  else:v=ends[int(x)-1];z=1 if op==b'+' else -1;add(tin[v],z);add(tout[v]+1,-z)
 print('\n'.join(out))
if __name__=='__main__':main()
'''
G25=r'''import argparse,random
from pathlib import Path
def case(r):
 n=r.randint(1,10);p=[''.join(r.choice('abc') for _ in range(r.randint(1,5))) for _ in range(n)];active=[0]*n;ops=[];ans=[]
 for _ in range(r.randint(1,35)):
  choices=['?']+(['+'] if not all(active) else [])+(['-'] if any(active) else []);o=r.choice(choices)
  if o=='?':
   s=''.join(r.choice('abc') for _ in range(r.randint(1,14)));ops.append(f'? {s}');ans.append(str(sum(sum(s[j:j+len(x)]==x for j in range(len(s)-len(x)+1)) for i,x in enumerate(p) if active[i])))
  else:
   a=[i for i,x in enumerate(active) if x==(o=='-')];i=r.choice(a);active[i]^=1;ops.append(f'{o} {i+1}')
 return f'{n} {len(ops)}\n'+'\n'.join(p)+'\n'+'\n'.join(ops)+'\n','\n'.join(ans)+('\n' if ans else '')
def main():
 p=argparse.ArgumentParser();p.add_argument('--count',type=int,default=25);p.add_argument('--seed',type=int,default=1);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);r=random.Random(a.seed)
 for i in range(a.count):x,y=case(r);z=a.out_dir/f'case{i:03d}';z.with_suffix('.in').write_text(x);z.with_suffix('.out').write_text(y)
if __name__=='__main__':main()
'''

R26=r'''# Cyclic Match Convolution

Strings `a,b` have equal length and use `a,b,c,?`; `?` matches every symbol.
For each left rotation `d` of `b`, compare `a[i]` with `b[(i+d) mod n]`.
Print all shifts having at most `K` mismatches.

## Input
```text
n K
a
b
```
`1 <= n <= 200000`, `0 <= K <= n`.

## Output
First print the number of valid shifts, then their zero-based indices.

## Sample input
```text
4 0
a?bc
bcaa
```
## Sample output
```text
1
2
```
'''
NTTPY=r'''import sys
MOD=998244353;G=3
def conv(a,b):
 n=1
 while n<len(a)+len(b)-1:n*=2
 a+= [0]*(n-len(a));b+= [0]*(n-len(b))
 def ntt(x,inv):
  j=0
  for i in range(1,n):
   bit=n>>1
   while j&bit:j^=bit;bit>>=1
   j^=bit
   if i<j:x[i],x[j]=x[j],x[i]
  z=2
  while z<=n:
   w=pow(G,(MOD-1)//z,MOD)
   if inv:w=pow(w,MOD-2,MOD)
   for i in range(0,n,z):
    q=1
    for j in range(i,i+z//2):u=x[j];v=x[j+z//2]*q%MOD;x[j]=(u+v)%MOD;x[j+z//2]=(u-v)%MOD;q=q*w%MOD
   z*=2
  if inv:
   q=pow(n,MOD-2,MOD)
   for i in range(n):x[i]=x[i]*q%MOD
 ntt(a,0);ntt(b,0)
 for i in range(n):a[i]=a[i]*b[i]%MOD
 ntt(a,1);return a
def main():
 d=sys.stdin.buffer.read().split();n=int(d[0]);K=int(d[1]);a=d[2];b=d[3];eq=[0]*n;both=[0]*n
 for chars,target in [((97,98,99),eq),((97,98,99),both)]:
  if target is both:
   x=[int(c!=63) for c in a][::-1];y=[int(c!=63) for c in b+b];z=conv(x,y)
   for i in range(n):both[i]=z[n-1+i]
  else:
   for c in chars:
    z=conv([int(x==c) for x in a][::-1],[int(x==c) for x in b+b])
    for i in range(n):eq[i]+=z[n-1+i]
 ans=[i for i in range(n) if both[i]-eq[i]<=K];print(len(ans));print(*ans)
if __name__=='__main__':main()
'''
NTTCPP=r'''#include <bits/stdc++.h>
using namespace std;const int M=998244353,G=3;int pw(int a,int b){long long z=1;for(;b;b>>=1,a=(long long)a*a%M)if(b&1)z=z*a%M;return z;}void ntt(vector<int>&a,bool iv){int n=a.size();for(int i=1,j=0;i<n;i++){int b=n>>1;for(;j&b;b>>=1)j^=b;j^=b;if(i<j)swap(a[i],a[j]);}for(int z=2;z<=n;z*=2){int w=pw(G,(M-1)/z);if(iv)w=pw(w,M-2);for(int i=0;i<n;i+=z)for(int j=0,q=1;j<z/2;j++,q=(long long)q*w%M){int u=a[i+j],v=(long long)a[i+j+z/2]*q%M;a[i+j]=(u+v)%M;a[i+j+z/2]=(u-v+M)%M;}}if(iv){int q=pw(n,M-2);for(int&x:a)x=(long long)x*q%M;}}vector<int>cv(vector<int>a,vector<int>b){int n=1;while(n<(int)a.size()+(int)b.size()-1)n*=2;a.resize(n);b.resize(n);ntt(a,0);ntt(b,0);for(int i=0;i<n;i++)a[i]=(long long)a[i]*b[i]%M;ntt(a,1);return a;}int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,K;string a,b;cin>>n>>K>>a>>b;vector<int>eq(n),both(n);string bb=b+b;for(char c:string("abc")){vector<int>x(n),y(2*n);for(int i=0;i<n;i++)x[n-1-i]=a[i]==c;for(int i=0;i<2*n;i++)y[i]=bb[i]==c;auto z=cv(x,y);for(int i=0;i<n;i++)eq[i]+=z[n-1+i];}{vector<int>x(n),y(2*n);for(int i=0;i<n;i++)x[n-1-i]=a[i]!='?';for(int i=0;i<2*n;i++)y[i]=bb[i]!='?';auto z=cv(x,y);for(int i=0;i<n;i++)both[i]=z[n-1+i];}vector<int>ans;for(int i=0;i<n;i++)if(both[i]-eq[i]<=K)ans.push_back(i);cout<<ans.size()<<'\n';for(int x:ans)cout<<x<<' ';cout<<'\n';}
'''
G26=r'''import argparse,random
from pathlib import Path
def case(r):
 n=r.randint(1,30);k=r.randint(0,n);a=''.join(r.choice('abc?') for _ in range(n));b=''.join(r.choice('abc?') for _ in range(n));z=[d for d in range(n) if sum(a[i]!='?' and b[(i+d)%n]!='?' and a[i]!=b[(i+d)%n] for i in range(n))<=k];return f'{n} {k}\n{a}\n{b}\n',str(len(z))+'\n'+' '.join(map(str,z))+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--count',type=int,default=25);p.add_argument('--seed',type=int,default=1);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);r=random.Random(a.seed)
 for i in range(a.count):x,y=case(r);z=a.out_dir/f'case{i:03d}';z.with_suffix('.in').write_text(x);z.with_suffix('.out').write_text(y)
if __name__=='__main__':main()
'''

OPTIMIZED_26=(BASE/'26_cyclic_match_convolution'/'solution.py').read_text()
P={'24_lexicographic_substring_laboratory':('Lexicographic Substring Laboratory',R24,C24,P24,G24,'banana\n3\n1 6 2\n2 5 2\n3 3 1\n','4 3\n2 0\n3 0\n'),'25_dynamic_pattern_ledger':('Dynamic Pattern Ledger',R25,C25,P25,G25,'3 6\na\naba\nba\n+ 1\n+ 2\n? ababa\n- 1\n+ 3\n? ababa\n','5\n4\n'),'26_cyclic_match_convolution':('Cyclic Match Convolution',R26,NTTCPP,OPTIMIZED_26,G26,'4 0\na?bc\nbcaa\n','1\n2\n')}
def main():
 for slug,(title,r,c,p,g,si,so) in P.items():
  d=BASE/slug;t=d/'tests';t.mkdir(parents=True,exist_ok=True)
  (d/'README.md').write_text(r);(d/'manifest.json').write_text(f'{{"title":"{title}","checker":"tokens","time_limit_seconds":20}}\n');(d/'solution.cpp').write_text(c);(d/'solution.py').write_text(p);(d/'solve.cpp').write_text(SC);(d/'solve.py').write_text(SP);(t/'sample1.in').write_text(si);(t/'sample1.out').write_text(so);(t/'random_cases.py').write_text(g)
if __name__=='__main__':main()
