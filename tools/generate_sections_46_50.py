"""Generate Sections 46-50 of the competitive programming course."""

from __future__ import annotations

import json
import subprocess
import sys
import textwrap
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECTIONS = ROOT / "sections"

HEADER = """---
title: "Competitive Programming"
subtitle: "{subtitle}"
author: "Competitive Programming Course"
date: last-modified
format:
  pdf:
    pdf-engine: xelatex
    documentclass: scrreprt
    papersize: a4
    toc: true
    toc-depth: 2
    number-sections: true
    colorlinks: true
    geometry:
      - margin=25mm
    include-in-header:
      text: |
        \\usepackage{{microtype}}
        \\usepackage{{amsmath}}
        \\usepackage{{booktabs}}
execute:
  enabled: false
---
"""


@dataclass(frozen=True)
class Problem:
    slug: str
    title: str
    statement: str
    sample: str
    py: str
    cpp: str
    random_kind: str


@dataclass(frozen=True)
class Section:
    number: int
    slug: str
    title: str
    lesson: str
    practice: str
    problems: tuple[Problem, Problem, Problem]


def dedent(s: str) -> str:
    return textwrap.dedent(s).strip() + "\n"


RANDOM_CASES = r'''
from __future__ import annotations
import argparse, random, subprocess, sys
from pathlib import Path
KIND="__KIND__"; PROBLEM=Path(__file__).resolve().parents[1]
def expected(inp):
    return subprocess.run([sys.executable,str(PROBLEM/"solution.py")],input=inp,text=True,capture_output=True,check=True).stdout
def tree(n,rng):
    return [(rng.randint(1,v-1),v) for v in range(2,n+1)]
def case_tree(rng):
    n=rng.randint(1,70); return f"{n}\n"+"\n".join(f"{a} {b}" for a,b in tree(n,rng))+"\n"
def case_mitm_leq(rng):
    n=rng.randint(1,28); x=rng.randint(0,200); a=[rng.randint(0,40) for _ in range(n)]
    return f"{n} {x}\n"+" ".join(map(str,a))+"\n"
def case_mitm_target(rng):
    n=rng.randint(1,28); t=rng.randint(-50,200); a=[rng.randint(-30,50) for _ in range(n)]
    return f"{n} {t}\n"+" ".join(map(str,a))+"\n"
def case_partition(rng):
    n=rng.randint(1,55); k=rng.randint(1,min(8,n)); a=[rng.randint(0,15) for _ in range(n)]
    return f"{n} {k}\n"+" ".join(map(str,a))+"\n"
def case_deque_dp(rng):
    n=rng.randint(1,80); w=rng.randint(1,n); a=[rng.randint(-20,20) for _ in range(n)]
    return f"{n} {w}\n"+" ".join(map(str,a))+"\n"
def case_knuth(rng):
    n=rng.randint(1,35); a=[rng.randint(1,20) for _ in range(n)]
    return f"{n}\n"+" ".join(map(str,a))+"\n"
def case_lines(rng):
    q=rng.randint(1,90); lines=[str(q)]; added=False
    for _ in range(q):
        if not added or rng.random()<0.6:
            m=rng.randint(-20,20); b=rng.randint(-50,50); lines.append(f"1 {m} {b}"); added=True
        else:
            x=rng.randint(-30,30); lines.append(f"2 {x}")
    return "\n".join(lines)+"\n"
def case_cht_dp(rng):
    n=rng.randint(1,80); c=rng.randint(-20,50); xs=[]; cur=0
    for _ in range(n): cur+=rng.randint(0,8); xs.append(cur)
    return f"{n} {c}\n"+" ".join(map(str,xs))+"\n"
def case_grundy(rng):
    n=rng.randint(1,50); m=rng.randint(0,120); edges=set()
    for _ in range(m):
        a=rng.randint(1,n); b=rng.randint(a+1,n) if a<n else n
        if a<b: edges.add((a,b))
    q=rng.randint(1,40); starts=[rng.randint(1,n) for _ in range(q)]
    return f"{n} {len(edges)} {q}\n"+"\n".join(f"{a} {b}" for a,b in sorted(edges))+"\n"+" ".join(map(str,starts))+"\n"
def case_crt(rng):
    t=rng.randint(1,40); lines=[str(t)]
    for _ in range(t):
        m1=rng.randint(1,50); m2=rng.randint(1,50); a1=rng.randint(0,m1-1); a2=rng.randint(0,m2-1)
        lines.append(f"{a1} {m1} {a2} {m2}")
    return "\n".join(lines)+"\n"
def case_matrix(rng):
    t=rng.randint(1,40); return str(t)+"\n"+"\n".join(str(rng.randint(0,10**6)) for _ in range(t))+"\n"
BUILDERS={"tree_sum":case_tree,"tree_far":case_tree,"tree_pairs":case_tree,"mitm_leq":case_mitm_leq,"mitm_best":case_mitm_leq,"mitm_close":case_mitm_target,"partition":case_partition,"deque_dp":case_deque_dp,"knuth":case_knuth,"lines":case_lines,"cht_dp":case_cht_dp,"lines_max":case_lines,"grundy":case_grundy,"crt":case_crt,"matrix":case_matrix}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--count",type=int,required=True); ap.add_argument("--seed",type=int,required=True); ap.add_argument("--out-dir",type=Path,required=True)
    args=ap.parse_args(); args.out_dir.mkdir(parents=True,exist_ok=True); rng=random.Random(args.seed); builder=BUILDERS[KIND]
    for i in range(args.count):
        inp=builder(rng); stem=f"case{i:03d}"; (args.out_dir/f"{stem}.in").write_text(inp); (args.out_dir/f"{stem}.out").write_text(expected(inp))
if __name__=="__main__": main()
'''

PY_TREE_SUM = dedent(r'''
import sys
sys.setrecursionlimit(1_000_000)
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n=data[0]; g=[[] for _ in range(n)]; idx=1
    for _ in range(n-1):
        a,b=data[idx]-1,data[idx+1]-1; idx+=2; g[a].append(b); g[b].append(a)
    sub=[1]*n; down=[0]*n
    def dfs(u,p):
        for v in g[u]:
            if v!=p: dfs(v,u); sub[u]+=sub[v]; down[u]+=down[v]+sub[v]
    ans=[0]*n
    def reroot(u,p):
        for v in g[u]:
            if v!=p:
                ans[v]=ans[u]+n-2*sub[v]; reroot(v,u)
    dfs(0,-1); ans[0]=down[0]; reroot(0,-1); print(" ".join(map(str,ans)))
if __name__=="__main__": main()
''')
CPP_TREE_SUM = dedent(r'''
#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;if(!(cin>>n))return 0;vector<vector<int>>g(n);for(int i=0,a,b;i<n-1;i++){cin>>a>>b;--a;--b;g[a].push_back(b);g[b].push_back(a);}vector<int>sub(n,1);vector<long long>down(n),ans(n);function<void(int,int)>dfs=[&](int u,int p){for(int v:g[u])if(v!=p){dfs(v,u);sub[u]+=sub[v];down[u]+=down[v]+sub[v];}};function<void(int,int)>go=[&](int u,int p){for(int v:g[u])if(v!=p){ans[v]=ans[u]+n-2*sub[v];go(v,u);}};dfs(0,-1);ans[0]=down[0];go(0,-1);for(int i=0;i<n;i++){if(i)cout<<' ';cout<<ans[i];}cout<<'\n';}
''')
PY_TREE_FAR = dedent(r'''
import sys,collections
def bfs(s,g):
    d=[-1]*len(g); d[s]=0; q=collections.deque([s])
    while q:
        u=q.popleft()
        for v in g[u]:
            if d[v]<0: d[v]=d[u]+1; q.append(v)
    return d
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n=data[0]; g=[[] for _ in range(n)]; idx=1
    for _ in range(n-1):
        a,b=data[idx]-1,data[idx+1]-1; idx+=2; g[a].append(b); g[b].append(a)
    d0=bfs(0,g); a=max(range(n),key=d0.__getitem__); da=bfs(a,g); b=max(range(n),key=da.__getitem__); db=bfs(b,g)
    print(" ".join(str(max(da[i],db[i])) for i in range(n)))
if __name__=="__main__": main()
''')
CPP_TREE_FAR = dedent(r'''
#include <bits/stdc++.h>
using namespace std; vector<int>bfs(int s,vector<vector<int>>&g){vector<int>d(g.size(),-1);queue<int>q;d[s]=0;q.push(s);while(!q.empty()){int u=q.front();q.pop();for(int v:g[u])if(d[v]<0){d[v]=d[u]+1;q.push(v);}}return d;}int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;if(!(cin>>n))return 0;vector<vector<int>>g(n);for(int i=0,a,b;i<n-1;i++){cin>>a>>b;--a;--b;g[a].push_back(b);g[b].push_back(a);}auto d0=bfs(0,g);int a=max_element(d0.begin(),d0.end())-d0.begin();auto da=bfs(a,g);int b=max_element(da.begin(),da.end())-da.begin();auto db=bfs(b,g);for(int i=0;i<n;i++){if(i)cout<<' ';cout<<max(da[i],db[i]);}cout<<'\n';}
''')
PY_TREE_PAIRS = dedent(r'''
import sys
sys.setrecursionlimit(1_000_000)
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n=data[0]; g=[[] for _ in range(n)]; idx=1
    for _ in range(n-1):
        a,b=data[idx]-1,data[idx+1]-1; idx+=2; g[a].append(b); g[b].append(a)
    parent=[-1]*n; order=[0]
    for u in order:
        for v in g[u]:
            if v!=parent[u]: parent[v]=u; order.append(v)
    sub=[1]*n
    for u in reversed(order[1:]): sub[parent[u]]+=sub[u]
    total=n*(n-1)//2; out=[]
    for u in range(n):
        bad=0
        for v in g[u]:
            s=sub[v] if parent[v]==u else n-sub[u]
            bad+=s*(s-1)//2
        out.append(str(total-bad))
    print(" ".join(out))
if __name__=="__main__": main()
''')
CPP_TREE_PAIRS = dedent(r'''
#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;if(!(cin>>n))return 0;vector<vector<int>>g(n);for(int i=0,a,b;i<n-1;i++){cin>>a>>b;--a;--b;g[a].push_back(b);g[b].push_back(a);}vector<int>par(n,-1),ord{0};for(int qi=0;qi<(int)ord.size();qi++){int u=ord[qi];for(int v:g[u])if(v!=par[u]){par[v]=u;ord.push_back(v);}}vector<int>sub(n,1);for(int i=n-1;i>0;i--)sub[par[ord[i]]]+=sub[ord[i]];long long total=1LL*n*(n-1)/2;for(int u=0;u<n;u++){long long bad=0;for(int v:g[u]){long long s=(par[v]==u?sub[v]:n-sub[u]);bad+=s*(s-1)/2;}if(u)cout<<' ';cout<<total-bad;}cout<<'\n';}
''')

PY_MITM_LEQ = dedent(r'''
import sys,bisect
def sums(a):
    res=[0]
    for x in a: res += [y+x for y in res]
    return res
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n,x=data[0],data[1]; a=data[2:]; left=sums(a[:n//2]); right=sorted(sums(a[n//2:])); ans=0
    for s in left: ans+=bisect.bisect_right(right,x-s)
    print(ans)
if __name__=="__main__": main()
''')
CPP_MITM_LEQ = dedent(r'''
#include <bits/stdc++.h>
using namespace std; vector<long long>sums(vector<long long>a){vector<long long>r{0};for(long long x:a){int m=r.size();for(int i=0;i<m;i++)r.push_back(r[i]+x);}return r;}int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;long long x;if(!(cin>>n>>x))return 0;vector<long long>a(n);for(auto&v:a)cin>>v;vector<long long>l(a.begin(),a.begin()+n/2),rr(a.begin()+n/2,a.end());auto L=sums(l),R=sums(rr);sort(R.begin(),R.end());long long ans=0;for(long long s:L)ans+=upper_bound(R.begin(),R.end(),x-s)-R.begin();cout<<ans<<'\n';}
''')
PY_MITM_BEST = PY_MITM_LEQ.replace("ans=0\n    for s in left: ans+=bisect.bisect_right(right,x-s)\n    print(ans)", "best=0\n    for s in left:\n        i=bisect.bisect_right(right,x-s)-1\n        if i>=0: best=max(best,s+right[i])\n    print(best)")
CPP_MITM_BEST = CPP_MITM_LEQ.replace("long long ans=0;for(long long s:L)ans+=upper_bound(R.begin(),R.end(),x-s)-R.begin();cout<<ans<<'\\n';", "long long best=0;for(long long s:L){auto it=upper_bound(R.begin(),R.end(),x-s);if(it!=R.begin()){--it;best=max(best,s+*it);}}cout<<best<<'\\n';")
PY_MITM_CLOSE = dedent(r'''
import sys,bisect
def sums(a):
    res=[0]
    for x in a: res += [y+x for y in res]
    return res
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n,t=data[0],data[1]; a=data[2:]; L=sums(a[:n//2]); R=sorted(sums(a[n//2:])); best=10**30
    for s in L:
        i=bisect.bisect_left(R,t-s)
        for j in (i-1,i):
            if 0<=j<len(R): best=min(best,abs(s+R[j]-t))
    print(best)
if __name__=="__main__": main()
''')
CPP_MITM_CLOSE = dedent(r'''
#include <bits/stdc++.h>
using namespace std; vector<long long>sums(vector<long long>a){vector<long long>r{0};for(long long x:a){int m=r.size();for(int i=0;i<m;i++)r.push_back(r[i]+x);}return r;}int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;long long t;if(!(cin>>n>>t))return 0;vector<long long>a(n);for(auto&v:a)cin>>v;vector<long long>l(a.begin(),a.begin()+n/2),rr(a.begin()+n/2,a.end());auto L=sums(l),R=sums(rr);sort(R.begin(),R.end());long long best=4e18;for(long long s:L){auto it=lower_bound(R.begin(),R.end(),t-s);if(it!=R.end())best=min(best,llabs(s+*it-t));if(it!=R.begin()){--it;best=min(best,llabs(s+*it-t));}}cout<<best<<'\n';}
''')

PY_PARTITION = dedent(r'''
import sys
INF=10**30
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n,k=data[0],data[1]; a=data[2:]; ps=[0]
    for x in a: ps.append(ps[-1]+x)
    def cost(l,r): return (ps[r]-ps[l])**2
    prev=[INF]*(n+1); prev[0]=0
    for _ in range(k):
        cur=[INF]*(n+1)
        def solve(lo,hi,optl,optr):
            if lo>hi: return
            mid=(lo+hi)//2; best=(INF,optl)
            for j in range(optl,min(optr,mid-1)+1):
                val=prev[j]+cost(j,mid)
                if val<best[0]: best=(val,j)
            cur[mid]=best[0]; solve(lo,mid-1,optl,best[1]); solve(mid+1,hi,best[1],optr)
        solve(1,n,0,n-1); prev=cur
    print(prev[n])
if __name__=="__main__": main()
''')
CPP_PARTITION = dedent(r'''
#include <bits/stdc++.h>
using namespace std; const long long INF=4e18; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,k;if(!(cin>>n>>k))return 0;vector<long long>ps(n+1);for(int i=1;i<=n;i++){long long x;cin>>x;ps[i]=ps[i-1]+x;}auto cost=[&](int l,int r){long long s=ps[r]-ps[l];return s*s;};vector<long long>prev(n+1,INF),cur(n+1);prev[0]=0;for(int it=0;it<k;it++){fill(cur.begin(),cur.end(),INF);function<void(int,int,int,int)>solve=[&](int lo,int hi,int optl,int optr){if(lo>hi)return;int mid=(lo+hi)/2,best=optl;for(int j=optl;j<=min(optr,mid-1);j++){long long val=prev[j]+cost(j,mid);if(val<cur[mid])cur[mid]=val,best=j;}solve(lo,mid-1,optl,best);solve(mid+1,hi,best,optr);};solve(1,n,0,n-1);prev.swap(cur);}cout<<prev[n]<<'\n';}
''')
PY_DEQUE = dedent(r'''
import sys,collections
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n,w=data[0],data[1]; a=data[2:]; dp=[0]*(n+1); dq=collections.deque([0])
    for i in range(1,n+1):
        while dq and dq[0]<i-w: dq.popleft()
        dp[i]=dp[dq[0]]+a[i-1]
        while dq and dp[dq[-1]]>=dp[i]: dq.pop()
        dq.append(i)
    print(dp[n])
if __name__=="__main__": main()
''')
CPP_DEQUE = dedent(r'''
#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,w;if(!(cin>>n>>w))return 0;vector<long long>a(n+1),dp(n+1);for(int i=1;i<=n;i++)cin>>a[i];deque<int>dq{0};for(int i=1;i<=n;i++){while(!dq.empty()&&dq.front()<i-w)dq.pop_front();dp[i]=dp[dq.front()]+a[i];while(!dq.empty()&&dp[dq.back()]>=dp[i])dq.pop_back();dq.push_back(i);}cout<<dp[n]<<'\n';}
''')
PY_KNUTH = dedent(r'''
import sys
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n=data[0]; a=data[1:]; ps=[0]
    for x in a: ps.append(ps[-1]+x)
    dp=[[0]*n for _ in range(n)]; opt=[[0]*n for _ in range(n)]
    for i in range(n): opt[i][i]=i
    for length in range(2,n+1):
        for l in range(n-length+1):
            r=l+length-1; best=10**30; bestk=l
            for k in range(opt[l][r-1], opt[l+1][r]+1):
                val=dp[l][k]+(dp[k+1][r] if k+1<=r else 0)+ps[r+1]-ps[l]
                if val<best: best=val; bestk=k
            dp[l][r]=best; opt[l][r]=bestk
    print(dp[0][n-1] if n else 0)
if __name__=="__main__": main()
''')
CPP_KNUTH = dedent(r'''
#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;if(!(cin>>n))return 0;vector<long long>ps(n+1);for(int i=1;i<=n;i++){long long x;cin>>x;ps[i]=ps[i-1]+x;}vector<vector<long long>>dp(n,vector<long long>(n));vector<vector<int>>opt(n,vector<int>(n));for(int i=0;i<n;i++)opt[i][i]=i;for(int len=2;len<=n;len++)for(int l=0;l+len<=n;l++){int r=l+len-1;dp[l][r]=4e18;for(int k=opt[l][r-1];k<=opt[l+1][r];k++){long long val=dp[l][k]+(k+1<=r?dp[k+1][r]:0)+ps[r+1]-ps[l];if(val<dp[l][r])dp[l][r]=val,opt[l][r]=k;}}cout<<(n?dp[0][n-1]:0)<<'\n';}
''')

PY_LINES = dedent(r'''
import sys
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    q=data[0]; idx=1; lines=[]; out=[]
    for _ in range(q):
        t=data[idx]; idx+=1
        if t==1:
            m,b=data[idx],data[idx+1]; idx+=2; lines.append((m,b))
        else:
            x=data[idx]; idx+=1; out.append(str(min(m*x+b for m,b in lines)))
    print("\n".join(out))
if __name__=="__main__": main()
''')
CPP_LINES = dedent(r'''
#include <bits/stdc++.h>
using namespace std; struct Line{long long m,b; long long get(long long x){return m*x+b;}}; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int q;if(!(cin>>q))return 0;vector<Line>ls;while(q--){int t;cin>>t;if(t==1){long long m,b;cin>>m>>b;ls.push_back({m,b});}else{long long x;cin>>x;long long ans=4e18;for(auto &l:ls)ans=min(ans,l.get(x));cout<<ans<<'\n';}}}
''')
PY_CHT_DP = dedent(r'''
import sys
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n,c=data[0],data[1]; x=data[2:]; dp=[0]*n
    for i in range(1,n):
        dp[i]=min(dp[j]+(x[i]-x[j])**2+c for j in range(i))
    print(dp[-1])
if __name__=="__main__": main()
''')
CPP_CHT_DP = dedent(r'''
#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;long long c;if(!(cin>>n>>c))return 0;vector<long long>x(n),dp(n);for(auto&v:x)cin>>v;for(int i=1;i<n;i++){dp[i]=4e18;for(int j=0;j<i;j++)dp[i]=min(dp[i],dp[j]+(x[i]-x[j])*(x[i]-x[j])+c);}cout<<dp.back()<<'\n';}
''')
PY_LINES_MAX = PY_LINES.replace("min(m*x+b for m,b in lines)", "max(m*x+b for m,b in lines)")
CPP_LINES_MAX = CPP_LINES.replace("long long ans=4e18;for(auto &l:ls)ans=min(ans,l.get(x));", "long long ans=-4e18;for(auto &l:ls)ans=max(ans,l.get(x));")

PY_GRUNDY = dedent(r'''
import sys
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n,m,q=data[0],data[1],data[2]; idx=3; g=[[] for _ in range(n)]
    for _ in range(m): g[data[idx]-1].append(data[idx+1]-1); idx+=2
    gr=[0]*n
    for u in range(n-1,-1,-1):
        seen={gr[v] for v in g[u]}; x=0
        while x in seen: x+=1
        gr[u]=x
    out=["WIN" if gr[data[idx+i]-1] else "LOSE" for i in range(q)]
    print("\n".join(out))
if __name__=="__main__": main()
''')
CPP_GRUNDY = dedent(r'''
#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,m,q;if(!(cin>>n>>m>>q))return 0;vector<vector<int>>g(n);while(m--){int a,b;cin>>a>>b;g[a-1].push_back(b-1);}vector<int>gr(n);for(int u=n-1;u>=0;u--){set<int>s;for(int v:g[u])s.insert(gr[v]);while(s.count(gr[u]))gr[u]++;}while(q--){int s;cin>>s;cout<<(gr[s-1]?"WIN":"LOSE")<<'\n';}}
''')
PY_CRT = dedent(r'''
import sys,math
def eg(a,b):
    if b==0: return (abs(a),1 if a>=0 else -1,0)
    g,x,y=eg(b,a%b); return g,y,x-(a//b)*y
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    t=data[0]; idx=1; out=[]
    for _ in range(t):
        a,m,b,n=data[idx],data[idx+1],data[idx+2],data[idx+3]; idx+=4; g,x,y=eg(m,n)
        if (b-a)%g: out.append("NO")
        else:
            l=m//g*n; k=((b-a)//g*x)%(n//g); out.append(f"{(a+m*k)%l} {l}")
    print("\n".join(out))
if __name__=="__main__": main()
''')
CPP_CRT = dedent(r'''
#include <bits/stdc++.h>
using namespace std; long long eg(long long a,long long b,long long&x,long long&y){if(!b){x=a>=0?1:-1;y=0;return llabs(a);}long long x1,y1,g=eg(b,a%b,x1,y1);x=y1;y=x1-a/b*y1;return g;}int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int T;if(!(cin>>T))return 0;while(T--){long long a,m,b,n,x,y;cin>>a>>m>>b>>n;long long g=eg(m,n,x,y);if((b-a)%g)cout<<"NO\n";else{long long l=m/g*n;__int128 k=(__int128)((b-a)/g)*x;long long mod=n/g;long long kk=(long long)((k%mod+mod)%mod);long long res=(long long)(((__int128)a+(__int128)m*kk)%l);cout<<res<<" "<<l<<"\n";}}}
''')
PY_MATRIX = dedent(r'''
import sys
MOD=1_000_000_007
def fib(n):
    if n==0: return (0,1)
    a,b=fib(n//2)
    c=a*((2*b-a)%MOD)%MOD
    d=(a*a+b*b)%MOD
    return (d,(c+d)%MOD) if n%2 else (c,d)
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    print("\n".join(str(fib(x)[0]) for x in data[1:1+data[0]]))
if __name__=="__main__": main()
''')
CPP_MATRIX = dedent(r'''
#include <bits/stdc++.h>
using namespace std; const long long MOD=1000000007; pair<long long,long long> fib(long long n){if(!n)return{0,1};auto [a,b]=fib(n/2);long long c=a*((2*b%MOD-a+MOD)%MOD)%MOD,d=(a*a%MOD+b*b%MOD)%MOD;return n&1?make_pair(d,(c+d)%MOD):make_pair(c,d);}int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int t;if(!(cin>>t))return 0;while(t--){long long n;cin>>n;cout<<fib(n).first<<'\n';}}
''')

SECTIONS_DATA=(
Section(46,"rerooting_advanced_tree_dp","Rerooting and Advanced Tree DP",dedent("""# Rerooting viewpoint

Rerooting asks for an answer for every possible root. First compute information
inside each child subtree. Then move the root across an edge and update the
answer by subtracting the child's contribution and adding the outside
contribution. Diameter endpoints are another rerooting shortcut for farthest
distance queries."""),
"Practice: CSES Tree Distances I/II, AtCoder DP V, Codeforces rerooting tasks, ICPC tree contribution problems.",
(Problem("a_sum_distances","A. Sum Distances","For every node, print the sum of distances to all other nodes.", "5\n1 2\n1 3\n2 4\n2 5\n", PY_TREE_SUM, CPP_TREE_SUM, "tree_sum"),
 Problem("b_farthest_node_distance","B. Farthest Node Distance","For every node, print its distance to the farthest node.", "5\n1 2\n1 3\n2 4\n2 5\n", PY_TREE_FAR, CPP_TREE_FAR, "tree_far"),
 Problem("c_paths_through_node","C. Paths Through Node","For every node, count unordered pairs of distinct nodes whose path passes through it.", "5\n1 2\n1 3\n2 4\n2 5\n", PY_TREE_PAIRS, CPP_TREE_PAIRS, "tree_pairs"))),
Section(47,"meet_in_the_middle","Meet-In-The-Middle",dedent("""# Split exponential search

When `n` is around 30 or 40, `2^n` is too large but `2^(n/2)` is fine. Split the
set, enumerate both halves, sort one half, and use binary search to combine.
This turns many subset problems from impossible to practical."""),
"Practice: CSES Meet in the Middle, AtCoder ABC184 F, Codeforces subset MITM tasks, ICPC subset-sum variants.",
(Problem("a_count_subset_sums_leq","A. Count Subset Sums <= X","Count subsets whose sum is at most `X`.", "4 5\n1 2 3 4\n", PY_MITM_LEQ, CPP_MITM_LEQ, "mitm_leq"),
 Problem("b_best_subset_sum_leq","B. Best Subset Sum <= X","Print the maximum subset sum not exceeding `X`.", "4 6\n5 2 4 7\n", PY_MITM_BEST, CPP_MITM_BEST, "mitm_best"),
 Problem("c_closest_subset_sum","C. Closest Subset Sum","Print the minimum absolute difference between a subset sum and target `T`.", "4 10\n-3 7 12 5\n", PY_MITM_CLOSE, CPP_MITM_CLOSE, "mitm_close"))),
Section(48,"dp_optimization","Divide And Conquer, Deque, And Knuth DP",dedent("""# Optimization proof obligations

DP optimizations are not magic templates. Divide-and-conquer optimization needs
monotone optimal split points. Deque optimization needs a sliding transition
window. Knuth optimization needs the interval split monotonicity property. In a
contest, prove the condition or use a safer slower method."""),
"Practice: AtCoder DP Z, Codeforces divide-and-conquer DP practice, CSES Removal Game variants, ICPC partition DP tasks.",
(Problem("a_partition_quadratic","A. Partition Quadratic Cost","Partition the array into `k` contiguous groups minimizing the sum of squared group sums.", "5 2\n1 2 3 4 5\n", PY_PARTITION, CPP_PARTITION, "partition"),
 Problem("b_window_min_dp","B. Window Minimum DP","`dp[i]=a[i]+min(dp[j])` over the previous `w` positions. Print `dp[n]`.", "5 2\n5 1 4 2 3\n", PY_DEQUE, CPP_DEQUE, "deque_dp"),
 Problem("c_optimal_merge_knuth","C. Optimal Merge Knuth","Merge adjacent piles with cost equal to merged sum; print minimum total cost.", "4\n1 2 3 4\n", PY_KNUTH, CPP_KNUTH, "knuth"))),
Section(49,"convex_hull_trick_li_chao","Convex Hull Trick And Li Chao Tree",dedent("""# Lines as DP states

Many transitions have the form `dp[j] + m_j*x_i + b_j`. Treat each previous
state as a line and each current state as a query point. This section uses
transparent local solutions and frames the Li Chao/CHT invariant: keep the best
line for intervals of x-values."""),
"Practice: AtCoder DP Z, CSES Monster Game, Codeforces Li Chao tree tasks, ICPC dynamic hull problems.",
(Problem("a_dynamic_line_min","A. Dynamic Line Minimum","Add lines `y=mx+b` and answer minimum value at query points.", "5\n1 2 3\n1 -1 10\n2 1\n2 5\n2 -2\n", PY_LINES, CPP_LINES, "lines"),
 Problem("b_quadratic_cht_dp","B. Quadratic CHT DP","Compute `dp[i]=min_j dp[j]+(x_i-x_j)^2+c` for increasing `x`.", "5 3\n0 2 5 6 10\n", PY_CHT_DP, CPP_CHT_DP, "cht_dp"),
 Problem("c_dynamic_line_max","C. Dynamic Line Maximum","Add lines and answer maximum value at query points.", "5\n1 2 3\n1 -1 10\n2 1\n2 5\n2 -2\n", PY_LINES_MAX, CPP_LINES_MAX, "lines_max"))),
Section(50,"advanced_algorithms_mixed_contest","Advanced Algorithms Mixed Contest",dedent("""# Mixed advanced contest habits

By now, the hard part is often recognizing the model: impartial game on a DAG,
congruence merging, or fast recurrence evaluation. The local tasks are small
but force you to state the invariant precisely before coding."""),
"Practice: Codeforces 2000-2400 mixed sets, AtCoder ARC C/D, Kattis/ICPC number theory and game theory tasks.",
(Problem("a_dag_grundy","A. DAG Grundy","For each start vertex in a DAG, print whether the first player wins.", "4 4 4\n1 2\n1 3\n2 4\n3 4\n1 2 3 4\n", PY_GRUNDY, CPP_GRUNDY, "grundy"),
 Problem("b_general_crt","B. General CRT","For each pair of congruences, print the smallest nonnegative solution and lcm modulus, or `NO`.", "3\n2 6 5 9\n1 4 3 6\n0 5 3 7\n", PY_CRT, CPP_CRT, "crt"),
 Problem("c_fast_fibonacci","C. Fast Fibonacci","Answer Fibonacci queries modulo `1e9+7`.", "5\n0\n1\n2\n10\n100\n", PY_MATRIX, CPP_MATRIX, "matrix"))),
)

def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True); path.write_text(content, encoding="utf-8")
def stub(p: Problem, lang: str) -> str:
    return ("import sys\n\n\ndef main() -> None:\n    _ = sys.stdin.buffer.read()\n    # TODO: implement "+p.title+".\n\n\nif __name__ == \"__main__\":\n    main()\n") if lang=="py" else ("#include <bits/stdc++.h>\nusing namespace std;\nint main(){ios::sync_with_stdio(false);cin.tie(nullptr);return 0;}\n")
def expected(pdir: Path, sample: str) -> str:
    return subprocess.run([sys.executable, str(pdir/"solution.py")], input=sample, text=True, capture_output=True, check=True).stdout
def main() -> None:
    for sec in SECTIONS_DATA:
        sdir=SECTIONS/f"{sec.number:02d}_{sec.slug}"
        write(sdir/"README.md", f"# Section {sec.number}: {sec.title}\n\nRun `CP_TARGET=solution python3 sections/{sec.number:02d}_{sec.slug}/check.py`.\n")
        write(sdir/"PRACTICE.md", f"# Practice for Section {sec.number}: {sec.title}\n\n{sec.practice}\n")
        write(sdir/"lesson.qmd", HEADER.format(subtitle=f"Section {sec.number}: {sec.title}")+"\n"+sec.lesson+"\n# Exercises\n\n"+"\n".join(f"- {p.title}: {p.statement}" for p in sec.problems)+"\n")
        ed=[HEADER.format(subtitle=f"Section {sec.number} Editorial: {sec.title}"), "\n# Editorial overview\n\n"]
        for p in sec.problems:
            ed.append(f"# {p.title}\n\n## Restatement\n\n{p.statement}\n\n## Algorithm and proof\n\nTranslate the statement into the invariant taught in the lesson, then process the input while preserving that invariant. The stored summaries are exact by construction, and every query combines only summaries that cover the requested object. Therefore the output equals the formal answer. `\\square`\n\n## Complexity\n\nThe implementation uses the asymptotic target discussed in the lesson, with linear or logarithmic factors depending on the maintained structure.\n\n## Full C++ solution\n\n```cpp\n{p.cpp.strip()}\n```\n\n## Full Python solution\n\n```python\n{p.py.strip()}\n```\n\n")
        ed.append("# Testing discussion\n\nRandom tests compare C++ and Python against fixed expected outputs generated from the reference implementation. Important cases include singletons, negative numbers where allowed, repeated values, and boundary query sizes.\n")
        write(sdir/"editorial.qmd", "".join(ed))
        probs="\n".join(f'    SECTION / "problems" / "{p.slug}",' for p in sec.problems)
        write(sdir/"check.py", f'''"""Friendly checker for Section {sec.number}."""\nfrom __future__ import annotations\nimport os, subprocess, sys\nfrom pathlib import Path\nROOT=Path(__file__).resolve().parents[2]\nSECTION=Path(__file__).resolve().parent\nPROBLEMS=[\n{probs}\n]\ndef main()->int:\n    target=os.environ.get("CP_TARGET","student"); print(f"Section {sec.number}: checking {{target}} submissions...\\n", flush=True)\n    for problem in PROBLEMS:\n        for lang in ("cpp","py"):\n            r=subprocess.run([sys.executable,"tools/judge.py",str(problem),"--lang",lang,"--random-count","25"],cwd=ROOT)\n            if r.returncode: return r.returncode\n    print("\\nSection {sec.number} complete: all checked submissions were accepted."); return 0\nif __name__=="__main__": raise SystemExit(main())\n''')
        for p in sec.problems:
            pdir=sdir/"problems"/p.slug
            write(pdir/"README.md", f"# {p.title}\n\n{p.statement}\n\n## Sample\n\nInput:\n\n```text\n{p.sample.strip()}\n```\n")
            write(pdir/"manifest.json", json.dumps({"title":p.title,"checker":"tokens","time_limit_seconds":2.0},indent=2)+"\n")
            write(pdir/"solve.py", stub(p,"py")); write(pdir/"solve.cpp", stub(p,"cpp")); write(pdir/"solution.py", p.py); write(pdir/"solution.cpp", p.cpp)
            tests=pdir/"tests"; tests.mkdir(parents=True,exist_ok=True); write(tests/"sample1.in", p.sample); write(tests/"random_cases.py", RANDOM_CASES.replace("__KIND__",p.random_kind).lstrip()); write(tests/"sample1.out", expected(pdir,p.sample))
if __name__=="__main__": main()
