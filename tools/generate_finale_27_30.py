"""Generate the final four problems of Section 100 Round III."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT/'sections/100_grandmaster_finale/problems';SC='#include <bits/stdc++.h>\nusing namespace std;\nint main(){/* TODO */}\n';SP='def main(): pass # TODO\nif __name__=="__main__":main()\n'

R27=r'''# Distinct Substring Rank

For each positive `k`, print the `k`-th **distinct nonempty substring** of `s`
in lexicographic order, or `-1` if it does not exist.

## Input
```text
s
q
q lines: k
```
Lowercase `s`; `|s|,q <= 200000`; `k <= 10^18`.

## Sample input
```text
aba
6
1
2
3
5
6
```
## Sample output
```text
a
ab
aba
ba
-1
```
'''
C27=r'''#include <bits/stdc++.h>
using namespace std;struct S{int l=0,p=-1;map<char,int>n;};int main(){ios::sync_with_stdio(false);cin.tie(nullptr);string s;if(!(cin>>s))return 0;vector<S>a(1);int last=0;for(char c:s){int u=a.size();a.push_back({a[last].l+1,-1,{}});int p=last;while(p>=0&&!a[p].n.count(c))a[p].n[c]=u,p=a[p].p;if(p<0)a[u].p=0;else{int q=a[p].n[c];if(a[p].l+1==a[q].l)a[u].p=q;else{int z=a.size();a.push_back(a[q]);a[z].l=a[p].l+1;while(p>=0&&a[p].n[c]==q)a[p].n[c]=z,p=a[p].p;a[q].p=a[u].p=z;}}last=u;}vector<int>o(a.size());iota(o.begin(),o.end(),0);sort(o.begin(),o.end(),[&](int x,int y){return a[x].l>a[y].l;});const unsigned long long CAP=4000000000000000000ULL;vector<unsigned long long>d(a.size(),1);for(int v:o)for(auto [c,u]:a[v].n)d[v]=min(CAP,d[v]+d[u]);int Q;cin>>Q;while(Q--){unsigned long long k;cin>>k;if(k>=d[0]){cout<<-1<<'\n';continue;}int v=0;string z;while(k){for(auto [c,u]:a[v].n){if(k>d[u])k-=d[u];else{z+=c;k--;v=u;break;}}}cout<<z<<'\n';}}
'''
P27=r'''import sys
def main():
 d=sys.stdin.buffer.read().split();s=d[0];ln=[0];link=[-1];to=[{}];last=0
 for c in s:
  u=len(ln);ln.append(ln[last]+1);link.append(0);to.append({});p=last
  while p>=0 and c not in to[p]:to[p][c]=u;p=link[p]
  if p<0:link[u]=0
  else:
   q=to[p][c]
   if ln[p]+1==ln[q]:link[u]=q
   else:
    z=len(ln);ln.append(ln[p]+1);link.append(link[q]);to.append(to[q].copy())
    while p>=0 and to[p].get(c)==q:to[p][c]=z;p=link[p]
    link[q]=link[u]=z
  last=u
 cnt=[1]*len(ln);CAP=4*10**18
 for v in sorted(range(len(ln)),key=ln.__getitem__,reverse=True):cnt[v]=min(CAP,1+sum(cnt[u] for u in to[v].values()))
 out=[]
 for x in d[2:]:
  k=int(x)
  if k>=cnt[0]:out.append('-1');continue
  v=0;z=[]
  while k:
   for c,u in sorted(to[v].items()):
    if k>cnt[u]:k-=cnt[u]
    else:z.append(chr(c));k-=1;v=u;break
  out.append(''.join(z))
 print('\n'.join(out))
if __name__=='__main__':main()
'''
G27=r'''import argparse,random
from pathlib import Path
def case(r):
 s=''.join(r.choice('abc') for _ in range(r.randint(1,13)));a=sorted({s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1)});q=r.randint(1,25);ks=[r.randint(1,len(a)+5) for _ in range(q)];return s+'\n'+str(q)+'\n'+'\n'.join(map(str,ks))+'\n','\n'.join(a[k-1] if k<=len(a) else '-1' for k in ks)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--count',type=int,default=25);p.add_argument('--seed',type=int,default=1);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);r=random.Random(a.seed)
 for i in range(a.count):x,y=case(r);z=a.out_dir/f'case{i:03d}';z.with_suffix('.in').write_text(x);z.with_suffix('.out').write_text(y)
if __name__=='__main__':main()
'''

R28=r'''# Interval LCP Aggregates

For every unordered pair of distinct suffixes of `s`, take their longest
common-prefix length. Print the sum over all pairs.

## Input
One nonempty lowercase string `s`, `|s| <= 500000`.

## Output
The sum (it fits signed 64-bit).

## Sample input
```text
banana
```
## Sample output
```text
7
```
'''
C28=r'''#include <bits/stdc++.h>
using namespace std;int main(){ios::sync_with_stdio(false);cin.tie(nullptr);string s;if(!(cin>>s))return 0;int n=s.size();vector<int>sa(n),r(n),z(n);iota(sa.begin(),sa.end(),0);for(int i=0;i<n;i++)r[i]=s[i];for(int k=1;;k*=2){sort(sa.begin(),sa.end(),[&](int a,int b){return pair(r[a],a+k<n?r[a+k]:-1)<pair(r[b],b+k<n?r[b+k]:-1);});z[sa[0]]=0;for(int i=1;i<n;i++)z[sa[i]]=z[sa[i-1]]+(pair(r[sa[i-1]],sa[i-1]+k<n?r[sa[i-1]+k]:-1)<pair(r[sa[i]],sa[i]+k<n?r[sa[i]+k]:-1));r=z;if(r[sa.back()]==n-1)break;}vector<tuple<int,int,int>>e;for(int i=0,k=0;i<n;i++){int x=r[i];if(x){int j=sa[x-1];while(i+k<n&&j+k<n&&s[i+k]==s[j+k])k++;e.push_back({k,x-1,x});if(k)k--;}}sort(e.rbegin(),e.rend());vector<int>p(n),sz(n,1);iota(p.begin(),p.end(),0);function<int(int)>F=[&](int x){return p[x]==x?x:p[x]=F(p[x]);};long long ans=0;for(auto [w,x,y]:e){x=F(x);y=F(y);if(x!=y)ans+=1LL*w*sz[x]*sz[y],p[y]=x,sz[x]+=sz[y];}cout<<ans<<'\n';}
'''
P28=r'''import sys
def main():
 s=sys.stdin.buffer.readline().strip();n=len(s);sa=list(range(n));r=list(s);k=1
 while True:
  sa.sort(key=lambda i:(r[i],r[i+k] if i+k<n else -1));z=[0]*n
  for i in range(1,n):z[sa[i]]=z[sa[i-1]]+((r[sa[i-1]],r[sa[i-1]+k] if sa[i-1]+k<n else -1)<(r[sa[i]],r[sa[i]+k] if sa[i]+k<n else -1))
  r=z
  if r[sa[-1]]==n-1:break
  k*=2
 e=[];k=0
 for i in range(n):
  x=r[i]
  if x:
   j=sa[x-1]
   while i+k<n and j+k<n and s[i+k]==s[j+k]:k+=1
   e.append((k,x-1,x));k=max(0,k-1)
 p=list(range(n));sz=[1]*n
 def f(x):
  while p[x]!=x:p[x]=p[p[x]];x=p[x]
  return x
 ans=0
 for w,x,y in sorted(e,reverse=True):x=f(x);y=f(y);ans+=w*sz[x]*sz[y];p[y]=x;sz[x]+=sz[y]
 print(ans)
if __name__=='__main__':main()
'''
G28=r'''import argparse,random
from pathlib import Path
def case(r):
 s=''.join(r.choice('abc') for _ in range(r.randint(1,25)));a=0
 for i in range(len(s)):
  for j in range(i+1,len(s)):
   k=0
   while j+k<len(s) and s[i+k]==s[j+k]:k+=1
   a+=k
 return s+'\n',f'{a}\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--count',type=int,default=25);p.add_argument('--seed',type=int,default=1);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);r=random.Random(a.seed)
 for i in range(a.count):x,y=case(r);z=a.out_dir/f'case{i:03d}';z.with_suffix('.in').write_text(x);z.with_suffix('.out').write_text(y)
if __name__=='__main__':main()
'''

R29=r'''# Editable Palindrome Rope

Maintain a lowercase string under operations `SET i c`, `REV l r`, and
`PAL l r`. Reverse the requested substring or print `YES`/`NO` according as
the queried substring is a palindrome.

## Input
```text
s
q
q operations
```
`|s|,q <= 200000`; indices are one-based and valid.

## Sample input
```text
abca
5
PAL 1 4
SET 2 c
PAL 1 4
REV 2 4
PAL 1 3
```
## Sample output
```text
NO
YES
NO
```
'''
C29=r'''#include <bits/stdc++.h>
using namespace std;const long long M1=1000000007,M2=1000000009,B=911382323;struct N{int l=0,r=0,z=1,v;unsigned p;bool rev=0;long long f1,f2,b1,b2;};vector<N>t(1);vector<long long>p1(1,1),p2(1,1);int Z(int x){return x?t[x].z:0;}void rv(int x){if(x)swap(t[x].l,t[x].r),swap(t[x].f1,t[x].b1),swap(t[x].f2,t[x].b2),t[x].rev^=1;}void push(int x){if(t[x].rev)rv(t[x].l),rv(t[x].r),t[x].rev=0;}void pull(int x){int l=t[x].l,r=t[x].r,R=Z(r),L=Z(l);t[x].z=L+R+1;t[x].f1=(t[l].f1*p1[R+1]+1LL*t[x].v*p1[R]+t[r].f1)%M1;t[x].f2=(t[l].f2*p2[R+1]+1LL*t[x].v*p2[R]+t[r].f2)%M2;t[x].b1=(t[r].b1*p1[L+1]+1LL*t[x].v*p1[L]+t[l].b1)%M1;t[x].b2=(t[r].b2*p2[L+1]+1LL*t[x].v*p2[L]+t[l].b2)%M2;}void split(int x,int k,int&a,int&b){if(!x){a=b=0;return;}push(x);if(Z(t[x].l)>=k)split(t[x].l,k,a,t[x].l),b=x,pull(b);else split(t[x].r,k-Z(t[x].l)-1,t[x].r,b),a=x,pull(a);}int merge(int a,int b){if(!a||!b)return a?a:b;if(t[a].p<t[b].p){push(a);t[a].r=merge(t[a].r,b);pull(a);return a;}push(b);t[b].l=merge(a,t[b].l);pull(b);return b;}int main(){ios::sync_with_stdio(false);cin.tie(nullptr);string s;cin>>s;for(int i=0;i<(int)s.size()+5;i++)p1.push_back(p1.back()*B%M1),p2.push_back(p2.back()*B%M2);mt19937 g(712367);int root=0;for(char c:s){int x=t.size();t.push_back({0,0,1,c-'a'+1,(unsigned)g(),0,c-'a'+1,c-'a'+1,c-'a'+1,c-'a'+1});root=merge(root,x);}int q;cin>>q;while(q--){string o;int l,r;cin>>o>>l;if(o=="SET"){char c;cin>>c;int a,b,x;split(root,l-1,a,b);split(b,1,x,b);t[x].v=c-'a'+1;pull(x);root=merge(a,merge(x,b));}else{cin>>r;int a,b,x;split(root,l-1,a,b);split(b,r-l+1,x,b);if(o=="REV")rv(x);else cout<<((t[x].f1==t[x].b1&&t[x].f2==t[x].b2)?"YES\n":"NO\n");root=merge(a,merge(x,b));}}}
'''
P29=r'''import sys,random
sys.setrecursionlimit(1000000);M1=1000000007;M2=1000000009;B=911382323
def main():
 d=sys.stdin.buffer.read().split();s=d[0];n=len(s);q=int(d[1]);pw1=[1]*(n+2);pw2=[1]*(n+2)
 for i in range(1,n+2):pw1[i]=pw1[i-1]*B%M1;pw2[i]=pw2[i-1]*B%M2
 L=[0];R=[0];P=[0];V=[0];Z=[0];F1=[0];F2=[0];G1=[0];G2=[0];REV=[0];rng=random.Random(712367)
 def node(v):L.append(0);R.append(0);P.append(rng.randrange(1<<30));V.append(v);Z.append(1);F1.append(v);F2.append(v);G1.append(v);G2.append(v);REV.append(0);return len(L)-1
 def rv(x):
  if x:L[x],R[x]=R[x],L[x];F1[x],G1[x]=G1[x],F1[x];F2[x],G2[x]=G2[x],F2[x];REV[x]^=1
 def push(x):
  if REV[x]:rv(L[x]);rv(R[x]);REV[x]=0
 def pull(x):
  l=L[x];r=R[x];Z[x]=Z[l]+Z[r]+1;F1[x]=(F1[l]*pw1[Z[r]+1]+V[x]*pw1[Z[r]]+F1[r])%M1;F2[x]=(F2[l]*pw2[Z[r]+1]+V[x]*pw2[Z[r]]+F2[r])%M2;G1[x]=(G1[r]*pw1[Z[l]+1]+V[x]*pw1[Z[l]]+G1[l])%M1;G2[x]=(G2[r]*pw2[Z[l]+1]+V[x]*pw2[Z[l]]+G2[l])%M2
 def split(x,k):
  if not x:return 0,0
  push(x)
  if Z[L[x]]>=k:a,L[x]=split(L[x],k);pull(x);return a,x
  R[x],b=split(R[x],k-Z[L[x]]-1);pull(x);return x,b
 def merge(a,b):
  if not a or not b:return a or b
  if P[a]<P[b]:push(a);R[a]=merge(R[a],b);pull(a);return a
  push(b);L[b]=merge(a,L[b]);pull(b);return b
 root=0
 for c in s:root=merge(root,node(c-96))
 out=[];at=2
 for _ in range(q):
  o=d[at];l=int(d[at+1]);at+=2;a,b=split(root,l-1)
  if o==b'SET':x,b=split(b,1);V[x]=d[at][0]-96;at+=1;pull(x)
  else:
   r=int(d[at]);at+=1;x,b=split(b,r-l+1)
   if o==b'REV':rv(x)
   else:out.append('YES' if F1[x]==G1[x] and F2[x]==G2[x] else 'NO')
  root=merge(a,merge(x,b))
 print('\n'.join(out))
if __name__=='__main__':main()
'''
G29=r'''import argparse,random
from pathlib import Path
def case(r):
 a=list(''.join(r.choice('abc') for _ in range(r.randint(1,18))));s=''.join(a);ops=[];ans=[]
 for _ in range(r.randint(1,40)):
  o=r.choice(['SET','REV','PAL']);l=r.randint(1,len(a))
  if o=='SET':c=r.choice('abc');a[l-1]=c;ops.append(f'SET {l} {c}')
  else:h=r.randint(l,len(a));ops.append(f'{o} {l} {h}');a[l-1:h]=a[l-1:h][::-1] if o=='REV' else a[l-1:h];ans+=([('YES' if a[l-1:h]==a[l-1:h][::-1] else 'NO')] if o=='PAL' else [])
 return s+'\n'+str(len(ops))+'\n'+'\n'.join(ops)+'\n','\n'.join(ans)+('\n' if ans else '')
def main():
 p=argparse.ArgumentParser();p.add_argument('--count',type=int,default=25);p.add_argument('--seed',type=int,default=1);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);r=random.Random(a.seed)
 for i in range(a.count):x,y=case(r);z=a.out_dir/f'case{i:03d}';z.with_suffix('.in').write_text(x);z.with_suffix('.out').write_text(y)
if __name__=='__main__':main()
'''

R30=r'''# Forbidden Superstring Count

Over alphabet `abc`, count length-`L` strings that contain every required
pattern and contain no forbidden pattern. Print the answer modulo `998244353`.

## Input
```text
R F L
R required patterns
F forbidden patterns
```
`0 <= R <= 5`, `0 <= F <= 5`, `0 <= L <= 10^18`; total pattern length `<= 18`.

## Sample input
```text
1 1 3
ab
cc
```
## Sample output
```text
5
```
'''
PY30=r'''import sys,collections
M=998244353
def mul(a,b):
 n=len(a);c=[[0]*n for _ in range(n)]
 for i in range(n):
  for k,x in enumerate(a[i]):
   if x:
    for j,y in enumerate(b[k]):
     if y:c[i][j]=(c[i][j]+x*y)%M
 return c
def main():
 d=sys.stdin.buffer.read().split();R=int(d[0]);F=int(d[1]);L=int(d[2]);p=d[3:3+R+F];to=[{}];fail=[0];mask=[0];bad=[0]
 for i,s in enumerate(p):
  v=0
  for c in s:
   if c not in to[v]:to[v][c]=len(to);to.append({});fail.append(0);mask.append(0);bad.append(0)
   v=to[v][c]
  if i<R:mask[v]|=1<<i
  else:bad[v]=1
 q=collections.deque()
 for c in b'abc':
  if c in to[0]:q.append(to[0][c])
  else:to[0][c]=0
 while q:
  v=q.popleft();mask[v]|=mask[fail[v]];bad[v]|=bad[fail[v]]
  for c in b'abc':
   if c in to[v]:fail[to[v][c]]=to[fail[v]][c];q.append(to[v][c])
   else:to[v][c]=to[fail[v]][c]
 ans=0;n=len(to)
 for ban in range(1<<R):
  ok=[not bad[i] and not(mask[i]&ban) for i in range(n)];a=[[0]*n for _ in range(n)]
  for i in range(n):
   if ok[i]:
    for c in b'abc':
     j=to[i][c]
     if ok[j]:a[i][j]+=1
  v=[[0]*n for _ in range(n)]
  for i in range(n):v[i][i]=1
  e=L
  while e:
   if e&1:v=mul(v,a)
   a=mul(a,a);e//=2
  z=sum(v[0])%M;ans+=( -z if ban.bit_count()&1 else z)
 print(ans%M)
if __name__=='__main__':main()
'''
C30=r'''#include <bits/stdc++.h>
using namespace std;const long long M=998244353;using A=vector<vector<long long>>;A mul(const A&a,const A&b){int n=a.size();A c(n,vector<long long>(n));for(int i=0;i<n;i++)for(int k=0;k<n;k++)if(a[i][k])for(int j=0;j<n;j++)c[i][j]=(c[i][j]+a[i][k]*b[k][j])%M;return c;}struct N{array<int,3>to{};int f=0,m=0;bool bad=0;};int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int R,F;unsigned long long L;cin>>R>>F>>L;vector<N>t(1);for(int i=0;i<R+F;i++){string s;cin>>s;int v=0;for(char c:s){int x=c-'a';if(!t[v].to[x])t[v].to[x]=t.size(),t.push_back({});v=t[v].to[x];}if(i<R)t[v].m|=1<<i;else t[v].bad=1;}queue<int>q;for(int c=0;c<3;c++)if(t[0].to[c])q.push(t[0].to[c]);while(!q.empty()){int v=q.front();q.pop();t[v].m|=t[t[v].f].m;t[v].bad|=t[t[v].f].bad;for(int c=0;c<3;c++)if(t[v].to[c])t[t[v].to[c]].f=t[t[v].f].to[c],q.push(t[v].to[c]);else t[v].to[c]=t[t[v].f].to[c];}long long ans=0;int n=t.size();for(int ban=0;ban<(1<<R);ban++){vector<int>ok(n);for(int i=0;i<n;i++)ok[i]=!t[i].bad&&!(t[i].m&ban);A a(n,vector<long long>(n)),v(n,vector<long long>(n));for(int i=0;i<n;i++){v[i][i]=1;if(ok[i])for(int c=0;c<3;c++)if(ok[t[i].to[c]])a[i][t[i].to[c]]++;}for(auto e=L;e;e>>=1,a=mul(a,a))if(e&1)v=mul(v,a);long long z=accumulate(v[0].begin(),v[0].end(),0LL)%M;ans+=(__builtin_popcount(ban)&1)?-z:z;}cout<<(ans%M+M)%M<<'\n';}
'''
G30=r'''import argparse,itertools,random
from pathlib import Path
def case(r):
 R=r.randint(0,3);F=r.randint(0,3);L=r.randint(0,7);req=[''.join(r.choice('abc') for _ in range(r.randint(1,3))) for _ in range(R)];bad=[''.join(r.choice('abc') for _ in range(r.randint(1,3))) for _ in range(F)];z=sum(all(x in s for x in req) and all(x not in s for x in bad) for s in map(''.join,itertools.product('abc',repeat=L)));return f'{R} {F} {L}\n'+'\n'.join(req+bad)+('\n' if req or bad else ''),f'{z}\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--count',type=int,default=25);p.add_argument('--seed',type=int,default=1);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);r=random.Random(a.seed)
 for i in range(a.count):x,y=case(r);z=a.out_dir/f'case{i:03d}';z.with_suffix('.in').write_text(x);z.with_suffix('.out').write_text(y)
if __name__=='__main__':main()
'''

P={'27_distinct_substring_rank':('Distinct Substring Rank',R27,C27,P27,G27,'aba\n5\n1\n2\n3\n5\n6\n','a\nab\naba\nba\n-1\n'),'28_interval_lcp_aggregates':('Interval LCP Aggregates',R28,C28,P28,G28,'banana\n','7\n'),'29_editable_palindrome_rope':('Editable Palindrome Rope',R29,C29,P29,G29,'abca\n5\nPAL 1 4\nSET 2 c\nPAL 1 4\nREV 2 4\nPAL 1 3\n','NO\nYES\nNO\n'),'30_forbidden_superstring_count':('Forbidden Superstring Count',R30,C30,PY30,G30,'1 1 3\nab\ncc\n','6\n')}
def main():
 for slug,(title,r,c,p,g,si,so) in P.items():
  d=BASE/slug;t=d/'tests';t.mkdir(parents=True,exist_ok=True);(d/'README.md').write_text(r);(d/'manifest.json').write_text(f'{{"title":"{title}","checker":"tokens","time_limit_seconds":20}}\n');(d/'solution.cpp').write_text(c);(d/'solution.py').write_text(p);(d/'solve.cpp').write_text(SC);(d/'solve.py').write_text(SP);(t/'sample1.in').write_text(si);(t/'sample1.out').write_text(so);(t/'random_cases.py').write_text(g)
if __name__=='__main__':main()
