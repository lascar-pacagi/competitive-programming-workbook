"""Generate the original Master+ geometry packages for Sections 73--75."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CPP_STUB = """#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // TODO: solve the problem.
    return 0;
}
"""

PY_STUB = """import sys


def main() -> None:
    # TODO: solve the problem.
    pass


if __name__ == "__main__":
    main()
"""

HULL_CPP = r'''#include <bits/stdc++.h>
using namespace std;
using int64 = long long;
struct P { int64 x, y; };
bool operator<(P a, P b) { return tie(a.x,a.y) < tie(b.x,b.y); }
bool operator==(P a, P b) { return a.x == b.x && a.y == b.y; }
P operator+(P a, P b) { return {a.x+b.x,a.y+b.y}; }
P operator-(P a, P b) { return {a.x-b.x,a.y-b.y}; }
int64 cross(P a, P b) { return a.x*b.y-a.y*b.x; }
int64 cross(P a, P b, P c) { return cross(b-a,c-a); }
int64 dist2(P a, P b) { int64 x=a.x-b.x,y=a.y-b.y; return x*x+y*y; }
vector<P> hull(vector<P> p) {
    sort(p.begin(),p.end()); p.erase(unique(p.begin(),p.end()),p.end());
    if (p.size() <= 1) return p;
    vector<P> h;
    for (P x:p) { while(h.size()>=2 && cross(h[h.size()-2],h.back(),x)<=0) h.pop_back(); h.push_back(x); }
    size_t lower=h.size();
    for (int i=(int)p.size()-2;i>=0;--i) { P x=p[i]; while(h.size()>lower && cross(h[h.size()-2],h.back(),x)<=0) h.pop_back(); h.push_back(x); }
    h.pop_back(); return h;
}
'''

HULL_PY = r'''import sys


def cross(a, b, c=None):
    if c is None:
        return a[0] * b[1] - a[1] * b[0]
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    lower = []
    for point in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    upper = []
    for point in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]
'''

HULL_STATS_CPP = HULL_CPP + r'''
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;if(!(cin>>n))return 0;vector<P>p(n);for(auto &q:p)cin>>q.x>>q.y;auto h=hull(p);long long a=0;for(int i=0;i<(int)h.size();++i)a+=cross(h[i],h[(i+1)%h.size()]);cout<<h.size()<<' '<<llabs(a)<<'\n';}
'''
HULL_STATS_PY = HULL_PY + r'''

def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data:return
    h=hull(list(zip(data[1::2],data[2::2])))
    area=abs(sum(cross(h[i],h[(i+1)%len(h)]) for i in range(len(h)))) if h else 0
    print(len(h),area)
if __name__=="__main__":main()
'''

DIAMETER_CPP = HULL_CPP + r'''
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;if(!(cin>>n))return 0;vector<P>p(n);for(auto&q:p)cin>>q.x>>q.y;auto h=hull(p);int m=h.size();if(m<2){cout<<0<<'\n';return 0;}long long ans=0;int j=1;for(int i=0;i<m;++i){int ni=(i+1)%m;while(cross(h[ni]-h[i],h[(j+1)%m]-h[i])>cross(h[ni]-h[i],h[j]-h[i]))j=(j+1)%m;ans=max({ans,dist2(h[i],h[j]),dist2(h[ni],h[j])});}cout<<ans<<'\n';}
'''
DIAMETER_PY = HULL_PY + r'''

def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data:return
    h=hull(list(zip(data[1::2],data[2::2])));m=len(h)
    if m<2:print(0);return
    def sub(a,b):return(a[0]-b[0],a[1]-b[1])
    def d2(a,b):return(a[0]-b[0])**2+(a[1]-b[1])**2
    ans=0;j=1
    for i in range(m):
        ni=(i+1)%m;e=sub(h[ni],h[i])
        while cross(e,sub(h[(j+1)%m],h[i]))>cross(e,sub(h[j],h[i])):j=(j+1)%m
        ans=max(ans,d2(h[i],h[j]),d2(h[ni],h[j]))
    print(ans)
if __name__=="__main__":main()
'''

MINKOWSKI_CPP = HULL_CPP + r'''
vector<P> normalize(vector<P> p){
    if(p.size()<=1)return p; if(cross(p[0],p[1],p[2])<0)reverse(p.begin(),p.end());
    int at=min_element(p.begin(),p.end(),[](P a,P b){return tie(a.y,a.x)<tie(b.y,b.x);})-p.begin();
    rotate(p.begin(),p.begin()+at,p.end());return p;
}
vector<P> minkowski(vector<P>a,vector<P>b){
    a=normalize(a);b=normalize(b);if(a.size()<3||b.size()<3){vector<P>s;for(P x:a)for(P y:b)s.push_back(x+y);return hull(s);}
    int n=a.size(),m=b.size(),i=0,j=0;vector<P>r={a[0]+b[0]};
    while(i<n||j<m){P ea=i<n?a[(i+1)%n]-a[i]:P{0,0};P eb=j<m?b[(j+1)%m]-b[j]:P{0,0};long long z=(i<n&&j<m)?cross(ea,eb):0;
        P step;if(j==m||(i<n&&z>0))step=ea,++i;else if(i==n||z<0)step=eb,++j;else step=ea+eb,++i,++j;r.push_back(r.back()+step);
    }r.pop_back();return hull(r);
}
int locate(const vector<P>&p,P q){int n=p.size();if(n==1)return q==p[0]?0:-1;if(n==2)return cross(p[0],p[1],q)==0&&min(p[0].x,p[1].x)<=q.x&&q.x<=max(p[0].x,p[1].x)&&min(p[0].y,p[1].y)<=q.y&&q.y<=max(p[0].y,p[1].y)?0:-1;
    long long a=cross(p[0],p[1],q),b=cross(p[0],p.back(),q);if(a<0||b>0)return-1;if(a==0)return dist2(p[0],q)<=dist2(p[0],p[1])?0:-1;if(b==0)return dist2(p[0],q)<=dist2(p[0],p.back())?0:-1;
    int l=1,r=n-1;while(r-l>1){int mid=(l+r)/2;if(cross(p[0],p[mid],q)>=0)l=mid;else r=mid;}long long z=cross(p[l],p[(l+1)%n],q);return z<0?-1:(z==0?0:1);}
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,m,q;if(!(cin>>n>>m>>q))return 0;vector<P>a(n),b(m);for(auto&x:a)cin>>x.x>>x.y;for(auto&x:b)cin>>x.x>>x.y;auto s=minkowski(a,b);while(q--){P x;cin>>x.x>>x.y;cout<<(locate(s,x)>=0?"YES\n":"NO\n");}}
'''

MINKOWSKI_PY = HULL_PY + r'''

def normalize(p):
    if len(p)>2 and cross(p[0],p[1],p[2])<0:p.reverse()
    at=min(range(len(p)),key=lambda i:(p[i][1],p[i][0]));return p[at:]+p[:at]
def minkowski(a,b):
    a=normalize(a);b=normalize(b)
    if len(a)<3 or len(b)<3:return hull([(x[0]+y[0],x[1]+y[1]) for x in a for y in b])
    n,m=len(a),len(b);i=j=0;r=[(a[0][0]+b[0][0],a[0][1]+b[0][1])]
    while i<n or j<m:
        ea=(a[(i+1)%n][0]-a[i][0],a[(i+1)%n][1]-a[i][1]) if i<n else (0,0)
        eb=(b[(j+1)%m][0]-b[j][0],b[(j+1)%m][1]-b[j][1]) if j<m else (0,0)
        z=cross(ea,eb) if i<n and j<m else 0
        if j==m or i<n and z>0:step=ea;i+=1
        elif i==n or z<0:step=eb;j+=1
        else:step=(ea[0]+eb[0],ea[1]+eb[1]);i+=1;j+=1
        r.append((r[-1][0]+step[0],r[-1][1]+step[1]))
    return hull(r[:-1])
def locate(p,q):
    n=len(p)
    if n==1:return 0 if p[0]==q else -1
    if n==2:return 0 if cross(p[0],p[1],q)==0 and min(p[0][0],p[1][0])<=q[0]<=max(p[0][0],p[1][0]) and min(p[0][1],p[1][1])<=q[1]<=max(p[0][1],p[1][1]) else -1
    a,b=cross(p[0],p[1],q),cross(p[0],p[-1],q)
    if a<0 or b>0:return -1
    if a==0:return 0 if (q[0]-p[0][0])**2+(q[1]-p[0][1])**2<=(p[1][0]-p[0][0])**2+(p[1][1]-p[0][1])**2 else -1
    if b==0:return 0 if (q[0]-p[0][0])**2+(q[1]-p[0][1])**2<=(p[-1][0]-p[0][0])**2+(p[-1][1]-p[0][1])**2 else -1
    l,r=1,n-1
    while r-l>1:
        mid=(l+r)//2
        if cross(p[0],p[mid],q)>=0:l=mid
        else:r=mid
    z=cross(p[l],p[(l+1)%n],q);return -1 if z<0 else (0 if z==0 else 1)
def main():
    data=list(map(int,sys.stdin.buffer.read().split()));it=iter(data);n,m,q=next(it),next(it),next(it)
    a=[(next(it),next(it)) for _ in range(n)];b=[(next(it),next(it)) for _ in range(m)];s=minkowski(a,b)
    print('\n'.join('YES' if locate(s,(next(it),next(it)))>=0 else 'NO' for _ in range(q)))
if __name__=="__main__":main()
'''

ORTH_CPP = r'''#include <bits/stdc++.h>
using namespace std;struct BIT{vector<long long>t;BIT(int n):t(n+1){}void add(int i,long long v){for(++i;i<(int)t.size();i+=i&-i)t[i]+=v;}long long sum(int i){long long s=0;for(;i;i-=i&-i)s+=t[i];return s;}long long range(int l,int r){return sum(r)-sum(l);}};
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int h,v;if(!(cin>>h>>v))return 0;struct E{long long x;int type;long long y1,y2,w;};vector<E>e;vector<long long>ys;for(int i=0;i<h;++i){long long x1,x2,y,w=1;cin>>x1>>x2>>y;if(x1>x2)swap(x1,x2);e.push_back({x1,0,y,y,w});e.push_back({x2,2,y,y,-w});ys.push_back(y);}for(int i=0;i<v;++i){long long x,y1,y2,w=1;cin>>x>>y1>>y2;if(y1>y2)swap(y1,y2);e.push_back({x,1,y1,y2,w});ys.push_back(y1);ys.push_back(y2);}sort(ys.begin(),ys.end());ys.erase(unique(ys.begin(),ys.end()),ys.end());sort(e.begin(),e.end(),[](E a,E b){return tie(a.x,a.type)<tie(b.x,b.type);});BIT bit(ys.size());long long ans=0;for(auto z:e){if(z.type!=1)bit.add(lower_bound(ys.begin(),ys.end(),z.y1)-ys.begin(),z.w);else{int l=lower_bound(ys.begin(),ys.end(),z.y1)-ys.begin(),r=upper_bound(ys.begin(),ys.end(),z.y2)-ys.begin();ans+=z.w*bit.range(l,r);}}cout<<ans<<'\n';}
'''
ORTH_PY = r'''import bisect,sys
def main():
 data=list(map(int,sys.stdin.buffer.read().split()));
 if not data:return
 it=iter(data);h,v=next(it),next(it);events=[];ys=[]
 for _ in range(h):
  x1,x2,y=next(it),next(it),next(it);x1,x2=sorted((x1,x2));events.extend(((x1,0,y,y,1),(x2,2,y,y,-1)));ys.append(y)
 for _ in range(v):
  x,y1,y2=next(it),next(it),next(it);y1,y2=sorted((y1,y2));events.append((x,1,y1,y2,1));ys.extend((y1,y2))
 ys=sorted(set(ys));bit=[0]*(len(ys)+1)
 def add(i,x):
  i+=1
  while i<len(bit):bit[i]+=x;i+=i&-i
 def pref(i):
  s=0
  while i:s+=bit[i];i-=i&-i
  return s
 ans=0
 for _,kind,y1,y2,w in sorted(events):
  if kind!=1:add(bisect.bisect_left(ys,y1),w)
  else:ans+=w*(pref(bisect.bisect_right(ys,y2))-pref(bisect.bisect_left(ys,y1)))
 print(ans)
if __name__=="__main__":main()
'''

RECT_CPP = r'''#include <bits/stdc++.h>
using namespace std;using ll=long long;struct E{ll x,y1,y2;int d;};int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;if(!(cin>>n))return 0;vector<E>e;vector<ll>ys;for(int i=0;i<n;++i){ll x1,y1,x2,y2;cin>>x1>>y1>>x2>>y2;if(x1>x2)swap(x1,x2);if(y1>y2)swap(y1,y2);if(x1==x2||y1==y2)continue;e.push_back({x1,y1,y2,1});e.push_back({x2,y1,y2,-1});ys.push_back(y1);ys.push_back(y2);}if(e.empty()){cout<<0<<'\n';return 0;}sort(ys.begin(),ys.end());ys.erase(unique(ys.begin(),ys.end()),ys.end());sort(e.begin(),e.end(),[](E a,E b){return a.x<b.x;});int m=ys.size()-1;vector<int>cover(4*m);vector<ll>len(4*m);function<void(int,int,int,int,int,int)>upd=[&](int x,int l,int r,int ql,int qr,int d){if(qr<=l||r<=ql)return;if(ql<=l&&r<=qr)cover[x]+=d;else{int mid=(l+r)/2;upd(2*x,l,mid,ql,qr,d);upd(2*x+1,mid,r,ql,qr,d);}if(cover[x])len[x]=ys[r]-ys[l];else len[x]=r-l==1?0:len[2*x]+len[2*x+1];};ll ans=0,last=e[0].x;for(int i=0;i<(int)e.size();){ll x=e[i].x;ans+=(x-last)*len[1];while(i<(int)e.size()&&e[i].x==x){int l=lower_bound(ys.begin(),ys.end(),e[i].y1)-ys.begin(),r=lower_bound(ys.begin(),ys.end(),e[i].y2)-ys.begin();upd(1,0,m,l,r,e[i].d);++i;}last=x;}cout<<ans<<'\n';}
'''
RECT_PY = r'''import sys
def main():
 data=list(map(int,sys.stdin.buffer.read().split()));
 if not data:return
 it=iter(data);n=next(it);events=[];ys=[]
 for _ in range(n):
  x1,y1,x2,y2=next(it),next(it),next(it),next(it);x1,x2=sorted((x1,x2));y1,y2=sorted((y1,y2))
  if x1!=x2 and y1!=y2:events.extend(((x1,y1,y2,1),(x2,y1,y2,-1)));ys.extend((y1,y2))
 if not events:print(0);return
 ys=sorted(set(ys));index={y:i for i,y in enumerate(ys)};m=len(ys)-1;cover=[0]*(4*m);length=[0]*(4*m)
 def update(x,l,r,ql,qr,d):
  if qr<=l or r<=ql:return
  if ql<=l and r<=qr:cover[x]+=d
  else:
   mid=(l+r)//2;update(2*x,l,mid,ql,qr,d);update(2*x+1,mid,r,ql,qr,d)
  length[x]=ys[r]-ys[l] if cover[x] else (0 if r-l==1 else length[2*x]+length[2*x+1])
 events.sort();ans=0;last=events[0][0];i=0
 while i<len(events):
  x=events[i][0];ans+=(x-last)*length[1]
  while i<len(events) and events[i][0]==x:
   _,y1,y2,d=events[i];update(1,0,m,index[y1],index[y2],d);i+=1
  last=x
 print(ans)
if __name__=="__main__":main()
'''

DOUBLE_RECT_CPP = r'''#include <bits/stdc++.h>
using namespace std;using ll=long long;struct E{ll x,y1,y2;int d;};int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;if(!(cin>>n))return 0;vector<E>e;vector<ll>ys;for(int i=0;i<n;++i){ll x1,y1,x2,y2;cin>>x1>>y1>>x2>>y2;if(x1>x2)swap(x1,x2);if(y1>y2)swap(y1,y2);if(x1==x2||y1==y2)continue;e.push_back({x1,y1,y2,1});e.push_back({x2,y1,y2,-1});ys.push_back(y1);ys.push_back(y2);}if(e.empty()){cout<<0<<'\n';return 0;}sort(ys.begin(),ys.end());ys.erase(unique(ys.begin(),ys.end()),ys.end());sort(e.begin(),e.end(),[](E a,E b){return a.x<b.x;});int m=ys.size()-1;vector<int>cover(4*m);vector<ll>one(4*m),two(4*m);function<void(int,int,int)>pull=[&](int x,int l,int r){ll full=ys[r]-ys[l],child1=r-l==1?0:one[2*x]+one[2*x+1],child2=r-l==1?0:two[2*x]+two[2*x+1];if(cover[x]>=2)one[x]=two[x]=full;else if(cover[x]==1)one[x]=full,two[x]=child1;else one[x]=child1,two[x]=child2;};function<void(int,int,int,int,int,int)>upd=[&](int x,int l,int r,int ql,int qr,int d){if(qr<=l||r<=ql)return;if(ql<=l&&r<=qr)cover[x]+=d;else{int mid=(l+r)/2;upd(2*x,l,mid,ql,qr,d);upd(2*x+1,mid,r,ql,qr,d);}pull(x,l,r);};ll ans=0,last=e[0].x;for(int i=0;i<(int)e.size();){ll x=e[i].x;ans+=(x-last)*two[1];while(i<(int)e.size()&&e[i].x==x){int l=lower_bound(ys.begin(),ys.end(),e[i].y1)-ys.begin(),r=lower_bound(ys.begin(),ys.end(),e[i].y2)-ys.begin();upd(1,0,m,l,r,e[i].d);++i;}last=x;}cout<<ans<<'\n';}
'''

DOUBLE_RECT_PY = r'''import sys
def main():
 data=list(map(int,sys.stdin.buffer.read().split()))
 if not data:return
 it=iter(data);n=next(it);events=[];ys=[]
 for _ in range(n):
  x1,y1,x2,y2=next(it),next(it),next(it),next(it);x1,x2=sorted((x1,x2));y1,y2=sorted((y1,y2))
  if x1!=x2 and y1!=y2:events.extend(((x1,y1,y2,1),(x2,y1,y2,-1)));ys.extend((y1,y2))
 if not events:print(0);return
 ys=sorted(set(ys));index={y:i for i,y in enumerate(ys)};m=len(ys)-1;cover=[0]*(4*m);one=[0]*(4*m);two=[0]*(4*m)
 def update(x,l,r,ql,qr,d):
  if qr<=l or r<=ql:return
  if ql<=l and r<=qr:cover[x]+=d
  else:
   mid=(l+r)//2;update(2*x,l,mid,ql,qr,d);update(2*x+1,mid,r,ql,qr,d)
  full=ys[r]-ys[l];child1=0 if r-l==1 else one[2*x]+one[2*x+1];child2=0 if r-l==1 else two[2*x]+two[2*x+1]
  if cover[x]>=2:one[x]=two[x]=full
  elif cover[x]==1:one[x],two[x]=full,child1
  else:one[x],two[x]=child1,child2
 events.sort();ans=0;last=events[0][0];i=0
 while i<len(events):
  x=events[i][0];ans+=(x-last)*two[1]
  while i<len(events) and events[i][0]==x:
   _,y1,y2,d=events[i];update(1,0,m,index[y1],index[y2],d);i+=1
  last=x
 print(ans)
if __name__=="__main__":main()
'''

CLOSE_CPP = r'''#include <bits/stdc++.h>
using namespace std;using ll=long long;const ll INF=LLONG_MAX;struct P{ll x,y;};ll d2(P a,P b){ll x=a.x-b.x,y=a.y-b.y;return x*x+y*y;}int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;if(!(cin>>n))return 0;vector<P>a(n),tmp(n);for(auto&p:a)cin>>p.x>>p.y;sort(a.begin(),a.end(),[](P p,P q){return tie(p.x,p.y)<tie(q.x,q.y);});function<ll(int,int)>solve=[&](int l,int r){if(r-l<=3){ll d=INF;for(int i=l;i<r;++i)for(int j=i+1;j<r;++j)d=min(d,d2(a[i],a[j]));sort(a.begin()+l,a.begin()+r,[](P p,P q){return p.y<q.y;});return d;}int m=(l+r)/2;ll mid=a[m].x,d=min(solve(l,m),solve(m,r));merge(a.begin()+l,a.begin()+m,a.begin()+m,a.begin()+r,tmp.begin(),[](P p,P q){return p.y<q.y;});copy(tmp.begin(),tmp.begin()+r-l,a.begin()+l);vector<P>s;for(int i=l;i<r;++i)if((a[i].x-mid)*(a[i].x-mid)<d){for(int j=(int)s.size()-1;j>=0&& (a[i].y-s[j].y)*(a[i].y-s[j].y)<d;--j)d=min(d,d2(a[i],s[j]));s.push_back(a[i]);}return d;};cout<<solve(0,n)<<'\n';}
'''
CLOSE_PY = r'''import sys
INF=10**50
def main():
 data=list(map(int,sys.stdin.buffer.read().split()));
 if not data:return
 points=sorted(zip(data[1::2],data[2::2]));n=len(points)
 def solve(p):
  n=len(p)
  if n<=3:
   d=min(((p[i][0]-p[j][0])**2+(p[i][1]-p[j][1])**2 for i in range(n) for j in range(i)),default=INF);return d,sorted(p,key=lambda x:x[1])
  m=n//2;mid=p[m][0];dl,l=solve(p[:m]);dr,r=solve(p[m:]);d=min(dl,dr);merged=[];i=j=0
  while i<len(l) or j<len(r):
   if j==len(r) or i<len(l) and l[i][1]<=r[j][1]:merged.append(l[i]);i+=1
   else:merged.append(r[j]);j+=1
  strip=[]
  for point in merged:
   if (point[0]-mid)**2<d:
    for other in reversed(strip):
     if (point[1]-other[1])**2>=d:break
     d=min(d,(point[0]-other[0])**2+(point[1]-other[1])**2)
    strip.append(point)
  return d,merged
 print(solve(points)[0])
if __name__=="__main__":main()
'''

LATTICE_CPP = HULL_CPP + r'''
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;if(!(cin>>n))return 0;vector<P>p(n);for(auto&q:p)cin>>q.x>>q.y;auto h=hull(p);llong:;long long area=0,b=0;for(int i=0;i<(int)h.size();++i){P a=h[i],c=h[(i+1)%h.size()];area+=cross(a,c);b+=gcd(llabs(a.x-c.x),llabs(a.y-c.y));}cout<<llabs(area)<<' '<<b<<'\n';}
'''
LATTICE_CPP = LATTICE_CPP.replace("llong:;", "")
LATTICE_PY = HULL_PY + r'''
import math
def main():
 data=list(map(int,sys.stdin.buffer.read().split()));h=hull(list(zip(data[1::2],data[2::2])));area=abs(sum(cross(h[i],h[(i+1)%len(h)]) for i in range(len(h))));b=sum(math.gcd(abs(h[i][0]-h[(i+1)%len(h)][0]),abs(h[i][1]-h[(i+1)%len(h)][1])) for i in range(len(h)));print(area,b)
if __name__=="__main__":main()
'''

TRI_CPP = HULL_CPP + r'''
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;if(!(cin>>n))return 0;vector<P>p(n);for(auto&q:p)cin>>q.x>>q.y;auto h=hull(p);int m=h.size();long long ans=0;for(int i=0;i<m;++i){int k=i+2;for(int j=i+1;j<m;++j){if(k<=j)k=j+1;if(k>=m)break;while(k+1<m&&llabs(cross(h[i],h[j],h[k+1]))>llabs(cross(h[i],h[j],h[k])))++k;ans=max(ans,llabs(cross(h[i],h[j],h[k])));}}cout<<ans<<'\n';}
'''
TRI_PY = HULL_PY + r'''
def main():
 data=list(map(int,sys.stdin.buffer.read().split()));h=hull(list(zip(data[1::2],data[2::2])));m=len(h);ans=0
 for i in range(m):
  k=i+2
  for j in range(i+1,m):
   k=max(k,j+1)
   if k>=m:break
   while k+1<m and abs(cross(h[i],h[j],h[k+1]))>abs(cross(h[i],h[j],h[k])):k+=1
   ans=max(ans,abs(cross(h[i],h[j],h[k])))
 print(ans)
if __name__=="__main__":main()
'''

POINT_HULL_CPP = HULL_CPP + MINKOWSKI_CPP.split('int locate',1)[1].split('int main',1)[0].join(['int locate','']) + r'''
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,q;if(!(cin>>n>>q))return 0;vector<P>p(n);for(auto&x:p)cin>>x.x>>x.y;auto h=hull(p);while(q--){P x;cin>>x.x>>x.y;int z=locate(h,x);cout<<(z<0?"OUT\n":z==0?"BOUNDARY\n":"IN\n");}}
'''

# Build point-hull explicitly; string surgery above retains the locate body.
POINT_HULL_PY = HULL_PY + MINKOWSKI_PY.split('def locate',1)[1].split('def main',1)[0].join(['def locate','']) + r'''
def main():
 data=list(map(int,sys.stdin.buffer.read().split()));it=iter(data);n,q=next(it),next(it);h=hull([(next(it),next(it)) for _ in range(n)]);out=[]
 for _ in range(q):
  z=locate(h,(next(it),next(it)));out.append('OUT' if z<0 else ('BOUNDARY' if z==0 else 'IN'))
 print('\n'.join(out))
if __name__=="__main__":main()
'''

WEIGHTED_ORTH_CPP = ORTH_CPP.replace('long long x1,x2,y,w=1;cin>>x1>>x2>>y;', 'long long x1,x2,y,w;cin>>x1>>x2>>y>>w;').replace('long long x,y1,y2,w=1;cin>>x>>y1>>y2;', 'long long x,y1,y2,w;cin>>x>>y1>>y2>>w;')
WEIGHTED_ORTH_PY = ORTH_PY.replace('x1,x2,y=next(it),next(it),next(it);', 'x1,x2,y,w=next(it),next(it),next(it),next(it);').replace('(x1,0,y,y,1),(x2,2,y,y,-1)', '(x1,0,y,y,w),(x2,2,y,y,-w)').replace('x,y1,y2=next(it),next(it),next(it);', 'x,y1,y2,w=next(it),next(it),next(it),next(it);').replace('(x,1,y1,y2,1)', '(x,1,y1,y2,w)')

COLLISION_CPP = MINKOWSKI_CPP.replace('auto s=minkowski(a,b);', 'reverse(b.begin(),b.end());for(auto &x:b)x=P{-x.x,-x.y};auto s=minkowski(a,b);')
COLLISION_PY = MINKOWSKI_PY.replace('s=minkowski(a,b)', 'b=[(-x,-y) for x,y in reversed(b)];s=minkowski(a,b)')

PROBLEMS={
73:[('a_hull_statistics','A. Hull Statistics','hull',HULL_STATS_CPP,HULL_STATS_PY),('b_farthest_pair','B. Farthest Pair','diameter',DIAMETER_CPP,DIAMETER_PY),('c_sum_polygon_queries','C. Sum Polygon Queries','minkowski',MINKOWSKI_CPP,MINKOWSKI_PY)],
74:[('a_orthogonal_crossings','A. Orthogonal Crossings','orth',ORTH_CPP,ORTH_PY),('b_rectangle_union','B. Rectangle Union','rect',RECT_CPP,RECT_PY),('c_closest_pair','C. Closest Pair','closest',CLOSE_CPP,CLOSE_PY)],
75:[('a_convex_lattice_shield','A. Convex Lattice Shield','lattice',LATTICE_CPP,LATTICE_PY),('b_maximum_triangle','B. Maximum Triangle','triangle',TRI_CPP,TRI_PY),('c_robot_collision_translations','C. Robot Collision Translations','collision',COLLISION_CPP,COLLISION_PY),('d_weighted_crossings','D. Weighted Crossings','weighted_orth',WEIGHTED_ORTH_CPP,WEIGHTED_ORTH_PY),('e_double_painted_map','E. Double-Painted Map','double_rect',DOUBLE_RECT_CPP,DOUBLE_RECT_PY),('f_fortress_queries','F. Fortress Queries','point_hull',POINT_HULL_CPP,POINT_HULL_PY)]}

NAMES={73:'Convex Geometry And Minkowski Sums',74:'Geometric Sweeps And Proximity',75:'Master+ Geometry Mixed Contest'}
DIRS={73:'73_convex_geometry_minkowski',74:'74_geometric_sweeps_proximity',75:'75_master_geometry_mixed'}

STATEMENTS={
'hull':'''Given integer points, take their convex hull with no redundant collinear boundary points. Print the number of hull vertices and twice its area. Duplicate input points are allowed.\n\nInput: `n`, then `n` points. `1 <= n <= 200000`, `|coordinate| <= 10^9`.\n\nSample:\n```text\n6\n0 0\n2 0\n2 2\n0 2\n1 0\n1 1\n```\n```text\n4 8\n```''',
'diameter':'''Print the maximum squared Euclidean distance between two of the given integer points.\n\nInput: `n`, then `n` points. `1 <= n <= 200000`, `|coordinate| <= 10^9`. The answer fits signed 64-bit.\n\nSample:\n```text\n5\n0 0\n3 0\n3 2\n0 2\n1 1\n```\n```text\n13\n```''',
'minkowski':'''Polygons `A` and `B` are convex and given counterclockwise, without repeated first vertices or consecutive collinear edges. For each point `p`, decide whether `p = a+b` for some `a` in `A` and `b` in `B`. Boundary points count.\n\nInput: `n m q`, polygon A, polygon B, then q points. `3 <= n,m`, `n+m,q <= 200000`.\n\nSample:\n```text\n4 3 3\n0 0\n2 0\n2 2\n0 2\n0 0\n1 0\n0 1\n1 1\n3 2\n4 4\n```\n```text\nYES\nYES\nNO\n```''',
'orth':'''Count intersections between closed horizontal and closed vertical segments. Every horizontal is `x1 x2 y`; every vertical is `x y1 y2`. An endpoint touching counts, and overlapping collinear pairs are irrelevant because only opposite orientations are counted.\n\nInput: `H V`, then H horizontals and V verticals. `H+V <= 200000`.\n\nSample:\n```text\n2 2\n0 4 1\n2 5 3\n1 0 4\n4 1 3\n```\n```text\n3\n```''',
'rect':'''Print the exact area covered by the union of axis-aligned rectangles. Boundaries have zero area; rectangles may overlap or be degenerate.\n\nInput: `n`, then `x1 y1 x2 y2`. `1 <= n <= 50000`, `|coordinate| <= 10^9`.\n\nSample:\n```text\n2\n0 0 3 2\n1 1 4 3\n```\n```text\n10\n```''',
'double_rect':'''Print the exact area covered by at least two of the axis-aligned rectangles. Boundaries have zero area; rectangles may overlap or be degenerate.\n\nInput: `n`, then `x1 y1 x2 y2`. `1 <= n <= 50000`, `|coordinate| <= 10^9`.\n\nSample:\n```text\n2\n0 0 3 2\n1 1 4 3\n```\n```text\n2\n```''',
'closest':'''Print the minimum squared Euclidean distance between two distinct input points. Equal coordinates at different indices are allowed.\n\nInput: `n`, then n points. `2 <= n <= 200000`, `|coordinate| <= 10^9`. The answer fits signed 64-bit.\n\nSample:\n```text\n4\n0 0\n5 0\n2 2\n3 2\n```\n```text\n1\n```''',
'lattice':'''Build the strict convex hull of the given lattice points. Print its doubled area and the number of lattice points on its boundary.\n\nInput: `n`, then n integer points. `3 <= n <= 200000`. The hull has positive area.\n\nSample:\n```text\n5\n0 0\n4 0\n4 2\n0 2\n2 1\n```\n```text\n16 12\n```''',
'triangle':'''Among all triples of the given points, print twice the maximum triangle area.\n\nInput: `n`, then n points. `3 <= n <= 5000`; the answer fits signed 64-bit.\n\nSample:\n```text\n5\n0 0\n4 0\n4 3\n0 3\n2 1\n```\n```text\n12\n```''',
'collision':'''Convex robots A and B are closed polygons given counterclockwise. Robot A stays fixed; B is translated by vector `t`. For every query, print whether the translated B intersects A, including boundary contact.\n\nInput: `n m q`, polygons A and B, then q translation vectors. `n+m,q <= 200000`.\n\nSample:\n```text\n4 4 3\n0 0\n2 0\n2 2\n0 2\n0 0\n1 0\n1 1\n0 1\n1 1\n2 0\n4 0\n```\n```text\nYES\nYES\nNO\n```''',
'weighted_orth':'''Each horizontal and vertical segment has an integer weight. For every horizontal-vertical intersection, add the product of their weights. Print the total. Segments are closed.\n\nInput: `H V`; H lines `x1 x2 y weight`; V lines `x y1 y2 weight`. `H+V <= 200000`, `|weight| <= 10^6`.\n\nSample:\n```text\n1 2\n0 5 2 3\n1 0 3 4\n5 2 4 4\n```\n```text\n24\n```''',
'point_hull':'''Build the strict convex hull of the input points. For each query point print `IN`, `BOUNDARY`, or `OUT` relative to the closed hull. Degenerate hulls of one point or one segment are allowed.\n\nInput: `n q`, then n points and q queries. `n,q <= 200000`.\n\nSample:\n```text\n5 3\n0 0\n4 0\n4 3\n0 3\n2 1\n2 2\n4 1\n5 1\n```\n```text\nIN\nBOUNDARY\nOUT\n```'''}

STATEMENTS['minkowski'] = STATEMENTS['minkowski'].replace(
    '`n+m,q <= 200000`', '`n+m,q <= 200000`, `|coordinate| <= 10^8`'
)
STATEMENTS['collision'] = STATEMENTS['collision'].replace(
    '`n+m,q <= 200000`', '`n+m,q <= 200000`, `|coordinate| <= 10^8`'
)
STATEMENTS['weighted_orth'] = STATEMENTS['weighted_orth'].replace(
    '`|weight| <= 10^6`', '`|weight| <= 1000`'
)

SAMPLES={'hull':('6\n0 0\n2 0\n2 2\n0 2\n1 0\n1 1\n','4 8\n'),'diameter':('5\n0 0\n3 0\n3 2\n0 2\n1 1\n','13\n'),'minkowski':('4 3 3\n0 0\n2 0\n2 2\n0 2\n0 0\n1 0\n0 1\n1 1\n3 2\n4 4\n','YES\nYES\nNO\n'),'orth':('2 2\n0 4 1\n2 5 3\n1 0 4\n4 1 3\n','4\n'),'rect':('2\n0 0 3 2\n1 1 4 3\n','10\n'),'closest':('4\n0 0\n5 0\n2 2\n3 2\n','1\n'),'lattice':('5\n0 0\n4 0\n4 2\n0 2\n2 1\n','16 12\n'),'triangle':('5\n0 0\n4 0\n4 3\n0 3\n2 1\n','12\n'),'collision':('4 4 3\n0 0\n2 0\n2 2\n0 2\n0 0\n1 0\n1 1\n0 1\n1 1\n2 0\n4 0\n','YES\nYES\nNO\n'),'weighted_orth':('1 2\n0 5 2 3\n1 0 3 4\n5 2 4 4\n','24\n'),'point_hull':('5 3\n0 0\n4 0\n4 3\n0 3\n2 1\n2 2\n4 1\n5 1\n','IN\nBOUNDARY\nOUT\n')}
SAMPLES['orth'] = (SAMPLES['orth'][0], '3\n')
SAMPLES['double_rect'] = ('2\n0 0 3 2\n1 1 4 3\n', '2\n')

LESSONS={73:r'''# The convex hull as a compression

For any objective maximized by a linear direction, interior points never win.
The convex hull replaces an arbitrary point set by its extreme boundary.
Andrew's monotone chain sorts points and maintains the invariant that every
consecutive triple on a partial chain is a strict counterclockwise turn.
Popping while the cross product is nonpositive removes both right turns and
redundant collinear boundary points.

# Rotating calipers

For a fixed hull edge, the signed distance of hull vertices from its line is
unimodal around a convex polygon. Its farthest supporting vertex therefore
moves only forward as the edge moves forward. This monotone pointer is the
rotating-calipers principle. For diameter, compare successive cross products
against the current edge and advance while area increases. Every antipodal
supporting pair is visited, so the maximum squared distance is found in linear
time after the hull.

# Minkowski sums

The Minkowski sum is `A+B = {a+b}`. A linear direction is maximized by adding
the maximizers from A and B, so the result of two convex polygons is convex.
After rotating both polygons to their lowest-leftmost vertex, their directed
edge vectors are already sorted by polar angle. Merge those two cyclic lists;
equal-angle vectors are added together. This is the same reason merging two
sorted arrays works.

Membership in a convex polygon is logarithmic. Fix vertex zero, reject points
outside its first/last rays, binary-search the fan triangle, then use one exact
cross-product test. Treat boundary rays and degenerate hulls separately.

# Exactness and overflow

Coordinates near `1e9` make a cross product approach `4e18`. Check the full
expression range, not merely one multiplication. Python integers are exact;
C++ may require `__int128` if the stated bounds exceed signed 64-bit.

# Exercises

A establishes a canonical strict hull. B adds rotating calipers. C composes
edge-angle merging with logarithmic point location.
''',74:r'''# Sweep events are geometric state changes

A sweep line is useful when the answer at coordinate `x` depends only on
objects currently crossing that line. Correctness begins with event ordering.
For closed horizontal segments, process `add`, then vertical `query`, then
`remove` at the same x; this makes both endpoints active.

Compress y-coordinates and store active horizontal counts in a Fenwick tree.
A vertical segment asks for the number of active y-values in its closed range.
The geometry has become a one-dimensional range-sum problem.

# Rectangle union area

Between consecutive x-events, the covered y-length is constant. Area gained is
`delta_x * covered_y`. A segment tree over elementary compressed y-intervals
stores a cover count and covered length. If a node's cover count is positive,
its full geometric interval is covered; otherwise its length is the sum of its
children. Group equal-x events so zero-width ordering cannot create area.

# Closest pair divide and conquer

Split points by x. After recursively solving both halves, only a vertical strip
of width `sqrt(d)` can contain a better cross-half pair. Keep each recursive
result sorted by y and merge them. In the strip, compare forward only while the
y-gap squared is below `d`. Packing equal squares shows that only constantly
many later points need examination.

The important subtlety is that the recursive array must remain y-sorted while
the split coordinate is saved before recursion. Duplicate points immediately
produce distance zero and must not break the strip logic.

# Exercises

A focuses on inclusive event order. B combines a sweep with a geometric-length
segment-tree invariant. C uses a geometric packing proof to remove a quadratic
comparison loop.
''',75:r'''# Contest contract

This six-problem contest synthesizes Sections 73--74 with entirely new local
statements.

| Problem | Main invariant |
|---|---|
| A | strict hull plus lattice count per edge |
| B | unimodal triangle area on a convex boundary |
| C | collision translations form a Minkowski difference |
| D | weighted active set under inclusive sweep events |
| E | lengths covered at least once and at least twice |
| F | strict hull plus logarithmic fan location |

# Suggested use

Allow four hours. Draw all degeneracies before coding: collinear input,
duplicate points, endpoint contact, equal event coordinates, and zero-area
rectangles. For every pointer or event order, write the monotonicity or
inclusion statement that makes it legal.

# Exercises

Solve A--F without opening the editorials. The set has exactly six exercises
and collectively covers every principal technique from Sections 73--74.
'''}

NOTES={'hull':'Sort and deduplicate. The lower and upper stacks retain only strict left turns. Every popped point lies on or inside the segment joining its neighbors, so it cannot be an extreme vertex. The two chains contain every extreme point once. Shoelace on that canonical cycle gives doubled area. Time is `O(n log n)`.','diameter':'Only hull vertices can form a farthest pair. For each directed hull edge, advance the opposite pointer while its cross product with that edge increases. Convexity makes this value unimodal and makes the pointer monotone. Rotating calipers visits every antipodal candidate in `O(h)` after the hull.','minkowski':'Support functions add under Minkowski sum, proving convexity and the edge-angle merge. Starting at the sum of lowest vertices and merging the sorted edge vectors traces the entire boundary once. A fan binary search then locates each query in `O(log(n+m))`.','orth':'At sweep coordinate x, the Fenwick tree contains exactly horizontals whose closed x-range contains x because adds precede queries and removals follow them. A vertical query sums exactly active y-values in its closed interval. Total time is `O((H+V) log(H+V))`.','rect':'The active rectangle set changes only at vertical sides. Between event x-values, covered y-length is constant, so multiplying it by the width is exact. The cover-count segment tree stores the union length of active y-intervals. Complexity is `O(n log n)`.','closest':'A better cross-half pair must lie inside the width-sqrt(d) strip. Sorting it by y permits stopping once the y-gap reaches sqrt(d); planar packing bounds the remaining comparisons per point by a constant. Merging y-orders at every recursion gives `O(n log n)`.','lattice':'Build the strict hull, apply shoelace, and sum `gcd(|dx|,|dy|)` over hull edges. That gcd counts each edge’s lattice steps; summing half-open edge counts counts every boundary lattice point exactly once.','triangle':'A maximum-area triangle uses hull vertices. For fixed ordered i,j, triangle area as k walks forward on a convex polygon is unimodal, so k never moves backward as j advances. The nested scan is `O(h^2)` rather than cubic.','collision':'A translated B intersects A exactly when there exist a in A and b in B with a=b+t, equivalently t=a-b. Thus valid translations are the closed convex polygon A+(-B). Build it by Minkowski edge merge and answer membership queries logarithmically.','weighted_orth':'The ordinary orthogonal sweep is linear in weights: store the sum of active horizontal weights at each y, query the range sum, and multiply by the vertical weight. Each intersecting pair contributes its product exactly once.','point_hull':'The convex hull is the closed region of interest. Rays from hull[0] partition it into triangles. The first and last ray reject impossible directions; binary search selects the unique fan wedge, and one cross product distinguishes inside, boundary, and outside.'}
NOTES['double_rect'] = 'Sweep vertical sides as for union area, but each node stores two measures: length covered at least once and length covered at least twice. With local cover at least two, both equal the full interval; with local cover one, twice-covered length equals the children’s once-covered length; with local cover zero, both are child sums. This induction makes the root’s second measure exact in `O(n log n)`.'

FIND = {
    'hull': 'The raw set has no useful cyclic order. Ask which points can maximize a dot product in some direction; only extreme points survive, suggesting a convex hull before any area computation.',
    'diameter': 'The quadratic search remains quadratic even after building a hull. Plot the area against one fixed hull edge: convexity makes the farthest supporting vertex move in one direction, which is the signal for calipers.',
    'minkowski': 'The quantifier “choose one point from each polygon and add them” names a Minkowski sum. Looking at one support direction shows both why the sum is convex and why its boundary edges can be merged by angle.',
    'orth': 'Sweeping by x turns every horizontal into an active interval in time and every vertical into a y-range query. Write the endpoint convention before selecting the add/query/remove order.',
    'rect': 'Do not attempt inclusion-exclusion over rectangles. Sweep between consecutive vertical sides; the only changing quantity is the one-dimensional union length on y.',
    'double_rect': 'Ordinary union length loses how much overlap remains below a covered node. Strengthen the state minimally: retain both once-covered and twice-covered length, then derive how a node’s local cover shifts those thresholds.',
    'closest': 'The slow pair search becomes useful after splitting by x: recursive answers eliminate everything except a narrow cross-boundary strip. The remaining question is why y-order plus packing makes that strip linear.',
    'lattice': 'Neither area nor lattice counting needs interior points. Compress to the hull, then recognize the two independent edge accumulations: cross products for area and gcd steps for boundary points.',
    'triangle': 'First move every triangle vertex to the hull without decreasing area. Fix two vertices and inspect area while the third walks around the convex boundary; its unimodality removes one loop.',
    'collision': 'Rewrite intersection algebraically as `a = b+t`. Solving for the query vector gives `t = a-b`, revealing that every valid translation lies in one Minkowski difference.',
    'weighted_orth': 'Start from the unweighted sweep and use linearity: counts become sums of horizontal weights, while each vertical query scales that sum by its own weight.',
    'point_hull': 'Many queries justify preprocessing. A convex polygon viewed from one vertex is an ordered fan of triangles, so angular monotonicity replaces a linear edge scan by binary search.',
}

def front(sub):return f'''---\ntitle: "Competitive Programming"\nsubtitle: "{sub}"\nauthor: "Competitive Programming Course"\nformat:\n  pdf:\n    pdf-engine: xelatex\n    documentclass: scrreprt\n    papersize: a4\n    toc: true\n    number-sections: true\n    colorlinks: true\n    geometry: [margin=25mm]\nexecute: {{enabled: false}}\n---\n\n'''
def write(p,s):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s.rstrip()+'\n')
def build():
 for sec,probs in PROBLEMS.items():
  base=ROOT/'sections'/DIRS[sec];rows='\n'.join(f'- [{t}](problems/{s}/README.md)' for s,t,*_ in probs)
  write(base/'README.md',f'# Section {sec}: {NAMES[sec]}\n\n{rows}');write(base/'PRACTICE.md',f'# Section {sec} Practice\n\nAll required exercises are local:\n\n{rows}')
  names=', '.join(repr(x[0]) for x in probs);write(base/'check.py',f'''"""Friendly checker for Section {sec}."""\nfrom pathlib import Path\nimport sys\nROOT=Path(__file__).resolve().parents[2]\nsys.path.insert(0,str(ROOT))\nfrom tools.section_checker import run_section_checks\nSECTION=Path(__file__).resolve().parent\nPROBLEMS=[SECTION/"problems"/x for x in ({names},)]\nif __name__=="__main__":raise SystemExit(run_section_checks({sec},PROBLEMS,ROOT))''')
  write(base/'lesson.qmd',front(f'Section {sec}: {NAMES[sec]}')+LESSONS[sec]);ed=[front(f'Section {sec} Editorial: {NAMES[sec]}'),'# How to use this editorial\n\nRecover the geometric invariant and degeneracy policy before comparing code.']
  for slug,title,kind,*_ in probs:ed.append(f'# {title}\n\n## How to find it\n\n{FIND[kind]}\n\n## Derivation and correctness\n\n{NOTES[kind]}\n\n## Failure-focused tests\n\nCompare with the independent tiny brute-force oracle. Include collinearity, duplicates, equal event coordinates, boundary contact, and the smallest legal instance.\n\n## C++\n\n```cpp\n{{{{< include problems/{slug}/solution.cpp >}}}}\n```\n\n## Python\n\n```python\n{{{{< include problems/{slug}/solution.py >}}}}\n```')
  write(base/'editorial.qmd','\n\n'.join(ed))
  for slug,title,kind,cpp,py in probs:
   d=base/'problems'/slug;write(d/'README.md',f'# {title}\n\n{STATEMENTS[kind]}');write(d/'manifest.json',json.dumps({'title':title,'checker':'tokens','time_limit_seconds':7.0},separators=(',',':')));write(d/'solve.cpp',CPP_STUB);write(d/'solve.py',PY_STUB);write(d/'solution.cpp',cpp);write(d/'solution.py',py);inp,out=SAMPLES[kind];write(d/'tests/sample1.in',inp);write(d/'tests/sample1.out',out);write(d/'tests/random_cases.py',f'''import subprocess,sys\nfrom pathlib import Path\nROOT=Path(__file__).resolve().parents[5]\nraise SystemExit(subprocess.call([sys.executable,str(ROOT/"tools"/"geometry_advanced_random.py"),"{kind}",*sys.argv[1:]]))''')
if __name__=='__main__':build()
