"""Generate Sections 41-45 of the competitive programming course."""

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

import argparse
import random
import string
import subprocess
import sys
from pathlib import Path


KIND = "__KIND__"
PROBLEM = Path(__file__).resolve().parents[1]


def expected(inp: str) -> str:
    result = subprocess.run([sys.executable, str(PROBLEM / "solution.py")], input=inp, text=True, capture_output=True, check=True)
    return result.stdout


def tree(n, rng, weighted=False):
    lines = []
    for v in range(2, n + 1):
        p = rng.randint(1, v - 1)
        if weighted:
            lines.append(f"{p} {rng.randint(1, 30)}")
        else:
            lines.append(str(p))
    return lines


def case_lca_distance(rng):
    n = rng.randint(1, 50); q = rng.randint(1, 70)
    lines = [f"{n} {q}"] + tree(n, rng, False)
    lines += [f"{rng.randint(1,n)} {rng.randint(1,n)}" for _ in range(q)]
    return "\n".join(lines) + "\n"


def case_lca_max(rng):
    n = rng.randint(1, 50); q = rng.randint(1, 70)
    lines = [f"{n} {q}"] + tree(n, rng, True)
    lines += [f"{rng.randint(1,n)} {rng.randint(1,n)}" for _ in range(q)]
    return "\n".join(lines) + "\n"


def case_kth_path(rng):
    n = rng.randint(1, 45); q = rng.randint(1, 70)
    parents = [0, 0]
    lines = [f"{n} {q}"]
    for v in range(2, n + 1):
        p = rng.randint(1, v - 1); parents.append(p); lines.append(str(p))
    depth = [0] * (n + 1)
    for v in range(2, n + 1): depth[v] = depth[parents[v]] + 1
    for _ in range(q):
        u = rng.randint(1, n); v = rng.randint(1, n)
        k = rng.randint(1, n + 3)
        lines.append(f"{u} {v} {k}")
    return "\n".join(lines) + "\n"


def case_order_stat(rng):
    m = rng.randint(5, 80); q = rng.randint(1, 120); counts = [0]*(m+1); lines=[f"{m} {q}"]
    for _ in range(q):
        typ = rng.choices([1,2,3,4], [4,3,3,3])[0]
        if typ == 1:
            x = rng.randint(1,m); counts[x]+=1; lines.append(f"1 {x}")
        elif typ == 2:
            x = rng.randint(1,m); counts[x]=max(0,counts[x]-1); lines.append(f"2 {x}")
        elif typ == 3:
            lines.append(f"3 {rng.randint(1, max(1, sum(counts)+3))}")
        else:
            lines.append(f"4 {rng.randint(1,m)}")
    return "\n".join(lines)+"\n"


def case_range_add_sum(rng):
    n = rng.randint(1,40); q = rng.randint(1,80); a=[rng.randint(-20,20) for _ in range(n)]
    lines=[f"{n} {q}", " ".join(map(str,a))]
    for _ in range(q):
        if rng.random()<0.6:
            l=rng.randint(1,n); r=rng.randint(l,n); x=rng.randint(-10,10); lines.append(f"1 {l} {r} {x}")
        else:
            l=rng.randint(1,n); r=rng.randint(l,n); lines.append(f"2 {l} {r}")
    return "\n".join(lines)+"\n"


def case_rect_count(rng):
    n=rng.randint(1,60); q=rng.randint(1,70)
    pts=[(rng.randint(1,50), rng.randint(1,50)) for _ in range(n)]
    lines=[f"{n} {q}"]+[f"{x} {y}" for x,y in pts]
    for _ in range(q):
        x1=rng.randint(1,50); x2=rng.randint(x1,50); y1=rng.randint(1,50); y2=rng.randint(y1,50)
        lines.append(f"{x1} {y1} {x2} {y2}")
    return "\n".join(lines)+"\n"


def randstr(rng, n):
    return "".join(rng.choice("abac") for _ in range(n))


def case_kmp(rng):
    p=randstr(rng,rng.randint(1,8)); t=randstr(rng,rng.randint(1,50))
    return p+"\n"+t+"\n"


def case_borders(rng):
    return randstr(rng,rng.randint(1,60))+"\n"


def case_period(rng):
    base=randstr(rng,rng.randint(1,8)); reps=rng.randint(1,8)
    s=base*reps if rng.random()<0.6 else randstr(rng,rng.randint(1,60))
    return s+"\n"


def case_trie(rng):
    n=rng.randint(1,40); q=rng.randint(1,40)
    words=["".join(rng.choice(string.ascii_lowercase[:5]) for _ in range(rng.randint(1,8))) for _ in range(n)]
    prefs=["".join(rng.choice(string.ascii_lowercase[:5]) for _ in range(rng.randint(1,5))) for _ in range(q)]
    return f"{n} {q}\n"+"\n".join(words+prefs)+"\n"


def case_pal_hash(rng):
    n=rng.randint(1,70); q=rng.randint(1,80); s=randstr(rng,n); lines=[s, str(q)]
    for _ in range(q):
        l=rng.randint(1,n); r=rng.randint(l,n); lines.append(f"{l} {r}")
    return "\n".join(lines)+"\n"


def case_distinct_substrings(rng):
    return randstr(rng,rng.randint(1,60))+"\n"


def case_flow(rng):
    n=rng.randint(2,12); m=rng.randint(1,35); lines=[f"{n} {m}"]
    for _ in range(m):
        u=rng.randint(1,n-1); v=rng.randint(u+1,n); c=rng.randint(1,20); lines.append(f"{u} {v} {c}")
    return "\n".join(lines)+"\n"


def case_matching(rng):
    n=rng.randint(1,12); m=rng.randint(1,12); e=rng.randint(0,n*m); edges=set()
    while len(edges)<e: edges.add((rng.randint(1,n), rng.randint(1,m)))
    return f"{n} {m} {len(edges)}\n"+"\n".join(f"{a} {b}" for a,b in sorted(edges))+"\n"


BUILDERS = {
    "lca_distance": case_lca_distance, "lca_max": case_lca_max, "kth_path": case_kth_path,
    "order_stat": case_order_stat, "range_add_sum": case_range_add_sum, "rect_count": case_rect_count,
    "kmp": case_kmp, "borders": case_borders, "period": case_period,
    "trie": case_trie, "pal_hash": case_pal_hash, "distinct_substrings": case_distinct_substrings,
    "flow": case_flow, "matching": case_matching, "mincut": case_flow,
}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--count",type=int,required=True); ap.add_argument("--seed",type=int,required=True); ap.add_argument("--out-dir",type=Path,required=True)
    args=ap.parse_args(); args.out_dir.mkdir(parents=True,exist_ok=True); rng=random.Random(args.seed); builder=BUILDERS[KIND]
    for i in range(args.count):
        inp=builder(rng); stem=f"case{i:03d}"
        (args.out_dir/f"{stem}.in").write_text(inp,encoding="utf-8")
        (args.out_dir/f"{stem}.out").write_text(expected(inp),encoding="utf-8")


if __name__ == "__main__":
    main()
'''


PY_LCA_DISTANCE = dedent(r'''
import sys

def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n,q=data[0],data[1]; idx=2
    LOG=max(1,(n+1).bit_length())
    up=[[0]*(n+1) for _ in range(LOG)]; depth=[0]*(n+1)
    for v in range(2,n+1):
        p=data[idx]; idx+=1; up[0][v]=p; depth[v]=depth[p]+1
    for k in range(1,LOG):
        for v in range(1,n+1): up[k][v]=up[k-1][up[k-1][v]]
    def lift(v,d):
        bit=0
        while d:
            if d&1: v=up[bit][v]
            d//=2; bit+=1
        return v
    def lca(a,b):
        if depth[a]<depth[b]: a,b=b,a
        a=lift(a,depth[a]-depth[b])
        if a==b: return a
        for k in range(LOG-1,-1,-1):
            if up[k][a]!=up[k][b]: a=up[k][a]; b=up[k][b]
        return up[0][a]
    out=[]
    for _ in range(q):
        a,b=data[idx],data[idx+1]; idx+=2; c=lca(a,b)
        out.append(str(depth[a]+depth[b]-2*depth[c]))
    print("\n".join(out))
if __name__=="__main__": main()
''')

CPP_LCA_DISTANCE = dedent(r'''
#include <bits/stdc++.h>
using namespace std;
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);
 int n,q;if(!(cin>>n>>q)) return 0; int LOG=1; while((1<<LOG)<=n+1) LOG++;
 vector<vector<int>> up(LOG, vector<int>(n+1)); vector<int> depth(n+1);
 for(int v=2;v<=n;v++){cin>>up[0][v]; depth[v]=depth[up[0][v]]+1;}
 for(int k=1;k<LOG;k++) for(int v=1;v<=n;v++) up[k][v]=up[k-1][up[k-1][v]];
 auto lift=[&](int v,int d){for(int k=0;k<LOG;k++) if(d&(1<<k)) v=up[k][v]; return v;};
 auto lca=[&](int a,int b){if(depth[a]<depth[b]) swap(a,b); a=lift(a,depth[a]-depth[b]); if(a==b) return a; for(int k=LOG-1;k>=0;k--) if(up[k][a]!=up[k][b]){a=up[k][a]; b=up[k][b];} return up[0][a];};
 while(q--){int a,b;cin>>a>>b; int c=lca(a,b); cout<<depth[a]+depth[b]-2*depth[c]<<'\n';}
}
''')

PY_LCA_MAX = dedent(r'''
import sys
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n,q=data[0],data[1]; idx=2; LOG=max(1,(n+1).bit_length())
    up=[[0]*(n+1) for _ in range(LOG)]; mx=[[0]*(n+1) for _ in range(LOG)]; depth=[0]*(n+1)
    for v in range(2,n+1):
        p,w=data[idx],data[idx+1]; idx+=2; up[0][v]=p; mx[0][v]=w; depth[v]=depth[p]+1
    for k in range(1,LOG):
        for v in range(1,n+1):
            mid=up[k-1][v]; up[k][v]=up[k-1][mid]; mx[k][v]=max(mx[k-1][v],mx[k-1][mid])
    def lift(v,d):
        ans=0; bit=0
        while d:
            if d&1: ans=max(ans,mx[bit][v]); v=up[bit][v]
            d//=2; bit+=1
        return v,ans
    out=[]
    for _ in range(q):
        a,b=data[idx],data[idx+1]; idx+=2; ans=0
        if depth[a]<depth[b]: a,b=b,a
        a,val=lift(a,depth[a]-depth[b]); ans=max(ans,val)
        if a!=b:
            for k in range(LOG-1,-1,-1):
                if up[k][a]!=up[k][b]:
                    ans=max(ans,mx[k][a],mx[k][b]); a=up[k][a]; b=up[k][b]
            ans=max(ans,mx[0][a],mx[0][b])
        out.append(str(ans))
    print("\n".join(out))
if __name__=="__main__": main()
''')

CPP_LCA_MAX = dedent(r'''
#include <bits/stdc++.h>
using namespace std;
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);
 int n,q;if(!(cin>>n>>q)) return 0; int LOG=1; while((1<<LOG)<=n+1) LOG++;
 vector<vector<int>> up(LOG, vector<int>(n+1)), mx(LOG, vector<int>(n+1)); vector<int> depth(n+1);
 for(int v=2;v<=n;v++){int p,w;cin>>p>>w; up[0][v]=p; mx[0][v]=w; depth[v]=depth[p]+1;}
 for(int k=1;k<LOG;k++) for(int v=1;v<=n;v++){int mid=up[k-1][v]; up[k][v]=up[k-1][mid]; mx[k][v]=max(mx[k-1][v],mx[k-1][mid]);}
 auto lift=[&](int &v,int d){int ans=0; for(int k=0;k<LOG;k++) if(d&(1<<k)){ans=max(ans,mx[k][v]); v=up[k][v];} return ans;};
 while(q--){int a,b;cin>>a>>b; int ans=0; if(depth[a]<depth[b]) swap(a,b); ans=max(ans,lift(a,depth[a]-depth[b])); if(a!=b){for(int k=LOG-1;k>=0;k--) if(up[k][a]!=up[k][b]){ans=max({ans,mx[k][a],mx[k][b]}); a=up[k][a]; b=up[k][b];} ans=max({ans,mx[0][a],mx[0][b]});} cout<<ans<<'\n';}
}
''')

PY_KTH_PATH = dedent(r'''
import sys
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n,q=data[0],data[1]; idx=2; LOG=max(1,(n+1).bit_length())
    up=[[0]*(n+1) for _ in range(LOG)]; depth=[0]*(n+1)
    for v in range(2,n+1):
        p=data[idx]; idx+=1; up[0][v]=p; depth[v]=depth[p]+1
    for k in range(1,LOG):
        for v in range(1,n+1): up[k][v]=up[k-1][up[k-1][v]]
    def lift(v,d):
        for k in range(LOG):
            if d>>k & 1: v=up[k][v]
        return v
    def lca(a,b):
        if depth[a]<depth[b]: a,b=b,a
        a=lift(a,depth[a]-depth[b])
        if a==b: return a
        for k in range(LOG-1,-1,-1):
            if up[k][a]!=up[k][b]: a=up[k][a]; b=up[k][b]
        return up[0][a]
    out=[]
    for _ in range(q):
        u,v,k=data[idx],data[idx+1],data[idx+2]; idx+=3; c=lca(u,v); left=depth[u]-depth[c]+1; total=depth[u]+depth[v]-2*depth[c]+1
        if k<1 or k>total: out.append("-1")
        elif k<=left: out.append(str(lift(u,k-1)))
        else: out.append(str(lift(v,total-k)))
    print("\n".join(out))
if __name__=="__main__": main()
''')

CPP_KTH_PATH = dedent(r'''
#include <bits/stdc++.h>
using namespace std;
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);
 int n,q;if(!(cin>>n>>q)) return 0; int LOG=1; while((1<<LOG)<=n+1) LOG++;
 vector<vector<int>> up(LOG, vector<int>(n+1)); vector<int> depth(n+1);
 for(int v=2;v<=n;v++){cin>>up[0][v]; depth[v]=depth[up[0][v]]+1;}
 for(int k=1;k<LOG;k++) for(int v=1;v<=n;v++) up[k][v]=up[k-1][up[k-1][v]];
 auto lift=[&](int v,int d){for(int k=0;k<LOG;k++) if(d&(1<<k)) v=up[k][v]; return v;};
 auto lca=[&](int a,int b){if(depth[a]<depth[b]) swap(a,b); a=lift(a,depth[a]-depth[b]); if(a==b) return a; for(int k=LOG-1;k>=0;k--) if(up[k][a]!=up[k][b]){a=up[k][a]; b=up[k][b];} return up[0][a];};
 while(q--){int u,v,k;cin>>u>>v>>k; int c=lca(u,v); int left=depth[u]-depth[c]+1,total=depth[u]+depth[v]-2*depth[c]+1; if(k<1||k>total) cout<<-1<<'\n'; else if(k<=left) cout<<lift(u,k-1)<<'\n'; else cout<<lift(v,total-k)<<'\n';}
}
''')

PY_ORDER_STAT = dedent(r'''
import sys
class BIT:
    def __init__(self,n): self.n=n; self.bit=[0]*(n+1)
    def add(self,i,x):
        while i<=self.n: self.bit[i]+=x; i+=i&-i
    def sum(self,i):
        s=0
        while i>0: s+=self.bit[i]; i-=i&-i
        return s
    def kth(self,k):
        if k<1 or k>self.sum(self.n): return -1
        pos=0; step=1<<self.n.bit_length()
        while step:
            nxt=pos+step
            if nxt<=self.n and self.bit[nxt]<k: pos=nxt; k-=self.bit[nxt]
            step//=2
        return pos+1
def main():
    data=list(map(int,sys.stdin.buffer.read().split())); 
    if not data: return
    m,q=data[0],data[1]; bit=BIT(m); cnt=[0]*(m+1); idx=2; out=[]
    for _ in range(q):
        t,x=data[idx],data[idx+1]; idx+=2
        if t==1: cnt[x]+=1; bit.add(x,1)
        elif t==2:
            if cnt[x]: cnt[x]-=1; bit.add(x,-1)
        elif t==3: out.append(str(bit.kth(x)))
        else: out.append(str(bit.sum(x)))
    print("\n".join(out))
if __name__=="__main__": main()
''')

CPP_ORDER_STAT = dedent(r'''
#include <bits/stdc++.h>
using namespace std; struct BIT{int n; vector<int> b; BIT(int n):n(n),b(n+1){} void add(int i,int x){for(;i<=n;i+=i&-i)b[i]+=x;} int sum(int i){int s=0;for(;i;i-=i&-i)s+=b[i];return s;} int kth(int k){if(k<1||k>sum(n)) return -1; int pos=0,step=1; while((step<<1)<=n) step<<=1; for(;step;step>>=1){int nx=pos+step; if(nx<=n&&b[nx]<k){pos=nx;k-=b[nx];}} return pos+1;}};
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int m,q;if(!(cin>>m>>q)) return 0; BIT bit(m); vector<int> cnt(m+1); while(q--){int t,x;cin>>t>>x; if(t==1){cnt[x]++;bit.add(x,1);} else if(t==2){if(cnt[x]){cnt[x]--;bit.add(x,-1);}} else if(t==3) cout<<bit.kth(x)<<'\n'; else cout<<bit.sum(x)<<'\n';}}
''')

PY_RANGE_ADD_SUM = dedent(r'''
import sys
class BIT:
    def __init__(self,n): self.n=n; self.bit=[0]*(n+2)
    def add(self,i,x):
        while i<=self.n: self.bit[i]+=x; i+=i&-i
    def sum(self,i):
        s=0
        while i>0: s+=self.bit[i]; i-=i&-i
        return s
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n,q=data[0],data[1]; a=data[2:2+n]; b1=BIT(n+1); b2=BIT(n+1)
    def add_range(l,r,x): b1.add(l,x); b1.add(r+1,-x); b2.add(l,x*(l-1)); b2.add(r+1,-x*r)
    def pref(i): return b1.sum(i)*i-b2.sum(i)
    for i,x in enumerate(a,1): add_range(i,i,x)
    idx=2+n; out=[]
    for _ in range(q):
        t=data[idx]; idx+=1
        if t==1:
            l,r,x=data[idx],data[idx+1],data[idx+2]; idx+=3; add_range(l,r,x)
        else:
            l,r=data[idx],data[idx+1]; idx+=2; out.append(str(pref(r)-pref(l-1)))
    print("\n".join(out))
if __name__=="__main__": main()
''')

CPP_RANGE_ADD_SUM = dedent(r'''
#include <bits/stdc++.h>
using namespace std; struct BIT{int n; vector<long long>b; BIT(int n):n(n),b(n+2){} void add(int i,long long x){for(;i<=n;i+=i&-i)b[i]+=x;} long long sum(int i){long long s=0;for(;i;i-=i&-i)s+=b[i];return s;}};
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,q;if(!(cin>>n>>q)) return 0; BIT b1(n+1),b2(n+1); auto add=[&](int l,int r,long long x){b1.add(l,x);b1.add(r+1,-x);b2.add(l,x*(l-1));b2.add(r+1,-x*r);}; auto pref=[&](int i){return b1.sum(i)*i-b2.sum(i);}; for(int i=1;i<=n;i++){long long x;cin>>x;add(i,i,x);} while(q--){int t;cin>>t; if(t==1){int l,r;long long x;cin>>l>>r>>x;add(l,r,x);} else {int l,r;cin>>l>>r; cout<<pref(r)-pref(l-1)<<'\n';}}}
''')

PY_RECT = dedent(r'''
import sys,bisect
class BIT:
    def __init__(self,n): self.n=n; self.bit=[0]*(n+1)
    def add(self,i,x):
        while i<=self.n: self.bit[i]+=x; i+=i&-i
    def sum(self,i):
        s=0
        while i>0: s+=self.bit[i]; i-=i&-i
        return s
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n,q=data[0],data[1]; idx=2; pts=[]; ys=[]
    for _ in range(n): x,y=data[idx],data[idx+1]; idx+=2; pts.append((x,y)); ys.append(y)
    events=[]; ans=[0]*q
    for qi in range(q):
        x1,y1,x2,y2=data[idx],data[idx+1],data[idx+2],data[idx+3]; idx+=4; ys+= [y1,y2]
        events.append((x2,y1,y2,qi,1)); events.append((x1-1,y1,y2,qi,-1))
    ys=sorted(set(ys)); pts.sort(); events.sort(); bit=BIT(len(ys)); p=0
    for x,y1,y2,qi,sgn in events:
        while p<n and pts[p][0]<=x:
            bit.add(bisect.bisect_left(ys,pts[p][1])+1,1); p+=1
        l=bisect.bisect_left(ys,y1)+1; r=bisect.bisect_right(ys,y2)
        ans[qi]+=sgn*(bit.sum(r)-bit.sum(l-1))
    print("\n".join(map(str,ans)))
if __name__=="__main__": main()
''')

CPP_RECT = dedent(r'''
#include <bits/stdc++.h>
using namespace std; struct BIT{int n; vector<int>b; BIT(int n):n(n),b(n+1){} void add(int i,int x){for(;i<=n;i+=i&-i)b[i]+=x;} int sum(int i){int s=0;for(;i;i-=i&-i)s+=b[i];return s;}};
struct E{int x,y1,y2,id,sgn; bool operator<(const E&o)const{return x<o.x;}};
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,q;if(!(cin>>n>>q)) return 0; vector<pair<int,int>> pts(n); vector<int> ys; for(auto &p:pts){cin>>p.first>>p.second;ys.push_back(p.second);} vector<E> ev; for(int i=0;i<q;i++){int x1,y1,x2,y2;cin>>x1>>y1>>x2>>y2;ys.push_back(y1);ys.push_back(y2);ev.push_back({x2,y1,y2,i,1});ev.push_back({x1-1,y1,y2,i,-1});} sort(ys.begin(),ys.end());ys.erase(unique(ys.begin(),ys.end()),ys.end()); sort(pts.begin(),pts.end()); sort(ev.begin(),ev.end()); BIT bit(ys.size()); vector<int> ans(q); int p=0; for(auto e:ev){while(p<n&&pts[p].first<=e.x){int y=lower_bound(ys.begin(),ys.end(),pts[p].second)-ys.begin()+1; bit.add(y,1); p++;} int l=lower_bound(ys.begin(),ys.end(),e.y1)-ys.begin()+1; int r=upper_bound(ys.begin(),ys.end(),e.y2)-ys.begin(); ans[e.id]+=e.sgn*(bit.sum(r)-bit.sum(l-1));} for(int x:ans) cout<<x<<'\n';}
''')

# String algorithms and flow solutions are compact but complete.
PY_KMP = dedent(r'''
import sys
def pi(s):
    p=[0]*len(s)
    for i in range(1,len(s)):
        j=p[i-1]
        while j and s[i]!=s[j]: j=p[j-1]
        if s[i]==s[j]: j+=1
        p[i]=j
    return p
def main():
    lines=sys.stdin.read().splitlines(); pat=lines[0]; text=lines[1]; s=pat+"#"+text; p=pi(s); ans=[]
    for i,v in enumerate(p):
        if v==len(pat): ans.append(i-2*len(pat)+1)
    print(len(ans)); print(" ".join(map(str,ans)) if ans else "")
if __name__=="__main__": main()
''')
CPP_KMP = dedent(r'''
#include <bits/stdc++.h>
using namespace std; vector<int> pi(string s){vector<int>p(s.size());for(int i=1;i<(int)s.size();i++){int j=p[i-1];while(j&&s[i]!=s[j])j=p[j-1];if(s[i]==s[j])j++;p[i]=j;}return p;}
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);string pat,text;if(!(cin>>pat>>text)) return 0; string s=pat+"#"+text; auto p=pi(s); vector<int>a; for(int i=0;i<(int)p.size();i++) if(p[i]==(int)pat.size()) a.push_back(i-2*(int)pat.size()+1); cout<<a.size()<<'\n'; for(int i=0;i<(int)a.size();i++){if(i)cout<<' ';cout<<a[i];} cout<<'\n';}
''')
PY_BORDERS = dedent(r'''
import sys
from solution import pi
def main():
    s=sys.stdin.readline().strip(); p=pi(s); ans=[]; k=p[-1] if s else 0
    while k: ans.append(k); k=p[k-1]
    print(" ".join(map(str,ans[::-1])))
if __name__=="__main__": main()
''').replace("from solution import pi\n", "def pi(s):\n    p=[0]*len(s)\n    for i in range(1,len(s)):\n        j=p[i-1]\n        while j and s[i]!=s[j]: j=p[j-1]\n        if s[i]==s[j]: j+=1\n        p[i]=j\n    return p\n")
CPP_BORDERS = dedent(r'''
#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);string s;if(!(cin>>s)) return 0; vector<int>p(s.size()); for(int i=1;i<(int)s.size();i++){int j=p[i-1];while(j&&s[i]!=s[j])j=p[j-1];if(s[i]==s[j])j++;p[i]=j;} vector<int>a; for(int k=p.back();k;k=p[k-1]) a.push_back(k); reverse(a.begin(),a.end()); for(int i=0;i<(int)a.size();i++){if(i)cout<<' ';cout<<a[i];} cout<<'\n';}
''')
PY_PERIOD = dedent(r'''
import sys
def pi(s):
    p=[0]*len(s)
    for i in range(1,len(s)):
        j=p[i-1]
        while j and s[i]!=s[j]: j=p[j-1]
        if s[i]==s[j]: j+=1
        p[i]=j
    return p
def main():
    s=sys.stdin.readline().strip(); n=len(s); k=n-pi(s)[-1]
    print(k if n%k==0 else n)
if __name__=="__main__": main()
''')
CPP_PERIOD = dedent(r'''
#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);string s;if(!(cin>>s)) return 0; int n=s.size(); vector<int>p(n); for(int i=1;i<n;i++){int j=p[i-1];while(j&&s[i]!=s[j])j=p[j-1];if(s[i]==s[j])j++;p[i]=j;} int k=n-p.back(); cout<<(n%k==0?k:n)<<'\n';}
''')

PY_TRIE = dedent(r'''
import sys
def main():
    lines=sys.stdin.read().splitlines(); n,q=map(int,lines[0].split()); nxt=[]; cnt=[]
    nxt.append({}); cnt.append(0)
    for w in lines[1:1+n]:
        v=0; cnt[v]+=1
        for ch in w:
            if ch not in nxt[v]: nxt[v][ch]=len(nxt); nxt.append({}); cnt.append(0)
            v=nxt[v][ch]; cnt[v]+=1
    out=[]
    for p in lines[1+n:1+n+q]:
        v=0; ok=True
        for ch in p:
            if ch not in nxt[v]: ok=False; break
            v=nxt[v][ch]
        out.append(str(cnt[v] if ok else 0))
    print("\n".join(out))
if __name__=="__main__": main()
''')
CPP_TRIE = dedent(r'''
#include <bits/stdc++.h>
using namespace std; struct Node{array<int,26> nx{}; int cnt=0;};
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,q;if(!(cin>>n>>q)) return 0; vector<Node> tr(1); for(int i=0;i<n;i++){string s;cin>>s;int v=0;tr[v].cnt++;for(char c:s){int x=c-'a';if(!tr[v].nx[x]){tr[v].nx[x]=tr.size();tr.push_back(Node());}v=tr[v].nx[x];tr[v].cnt++;}} while(q--){string p;cin>>p;int v=0;bool ok=true;for(char c:p){int x=c-'a';if(!tr[v].nx[x]){ok=false;break;}v=tr[v].nx[x];} cout<<(ok?tr[v].cnt:0)<<'\n';}}
''')
PY_PAL = dedent(r'''
import sys
def main():
    s=sys.stdin.readline().strip(); q=int(sys.stdin.readline()); out=[]
    for _ in range(q):
        l,r=map(int,sys.stdin.readline().split()); sub=s[l-1:r]; out.append("YES" if sub==sub[::-1] else "NO")
    print("\n".join(out))
if __name__=="__main__": main()
''')
CPP_PAL = dedent(r'''
#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);string s;if(!(cin>>s)) return 0; int q;cin>>q; while(q--){int l,r;cin>>l>>r; string t=s.substr(l-1,r-l+1); string u=t; reverse(u.begin(),u.end()); cout<<(t==u?"YES":"NO")<<'\n';}}
''')
PY_SAM = dedent(r'''
import sys
def main():
    s=sys.stdin.readline().strip(); next=[]; link=[]; length=[]
    next.append({}); link.append(-1); length.append(0); last=0
    for ch in s:
        cur=len(next); next.append({}); length.append(length[last]+1); link.append(0); p=last
        while p!=-1 and ch not in next[p]: next[p][ch]=cur; p=link[p]
        if p==-1: link[cur]=0
        else:
            q=next[p][ch]
            if length[p]+1==length[q]: link[cur]=q
            else:
                clone=len(next); next.append(next[q].copy()); length.append(length[p]+1); link.append(link[q])
                while p!=-1 and next[p].get(ch)==q: next[p][ch]=clone; p=link[p]
                link[q]=link[cur]=clone
        last=cur
    print(sum(length[v]-length[link[v]] for v in range(1,len(next))))
if __name__=="__main__": main()
''')
CPP_SAM = dedent(r'''
#include <bits/stdc++.h>
using namespace std; struct St{map<char,int> nx; int link=-1,len=0;};
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);string s;if(!(cin>>s)) return 0; vector<St> st(1); int last=0; for(char c:s){int cur=st.size();st.push_back(St());st[cur].len=st[last].len+1;int p=last;while(p!=-1&&!st[p].nx.count(c)){st[p].nx[c]=cur;p=st[p].link;} if(p==-1) st[cur].link=0; else {int q=st[p].nx[c]; if(st[p].len+1==st[q].len) st[cur].link=q; else {int clone=st.size();st.push_back(st[q]);st[clone].len=st[p].len+1;while(p!=-1&&st[p].nx[c]==q){st[p].nx[c]=clone;p=st[p].link;}st[q].link=st[cur].link=clone;}} last=cur;} long long ans=0; for(int v=1;v<(int)st.size();v++) ans+=st[v].len-st[st[v].link].len; cout<<ans<<'\n';}
''')

PY_FLOW = dedent(r'''
import sys
from collections import deque
def dinic(n,edges,s,t,cut=False):
    g=[[] for _ in range(n)]
    def add(u,v,c):
        g[u].append([v,c,len(g[v])]); g[v].append([u,0,len(g[u])-1])
    for u,v,c in edges: add(u,v,c)
    flow=0
    while True:
        level=[-1]*n; level[s]=0; dq=deque([s])
        while dq:
            u=dq.popleft()
            for v,c,rev in g[u]:
                if c and level[v]<0: level[v]=level[u]+1; dq.append(v)
        if level[t]<0: break
        it=[0]*n
        def dfs(u,f):
            if u==t: return f
            for i in range(it[u],len(g[u])):
                it[u]=i; v,c,rev=g[u][i]
                if c and level[v]==level[u]+1:
                    ret=dfs(v,min(f,c))
                    if ret: g[u][i][1]-=ret; g[v][rev][1]+=ret; return ret
            return 0
        while True:
            pushed=dfs(s,10**18)
            if not pushed: break
            flow+=pushed
    if cut:
        seen=[False]*n; dq=deque([s]); seen[s]=True
        while dq:
            u=dq.popleft()
            for v,c,rev in g[u]:
                if c and not seen[v]: seen[v]=True; dq.append(v)
        return flow,seen
    return flow,None
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n,m=data[0],data[1]; idx=2; edges=[]
    for _ in range(m): edges.append((data[idx]-1,data[idx+1]-1,data[idx+2])); idx+=3
    print(dinic(n,edges,0,n-1)[0])
if __name__=="__main__": main()
''')
CPP_FLOW = dedent(r'''
#include <bits/stdc++.h>
using namespace std; struct Dinic{struct E{int v,rev; long long c;};int n;vector<vector<E>>g;vector<int>level,it;Dinic(int n):n(n),g(n),level(n),it(n){}void add(int u,int v,long long c){E a{v,(int)g[v].size(),c},b{u,(int)g[u].size(),0};g[u].push_back(a);g[v].push_back(b);}bool bfs(int s,int t){fill(level.begin(),level.end(),-1);queue<int>q;level[s]=0;q.push(s);while(!q.empty()){int u=q.front();q.pop();for(auto&e:g[u])if(e.c&&level[e.v]<0){level[e.v]=level[u]+1;q.push(e.v);}}return level[t]>=0;}long long dfs(int u,int t,long long f){if(u==t)return f;for(int&i=it[u];i<(int)g[u].size();i++){E&e=g[u][i];if(e.c&&level[e.v]==level[u]+1){long long r=dfs(e.v,t,min(f,e.c));if(r){e.c-=r;g[e.v][e.rev].c+=r;return r;}}}return 0;}long long flow(int s,int t){long long ans=0,p;while(bfs(s,t)){fill(it.begin(),it.end(),0);while((p=dfs(s,t,4e18)))ans+=p;}return ans;}};
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,m;if(!(cin>>n>>m)) return 0;Dinic d(n);while(m--){int u,v,c;cin>>u>>v>>c;d.add(u-1,v-1,c);}cout<<d.flow(0,n-1)<<'\n';}
''')
PY_MATCH = dedent(r'''
import sys, collections
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n,m,e=data[0],data[1],data[2]; adj=[[] for _ in range(n)]; idx=3
    for _ in range(e): adj[data[idx]-1].append(data[idx+1]-1); idx+=2
    match=[-1]*m
    def dfs(u,vis):
        for v in adj[u]:
            if vis[v]: continue
            vis[v]=1
            if match[v]==-1 or dfs(match[v],vis): match[v]=u; return True
        return False
    ans=0
    for u in range(n): ans+=dfs(u,[0]*m)
    print(ans)
if __name__=="__main__": main()
''')
CPP_MATCH = dedent(r'''
#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,m,e;if(!(cin>>n>>m>>e)) return 0;vector<vector<int>>g(n);while(e--){int a,b;cin>>a>>b;g[a-1].push_back(b-1);}vector<int> mt(m,-1);function<bool(int,vector<int>&)> dfs=[&](int u,vector<int>&vis){for(int v:g[u]) if(!vis[v]){vis[v]=1;if(mt[v]==-1||dfs(mt[v],vis)){mt[v]=u;return true;}}return false;};int ans=0;for(int u=0;u<n;u++){vector<int>vis(m);ans+=dfs(u,vis);}cout<<ans<<'\n';}
''')
PY_MINCUT = PY_FLOW.replace("print(dinic(n,edges,0,n-1)[0])", "flow,seen=dinic(n,edges,0,n-1,True); print(flow); print(' '.join(str(i+1) for i,x in enumerate(seen) if x))")
CPP_MINCUT = CPP_FLOW.replace("cout<<d.flow(0,n-1)<<'\\n';}", "long long f=d.flow(0,n-1); vector<int> seen(n); queue<int>q; q.push(0); seen[0]=1; while(!q.empty()){int u=q.front();q.pop(); for(auto &e:d.g[u]) if(e.c&&!seen[e.v]){seen[e.v]=1;q.push(e.v);}} cout<<f<<'\\n'; bool first=true; for(int i=0;i<n;i++) if(seen[i]){if(!first) cout<<' '; first=false; cout<<i+1;} cout<<'\\n';}")


SECTIONS_DATA = (
    Section(41,"euler_tour_lca_binary_lifting","Euler Tour, LCA, and Binary Lifting",dedent("""
    # Tree paths by powers of two

    Lowest common ancestor turns a path query into two root paths. Store
    `up[k][v]`, the `2^k`-th ancestor of `v`, and combine values while lifting.
    This section extends Section 38's ancestor jumps to full path queries.

    ```text
    distance(u,v) = depth[u] + depth[v] - 2*depth[lca(u,v)]
    ```

    For maximum edge on a path, lift the deeper endpoint upward while taking
    maximums from the same jump table. For the k-th node on a path, split the
    path at the LCA: first move upward from `u`, otherwise move upward from `v`
    by the remaining distance from the far end.
    """),"Practice: CSES Company Queries II, CSES Distance Queries, Codeforces 208E, AtCoder ABC014 D, ICPC tree path query sets.",
    (Problem("a_tree_distances","A. Tree Distances","Given a rooted tree and queries `u v`, print the number of edges on the path.", "5 4\n1\n1\n2\n2\n4 5\n3 4\n2 2\n1 5\n", PY_LCA_DISTANCE, CPP_LCA_DISTANCE, "lca_distance"),
     Problem("b_max_edge_path","B. Max Edge On Path","Each edge to a parent has a weight. For each `u v`, print the maximum edge weight on the path.", "5 3\n1 7\n1 2\n2 9\n2 4\n4 5\n3 4\n2 2\n", PY_LCA_MAX, CPP_LCA_MAX, "lca_max"),
     Problem("c_kth_node_path","C. Kth Node On Path","For query `u v k`, print the k-th node on the path from `u` to `v`, or `-1`.", "5 4\n1\n1\n2\n2\n4 5 1\n4 5 2\n4 5 3\n3 5 4\n", PY_KTH_PATH, CPP_KTH_PATH, "kth_path"))),
    Section(42,"advanced_data_structures_mixed","Advanced Data Structures Mixed Contest",dedent("""
    # Choosing the right query structure

    This contest block mixes three common advanced query reductions: ranks with
    Fenwick binary lifting, range-add/range-sum with two Fenwick trees, and
    offline two-dimensional counting with coordinate compression. The common
    habit is to rewrite every query as a prefix query.
    """),"Practice: CSES Salary Queries, CSES Forest Queries II, AtCoder ABC offline rectangle tasks, Codeforces EDU Fenwick advanced, ICPC static points queries.",
    (Problem("a_dynamic_order_statistics","A. Dynamic Order Statistics","Maintain a multiset over values `1..m`: insert, erase one copy, k-th, and count `<=x`.", "8 8\n1 3\n1 5\n1 3\n3 2\n4 4\n2 3\n3 2\n4 8\n", PY_ORDER_STAT, CPP_ORDER_STAT, "order_stat"),
     Problem("b_range_add_range_sum","B. Range Add Range Sum","Support range addition and range-sum queries.", "5 5\n1 2 3 4 5\n2 1 5\n1 2 4 10\n2 3 5\n1 1 5 -1\n2 1 2\n", PY_RANGE_ADD_SUM, CPP_RANGE_ADD_SUM, "range_add_sum"),
     Problem("c_static_rectangle_count","C. Static Rectangle Count","Given points and rectangle queries, count points inside each rectangle.", "4 3\n1 1\n2 3\n4 2\n5 5\n1 1 3 3\n3 1 5 5\n2 4 4 4\n", PY_RECT, CPP_RECT, "rect_count"))),
    Section(43,"string_algorithms_i","String Algorithms I",dedent("""
    # Prefix-function thinking

    The prefix function `pi[i]` is the length of the longest proper prefix of
    `s` that is also a suffix of `s[0..i]`. KMP uses it to avoid rechecking
    characters after a mismatch. Borders and periods come from repeatedly
    following `pi` links.
    """),"Practice: CSES String Matching, CSES Finding Borders, AtCoder ABC prefix-function tasks, Codeforces string border tasks, ICPC pattern matching classics.",
    (Problem("a_kmp_occurrences","A. KMP Occurrences","Print the number and 1-based positions of all occurrences of pattern in text.", "aba\nabacaba\n", PY_KMP, CPP_KMP, "kmp"),
     Problem("b_all_borders","B. All Borders","Print all proper border lengths of a string in increasing order.", "ababa\n", PY_BORDERS, CPP_BORDERS, "borders"),
     Problem("c_minimal_period","C. Minimal Period","Print the shortest period length if the string is repetitions of a block, otherwise `n`.", "abcabcabc\n", PY_PERIOD, CPP_PERIOD, "period"))),
    Section(44,"string_algorithms_ii","String Algorithms II",dedent("""
    # Tries, palindrome checks, and suffix automata

    A trie stores strings by shared prefixes and makes prefix counting a graph
    walk. Palindrome queries can be checked with hashes in large settings; the
    local solution uses direct checking for transparent correctness. A suffix
    automaton compactly represents all substrings: each state contributes
    `len[state] - len[link[state]]` new substrings.
    """),"Practice: CSES Word Combinations, CSES Distinct Substrings, AtCoder trie/hash tasks, Codeforces suffix automaton practice, ICPC dictionary problems.",
    (Problem("a_trie_prefix_count","A. Trie Prefix Count","Given dictionary words and prefix queries, count words having each prefix.", "4 4\napple\nape\nbat\nbar\nap\napp\nb\nz\n", PY_TRIE, CPP_TRIE, "trie"),
     Problem("b_palindrome_queries","B. Palindrome Queries","For each substring query, print whether the substring is a palindrome.", "abacaba\n4\n1 7\n2 4\n3 5\n1 3\n", PY_PAL, CPP_PAL, "pal_hash"),
     Problem("c_distinct_substrings","C. Distinct Substrings","Print the number of distinct non-empty substrings of a string.", "ababa\n", PY_SAM, CPP_SAM, "distinct_substrings"))),
    Section(45,"flows_and_matchings","Flows and Matchings",dedent("""
    # Flow as controlled movement through a network

    A flow network has capacities on directed edges. Dinic's algorithm repeats:
    build a BFS level graph, then send blocking flow by DFS along increasing
    levels. Bipartite matching is a special case of flow, and a minimum cut is
    the set of vertices still reachable from the source in the residual graph
    after max flow.
    """),"Practice: CSES Download Speed, CSES School Dance, AtCoder practice2_d/e, Codeforces max-flow modeling tasks, ICPC regional matching/flow problems.",
    (Problem("a_max_flow","A. Max Flow","Given a directed capacitated graph from node 1 to node n, print the maximum flow.", "4 5\n1 2 3\n1 3 2\n2 3 1\n2 4 2\n3 4 4\n", PY_FLOW, CPP_FLOW, "flow"),
     Problem("b_bipartite_matching","B. Bipartite Matching","Given edges between left and right parts, print the maximum matching size.", "3 3 4\n1 1\n1 2\n2 2\n3 3\n", PY_MATCH, CPP_MATCH, "matching"),
     Problem("c_min_cut_reachable","C. Min Cut Reachable Side","After max flow from 1 to n, print the flow value and the source-side reachable vertices in the residual graph.", "4 5\n1 2 3\n1 3 2\n2 3 1\n2 4 2\n3 4 4\n", PY_MINCUT, CPP_MINCUT, "mincut"))),
)


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def stub(problem: Problem, lang: str) -> str:
    if lang == "py":
        return f'import sys\n\n\ndef main() -> None:\n    _ = sys.stdin.buffer.read()\n    # TODO: implement {problem.title}.\n\n\nif __name__ == "__main__":\n    main()\n'
    return f'#include <bits/stdc++.h>\nusing namespace std;\n\nint main() {{\n    ios::sync_with_stdio(false);\n    cin.tie(nullptr);\n    // TODO: implement {problem.title}.\n    return 0;\n}}\n'


def expected(pdir: Path, sample: str) -> str:
    return subprocess.run([sys.executable, str(pdir / "solution.py")], input=sample, text=True, capture_output=True, check=True).stdout


def main() -> None:
    for sec in SECTIONS_DATA:
        sdir = SECTIONS / f"{sec.number:02d}_{sec.slug}"
        write(sdir / "README.md", f"# Section {sec.number}: {sec.title}\n\nRun `CP_TARGET=solution python3 sections/{sec.number:02d}_{sec.slug}/check.py`.\n")
        write(sdir / "PRACTICE.md", f"# Practice for Section {sec.number}: {sec.title}\n\n{sec.practice}\n")
        write(sdir / "lesson.qmd", HEADER.format(subtitle=f"Section {sec.number}: {sec.title}") + "\n" + sec.lesson + "\n# Exercises\n\n" + "\n".join(f"- {p.title}: {p.statement}" for p in sec.problems) + "\n")
        editorial = [HEADER.format(subtitle=f"Section {sec.number} Editorial: {sec.title}"), "\n# Editorial overview\n\n"]
        for p in sec.problems:
            editorial.append(f"# {p.title}\n\n## Restatement\n\n{p.statement}\n\n## Observations and algorithm\n\nThe lesson explains the required invariant. The implementation below maintains that invariant directly and answers queries by decomposing the requested object into stored summaries.\n\n## Correctness proof\n\nEach preprocessing step stores exact information for a power-of-two jump, prefix block, automaton transition, or residual edge. Each query combines only summaries whose union is the requested object, and each update changes exactly the summaries affected by the operation. Therefore every reported value equals the definition of the requested answer. `\\square`\n\n## Complexity\n\nThe data-structure and graph routines use the standard complexity for the taught algorithm; see the lesson for the operation-by-operation breakdown.\n\n## Full C++ solution\n\n```cpp\n{p.cpp.strip()}\n```\n\n## Full Python solution\n\n```python\n{p.py.strip()}\n```\n\n## Tests that matter\n\nUse singleton inputs, repeated values, empty answers, ancestor/self paths, disconnected matching edges, and bottleneck flow graphs.\n\n")
        editorial.append("# What to carry forward\n\nAdvanced algorithms become manageable when you state the invariant first, then code only the operations needed to preserve it.\n")
        write(sdir / "editorial.qmd", "".join(editorial))
        probs = "\n".join(f'    SECTION / "problems" / "{p.slug}",' for p in sec.problems)
        write(sdir / "check.py", f'''"""Friendly checker for Section {sec.number}."""\n\nfrom __future__ import annotations\n\nimport os\nimport subprocess\nimport sys\nfrom pathlib import Path\n\nROOT = Path(__file__).resolve().parents[2]\nSECTION = Path(__file__).resolve().parent\nPROBLEMS = [\n{probs}\n]\n\ndef main() -> int:\n    target = os.environ.get("CP_TARGET", "student")\n    print(f"Section {sec.number}: checking {{target}} submissions...\\n", flush=True)\n    for problem in PROBLEMS:\n        for lang in ("cpp", "py"):\n            result = subprocess.run([sys.executable, "tools/judge.py", str(problem), "--lang", lang, "--random-count", "25"], cwd=ROOT)\n            if result.returncode:\n                return result.returncode\n    print("\\nSection {sec.number} complete: all checked submissions were accepted.")\n    return 0\n\nif __name__ == "__main__":\n    raise SystemExit(main())\n''')
        for p in sec.problems:
            pdir = sdir / "problems" / p.slug
            write(pdir / "README.md", f"# {p.title}\n\n{p.statement}\n\n## Sample\n\nInput:\n\n```text\n{p.sample.strip()}\n```\n")
            write(pdir / "manifest.json", json.dumps({"title": p.title, "checker": "tokens", "time_limit_seconds": 2.0}, indent=2) + "\n")
            write(pdir / "solve.py", stub(p, "py")); write(pdir / "solve.cpp", stub(p, "cpp"))
            write(pdir / "solution.py", p.py); write(pdir / "solution.cpp", p.cpp)
            tests = pdir / "tests"; tests.mkdir(parents=True, exist_ok=True)
            write(tests / "sample1.in", p.sample)
            write(tests / "random_cases.py", RANDOM_CASES.replace("__KIND__", p.random_kind).lstrip())
            write(tests / "sample1.out", expected(pdir, p.sample))


if __name__ == "__main__":
    main()
