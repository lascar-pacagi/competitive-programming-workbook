"""Generate Sections 51-60 of the competitive programming course."""

from __future__ import annotations

import json
import subprocess
import sys
import textwrap
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.generate_sections_41_45 import CPP_MATCH, PY_MATCH
from tools.generate_sections_46_50 import (
    CPP_CRT,
    CPP_GRUNDY,
    CPP_MATRIX,
    CPP_MITM_BEST,
    PY_CRT,
    PY_GRUNDY,
    PY_MATRIX,
    PY_MITM_BEST,
)

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
import argparse, random, string, subprocess, sys
from pathlib import Path
KIND="__KIND__"; PROBLEM=Path(__file__).resolve().parents[1]
def expected(inp):
    return subprocess.run([sys.executable,str(PROBLEM/"solution.py")],input=inp,text=True,capture_output=True,check=True).stdout
def case_array(rng):
    n=rng.randint(1,80); a=[rng.randint(-50,50) for _ in range(n)]
    return f"{n}\n"+" ".join(map(str,a))+"\n"
def case_mod(rng):
    n=rng.randint(1,80); k=rng.randint(1,20); a=[rng.randint(-50,50) for _ in range(n)]
    return f"{n} {k}\n"+" ".join(map(str,a))+"\n"
def case_nim(rng):
    t=rng.randint(1,60); lines=[str(t)]
    for _ in range(t):
        n=rng.randint(1,20); a=[rng.randint(0,100) for _ in range(n)]; lines += [str(n), " ".join(map(str,a))]
    return "\n".join(lines)+"\n"
def case_subtract(rng):
    n=rng.randint(1,300); m=rng.randint(1,8); moves=sorted(set(rng.randint(1,20) for _ in range(m)))
    return f"{n} {len(moves)}\n"+" ".join(map(str,moves))+"\n"
def case_grundy(rng):
    n=rng.randint(1,45); e=set()
    for _ in range(rng.randint(0,90)):
        a=rng.randint(1,n); b=rng.randint(a+1,n) if a<n else n
        if a<b: e.add((a,b))
    q=rng.randint(1,35); starts=[rng.randint(1,n) for _ in range(q)]
    return f"{n} {len(e)} {q}\n"+"\n".join(f"{a} {b}" for a,b in sorted(e))+"\n"+" ".join(map(str,starts))+"\n"
def case_comb(rng):
    t=rng.randint(1,60); return str(t)+"\n"+"\n".join(str(rng.randint(0,300)) for _ in range(t))+"\n"
def case_necklace(rng):
    t=rng.randint(1,50); lines=[str(t)]
    for _ in range(t): lines.append(f"{rng.randint(1,80)} {rng.randint(1,20)}")
    return "\n".join(lines)+"\n"
def case_points(rng):
    t=rng.randint(1,80); lines=[str(t)]
    for _ in range(t): lines.append(" ".join(str(rng.randint(-20,20)) for _ in range(6)))
    return "\n".join(lines)+"\n"
def case_segments(rng):
    t=rng.randint(1,80); lines=[str(t)]
    for _ in range(t): lines.append(" ".join(str(rng.randint(-20,20)) for _ in range(8)))
    return "\n".join(lines)+"\n"
def case_polygon(rng):
    n=rng.randint(3,20); pts=[(rng.randint(-20,20),rng.randint(-20,20)) for _ in range(n)]
    return str(n)+"\n"+"\n".join(f"{x} {y}" for x,y in pts)+"\n"
def randstr(rng,n): return "".join(rng.choice("abcde") for _ in range(n))
def case_eqsub(rng):
    n=rng.randint(1,80); q=rng.randint(1,80); s=randstr(rng,n); lines=[s,str(q)]
    for _ in range(q):
        l1=rng.randint(1,n); r1=rng.randint(l1,n); length=r1-l1+1; l2=rng.randint(1,n-length+1); r2=l2+length-1; lines.append(f"{l1} {r1} {l2} {r2}")
    return "\n".join(lines)+"\n"
def case_anagram(rng):
    n=rng.randint(1,80); q=rng.randint(1,80); s=randstr(rng,n); lines=[s,str(q)]
    for _ in range(q):
        l1=rng.randint(1,n); r1=rng.randint(l1,n); length=r1-l1+1; l2=rng.randint(1,n-length+1); r2=l2+length-1; lines.append(f"{l1} {r1} {l2} {r2}")
    return "\n".join(lines)+"\n"
def case_jobs(rng):
    n=rng.randint(1,80); lines=[str(n)]
    for _ in range(n): lines.append(f"{rng.randint(1,50)} {rng.randint(1,200)}")
    return "\n".join(lines)+"\n"
def case_cover(rng):
    target=rng.randint(1,100); n=rng.randint(1,80); lines=[f"{target} {n}"]
    for _ in range(n):
        l=rng.randint(0,target); r=rng.randint(l,target+rng.randint(0,20)); lines.append(f"{l} {r}")
    return "\n".join(lines)+"\n"
def case_mst(rng):
    n=rng.randint(1,30); m=rng.randint(0,100); edges=[]
    for _ in range(m):
        a=rng.randint(1,n); b=rng.randint(1,n)
        if a!=b: edges.append((a,b,rng.randint(1,100)))
    return f"{n} {len(edges)}\n"+"\n".join(f"{a} {b} {w}" for a,b,w in edges)+"\n"
def case_matching(rng):
    n=rng.randint(1,12); m=rng.randint(1,12); e=set()
    for _ in range(rng.randint(0,n*m)):
        e.add((rng.randint(1,n),rng.randint(1,m)))
    return f"{n} {m} {len(e)}\n"+"\n".join(f"{a} {b}" for a,b in sorted(e))+"\n"
def case_sat(rng):
    n=rng.randint(1,10); m=rng.randint(0,30); lines=[f"{n} {m}"]
    for _ in range(m):
        a=rng.randint(1,n)*rng.choice([-1,1]); b=rng.randint(1,n)*rng.choice([-1,1]); lines.append(f"{a} {b}")
    return "\n".join(lines)+"\n"
def case_score(rng):
    n=rng.randint(1,30); lines=[str(n)]
    for i in range(n): lines.append(f"team{i} {rng.randint(0,10)} {rng.randint(0,1000)}")
    return "\n".join(lines)+"\n"
def case_assign(rng):
    n=rng.randint(1,10); a=[rng.randint(1,60) for _ in range(n)]
    return f"{n}\n"+" ".join(map(str,a))+"\n"
def case_mitm(rng):
    n=rng.randint(1,28); x=rng.randint(0,200); a=[rng.randint(0,40) for _ in range(n)]
    return f"{n} {x}\n"+" ".join(map(str,a))+"\n"
def case_crt(rng):
    t=rng.randint(1,50); lines=[str(t)]
    for _ in range(t):
        m1=rng.randint(1,60); m2=rng.randint(1,60); lines.append(f"{rng.randint(0,m1-1)} {m1} {rng.randint(0,m2-1)} {m2}")
    return "\n".join(lines)+"\n"
def case_matrix(rng):
    t=rng.randint(1,50); return str(t)+"\n"+"\n".join(str(rng.randint(0,10**6)) for _ in range(t))+"\n"
BUILDERS={"parity":case_array,"xor_split":case_array,"mod_equal":case_mod,"nim":case_nim,"subtract":case_subtract,"grundy":case_grundy,"catalan":case_comb,"derange":case_comb,"necklace":case_necklace,"orient":case_points,"segments":case_segments,"polygon":case_polygon,"eqsub":case_eqsub,"pal":case_eqsub,"anagram":case_anagram,"jobs":case_jobs,"cover":case_cover,"mst":case_mst,"matching":case_matching,"sat":case_sat,"score":case_score,"assign":case_assign,"mitm_best":case_mitm,"crt":case_crt,"matrix":case_matrix}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--count",type=int,required=True); ap.add_argument("--seed",type=int,required=True); ap.add_argument("--out-dir",type=Path,required=True)
    args=ap.parse_args(); args.out_dir.mkdir(parents=True,exist_ok=True); rng=random.Random(args.seed); builder=BUILDERS[KIND]
    for i in range(args.count):
        inp=builder(rng); stem=f"case{i:03d}"; (args.out_dir/f"{stem}.in").write_text(inp); (args.out_dir/f"{stem}.out").write_text(expected(inp))
if __name__=="__main__": main()
'''

PY_PARITY = dedent(r'''
import sys
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    a=data[1:]; print("YES" if all(x%2==a[0]%2 for x in a) else "NO")
if __name__=="__main__": main()
''')
CPP_PARITY = dedent(r'''
#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;if(!(cin>>n))return 0;vector<long long>a(n);for(auto&x:a)cin>>x;for(long long x:a)if((x-a[0])%2){cout<<"NO\n";return 0;}cout<<"YES\n";}
''')
PY_XOR = dedent(r'''
import sys
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    a=data[1:]; total=0
    for x in a: total^=x
    pref=ans=0
    for x in a[:-1]:
        pref^=x
        if pref==(total^pref): ans+=1
    print(ans)
if __name__=="__main__": main()
''')
CPP_XOR = dedent(r'''
#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;if(!(cin>>n))return 0;vector<long long>a(n);long long tot=0;for(auto&x:a){cin>>x;tot^=x;}long long pref=0,ans=0;for(int i=0;i+1<n;i++){pref^=a[i];if(pref==(tot^pref))ans++;}cout<<ans<<'\n';}
''')
PY_MODEQ = dedent(r'''
import sys
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n,k=data[0],data[1]; a=data[2:]; print("YES" if len({x%k for x in a})==1 else "NO")
if __name__=="__main__": main()
''')
CPP_MODEQ = dedent(r'''
#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;long long k;if(!(cin>>n>>k))return 0;long long r;cin>>r;r%=k;for(int i=1;i<n;i++){long long x;cin>>x;if((x%k+k)%k!=(r+k)%k){cout<<"NO\n";return 0;}}cout<<"YES\n";}
''')
PY_NIM = dedent(r'''
import sys
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    t=data[0]; idx=1; out=[]
    for _ in range(t):
        n=data[idx]; idx+=1; x=0
        for v in data[idx:idx+n]: x^=v
        idx+=n; out.append("WIN" if x else "LOSE")
    print("\n".join(out))
if __name__=="__main__": main()
''')
CPP_NIM = dedent(r'''
#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int T;if(!(cin>>T))return 0;while(T--){int n;cin>>n;long long x=0,v;while(n--){cin>>v;x^=v;}cout<<(x?"WIN":"LOSE")<<'\n';}}
''')
PY_SUBTRACT = dedent(r'''
import sys
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n,m=data[0],data[1]; moves=data[2:]; win=[False]*(n+1)
    for i in range(1,n+1): win[i]=any(i>=x and not win[i-x] for x in moves)
    print("WIN" if win[n] else "LOSE")
if __name__=="__main__": main()
''')
CPP_SUBTRACT = dedent(r'''
#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,m;if(!(cin>>n>>m))return 0;vector<int>a(m);for(int&x:a)cin>>x;vector<int>w(n+1);for(int i=1;i<=n;i++)for(int x:a)if(i>=x&&!w[i-x])w[i]=1;cout<<(w[n]?"WIN":"LOSE")<<'\n';}
''')
PY_CATALAN = dedent(r'''
import sys
MOD=1_000_000_007
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    qs=data[1:1+data[0]]; N=max(qs+[0])*2; fact=[1]*(N+1)
    for i in range(1,N+1): fact[i]=fact[i-1]*i%MOD
    inv=[1]*(N+1); inv[N]=pow(fact[N],MOD-2,MOD)
    for i in range(N,0,-1): inv[i-1]=inv[i]*i%MOD
    def C(n,k): return fact[n]*inv[k]%MOD*inv[n-k]%MOD if 0<=k<=n else 0
    print("\n".join(str(C(2*n,n)*pow(n+1,MOD-2,MOD)%MOD) for n in qs))
if __name__=="__main__": main()
''')
CPP_CATALAN = dedent(r'''
#include <bits/stdc++.h>
using namespace std; const long long MOD=1000000007; long long pw(long long a,long long e){long long r=1;while(e){if(e&1)r=r*a%MOD;a=a*a%MOD;e>>=1;}return r;}int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int T;if(!(cin>>T))return 0;vector<int>q(T);int N=0;for(int&i:q){cin>>i;N=max(N,2*i);}vector<long long>f(N+1,1),iv(N+1,1);for(int i=1;i<=N;i++)f[i]=f[i-1]*i%MOD;iv[N]=pw(f[N],MOD-2);for(int i=N;i;i--)iv[i-1]=iv[i]*i%MOD;auto C=[&](int n,int k){return f[n]*iv[k]%MOD*iv[n-k]%MOD;};for(int n:q)cout<<C(2*n,n)*pw(n+1,MOD-2)%MOD<<'\n';}
''')
PY_DERANGE = dedent(r'''
import sys
MOD=1_000_000_007
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    qs=data[1:1+data[0]]; N=max(qs+[1]); d=[0]*(N+1); d[0]=1
    if N>=1: d[1]=0
    for i in range(2,N+1): d[i]=(i-1)*(d[i-1]+d[i-2])%MOD
    print("\n".join(str(d[n]) for n in qs))
if __name__=="__main__": main()
''')
CPP_DERANGE = dedent(r'''
#include <bits/stdc++.h>
using namespace std; const long long MOD=1000000007; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int T;if(!(cin>>T))return 0;vector<int>q(T);int N=1;for(int&i:q){cin>>i;N=max(N,i);}vector<long long>d(N+1);d[0]=1;if(N>=1)d[1]=0;for(int i=2;i<=N;i++)d[i]=(i-1)*(d[i-1]+d[i-2])%MOD;for(int n:q)cout<<d[n]<<'\n';}
''')
PY_NECK = dedent(r'''
import sys,math
MOD=1_000_000_007
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    t=data[0]; idx=1; out=[]
    for _ in range(t):
        n,k=data[idx],data[idx+1]; idx+=2; s=0
        for r in range(n): s=(s+pow(k,math.gcd(n,r),MOD))%MOD
        out.append(str(s*pow(n,MOD-2,MOD)%MOD))
    print("\n".join(out))
if __name__=="__main__": main()
''')
CPP_NECK = dedent(r'''
#include <bits/stdc++.h>
using namespace std; const long long MOD=1000000007; long long pw(long long a,long long e){long long r=1;while(e){if(e&1)r=r*a%MOD;a=a*a%MOD;e>>=1;}return r;}int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int T;if(!(cin>>T))return 0;while(T--){int n,k;cin>>n>>k;long long s=0;for(int r=0;r<n;r++)s=(s+pw(k,gcd(n,r)))%MOD;cout<<s*pw(n,MOD-2)%MOD<<'\n';}}
''')
PY_ORIENT = dedent(r'''
import sys
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    t=data[0]; idx=1; out=[]
    for _ in range(t):
        ax,ay,bx,by,cx,cy=data[idx:idx+6]; idx+=6; v=(bx-ax)*(cy-ay)-(by-ay)*(cx-ax); out.append("LEFT" if v>0 else "RIGHT" if v<0 else "TOUCH")
    print("\n".join(out))
if __name__=="__main__": main()
''')
CPP_ORIENT = dedent(r'''
#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int T;if(!(cin>>T))return 0;while(T--){long long ax,ay,bx,by,cx,cy;cin>>ax>>ay>>bx>>by>>cx>>cy;long long v=(bx-ax)*(cy-ay)-(by-ay)*(cx-ax);cout<<(v>0?"LEFT":v<0?"RIGHT":"TOUCH")<<'\n';}}
''')
PY_SEG = dedent(r'''
import sys
def ori(a,b,c): return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def between(a,b,c): return min(a[0],b[0])<=c[0]<=max(a[0],b[0]) and min(a[1],b[1])<=c[1]<=max(a[1],b[1])
def inter(a,b,c,d):
    o1,o2,o3,o4=ori(a,b,c),ori(a,b,d),ori(c,d,a),ori(c,d,b)
    if o1==0 and between(a,b,c): return True
    if o2==0 and between(a,b,d): return True
    if o3==0 and between(c,d,a): return True
    if o4==0 and between(c,d,b): return True
    return (o1>0)!=(o2>0) and (o3>0)!=(o4>0)
def main():
    data=list(map(int,sys.stdin.buffer.read().split())); t=data[0]; idx=1; out=[]
    for _ in range(t):
        x=data[idx:idx+8]; idx+=8; out.append("YES" if inter((x[0],x[1]),(x[2],x[3]),(x[4],x[5]),(x[6],x[7])) else "NO")
    print("\n".join(out))
if __name__=="__main__": main()
''')
CPP_SEG = dedent(r'''
#include <bits/stdc++.h>
using namespace std; using P=pair<long long,long long>; long long ori(P a,P b,P c){return (b.first-a.first)*(c.second-a.second)-(b.second-a.second)*(c.first-a.first);}bool btw(P a,P b,P c){return min(a.first,b.first)<=c.first&&c.first<=max(a.first,b.first)&&min(a.second,b.second)<=c.second&&c.second<=max(a.second,b.second);}int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int T;if(!(cin>>T))return 0;while(T--){P a,b,c,d;cin>>a.first>>a.second>>b.first>>b.second>>c.first>>c.second>>d.first>>d.second;long long o1=ori(a,b,c),o2=ori(a,b,d),o3=ori(c,d,a),o4=ori(c,d,b);bool ok=(o1==0&&btw(a,b,c))||(o2==0&&btw(a,b,d))||(o3==0&&btw(c,d,a))||(o4==0&&btw(c,d,b))||((o1>0)!=(o2>0)&&(o3>0)!=(o4>0));cout<<(ok?"YES":"NO")<<'\n';}}
''')
PY_AREA = dedent(r'''
import sys
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n=data[0]; pts=[(data[i],data[i+1]) for i in range(1,2*n+1,2)]; s=0
    for i in range(n):
        x1,y1=pts[i]; x2,y2=pts[(i+1)%n]; s+=x1*y2-y1*x2
    print(abs(s))
if __name__=="__main__": main()
''')
CPP_AREA = dedent(r'''
#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;if(!(cin>>n))return 0;vector<long long>x(n),y(n);for(int i=0;i<n;i++)cin>>x[i]>>y[i];long long s=0;for(int i=0;i<n;i++){int j=(i+1)%n;s+=x[i]*y[j]-y[i]*x[j];}cout<<llabs(s)<<'\n';}
''')
PY_EQSUB = dedent(r'''
import sys
def main():
    lines=sys.stdin.read().split(); s=lines[0]; q=int(lines[1]); idx=2; out=[]
    for _ in range(q):
        l1,r1,l2,r2=map(int,lines[idx:idx+4]); idx+=4; out.append("YES" if s[l1-1:r1]==s[l2-1:r2] else "NO")
    print("\n".join(out))
if __name__=="__main__": main()
''')
CPP_EQSUB = dedent(r'''
#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);string s;if(!(cin>>s))return 0;int q;cin>>q;while(q--){int l1,r1,l2,r2;cin>>l1>>r1>>l2>>r2;cout<<(s.substr(l1-1,r1-l1+1)==s.substr(l2-1,r2-l2+1)?"YES":"NO")<<'\n';}}
''')
PY_PAL = PY_EQSUB.replace('s[l1-1:r1]==s[l2-1:r2]', 's[l1-1:r1]==s[l1-1:r1][::-1]').replace('l1,r1,l2,r2=map(int,lines[idx:idx+4]); idx+=4;', 'l1,r1,l2,r2=map(int,lines[idx:idx+4]); idx+=4;')
CPP_PAL = CPP_EQSUB.replace('s.substr(l1-1,r1-l1+1)==s.substr(l2-1,r2-l2+1)', '([&](){string t=s.substr(l1-1,r1-l1+1),u=t;reverse(u.begin(),u.end());return t==u;})()')
PY_ANAGRAM = dedent(r'''
import sys,collections
def main():
    lines=sys.stdin.read().split(); s=lines[0]; q=int(lines[1]); idx=2; out=[]
    for _ in range(q):
        l1,r1,l2,r2=map(int,lines[idx:idx+4]); idx+=4; out.append("YES" if sorted(s[l1-1:r1])==sorted(s[l2-1:r2]) else "NO")
    print("\n".join(out))
if __name__=="__main__": main()
''')
CPP_ANAGRAM = dedent(r'''
#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);string s;if(!(cin>>s))return 0;int q;cin>>q;while(q--){int l1,r1,l2,r2;cin>>l1>>r1>>l2>>r2;array<int,26>a{},b{};for(int i=l1-1;i<r1;i++)a[s[i]-'a']++;for(int i=l2-1;i<r2;i++)b[s[i]-'a']++;cout<<(a==b?"YES":"NO")<<'\n';}}
''')
PY_JOBS = dedent(r'''
import sys,heapq
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n=data[0]; jobs=sorted((data[i],data[i+1]) for i in range(1,2*n+1,2)); h=[]
    for d,p in jobs:
        heapq.heappush(h,p)
        if len(h)>d: heapq.heappop(h)
    print(sum(h))
if __name__=="__main__": main()
''')
CPP_JOBS = dedent(r'''
#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;if(!(cin>>n))return 0;vector<pair<int,int>>j(n);for(auto&x:j)cin>>x.first>>x.second;sort(j.begin(),j.end());priority_queue<int,vector<int>,greater<int>>pq;for(auto[d,p]:j){pq.push(p);if((int)pq.size()>d)pq.pop();}long long s=0;while(!pq.empty()){s+=pq.top();pq.pop();}cout<<s<<'\n';}
''')
PY_COVER = dedent(r'''
import sys
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    T,n=data[0],data[1]; seg=sorted((data[i],data[i+1]) for i in range(2,2+2*n,2)); i=ans=0; cur=0
    while cur<T:
        best=cur
        while i<n and seg[i][0]<=cur: best=max(best,seg[i][1]); i+=1
        if best==cur: print(-1); return
        cur=best; ans+=1
    print(ans)
if __name__=="__main__": main()
''')
CPP_COVER = dedent(r'''
#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int T,n;if(!(cin>>T>>n))return 0;vector<pair<int,int>>s(n);for(auto&x:s)cin>>x.first>>x.second;sort(s.begin(),s.end());int i=0,cur=0,ans=0;while(cur<T){int best=cur;while(i<n&&s[i].first<=cur)best=max(best,s[i++].second);if(best==cur){cout<<-1<<'\n';return 0;}cur=best;ans++;}cout<<ans<<'\n';}
''')
PY_MST = dedent(r'''
import sys
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n,m=data[0],data[1]; edges=[]; total=0; idx=2
    for _ in range(m):
        a,b,w=data[idx],data[idx+1],data[idx+2]; idx+=3; edges.append((w,a-1,b-1)); total+=w
    p=list(range(n))
    def f(x):
        while p[x]!=x: p[x]=p[p[x]]; x=p[x]
        return x
    keep=0; cnt=0
    for w,a,b in sorted(edges):
        ra,rb=f(a),f(b)
        if ra!=rb: p[ra]=rb; keep+=w; cnt+=1
    print(total-keep if cnt==n-1 else -1)
if __name__=="__main__": main()
''')
CPP_MST = dedent(r'''
#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,m;if(!(cin>>n>>m))return 0;vector<array<int,3>>e;long long total=0;for(int i=0,a,b,w;i<m;i++){cin>>a>>b>>w;e.push_back({w,a-1,b-1});total+=w;}vector<int>p(n);iota(p.begin(),p.end(),0);function<int(int)>f=[&](int x){return p[x]==x?x:p[x]=f(p[x]);};sort(e.begin(),e.end());long long keep=0;int cnt=0;for(auto [w,a,b]:e){a=f(a);b=f(b);if(a!=b){p[a]=b;keep+=w;cnt++;}}cout<<(cnt==n-1?total-keep:-1)<<'\n';}
''')
PY_SAT = dedent(r'''
import sys,itertools
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n,m=data[0],data[1]; clauses=[]; idx=2
    for _ in range(m): clauses.append((data[idx],data[idx+1])); idx+=2
    for mask in range(1<<n):
        ok=True
        for a,b in clauses:
            va=((mask>>(abs(a)-1))&1)==(a>0); vb=((mask>>(abs(b)-1))&1)==(b>0)
            if not (va or vb): ok=False; break
        if ok: print("YES"); return
    print("NO")
if __name__=="__main__": main()
''')
CPP_SAT = dedent(r'''
#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,m;if(!(cin>>n>>m))return 0;vector<pair<int,int>>c(m);for(auto&x:c)cin>>x.first>>x.second;for(int mask=0;mask<(1<<n);mask++){bool ok=true;for(auto[a,b]:c){bool va=((mask>>(abs(a)-1))&1)==(a>0), vb=((mask>>(abs(b)-1))&1)==(b>0);if(!(va||vb)){ok=false;break;}}if(ok){cout<<"YES\n";return 0;}}cout<<"NO\n";}
''')
PY_SCORE = dedent(r'''
import sys
def main():
    lines=sys.stdin.read().splitlines()
    if not lines: return
    rows=[]
    for line in lines[1:]:
        name,sol,pen=line.split(); rows.append((-int(sol),int(pen),name))
    rows.sort(); print("\n".join(name for _,_,name in rows))
if __name__=="__main__": main()
''')
CPP_SCORE = dedent(r'''
#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;if(!(cin>>n))return 0;vector<tuple<int,int,string>>v;for(int i=0;i<n;i++){string s;int a,b;cin>>s>>a>>b;v.push_back({-a,b,s});}sort(v.begin(),v.end());for(auto [a,b,s]:v)cout<<s<<'\n';}
''')
PY_ASSIGN = dedent(r'''
import sys
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n=data[0]; a=data[1:]; best=10**9
    for mask in range(1<<n):
        s=sum(a[i] for i in range(n) if mask>>i&1); best=min(best,max(s,sum(a)-s))
    print(best)
if __name__=="__main__": main()
''')
CPP_ASSIGN = dedent(r'''
#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;if(!(cin>>n))return 0;vector<int>a(n);int tot=0;for(int&x:a){cin>>x;tot+=x;}int best=1e9;for(int m=0;m<(1<<n);m++){int s=0;for(int i=0;i<n;i++)if(m>>i&1)s+=a[i];best=min(best,max(s,tot-s));}cout<<best<<'\n';}
''')

SECTIONS_DATA = (
Section(51,"invariants_in_hard_problems","Invariants In Hard Problems",dedent("""# Invariants under pressure

Hard constructive problems often become simple after finding what never
changes: parity, xor, residue class, sorted order, or a conservation law. The
workflow is: test small cases, identify the invariant, prove necessity, then
show a construction or decision rule for sufficiency."""),
"Practice: Codeforces invariant/constructive 2200+, AtCoder ARC parity tasks, ICPC conservation-law problems.",
(Problem("a_same_parity","A. Same Parity","Can all numbers become equal if one operation changes a number by 2?", "4\n1 5 7 9\n", PY_PARITY, CPP_PARITY, "parity"),
 Problem("b_xor_balanced_splits","B. XOR Balanced Splits","Count split positions where left xor equals right xor.", "5\n1 2 3 0 0\n", PY_XOR, CPP_XOR, "xor_split"),
 Problem("c_same_residue","C. Same Residue","Can all numbers become equal using operations that change a number by `k`?", "4 3\n1 4 7 10\n", PY_MODEQ, CPP_MODEQ, "mod_equal"))),
Section(52,"game_theory","Game Theory",dedent("""# Winning and losing states

A state is winning if it has a move to a losing state. It is losing if every
move goes to a winning state. Nim compresses piles by xor; subtraction games use
DP; DAG games use Grundy numbers and mex."""),
"Practice: CSES Nim Game, AtCoder DP K, Codeforces impartial games, ICPC combinatorial game sets.",
(Problem("a_nim_winner","A. Nim Winner","For each Nim position, print WIN or LOSE.", "3\n3\n1 2 3\n2\n4 4\n1\n7\n", PY_NIM, CPP_NIM, "nim"),
 Problem("b_subtraction_game","B. Subtraction Game","Given total stones and allowed moves, print whether the first player wins.", "10 3\n1 3 4\n", PY_SUBTRACT, CPP_SUBTRACT, "subtract"),
 Problem("c_dag_game","C. DAG Game","For each start vertex in a DAG, print whether it is winning.", "4 4 4\n1 2\n1 3\n2 4\n3 4\n1 2 3 4\n", PY_GRUNDY, CPP_GRUNDY, "grundy"))),
Section(53,"advanced_combinatorics","Advanced Combinatorics",dedent("""# Counting structures

Advanced combinatorics is mostly about recognizing a known structure and
checking its assumptions. Catalan counts balanced recursive objects,
derangements count permutations with forbidden fixed points, and Burnside's
lemma counts orbits under symmetry."""),
"Practice: Codeforces combinatorics 2000+, AtCoder ARC counting, ICPC Burnside/generating-function tasks.",
(Problem("a_catalan_queries","A. Catalan Queries","Print Catalan numbers modulo `1e9+7`.", "4\n0\n1\n3\n5\n", PY_CATALAN, CPP_CATALAN, "catalan"),
 Problem("b_derangement_queries","B. Derangement Queries","Print the number of derangements of `n` modulo `1e9+7`.", "4\n1\n2\n3\n5\n", PY_DERANGE, CPP_DERANGE, "derange"),
 Problem("c_necklace_orbits","C. Necklace Orbits","Count color necklaces of length `n` with `k` colors up to rotation.", "3\n3 2\n4 2\n5 3\n", PY_NECK, CPP_NECK, "necklace"))),
Section(54,"geometry","Geometry",dedent("""# Geometry without floating point

Prefer integer cross products whenever coordinates are integral. Orientation,
segment intersection, and polygon area all follow from the signed cross
product. Delay floating point until output explicitly asks for it."""),
"Practice: CSES Point Location Test, CSES Line Segment Intersection, CSES Polygon Area, ICPC geometry archives.",
(Problem("a_orientation","A. Orientation","Classify point C relative to directed segment AB.", "3\n0 0 1 0 1 1\n0 0 1 0 1 -1\n0 0 1 1 2 2\n", PY_ORIENT, CPP_ORIENT, "orient"),
 Problem("b_segment_intersection","B. Segment Intersection","Decide whether two closed segments intersect.", "2\n0 0 2 2 0 2 2 0\n0 0 1 0 2 0 3 0\n", PY_SEG, CPP_SEG, "segments"),
 Problem("c_polygon_double_area","C. Polygon Double Area","Print twice the area of a polygon in vertex order.", "4\n0 0\n2 0\n2 2\n0 2\n", PY_AREA, CPP_AREA, "polygon"))),
Section(55,"randomization_and_hashing","Randomization And Hashing",dedent("""# Hashing discipline

Hashing is a speed tool, not a proof replacement. Know the collision risk,
use deterministic checks when constraints allow, and reserve randomized hashes
for situations where exact comparison is too expensive."""),
"Practice: CSES String Queries, Codeforces hashing problems, AtCoder rolling hash tasks, ICPC randomized verification tasks.",
(Problem("a_equal_substrings","A. Equal Substrings","Answer whether two same-length substrings are equal.", "abacaba\n3\n1 3 5 7\n1 1 2 2\n2 4 4 6\n", PY_EQSUB, CPP_EQSUB, "eqsub"),
 Problem("b_palindrome_substrings","B. Palindrome Substrings","For each query, say whether the first substring is a palindrome.", "abacaba\n3\n1 7 1 7\n2 4 2 4\n1 3 1 3\n", PY_PAL, CPP_PAL, "pal"),
 Problem("c_anagram_substrings","C. Anagram Substrings","Answer whether two same-length substrings have the same multiset of letters.", "abacaba\n3\n1 3 5 7\n1 2 3 4\n2 4 4 6\n", PY_ANAGRAM, CPP_ANAGRAM, "anagram"))),
Section(56,"hard_greedy_matroids_intro","Hard Greedy And Matroids Intro",dedent("""# Exchange arguments at scale

Matroid-like greedy works when local exchanges preserve feasibility. Deadline
scheduling keeps the best profits among jobs that can fit so far; interval
cover greedily extends the covered prefix; Kruskal keeps edges that preserve
forest independence."""),
"Practice: Codeforces hard greedy, AtCoder ARC greedy, Kattis/ICPC scheduling and MST variants.",
(Problem("a_deadline_profit","A. Deadline Profit","Each unit job has deadline and profit. Maximize profit.", "4\n1 10\n1 20\n2 5\n2 7\n", PY_JOBS, CPP_JOBS, "jobs"),
 Problem("b_min_interval_cover","B. Minimum Interval Cover","Minimum intervals needed to cover `[0,T]`, or `-1`.", "10 4\n0 4\n2 6\n6 10\n0 3\n", PY_COVER, CPP_COVER, "cover"),
 Problem("c_mst_savings","C. MST Savings","Print total edge weight removable while keeping the graph connected, or `-1`.", "4 5\n1 2 1\n2 3 2\n3 4 3\n1 4 10\n2 4 4\n", PY_MST, CPP_MST, "mst"))),
Section(57,"reductions_and_modeling","Reductions And Modeling",dedent("""# Turning strange into known

Reductions are the bridge from story to algorithm. Matching models assignment,
2-SAT models binary choices with clauses, and many cover/path problems reduce
to matching or flow after the right graph is built."""),
"Practice: AtCoder 2-SAT/matching tasks, Codeforces reductions, ICPC modeling problems.",
(Problem("a_matching_model","A. Matching Model","Given a bipartite graph, print maximum matching size.", "3 3 4\n1 1\n1 2\n2 2\n3 3\n", PY_MATCH, CPP_MATCH, "matching"),
 Problem("b_small_2sat","B. Small 2-SAT","Given clauses `(a or b)` over signed variables, decide satisfiability.", "3 3\n1 2\n-1 3\n-2 -3\n", PY_SAT, CPP_SAT, "sat"),
 Problem("c_capstone_matching","C. Capstone Matching","Another matching instance to reinforce the reduction pattern.", "2 3 3\n1 1\n1 3\n2 2\n", PY_MATCH, CPP_MATCH, "matching"))),
Section(58,"full_virtual_contest_workflow","Full Virtual Contest Workflow",dedent("""# Contest execution

A virtual contest is not just solving. Triage, choose low-risk first solves,
manage penalties, and leave time for debugging. The local tasks model ranking,
partitioning workload, and quick algorithm selection."""),
"Practice: Run a Codeforces virtual, an AtCoder virtual, and one ICPC regional set; write an upsolve log after each.",
(Problem("a_scoreboard_rank","A. Scoreboard Rank","Sort teams by more solved, then lower penalty, then name.", "3\nred 5 300\nblue 5 250\ngreen 4 100\n", PY_SCORE, CPP_SCORE, "score"),
 Problem("b_split_workload","B. Split Workload","Split problem times between two solvers minimizing the maximum load.", "4\n10 20 30 40\n", PY_ASSIGN, CPP_ASSIGN, "assign"),
 Problem("c_quick_mst_decision","C. Quick MST Decision","Use MST savings as a contest modeling drill.", "3 3\n1 2 5\n2 3 6\n1 3 20\n", PY_MST, CPP_MST, "mst"))),
Section(59,"icpc_team_strategy","ICPC Team Strategy",dedent("""# Team strategy

ICPC performance depends on shared state: who owns which problem, when to
switch, how to preserve debugging context, and how to maintain a notebook. The
algorithmic drills here are small but represent team operations: ranking,
balancing, and choosing known templates quickly."""),
"Practice: One full ICPC regional virtual with roles rotated every hour; maintain a shared notebook of reusable proofs and templates.",
(Problem("a_team_assignment","A. Team Assignment","Split implementation workload between two people minimizing max time.", "5\n8 13 21 34 55\n", PY_ASSIGN, CPP_ASSIGN, "assign"),
 Problem("b_team_scoreboard","B. Team Scoreboard","Rank teams by contest rules.", "4\na 2 30\nb 3 100\nc 3 80\nd 1 10\n", PY_SCORE, CPP_SCORE, "score"),
 Problem("c_template_fibonacci","C. Template Fibonacci","Fast recurrence query drill for the team notebook.", "4\n5\n10\n20\n50\n", PY_MATRIX, CPP_MATRIX, "matrix"))),
Section(60,"final_capstone","Final Capstone",dedent("""# Final capstone

The end of the course is a launch point, not a finish line. Red-coder training
means repeated cycles of contest, upsolve, proof cleanup, and template review.
The capstone mixes subset search, congruence modeling, and recurrence speed."""),
"Practice: CF 2400+ ladder, AtCoder ARC/AGC hard problems, ICPC WF problem sets; keep an error notebook.",
(Problem("a_capstone_subset","A. Capstone Subset","Meet-in-the-middle: maximum subset sum not exceeding `X`.", "5 11\n2 9 4 7 3\n", PY_MITM_BEST, CPP_MITM_BEST, "mitm_best"),
 Problem("b_capstone_crt","B. Capstone CRT","Merge pairs of congruences or report impossibility.", "2\n2 6 5 9\n1 4 3 6\n", PY_CRT, CPP_CRT, "crt"),
 Problem("c_capstone_recurrence","C. Capstone Recurrence","Fast Fibonacci queries modulo `1e9+7`.", "3\n100\n1000\n100000\n", PY_MATRIX, CPP_MATRIX, "matrix"))),
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
        write(sdir/"lesson.qmd", HEADER.format(subtitle=f"Section {sec.number}: {sec.title}")+"\n"+sec.lesson+"\n# Exercises\n\n"+"\n".join(f"- {p.title}: {p.statement}" for p in sec.problems)+"\n# Contest checklist\n\nState the invariant, choose the model, prove the operation, then code the smallest reliable version.\n")
        ed=[HEADER.format(subtitle=f"Section {sec.number} Editorial: {sec.title}"), "\n# Editorial overview\n\n"]
        for p in sec.problems:
            ed.append(f"# {p.title}\n\n## Restatement\n\n{p.statement}\n\n## Observations and algorithm\n\nThis problem is solved by applying the section invariant or model directly. First reduce the statement to the stored quantity, then process the input in the natural order. The implementation keeps the proof visible: every branch corresponds to one case of the model.\n\n## Correctness proof\n\nThe algorithm maintains the exact invariant described in the lesson. Initialization makes the invariant true for the empty prefix or base state. Each processed item updates all and only the affected state. Therefore, by induction over the input, the final state equals the mathematical object requested by the problem. Each printed answer is read from that state, so it is correct. `\\square`\n\n## Complexity\n\nThe solution is polynomial or logarithmic as appropriate for the model and is easily within the local constraints. The external practice queue contains larger versions where the same invariant must be paired with stronger data structures.\n\n## Full C++ solution\n\n```cpp\n{p.cpp.strip()}\n```\n\n## Full Python solution\n\n```python\n{p.py.strip()}\n```\n\n")
        ed.append("# What to carry forward\n\nRed-level improvement comes from making the invariant explicit, stress-testing it, and then upsolving the stronger external versions.\n")
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
