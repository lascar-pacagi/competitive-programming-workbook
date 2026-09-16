"""Generate Sections 94--96: continuous geometry and Delaunay structure."""
from __future__ import annotations
import ast,json,textwrap
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
INCIRCLE_DIR=ROOT/'sections/94_half_planes_circle_geometry/problems/d_largest_inscribed_circle'
OPTIMIZED_INCIRCLE_PY=(INCIRCLE_DIR/'solution.py').read_text()
OPTIMIZED_INCIRCLE_CPP=(INCIRCLE_DIR/'solution.cpp').read_text()
CPP_STUB='''#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // TODO: solve the problem.
    return 0;
}
'''
PY_STUB='''import sys


def main() -> None:
    # TODO: solve the problem.
    pass


if __name__ == "__main__":
    main()
'''
SECTIONS={94:("half_planes_circle_geometry","Half-Planes And Circle Geometry"),95:("geometric_optimization_delaunay","Geometric Optimization And Delaunay Structure"),96:("master_continuous_geometry_mixed","Master Continuous Geometry Mixed Contest")}
PROBLEMS={94:[("a_half_plane_region","Half-Plane Region","hpi"),("b_circle_overlap","Circle Overlap","overlap"),("c_common_tangent_count","Common Tangent Count","tangents"),("d_largest_inscribed_circle","Largest Inscribed Circle","incircle")],95:[("a_minimum_enclosing_circle","Minimum Enclosing Circle","mec"),("b_delaunay_radius_sum","Delaunay Radius Sum","delaunay"),("c_euclidean_network","Euclidean Network","mst"),("d_largest_empty_delaunay_circle","Largest Empty Delaunay Circle","empty")]}
STATEMENTS={
'hpi':'''Each directed line from `A` to `B` keeps the closed half-plane on its left. Compute the area of their intersection. Print `0` if it is empty. The input guarantees that every nonempty intersection is bounded. `n <= 200000`; coordinates have absolute value at most `10^6`.

Sample input
```text
4
0 0 2 0
2 0 2 2
2 2 0 2
0 2 0 0
```
Sample output
```text
4.0000000000
```''',
'overlap':'''Given two circles `(x,y,r)`, print the area common to both disks. Coordinates and positive radii are at most `10^9` in absolute value.

Sample input
```text
0 0 1
1 0 1
```
Sample output
```text
1.2283696986
```''',
'tangents':'''Print the number of distinct lines tangent to both given circles. Print `-1` if the circles coincide and therefore have infinitely many common tangents. Coordinates and positive radii are at most `10^9` in absolute value.

Sample input
```text
0 0 1
4 0 1
```
Sample output
```text
4
```''',
'incircle':'''A strictly convex polygon is given counterclockwise. Print the greatest radius of a circle contained in it. `3 <= n <= 200000`; coordinates have absolute value at most `10^6`.

Sample input
```text
4
0 0
2 0
2 2
0 2
```
Sample output
```text
1.0000000000
```''',
'mec':'''Given `1 <= n <= 200000` points with coordinates of absolute value at most `10^9`, print the center and radius of their minimum enclosing circle. Output `cx cy r`.

Sample input
```text
3
0 0
2 0
0 2
```
Sample output
```text
1.0000000000 1.0000000000 1.4142135624
```''',
'delaunay':'''Given `3 <= n <= 2500` planar points with coordinates of absolute value at most `10^9`, print the sum of the circumradii of all triangles in their Delaunay triangulation. No three points are collinear and no four are cocircular, so the triangulation is unique.

Sample input
```text
3
0 0
2 0
0 2
```
Sample output
```text
1.4142135624
```''',
'mst':'''Given `0 <= n <= 2500` planar points with coordinates of absolute value at most `10^9`, print the total Euclidean length of a minimum spanning tree of the complete geometric graph. No three points are collinear and no four are cocircular.

Sample input
```text
3
0 0
2 0
0 2
```
Sample output
```text
4.0000000000
```''',
'empty':'''For points in general position, consider only empty circles passing through three points. Print the largest radius among these circles, or `0` when fewer than three points are given. `0 <= n <= 2500`; coordinates have absolute value at most `10^9`; no three points are collinear and no four are cocircular.

Sample input
```text
3
0 0
2 0
0 2
```
Sample output
```text
1.4142135624
```''',
}
STATEMENTS['hpi_story']=STATEMENTS['hpi'].replace('Each directed line','Safety rule: each directed boundary').replace('Compute the area','Compute the safe operating area')
STATEMENTS['incircle_story']=STATEMENTS['incircle'].replace('A strictly convex polygon','A strictly convex hall').replace('circle contained in it','round table contained in it')
STATEMENTS['overlap_story']=STATEMENTS['overlap'].replace('two circles','two circular sensor ranges').replace('both disks','both ranges')
STATEMENTS['mec_story']=STATEMENTS['mec'].replace('points','emergency sites').replace('minimum enclosing circle','smallest broadcast disk')
STATEMENTS['empty_story']=STATEMENTS['empty'].replace('points in general position','observation posts in general position').replace('empty circles','observation circles containing no post in their interior')
STATEMENTS['mst_story']=STATEMENTS['mst'].replace('points','stations').replace('minimum spanning tree','minimum-length fiber network')

PY_CORE=r'''import sys,math,random
from collections import deque
EPS=1e-10
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def sub(a,b):return(a[0]-b[0],a[1]-b[1])
def mul(a,k):return(a[0]*k,a[1]*k)
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def dot(a,b):return a[0]*b[0]+a[1]*b[1]
def norm(a):return math.hypot(a[0],a[1])
def intersection(a,b):
 t=cross(sub(b[0],a[0]),b[1])/cross(a[1],b[1]);return add(a[0],mul(a[1],t))
def halfplanes(raw):
 lines=[]
 for a,b in raw:
  v=sub(b,a);lines.append((a,v,math.atan2(v[1],v[0])))
 lines.sort(key=lambda z:z[2]);unique=[]
 for p,v,angle in lines:
  if unique and abs(cross(unique[-1][1],v))<=EPS and dot(unique[-1][1],v)>0:
   if cross(unique[-1][1],sub(p,unique[-1][0]))>EPS:unique[-1]=(p,v,angle)
  else:unique.append((p,v,angle))
 dq=deque();points=deque()
 def inside(line,p):return cross(line[1],sub(p,line[0]))>=-EPS
 for line in unique:
  while points and not inside(line,points[-1]):points.pop();dq.pop()
  while points and not inside(line,points[0]):points.popleft();dq.popleft()
  if dq and abs(cross(dq[-1][1],line[1]))<=EPS:return []
  if dq:points.append(intersection(dq[-1],line))
  dq.append(line)
 while points and not inside(dq[0],points[-1]):points.pop();dq.pop()
 while points and not inside(dq[-1],points[0]):points.popleft();dq.popleft()
 if len(dq)<3:return []
 points.append(intersection(dq[-1],dq[0]));return list(points)
def area(poly):return abs(sum(cross(poly[i],poly[(i+1)%len(poly)]) for i in range(len(poly))))/2 if len(poly)>=3 else 0.0
def overlap(c1,c2):
 x1,y1,r1=c1;x2,y2,r2=c2;d=math.hypot(x1-x2,y1-y2)
 if d>=r1+r2:return 0.0
 if d<=abs(r1-r2):return math.pi*min(r1,r2)**2
 a=math.acos(max(-1,min(1,(d*d+r1*r1-r2*r2)/(2*d*r1))));b=math.acos(max(-1,min(1,(d*d+r2*r2-r1*r1)/(2*d*r2))))
 return r1*r1*a+r2*r2*b-d*r1*math.sin(a)
def tangent_count(c1,c2):
 x1,y1,r1=c1;x2,y2,r2=c2;d=math.hypot(x1-x2,y1-y2)
 if d<=EPS:return -1 if abs(r1-r2)<=EPS else 0
 ans=0
 for z in (abs(r1-r2),r1+r2):ans+=2 if d>z+EPS else (1 if abs(d-z)<=EPS else 0)
 return ans
def shifted_polygon(poly,r):
 lines=[]
 for i,p in enumerate(poly):
  q=poly[(i+1)%len(poly)];v=sub(q,p);length=norm(v);shift=(-v[1]*r/length,v[0]*r/length);lines.append((add(p,shift),add(q,shift)))
 return halfplanes(lines)
def inradius(poly):
 low=0.0;high=max(max(x for x,y in poly)-min(x for x,y in poly),max(y for x,y in poly)-min(y for x,y in poly))+1
 for _ in range(70):
  mid=(low+high)/2
  if shifted_polygon(poly,mid):low=mid
  else:high=mid
 return low
def circle2(a,b):
 c=((a[0]+b[0])/2,(a[1]+b[1])/2);return(c,norm(sub(a,b))/2)
def circle3(a,b,c):
 d=2*cross(sub(b,a),sub(c,a))
 ux=(dot(a,a)*(b[1]-c[1])+dot(b,b)*(c[1]-a[1])+dot(c,c)*(a[1]-b[1]))/d
 uy=(dot(a,a)*(c[0]-b[0])+dot(b,b)*(a[0]-c[0])+dot(c,c)*(b[0]-a[0]))/d
 center=(ux,uy);return(center,norm(sub(center,a)))
def minimum_circle(points):
 p=points[:];random.Random(947311).shuffle(p);circle=((0.0,0.0),-1.0)
 def outside(x,c):return c[1]<0 or norm(sub(x,c[0]))>c[1]+1e-9
 for i in range(len(p)):
  if outside(p[i],circle):
   circle=(p[i],0.0)
   for j in range(i):
    if outside(p[j],circle):
     circle=circle2(p[i],p[j])
     for k in range(j):
      if outside(p[k],circle):circle=circle3(p[i],p[j],p[k])
 return circle
def orient(a,b,c):return cross(sub(b,a),sub(c,a))
def in_circumcircle(a,b,c,p):
 ax=a[0]-p[0];ay=a[1]-p[1];bx=b[0]-p[0];by=b[1]-p[1];cx=c[0]-p[0];cy=c[1]-p[1]
 det=(ax*ax+ay*ay)*(bx*cy-by*cx)-(bx*bx+by*by)*(ax*cy-ay*cx)+(cx*cx+cy*cy)*(ax*by-ay*bx)
 return det>EPS
def delaunay(points):
 n=len(points)
 if n<3:return [],[]
 minx=min(x for x,y in points);maxx=max(x for x,y in points);miny=min(y for x,y in points);maxy=max(y for x,y in points);span=max(maxx-minx,maxy-miny,1.0);cx=(minx+maxx)/2;cy=(miny+maxy)/2
 p=points+[(cx-10000*span,cy-8000*span),(cx+10000*span,cy-8000*span),(cx,cy+10000*span)];tri=[(n,n+1,n+2)]
 for idx in range(n):
  bad=[t for t in tri if in_circumcircle(p[t[0]],p[t[1]],p[t[2]],p[idx])];count={};direct={}
  for t in bad:
   for e in ((t[0],t[1]),(t[1],t[2]),(t[2],t[0])):key=tuple(sorted(e));count[key]=count.get(key,0)+1;direct[key]=e
  gone=set(bad);tri=[t for t in tri if t not in gone]
  for key,cnt in count.items():
   if cnt==1:
    u,v=direct[key]
    if orient(p[u],p[v],p[idx])<0:u,v=v,u
    tri.append((u,v,idx))
 tri=[t for t in tri if max(t)<n];edges=set()
 for a,b,c in tri:
  edges|={tuple(sorted((a,b))),tuple(sorted((b,c))),tuple(sorted((c,a)))}
 return tri,sorted(edges)
def radius_sum(points,maximum=False):
 tri,_=delaunay(points);values=[circle3(points[a],points[b],points[c])[1] for a,b,c in tri]
 return (max(values) if values else 0.0) if maximum else sum(values)
def mst(points):
 n=len(points)
 if n<2:return 0.0
 _,edges=delaunay(points)
 if not edges:edges=[(i,i+1) for i in range(n-1)]
 parent=list(range(n))
 def find(x):
  while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
  return x
 ans=0.0
 for w,u,v in sorted((norm(sub(points[u],points[v])),u,v) for u,v in edges):
  u=find(u);v=find(v)
  if u!=v:parent[u]=v;ans+=w
 return ans
'''

def py_solution(kind):
 base={'hpi_story':'hpi','incircle_story':'incircle','overlap_story':'overlap','mec_story':'mec','empty_story':'empty','mst_story':'mst'}.get(kind,kind)
 if base=='incircle':return OPTIMIZED_INCIRCLE_PY
 body={
 'hpi':'''n=int(d[0]);raw=[]
 for i in range(n):x1,y1,x2,y2=d[1+4*i:5+4*i];raw.append(((x1,y1),(x2,y2)))
 print(f'{area(halfplanes(raw)):.10f}')''',
 'overlap':'''print(f'{overlap(d[:3],d[3:6]):.10f}')''',
 'tangents':'''print(tangent_count(d[:3],d[3:6]))''',
 'incircle':'''n=int(d[0]);p=[tuple(d[1+2*i:3+2*i]) for i in range(n)];print(f'{inradius(p):.10f}')''',
 'mec':'''n=int(d[0]);p=[tuple(d[1+2*i:3+2*i]) for i in range(n)];c,r=minimum_circle(p);print(f'{c[0]:.10f} {c[1]:.10f} {r:.10f}')''',
 'delaunay':'''n=int(d[0]);p=[tuple(d[1+2*i:3+2*i]) for i in range(n)];print(f'{radius_sum(p):.10f}')''',
 'empty':'''n=int(d[0]);p=[tuple(d[1+2*i:3+2*i]) for i in range(n)];print(f'{radius_sum(p,True):.10f}')''',
 'mst':'''n=int(d[0]);p=[tuple(d[1+2*i:3+2*i]) for i in range(n)];print(f'{mst(p):.10f}')'''}[base]
 lines=textwrap.dedent(body).strip().splitlines()
 if len(lines)>1 and lines[1].startswith(' '):lines=[lines[0]]+[x[1:] if x.startswith(' ') else x for x in lines[1:]]
 body='\n'.join(lines)
 roots={'hpi':{'area','halfplanes'},'overlap':{'overlap'},'tangents':{'tangent_count'},'incircle':{'inradius'},'mec':{'minimum_circle'},'delaunay':{'radius_sum'},'empty':{'radius_sum'},'mst':{'mst'}}[base]
 tree=ast.parse(PY_CORE);definitions={node.name:node for node in tree.body if isinstance(node,(ast.FunctionDef,ast.ClassDef))};needed=set(roots);changed=True
 while changed:
  changed=False
  for name in list(needed):
   node=definitions.get(name)
   if node:
    for child in ast.walk(node):
     if isinstance(child,ast.Name) and isinstance(child.ctx,ast.Load) and child.id in definitions and child.id not in needed:needed.add(child.id);changed=True
 keep=[]
 for node in tree.body:
  if isinstance(node,(ast.Import,ast.ImportFrom)):keep.append(node)
  elif isinstance(node,(ast.FunctionDef,ast.ClassDef)) and node.name in needed:keep.append(node)
  elif isinstance(node,(ast.Assign,ast.AnnAssign)):
   names={x.id for x in ast.walk(node) if isinstance(x,ast.Name) and isinstance(x.ctx,ast.Store)}
   if names&{'EPS'}:keep.append(node)
 core=ast.unparse(ast.Module(body=keep,type_ignores=[]))+'\n'
 return core+'def main():\n d=list(map(float,sys.stdin.buffer.read().split()))\n'+textwrap.indent(body,' ')+'\nif __name__==\'__main__\':main()\n'

CPP_CORE=r'''#include <bits/stdc++.h>
using namespace std;const double EPS=1e-10,PI=acos(-1.0);struct P{double x,y;P operator+(P b)const{return{x+b.x,y+b.y};}P operator-(P b)const{return{x-b.x,y-b.y};}P operator*(double k)const{return{x*k,y*k};}};double cross(P a,P b){return a.x*b.y-a.y*b.x;}double dot(P a,P b){return a.x*b.x+a.y*b.y;}double norm(P a){return hypot(a.x,a.y);}struct L{P p,v;double angle;};P meet(L a,L b){double t=cross(b.p-a.p,b.v)/cross(a.v,b.v);return a.p+a.v*t;}
vector<P>halfplanes(vector<pair<P,P>>raw){vector<L>a;for(auto[p,q]:raw){P v=q-p;a.push_back({p,v,atan2(v.y,v.x)});}sort(a.begin(),a.end(),[](L x,L y){return x.angle<y.angle;});vector<L>u;for(L z:a){if(!u.empty()&&abs(cross(u.back().v,z.v))<=EPS&&dot(u.back().v,z.v)>0){if(cross(u.back().v,z.p-u.back().p)>EPS)u.back()=z;}else u.push_back(z);}deque<L>q;deque<P>pts;auto inside=[](L l,P p){return cross(l.v,p-l.p)>=-EPS;};for(L z:u){while(!pts.empty()&&!inside(z,pts.back()))pts.pop_back(),q.pop_back();while(!pts.empty()&&!inside(z,pts.front()))pts.pop_front(),q.pop_front();if(!q.empty()&&abs(cross(q.back().v,z.v))<=EPS)return{};if(!q.empty())pts.push_back(meet(q.back(),z));q.push_back(z);}while(!pts.empty()&&!inside(q.front(),pts.back()))pts.pop_back(),q.pop_back();while(!pts.empty()&&!inside(q.back(),pts.front()))pts.pop_front(),q.pop_front();if(q.size()<3)return{};pts.push_back(meet(q.back(),q.front()));return vector<P>(pts.begin(),pts.end());}
double area(vector<P>p){double s=0;for(int i=0;i<(int)p.size();i++)s+=cross(p[i],p[(i+1)%p.size()]);return abs(s)/2;}struct C{P p;double r;};double overlap(C a,C b){double d=norm(a.p-b.p);if(d>=a.r+b.r)return 0;if(d<=abs(a.r-b.r))return PI*min(a.r,b.r)*min(a.r,b.r);double x=acos(clamp((d*d+a.r*a.r-b.r*b.r)/(2*d*a.r),-1.0,1.0)),y=acos(clamp((d*d+b.r*b.r-a.r*a.r)/(2*d*b.r),-1.0,1.0));return a.r*a.r*x+b.r*b.r*y-d*a.r*sin(x);}int tangents(C a,C b){double d=norm(a.p-b.p);if(d<=EPS)return abs(a.r-b.r)<=EPS?-1:0;int ans=0;for(double z:{abs(a.r-b.r),a.r+b.r})ans+=d>z+EPS?2:(abs(d-z)<=EPS);return ans;}
vector<P>shifted(vector<P>p,double r){vector<pair<P,P>>l;for(int i=0;i<(int)p.size();i++){P q=p[(i+1)%p.size()],v=q-p[i],s={-v.y*r/norm(v),v.x*r/norm(v)};l.push_back({p[i]+s,q+s});}return halfplanes(l);}double inradius(vector<P>p){double lo=0,hi=1;for(P x:p)for(P y:p)hi=max(hi,norm(x-y));for(int z=0;z<70;z++){double m=(lo+hi)/2;(shifted(p,m).empty()?hi:lo)=m;}return lo;}
C circle2(P a,P b){P c=(a+b)*.5;return{c,norm(a-b)/2};}C circle3(P a,P b,P c){double d=2*cross(b-a,c-a);double aa=dot(a,a),bb=dot(b,b),cc=dot(c,c);P o={(aa*(b.y-c.y)+bb*(c.y-a.y)+cc*(a.y-b.y))/d,(aa*(c.x-b.x)+bb*(a.x-c.x)+cc*(b.x-a.x))/d};return{o,norm(o-a)};}C mec(vector<P>p){mt19937 rng(947311);shuffle(p.begin(),p.end(),rng);C c{{0,0},-1};auto outside=[](P x,C c){return c.r<0||norm(x-c.p)>c.r+1e-9;};for(int i=0;i<(int)p.size();i++)if(outside(p[i],c)){c={p[i],0};for(int j=0;j<i;j++)if(outside(p[j],c)){c=circle2(p[i],p[j]);for(int k=0;k<j;k++)if(outside(p[k],c))c=circle3(p[i],p[j],p[k]);}}return c;}
struct T{int a,b,c;};double orient(P a,P b,P c){return cross(b-a,c-a);}bool incircle(P a,P b,P c,P p){double ax=a.x-p.x,ay=a.y-p.y,bx=b.x-p.x,by=b.y-p.y,cx=c.x-p.x,cy=c.y-p.y;double d=(ax*ax+ay*ay)*(bx*cy-by*cx)-(bx*bx+by*by)*(ax*cy-ay*cx)+(cx*cx+cy*cy)*(ax*by-ay*bx);return d>EPS;}pair<vector<T>,vector<pair<int,int>>>delaunay(vector<P>p){int n=p.size();if(n<3)return{{},{}};double minx=p[0].x,maxx=p[0].x,miny=p[0].y,maxy=p[0].y;for(P x:p)minx=min(minx,x.x),maxx=max(maxx,x.x),miny=min(miny,x.y),maxy=max(maxy,x.y);double s=max({maxx-minx,maxy-miny,1.0}),cx=(minx+maxx)/2,cy=(miny+maxy)/2;p.push_back({cx-10000*s,cy-8000*s});p.push_back({cx+10000*s,cy-8000*s});p.push_back({cx,cy+10000*s});vector<T>tri={{n,n+1,n+2}};for(int x=0;x<n;x++){map<pair<int,int>,pair<int,pair<int,int>>>edges;vector<char>bad(tri.size());for(int i=0;i<(int)tri.size();i++)if(incircle(p[tri[i].a],p[tri[i].b],p[tri[i].c],p[x])){bad[i]=1;for(auto e:{pair{tri[i].a,tri[i].b},pair{tri[i].b,tri[i].c},pair{tri[i].c,tri[i].a}}){auto key=minmax(e.first,e.second);edges[key].first++;edges[key].second=e;}}vector<T>next;for(int i=0;i<(int)tri.size();i++)if(!bad[i])next.push_back(tri[i]);for(auto[key,data]:edges)if(data.first==1){auto[u,v]=data.second;if(orient(p[u],p[v],p[x])<0)swap(u,v);next.push_back({u,v,x});}tri.swap(next);}vector<T>clean;set<pair<int,int>>edges;for(T t:tri)if(max({t.a,t.b,t.c})<n){clean.push_back(t);edges.insert(minmax(t.a,t.b));edges.insert(minmax(t.b,t.c));edges.insert(minmax(t.c,t.a));}return{clean,vector<pair<int,int>>(edges.begin(),edges.end())};}
double radii(vector<P>p,bool maximum){auto[tri,e]=delaunay(p);double ans=0;for(T t:tri){double r=circle3(p[t.a],p[t.b],p[t.c]).r;if(maximum)ans=max(ans,r);else ans+=r;}return ans;}struct DSU{vector<int>p;DSU(int n):p(n){iota(p.begin(),p.end(),0);}int f(int x){return p[x]==x?x:p[x]=f(p[x]);}};double mst(vector<P>p){int n=p.size();if(n<2)return 0;auto[tri,e]=delaunay(p);if(e.empty())for(int i=1;i<n;i++)e.push_back({i-1,i});vector<tuple<double,int,int>>all;for(auto[u,v]:e)all.push_back({norm(p[u]-p[v]),u,v});sort(all.begin(),all.end());DSU d(n);double ans=0;for(auto[w,u,v]:all){u=d.f(u);v=d.f(v);if(u!=v)d.p[u]=v,ans+=w;}return ans;}
'''

def cpp_solution(kind):
 base={'hpi_story':'hpi','incircle_story':'incircle','overlap_story':'overlap','mec_story':'mec','empty_story':'empty','mst_story':'mst'}.get(kind,kind)
 if base=='incircle':return OPTIMIZED_INCIRCLE_CPP
 body={'hpi':'''int n;cin>>n;vector<pair<P,P>>l(n);for(auto&[a,b]:l)cin>>a.x>>a.y>>b.x>>b.y;cout<<area(halfplanes(l))<<'\\n';''','overlap':'''C a,b;cin>>a.p.x>>a.p.y>>a.r>>b.p.x>>b.p.y>>b.r;cout<<overlap(a,b)<<'\\n';''','tangents':'''C a,b;cin>>a.p.x>>a.p.y>>a.r>>b.p.x>>b.p.y>>b.r;cout<<tangents(a,b)<<'\\n';''','incircle':'''int n;cin>>n;vector<P>p(n);for(auto&x:p)cin>>x.x>>x.y;cout<<inradius(p)<<'\\n';''','mec':'''int n;cin>>n;vector<P>p(n);for(auto&x:p)cin>>x.x>>x.y;C c=mec(p);cout<<c.p.x<<' '<<c.p.y<<' '<<c.r<<'\\n';''','delaunay':'''int n;cin>>n;vector<P>p(n);for(auto&x:p)cin>>x.x>>x.y;cout<<radii(p,false)<<'\\n';''','empty':'''int n;cin>>n;vector<P>p(n);for(auto&x:p)cin>>x.x>>x.y;cout<<radii(p,true)<<'\\n';''','mst':'''int n;cin>>n;vector<P>p(n);for(auto&x:p)cin>>x.x>>x.y;cout<<mst(p)<<'\\n';'''}[base]
 common=CPP_CORE[:CPP_CORE.index('vector<P>halfplanes')]
 hpi=CPP_CORE[CPP_CORE.index('vector<P>halfplanes'):CPP_CORE.index('struct C')]
 circle=CPP_CORE[CPP_CORE.index('struct C'):CPP_CORE.index('vector<P>shifted')]
 incircle=CPP_CORE[CPP_CORE.index('vector<P>shifted'):CPP_CORE.index('C circle2')]
 mecpart=CPP_CORE[CPP_CORE.index('C circle2'):CPP_CORE.index('struct T')]
 delpart=CPP_CORE[CPP_CORE.index('struct T'):CPP_CORE.index('struct DSU')]
 mstpart=CPP_CORE[CPP_CORE.index('struct DSU'):]
 core={'hpi':common+hpi,'overlap':common+circle,'tangents':common+circle,'incircle':common+hpi+incircle,'mec':common+circle+mecpart,'delaunay':common+circle+mecpart+delpart,'empty':common+circle+mecpart+delpart,'mst':common+circle+mecpart+delpart+mstpart}[base]
 return core+'int main(){ios::sync_with_stdio(false);cin.tie(nullptr);cout<<fixed<<setprecision(10);'+body+'}\n'

LESSONS={94:r'''---
title: "Section 94 — Half-Planes And Circle Geometry"
format: pdf
geometry: margin=1.75cm
---

# Continuous feasible regions need oriented predicates

This lesson derives A--C. Problem D is editorial-only.

# A. Half-plane intersection

A directed line `p + t*v` keeps points `x` satisfying `cross(v,x-p) >= 0`. Sort boundaries by direction. Equal-direction lines carry redundant information: retain only the one whose left side is smaller. A deque then stores the boundaries of the current intersection in angular order, while a second deque stores consecutive intersection points.

Before appending a new line, remove boundaries from the back while their last corner violates it, and from the front while their first corner violates it. Each line enters and leaves once. Close the deque with the same two tests, intersect its last and first lines, then use the shoelace formula.

The invariant is geometric: after every insertion, deque lines occur in angle order and its stored corners are exactly the boundary corners that satisfy every processed half-plane. Parallel lines require an explicit policy; never divide by a cross product merely because two floating angles look different.

# B. Two-disk overlap

Classify before applying trigonometry: disjoint disks have area zero; containment gives the smaller disk area. Otherwise the common lens is two circular sectors minus two triangles. Obtain each sector angle from the cosine rule and clamp the `acos` argument into `[-1,1]` to absorb roundoff.

# C. Common tangents

For external tangents compare center distance `d` with `|r1-r2|`; for internal tangents compare it with `r1+r2`. A strict inequality gives two mirror-image lines, equality gives one, and failure gives none. Coincident equal circles are the exceptional infinite family.

# How to find it

Write one signed predicate first. Then list degeneracies before deriving coordinates: parallel support lines, empty regions, coincident centers, containment, and tangency. Continuous geometry becomes reliable when combinatorial classification happens before division, square roots, or inverse trigonometry.

# Exercises

A--C cover oriented feasible regions and circle classification. D combines offset half-planes with monotone binary search.
''',95:r'''---
title: "Section 95 — Geometric Optimization And Delaunay Structure"
format: pdf
geometry: margin=1.75cm
---

# A few boundary witnesses determine the optimum

This lesson derives A--C. Problem D is editorial-only.

# A. Randomized minimum enclosing circle

Shuffle the points. Maintain the minimum circle for the processed prefix. If a new point lies outside, it must lie on the new boundary. Rebuild with that point fixed; whenever an earlier point is outside, both become boundary points; a third violation fixes the unique circumcircle.

The nested loops look cubic, but random insertion order gives linear expected time: a circle determined by at most three boundary points changes with probability at most `3/i` at step `i`. The correctness proof is deterministic; only the running-time analysis uses randomness.

# B. Incremental Delaunay triangulation

A triangle is Delaunay when its open circumdisk contains no input point. Begin with a supertriangle. For each point, remove every triangle whose circumcircle contains it. Those bad triangles form a cavity; edges occurring once on their boundaries form its polygon. Join the new point to every cavity boundary edge.

The in-circle determinant must be interpreted with the triangle orientation. With counterclockwise triangles, a positive sign means inside. Generic-position constraints remove zero-sign ambiguity; production implementations still need a symbolic or deterministic tie policy.

# C. Euclidean MST from Delaunay edges

Every Euclidean MST edge belongs to the Delaunay triangulation. One proof uses the empty diameter disk: if an MST edge had a point strictly inside that disk, replacing it by a shorter edge across the induced cut would contradict minimality. Therefore construct Delaunay edges, sort only those by length, and run Kruskal.

# Recognition guide

When an optimum circle or proximity edge seems to depend on all points, ask which small witness set makes it tight. Enclosing circles need at most three boundary points; Voronoi vertices are fixed by three equidistant sites; MST edges admit an empty-region certificate.

# Exercises

A--C develop enclosing disks, empty-circle triangulation, and proximity sparsification. D asks you to extract the largest finite empty circumcircle.
''',96:r'''---
title: "Section 96 — Master Continuous Geometry Mixed Contest"
format: pdf
geometry: margin=1.75cm
---

# Contest contract

Six original problems revisit the predicates and optimization structures of Sections 94--95 under different models.

| Problem | Main tool |
|---|---|
| A | half-plane intersection and shoelace area |
| B | inward offsets plus feasibility search |
| C | circle-overlap classification |
| D | randomized minimum enclosing circle |
| E | Delaunay empty circumcircles |
| F | Delaunay sparsification plus Kruskal |

For every floating solution, state the exact combinatorial event being approximated. Epsilon is a policy for a known predicate, not a substitute for choosing the predicate.

# Exercises

A--F form the complete mixed contest.
'''}

NOTES={
'hpi':('Sort directed boundaries by angle, discard weaker parallel copies, and maintain feasible consecutive intersections in a deque.','The deque invariant retains exactly the processed region boundaries in angular order; every removed corner violates the new constraint and can never return. Closing yields precisely the intersection polygon.','`O(n log n)` time and `O(n)` memory.'),
'overlap':('Separate disjoint and containment cases before using the two-sector lens formula.','In the proper-overlap case the common region partitions into two sectors minus their center triangles; the other classifications are immediate.','`O(1)` time and memory.'),
'tangents':('Count external and internal tangent families by comparing center distance with radius difference and sum.','Each positive perpendicular offset produces two mirror lines, zero produces their merged tangent, and a negative squared offset produces none.','`O(1)`.'),
'incircle':('Offset every counterclockwise edge inward by radius `r`; exploit the convex polygon edge order for a linear deque feasibility test, then binary-search `r`.','A center supports radius `r` exactly when its distance from every edge is at least `r`. The deque finds a candidate intersection in edge order, and the final all-edge witness check certifies that candidate before declaring feasibility.','`O(n log precision)` time and `O(n)` memory.'),
'mec':('Randomize insertion order and rebuild only when a point violates the current circle, fixing one, two, then three boundary witnesses.','At every nesting level the violating fixed points must lie on the new optimum boundary; one to three such points uniquely determine the minimum circle for the processed prefix.','Expected `O(n)` time and `O(n)` storage.'),
'delaunay':('Use Bowyer--Watson cavity deletion and sum the circumradii of final non-supertriangle faces.','The cavity boundary is retriangulated with the inserted point; the empty-circumcircle invariant is restored after every insertion. Generic position makes the final triangulation unique.','Expected `O(n squared)` for the supplied incremental implementation.'),
'mst':('Build Delaunay edges and run Kruskal on that sparse graph.','Every Euclidean MST edge has an empty-disk certificate and belongs to Delaunay, so discarding all other complete-graph edges preserves an optimum.','Expected `O(n squared + n log n)` here.'),
'empty':('Enumerate the final Delaunay triangles and maximize their circumradii.','A finite empty circle through three sites is a Delaunay face circumcircle, and every Delaunay face supplies such an empty circle.','Expected `O(n squared)` here.')}
for story,base in [('hpi_story','hpi'),('incircle_story','incircle'),('overlap_story','overlap'),('mec_story','mec'),('empty_story','empty'),('mst_story','mst')]:NOTES[story]=NOTES[base]

def editorial(section):
 out=[f'---\ntitle: "Section {section} Editorial — {SECTIONS[section][1]}"\nformat:\n  pdf:\n    code-overflow: wrap\ngeometry: margin=1.6cm\nfontsize: 9pt\n---\n']
 for i,(slug,title,kind) in enumerate(PROBLEMS[section]):
  idea,proof,complexity=NOTES[kind];out.append(f'''# {chr(65+i)}. {title}\n\n## How to find it\n\n{idea}\n\n## Correctness\n\n{proof}\n\n## Complexity\n\n{complexity}\n\n## C++\n\n```cpp\n{{{{< include problems/{slug}/solution.cpp >}}}}\n```\n\n## Python\n\n```python\n{{{{< include problems/{slug}/solution.py >}}}}\n```\n''')
 return '\n'.join(out)

SAMPLES={'hpi':('4\n0 0 2 0\n2 0 2 2\n2 2 0 2\n0 2 0 0\n','4.0000000000\n'),'overlap':('0 0 1\n1 0 1\n','1.2283696986\n'),'tangents':('0 0 1\n4 0 1\n','4\n'),'incircle':('4\n0 0\n2 0\n2 2\n0 2\n','1.0000000000\n'),'mec':('3\n0 0\n2 0\n0 2\n','1.0000000000 1.0000000000 1.4142135624\n'),'delaunay':('3\n0 0\n2 0\n0 2\n','1.4142135624\n'),'mst':('3\n0 0\n2 0\n0 2\n','4.0000000000\n'),'empty':('3\n0 0\n2 0\n0 2\n','1.4142135624\n')}
for story,base in [('hpi_story','hpi'),('incircle_story','incircle'),('overlap_story','overlap'),('mec_story','mec'),('empty_story','empty'),('mst_story','mst')]:SAMPLES[story]=SAMPLES[base]

def format_python(source):return ast.unparse(ast.parse(source))+'\n'
def format_cpp(source):
 lines=[];current='';indent=0;paren=0;quote=None;escaped=False
 def flush():
  nonlocal current
  if current.strip():lines.append('    '*indent+current.strip())
  current=''
 for ch in source:
  if quote:
   current+=ch
   if escaped:escaped=False
   elif ch=='\\':escaped=True
   elif ch==quote:quote=None
  elif ch in ('"',"'"):quote=ch;current+=ch
  elif ch=='(':paren+=1;current+=ch
  elif ch==')':paren-=1;current+=ch
  elif ch=='{' and paren==0:current=current.rstrip()+' {';flush();indent+=1
  elif ch=='}' and paren==0:flush();indent=max(0,indent-1);current='}';flush()
  elif ch==';' and paren==0:current+=';';flush()
  elif ch=='\n':flush()
  else:current+=ch
 flush();return '\n'.join(lines)+'\n'

def generate():
 for section,(directory,title) in SECTIONS.items():
  base=ROOT/'sections'/f'{section:02d}_{directory}';base.mkdir(parents=True,exist_ok=True);(base/'lesson.qmd').write_text(LESSONS[section]);(base/'editorial.qmd').write_text(editorial(section));links=[];checks=[]
  for slug,name,kind in PROBLEMS[section]:
   links.append(f'- [{name}](problems/{slug}/README.md)');checks.append(f'- [ ] [{name}](problems/{slug}/README.md)');p=base/'problems'/slug;p.mkdir(parents=True,exist_ok=True);tests=p/'tests';tests.mkdir(exist_ok=True);(p/'README.md').write_text(f'# {name}\n\n{STATEMENTS[kind]}\n');(p/'solve.cpp').write_text(CPP_STUB);(p/'solve.py').write_text(PY_STUB);(p/'solution.cpp').write_text(format_cpp(cpp_solution(kind)));(p/'solution.py').write_text(format_python(py_solution(kind)));checker='tokens' if kind=='tangents' else 'float';(p/'manifest.json').write_text(json.dumps({'title':name,'checker':checker,'time_limit_seconds':20})+'\n');x,y=SAMPLES[kind];(tests/'sample1.in').write_text(x);(tests/'sample1.out').write_text(y);(tests/'random_cases.py').write_text(f'''import subprocess,sys\nfrom pathlib import Path\nROOT=Path(__file__).resolve().parents[5]\nraise SystemExit(subprocess.call([sys.executable,str(ROOT/"tools"/"continuous_geometry_random.py"),"{kind}",*sys.argv[1:]]))\n''')
  note='The lesson derives A--C; D is editorial-only.' if section<96 else 'Exactly six new problems form the mixed contest.';(base/'README.md').write_text(f'# Section {section}: {title}\n\n{note}\n\n## Problems\n\n'+'\n'.join(links)+'\n');(base/'PRACTICE.md').write_text(f'# Section {section} Practice\n\n'+'\n'.join(checks)+'\n');names=',\n        '.join(repr(x[0]) for x in PROBLEMS[section]);(base/'check.py').write_text(f'''from pathlib import Path\nimport sys\nROOT=Path(__file__).resolve().parents[2]\nsys.path.insert(0,str(ROOT))\nfrom tools.section_checker import run_section_checks\nSECTION=Path(__file__).resolve().parent\nPROBLEMS=[SECTION/"problems"/x for x in (\n        {names},\n)]\nif __name__=="__main__":raise SystemExit(run_section_checks({section},PROBLEMS,ROOT))\n''')
if __name__=='__main__':generate()
