"""Generate the validated Round-II finale packages (problems 18--20)."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "sections/100_grandmaster_finale/problems"


STUB_CPP = r'''#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // TODO: solve the problem.
    return 0;
}
'''

STUB_PY = '''import sys


def main() -> None:
    # TODO: solve the problem.
    pass


if __name__ == "__main__":
    main()
'''


P18_README = r'''# Circulation Repair Queries

A directed network currently carries a feasible integer circulation. Edge `e`
has lower bound `lower[e]`, upper bound `upper[e]`, and current flow `flow[e]`.

Each query independently proposes adding a new directed edge `u -> v` whose
lower and upper bounds are both `1`. You may change the old edge flows, while
respecting their bounds. Print whether the enlarged network has a feasible
circulation. The original circulation is restored before the next query.

## Input

```text
n m q
m lines: u v lower upper flow
q lines: u v
```

- `1 <= n <= 700`, `0 <= m <= 5000`, `1 <= q <= 200000`;
- `0 <= lower <= flow <= upper <= 10^9`;
- the supplied old flow conserves flow at every vertex.

## Output

For each query print `YES` or `NO`.

## Sample input

```text
3 2 2
1 2 0 1 0
2 3 0 1 0
3 1
1 3
```

## Sample output

```text
YES
NO
```
'''

P18_CPP = r'''#include <bits/stdc++.h>
using namespace std;
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);
 int n,m,q;if(!(cin>>n>>m>>q))return 0; vector<bitset<700>> r(n);
 for(int i=0,u,v;i<m;i++){long long l,h,f;cin>>u>>v>>l>>h>>f;--u;--v;if(f<h)r[u].set(v);if(f>l)r[v].set(u);}
 for(int i=0;i<n;i++)r[i].set(i);
 for(int k=0;k<n;k++)for(int i=0;i<n;i++)if(r[i].test(k))r[i]|=r[k];
 while(q--){int u,v;cin>>u>>v;--u;--v;cout<<(r[v].test(u)?"YES\n":"NO\n");}
}
'''

P18_PY = r'''import sys
def main():
    it=iter(map(int,sys.stdin.buffer.read().split())); n=next(it);m=next(it);q=next(it); reach=[1<<i for i in range(n)]
    for _ in range(m):
        u=next(it)-1;v=next(it)-1;l=next(it);h=next(it);f=next(it)
        if f<h: reach[u]|=1<<v
        if f>l: reach[v]|=1<<u
    for k in range(n):
        bit=1<<k; add=reach[k]
        for i in range(n):
            if reach[i]&bit: reach[i]|=add
    out=[]
    for _ in range(q):
        u=next(it)-1;v=next(it)-1;out.append("YES" if reach[v]>>u&1 else "NO")
    print("\n".join(out))
if __name__=="__main__":main()
'''

P18_RANDOM = r'''import argparse, random
from pathlib import Path
def case(r):
 n=r.randint(1,9); m=r.randint(0,18); q=r.randint(1,20); edges=[]; bal=[0]*n
 # Zero is always a feasible circulation; bounds sometimes pin an edge at zero.
 for _ in range(m):
  u=r.randrange(n);v=r.randrange(n);h=r.randint(0,2);edges.append((u,v,0,h,0))
 g=[[] for _ in range(n)]
 for u,v,l,h,f in edges:
  if f<h:g[u].append(v)
  if f>l:g[v].append(u)
 ans=[]; queries=[]
 for _ in range(q):
  u=r.randrange(n);v=r.randrange(n);queries.append((u,v)); seen={v};st=[v]
  while st:
   x=st.pop()
   for y in g[x]:
    if y not in seen:seen.add(y);st.append(y)
  ans.append("YES" if u in seen else "NO")
 text=f"{n} {m} {q}\n"+''.join(f"{u+1} {v+1} {l} {h} {f}\n" for u,v,l,h,f in edges)+''.join(f"{u+1} {v+1}\n" for u,v in queries)
 return text,'\n'.join(ans)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--count',type=int,default=25);p.add_argument('--seed',type=int,default=1);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);r=random.Random(a.seed)
 for i in range(a.count):
  x,y=case(r);s=a.out_dir/f"case{i:03d}";s.with_suffix('.in').write_text(x);s.with_suffix('.out').write_text(y)
if __name__=='__main__':main()
'''


P19_README = r'''# Convex Resource Schedule

Split the nonnegative sequence `a[1..n]` into exactly `K` nonempty contiguous
batches. A batch whose sum is `s` costs `s^2`. Find the minimum total cost.

## Input

```text
n K
a[1] ... a[n]
```

- `1 <= K <= n <= 5000`;
- `0 <= a[i] <= 10000`;
- the answer fits in a signed 64-bit integer.

## Output

Print the minimum cost.

## Sample input

```text
5 3
2 1 4 1 2
```

## Sample output

```text
34
```
'''

P19_PY = r'''import sys
INF=10**80
def run(xs,lam,prefer_max):
 n=len(xs)-1; tree=[None]*(4*(n+1))
 def better(a,b,x):
  if b is None:return True
  va=a[0]*x+a[1];vb=b[0]*x+b[1]
  return va<vb or (va==vb and ((a[2]>b[2]) if prefer_max else (a[2]<b[2])))
 def add(line,p=1,l=0,r=n):
  mid=(l+r)//2
  if tree[p] is None:tree[p]=line;return
  left=better(line,tree[p],xs[l]);middle=better(line,tree[p],xs[mid])
  if middle:tree[p],line=line,tree[p]
  if l==r:return
  if left!=middle:add(line,p*2,l,mid)
  elif better(line,tree[p],xs[r])!=better(line,tree[p],xs[mid]):add(line,p*2+1,mid+1,r)
 def query(idx,p=1,l=0,r=n):
  line=tree[p];best=line
  if l==r:return best
  mid=(l+r)//2;child=p*2 if idx<=mid else p*2+1
  if tree[child] is None:return best
  other=query(idx,child,l,mid) if idx<=mid else query(idx,child,mid+1,r)
  return other if better(other,best,xs[idx]) else best
 add((0,0,0)); val=cnt=0
 for i in range(1,n+1):
  z=query(i);val=z[0]*xs[i]+z[1]+xs[i]*xs[i]+lam;cnt=z[2]+1;add((-2*xs[i],val+xs[i]*xs[i],cnt))
 return val,cnt
def main():
 d=list(map(int,sys.stdin.buffer.read().split()));n,k=d[:2];xs=[0]
 for a in d[2:]:xs.append(xs[-1]+a)
 if k==1:print(xs[-1]*xs[-1]);return
 if k==n:print(sum(a*a for a in d[2:]));return
 B=xs[-1]*xs[-1]+1;lo=-B;hi=B
 while lo<hi:
  mid=(lo+hi+1)//2
  if run(xs,mid,True)[1]>=k:lo=mid
  else:hi=mid-1
 value,maxc=run(xs,lo,True);_,minc=run(xs,lo,False)
 if not minc<=k<=maxc:raise RuntimeError("convexity invariant failed")
 print(value-lo*k)
if __name__=="__main__":main()
'''

P19_CPP = r'''#include <bits/stdc++.h>
using namespace std; using i128=__int128_t; const i128 INF=(i128(1)<<120);
struct L{long long m; i128 b; int c;};
pair<i128,int> run(const vector<long long>&x,long long lam,bool mx){int n=x.size()-1;vector<optional<L>>t(4*(n+1));
 auto better=[&](const L&a,const L&b,long long z){i128 u=i128(a.m)*z+a.b,v=i128(b.m)*z+b.b;return u<v||(u==v&&(mx?a.c>b.c:a.c<b.c));};
 function<void(L,int,int,int)>add=[&](L z,int p,int l,int r){if(!t[p]){t[p]=z;return;}int md=(l+r)/2;bool le=better(z,*t[p],x[l]),mi=better(z,*t[p],x[md]);if(mi)swap(z,*t[p]);if(l==r)return;if(le!=mi)add(z,p*2,l,md);else if(better(z,*t[p],x[r])!=better(z,*t[p],x[md]))add(z,p*2+1,md+1,r);};
 function<L(int,int,int,int)>qry=[&](int at,int p,int l,int r){L z=*t[p];if(l==r)return z;int md=(l+r)/2,q=at<=md?p*2:p*2+1;if(!t[q])return z;L o=at<=md?qry(at,q,l,md):qry(at,q,md+1,r);return better(o,z,x[at])?o:z;};
 add({0,0,0},1,0,n);i128 val=0;int cnt=0;for(int i=1;i<=n;i++){L z=qry(i,1,0,n);val=i128(z.m)*x[i]+z.b+i128(x[i])*x[i]+lam;cnt=z.c+1;add({-2*x[i],val+i128(x[i])*x[i],cnt},1,0,n);}return {val,cnt};}
void print128(i128 x){if(x==0){cout<<0;return;}string s;while(x){s+=char('0'+x%10);x/=10;}reverse(s.begin(),s.end());cout<<s;}
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,k;if(!(cin>>n>>k))return 0;vector<long long>a(n),s(n+1);for(int i=0;i<n;i++){cin>>a[i];s[i+1]=s[i]+a[i];}if(k==1){print128(i128(s[n])*s[n]);cout<<'\n';return 0;}if(k==n){i128 z=0;for(auto v:a)z+=i128(v)*v;print128(z);cout<<'\n';return 0;}long long B=s[n]*s[n]+1,lo=-B,hi=B;while(lo<hi){long long md=lo+(hi-lo+1)/2;if(run(s,md,true).second>=k)lo=md;else hi=md-1;}auto [v,ma]=run(s,lo,true);int mi=run(s,lo,false).second;assert(mi<=k&&k<=ma);print128(v-i128(lo)*k);cout<<'\n';}
'''

P19_RANDOM = r'''import argparse,random
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
'''


P20_README = r'''# Laminar Assignment

A rooted tree has some vertices marked as leaves. There are `w` workers. An
offer `(v,c)` for worker `i` means that the worker may be assigned to any leaf
in the subtree of `v`, at cost `c`. Assign every worker to a distinct leaf and
minimize total cost, or report `IMPOSSIBLE`.

## Input

```text
n w
parent[2] ... parent[n]
for i=1..w: t followed by t pairs v c
```

- root is vertex `1`; `parent[v] < v`;
- `1 <= n <= 1000`, `1 <= w <= 300`, total offers `<= 5000`;
- `0 <= c <= 10^9`; every worker has at least one offer.

A vertex with no children is a leaf. Duplicate offers are allowed.

## Output

Print the minimum cost, or `IMPOSSIBLE`.

## Sample input

```text
5 2
1 1 2 2
2 2 7 3 1
1 2 4
```

## Sample output

```text
5
```
'''

P20_PY = r'''import sys,heapq
def main():
 d=list(map(int,sys.stdin.buffer.read().split()));it=iter(d);n=next(it);w=next(it);par=[-1]+[next(it)-1 for _ in range(n-1)];offers=[]
 for _ in range(w):offers.append([(next(it)-1,next(it)) for _ in range(next(it))])
 N=1+w+n+1;S=0;T=N-1;g=[[] for _ in range(N)]
 def add(u,v,cap,c):g[u].append([v,cap,c,len(g[v])]);g[v].append([u,0,-c,len(g[u])-1])
 for i,o in enumerate(offers):
  add(S,1+i,1,0)
  for v,c in o:add(1+i,1+w+v,1,c)
 child=[0]*n
 for v in range(1,n):add(1+w+par[v],1+w+v,w,0);child[par[v]]+=1
 for v in range(n):
  if not child[v]:add(1+w+v,T,1,0)
 pot=[0]*N;cost=flow=0;INF=10**30
 while flow<w:
  dist=[INF]*N;dist[S]=0;prev=[None]*N;pq=[(0,S)]
  while pq:
   du,u=heapq.heappop(pq)
   if du!=dist[u]:continue
   for ei,e in enumerate(g[u]):
    if e[1] and du+e[2]+pot[u]-pot[e[0]]<dist[e[0]]:dist[e[0]]=du+e[2]+pot[u]-pot[e[0]];prev[e[0]]=(u,ei);heapq.heappush(pq,(dist[e[0]],e[0]))
  if dist[T]==INF:print('IMPOSSIBLE');return
  for v in range(N):
   if dist[v]<INF:pot[v]+=dist[v]
  v=T
  while v!=S:u,ei=prev[v];e=g[u][ei];e[1]-=1;g[v][e[3]][1]+=1;cost+=e[2];v=u
  flow+=1
 print(cost)
if __name__=='__main__':main()
'''

P20_CPP = r'''#include <bits/stdc++.h>
using namespace std;using ll=long long;struct E{int v,cap,rev;ll c;};int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,w;if(!(cin>>n>>w))return 0;vector<int>p(n,-1),ch(n);for(int i=1;i<n;i++){cin>>p[i];--p[i];ch[p[i]]++;}int N=1+w+n+1,S=0,T=N-1;vector<vector<E>>g(N);auto add=[&](int u,int v,int z,ll c){g[u].push_back({v,z,(int)g[v].size(),c});g[v].push_back({u,0,(int)g[u].size()-1,-c});};for(int i=0;i<w;i++){add(S,1+i,1,0);int z;cin>>z;while(z--){int v;ll c;cin>>v>>c;add(1+i,1+w+v-1,1,c);}}for(int v=1;v<n;v++)add(1+w+p[v],1+w+v,w,0);for(int v=0;v<n;v++)if(!ch[v])add(1+w+v,T,1,0);const ll INF=4e18;vector<ll>pot(N);ll cost=0;int flow=0;while(flow<w){vector<ll>d(N,INF);vector<int>pv(N),pe(N);priority_queue<pair<ll,int>,vector<pair<ll,int>>,greater<pair<ll,int>>>q;d[S]=0;q.push({0,S});while(!q.empty()){auto [du,u]=q.top();q.pop();if(du!=d[u])continue;for(int i=0;i<(int)g[u].size();i++){auto&e=g[u][i];ll nd=du+e.c+pot[u]-pot[e.v];if(e.cap&&nd<d[e.v])d[e.v]=nd,pv[e.v]=u,pe[e.v]=i,q.push({nd,e.v});}}if(d[T]==INF){cout<<"IMPOSSIBLE\n";return 0;}for(int i=0;i<N;i++)if(d[i]<INF)pot[i]+=d[i];for(int v=T;v!=S;v=pv[v]){auto&e=g[pv[v]][pe[v]];cost+=e.c;e.cap--;g[v][e.rev].cap++;}flow++;}cout<<cost<<'\n';}
'''

P20_RANDOM = r'''import argparse,itertools,random
from pathlib import Path
def case(r):
 n=r.randint(1,9);p=[-1]+[r.randrange(v) for v in range(1,n)];kids=[[] for _ in range(n)]
 for v in range(1,n):kids[p[v]].append(v)
 leaves=[v for v in range(n) if not kids[v]];w=r.randint(1,min(5,len(leaves)+1));desc=[]
 for v in range(n):
  st=[v];z=[]
  while st:
   x=st.pop()
   if not kids[x]:z.append(x)
   st+=kids[x]
  desc.append(z)
 offers=[]
 for _ in range(w):offers.append([(r.randrange(n),r.randint(0,12)) for _ in range(r.randint(1,4))])
 best=None
 for ass in itertools.permutations(leaves,w) if w<=len(leaves) else []:
  val=0;ok=True
  for i,x in enumerate(ass):
   z=[c for v,c in offers[i] if x in desc[v]]
   if not z:ok=False;break
   val+=min(z)
  if ok:best=val if best is None else min(best,val)
 text=f"{n} {w}\n"+(' '.join(str(x+1) for x in p[1:])+'\n' if n>1 else '\n')+''.join(str(len(o))+' '+ ' '.join(f"{v+1} {c}" for v,c in o)+'\n' for o in offers)
 return text,('IMPOSSIBLE\n' if best is None else f'{best}\n')
def main():
 p=argparse.ArgumentParser();p.add_argument('--count',type=int,default=25);p.add_argument('--seed',type=int,default=1);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);r=random.Random(a.seed)
 for i in range(a.count):x,y=case(r);s=a.out_dir/f"case{i:03d}";s.with_suffix('.in').write_text(x);s.with_suffix('.out').write_text(y)
if __name__=='__main__':main()
'''


PACKAGES = {
    "18_circulation_repair_queries": ("Circulation Repair Queries", P18_README, P18_CPP, P18_PY, P18_RANDOM,
        "3 2 2\n1 2 0 1 0\n2 3 0 1 0\n3 1\n1 3\n", "YES\nNO\n"),
    "19_convex_resource_schedule": ("Convex Resource Schedule", P19_README, P19_CPP, P19_PY, P19_RANDOM,
        "5 3\n2 1 4 1 2\n", "34\n"),
    "20_laminar_assignment": ("Laminar Assignment", P20_README, P20_CPP, P20_PY, P20_RANDOM,
        "5 2\n1 1 2 2\n2 2 7 3 1\n1 2 4\n", "5\n"),
}


def main() -> None:
    for slug, (title, readme, cpp, py, random_cases, sample_in, sample_out) in PACKAGES.items():
        directory = BASE / slug
        tests = directory / "tests"
        tests.mkdir(parents=True, exist_ok=True)
        (directory / "README.md").write_text(readme)
        (directory / "manifest.json").write_text(
            f'{{"title":"{title}","checker":"tokens","time_limit_seconds":20}}\n'
        )
        (directory / "solution.cpp").write_text(cpp)
        (directory / "solution.py").write_text(py)
        (directory / "solve.cpp").write_text(STUB_CPP)
        (directory / "solve.py").write_text(STUB_PY)
        (tests / "sample1.in").write_text(sample_in)
        (tests / "sample1.out").write_text(sample_out)
        (tests / "random_cases.py").write_text(random_cases)


if __name__ == "__main__":
    main()
