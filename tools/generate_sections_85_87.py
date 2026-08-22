"""Generate Sections 85--87: matching, cut trees, and matroids."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
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
SECTIONS={85:("weighted_general_matching","Weighted And General Matching"),86:("cut_trees_matroid_intersection","Cut Trees And Matroid Intersection"),87:("master_matching_matroids_mixed","Master Matching And Matroids Mixed Contest")}
TIME_LIMITS = {"bottleneck": 15}
PROBLEMS={85:[("a_assignment_cost","Assignment Cost","assignment"),("b_forbidden_profit_assignment","Forbidden Profit Assignment","profit_assignment"),("c_general_pairing","General Pairing","blossom"),("d_compatibility_pairing","Compatibility Pairing","compat_pairing")],86:[("a_all_pairs_cut_queries","All-Pairs Cut Queries","gomory_queries"),("b_rainbow_forest","Rainbow Forest","rainbow"),("c_dual_forest","Dual Forest","dual_forest"),("d_directed_arborescence","Directed Arborescence","arborescence")],87:[("a_bottleneck_assignment","Bottleneck Assignment","bottleneck"),("b_roommate_rescue","Roommate Rescue","roommates"),("c_cut_threshold_pairs","Cut Threshold Pairs","cut_pairs"),("d_rainbow_spanning_tree","Rainbow Spanning Tree","rainbow_tree"),("e_broadcast_backbone","Broadcast Backbone","broadcast"),("f_two_map_forest","Two-Map Forest","two_map")]}
STATEMENTS={
"assignment":"""Assign each of `n` workers to a distinct job, minimizing total cost. Input: `n` then an `n by n` signed cost matrix, `n <= 500`. Output the minimum cost.\n\nSample input\n```text\n3\n4 1 3\n2 0 5\n3 2 2\n```\nSample output\n```text\n5\n```""",
"profit_assignment":"""There are `n` agents and `m` projects (`n <= m <= 500`). Entry `-1` forbids an assignment; otherwise it is a nonnegative profit. Assign every agent a distinct allowed project and maximize profit, or print `IMPOSSIBLE`.\n\nSample input\n```text\n2 3\n5 -1 4\n2 7 3\n```\nSample output\n```text\n12\n```""",
"blossom":"""Given a simple undirected graph, print the maximum number of vertex-disjoint edges. `n <= 500`, `m <= 100000`.\n\nSample input\n```text\n5 5\n1 2\n2 3\n3 1\n3 4\n4 5\n```\nSample output\n```text\n2\n```""",
"compat_pairing":"""Each participant has an integer skill. Two participants may pair exactly when the absolute difference of their skills belongs to a given allowed set. Print the maximum number of pairs. `n <= 500`.\n\nSample input\n```text\n5 2\n1 4 6 7 10\n2 3\n```\nSample output\n```text\n2\n```""",
"gomory_queries":"""A connected undirected capacitated multigraph is fixed. For each `(u,v)`, print the minimum capacity of an edge cut separating them. `n <= 180`, `m <= 2000`, `q <= 200000`; capacities are positive.\n\nSample input\n```text\n3 3 2\n1 2 4\n2 3 2\n1 3 3\n1 2\n1 3\n```\nSample output\n```text\n6\n5\n```""",
"rainbow":"""Choose as many edges as possible from an undirected graph subject to two rules: the chosen edges form a forest, and no two have the same color. `n,m <= 180`. Output the maximum size.\n\nSample input\n```text\n4 4\n1 2 1\n2 3 1\n3 4 2\n1 4 3\n```\nSample output\n```text\n3\n```""",
"dual_forest":"""There are `m` selectable links. Link `i` joins `(a_i,b_i)` on the first map and `(c_i,d_i)` on the second map. Choose the largest set forming a forest on both maps. `n1,n2,m <= 150`.\n\nSample input\n```text\n3 3 3\n1 2 1 2\n2 3 2 3\n1 3 1 3\n```\nSample output\n```text\n2\n```""",
"arborescence":"""Find the minimum total weight of a directed spanning arborescence rooted at vertex `r`: every other vertex has exactly one selected incoming edge and is reachable from `r`. Print `IMPOSSIBLE` if none exists. `n <= 500`, `m <= 10000`; weights may be negative.\n\nSample input\n```text\n3 4 1\n1 2 5\n1 3 4\n2 3 1\n3 2 2\n```\nSample output\n```text\n6\n```""",
"bottleneck":"""Assign each worker a distinct job while minimizing the maximum assigned cost. `n <= 500`.\n\nSample input\n```text\n3\n8 2 5\n6 4 7\n3 9 1\n```\nSample output\n```text\n5\n```""",
"roommates":"""An undirected compatibility graph is given. Print how many participants remain unmatched in an optimal pairing. `n <= 500`.\n\nSample input\n```text\n5 4\n1 2\n2 3\n3 1\n4 5\n```\nSample output\n```text\n1\n```""",
"cut_pairs":"""For each threshold `x`, count unordered vertex pairs whose minimum separating cut has capacity at most `x`. Use a connected undirected capacitated graph; `n <= 180`, `q <= 200000`.\n\nSample input\n```text\n3 3 3\n1 2 4\n2 3 2\n1 3 3\n4\n5\n6\n```\nSample output\n```text\n0\n2\n3\n```""",
"rainbow_tree":"""Decide whether an undirected colored graph contains a spanning tree with all edge colors distinct. `n,m <= 180`. Output `YES` or `NO`.\n\nSample input\n```text\n4 4\n1 2 1\n2 3 2\n3 4 3\n1 4 1\n```\nSample output\n```text\nYES\n```""",
"broadcast":"""Print the minimum directed arborescence cost from root `r`, or `IMPOSSIBLE`. This mixed version permits parallel edges, loops, and negative weights; `n <= 500`.\n\nSample input\n```text\n3 4 1\n1 2 5\n1 3 4\n2 3 1\n3 2 2\n```\nSample output\n```text\n6\n```""",
"two_map":"""Two maps share `n` labeled vertices. Candidate link `i` joins `(a_i,b_i)` on the first map and `(c_i,d_i)` on the second. Decide whether some `n-1` links form a spanning tree on both maps. `n,m <= 150`.\n\nSample input\n```text\n3 3\n1 2 1 2\n2 3 2 3\n1 3 1 3\n```\nSample output\n```text\nYES\n```"""
}

# The Python references use the same algorithms, so limits reflect their
# practical polynomial constants as well as the C++ implementations.
STATEMENTS["assignment"] = STATEMENTS["assignment"].replace("n <= 500", "n <= 350")
STATEMENTS["profit_assignment"] = STATEMENTS["profit_assignment"].replace("m <= 500", "m <= 350")
STATEMENTS["gomory_queries"] = STATEMENTS["gomory_queries"].replace("n <= 180", "n <= 80").replace("m <= 2000", "m <= 1000")
STATEMENTS["cut_pairs"] = STATEMENTS["cut_pairs"].replace("n <= 180", "n <= 80")
STATEMENTS["rainbow"] = STATEMENTS["rainbow"].replace("n,m <= 180", "n <= 150, m <= 70")
STATEMENTS["rainbow_tree"] = STATEMENTS["rainbow_tree"].replace("n,m <= 180", "n <= 150, m <= 70")
STATEMENTS["dual_forest"] = STATEMENTS["dual_forest"].replace("n1,n2,m <= 150", "n1,n2 <= 150, m <= 60")
STATEMENTS["two_map"] = STATEMENTS["two_map"].replace("n,m <= 150", "n <= 150, m <= 60")
STATEMENTS["compat_pairing"] = STATEMENTS["compat_pairing"].replace(
    "`n <= 500`.",
    "`n <= 500`, and the allowed set contains at most `200000` values.",
)
STATEMENTS["roommates"] = STATEMENTS["roommates"].replace(
    "`n <= 500`.", "`n <= 500`, `m <= 100000`.",
)
STATEMENTS["cut_pairs"] = STATEMENTS["cut_pairs"].replace(
    "`n <= 80`, `q <= 200000`.",
    "`n <= 80`, `m <= 1000`, `q <= 200000`, and capacities are positive.",
)
STATEMENTS["broadcast"] = STATEMENTS["broadcast"].replace(
    "`n <= 500`.", "`n <= 500`, `m <= 10000`.",
)

PY_MATCH=r'''import sys
def hungarian(cost):
 n=len(cost);m=len(cost[0]);u=[0]*(n+1);v=[0]*(m+1);p=[0]*(m+1);way=[0]*(m+1)
 for i in range(1,n+1):
  p[0]=i;j0=0;minimum=[10**30]*(m+1);used=[False]*(m+1)
  while True:
   used[j0]=True;i0=p[j0];delta=10**30;j1=0
   for j in range(1,m+1):
    if not used[j]:
     cur=cost[i0-1][j-1]-u[i0]-v[j]
     if cur<minimum[j]:minimum[j]=cur;way[j]=j0
     if minimum[j]<delta:delta=minimum[j];j1=j
   for j in range(m+1):
    if used[j]:u[p[j]]+=delta;v[j]-=delta
    else:minimum[j]-=delta
   j0=j1
   if p[j0]==0:break
  while True:
   j1=way[j0];p[j0]=p[j1];j0=j1
   if j0==0:break
 match=[-1]*n
 for j in range(1,m+1):
  if p[j]:match[p[j]-1]=j-1
 return -v[0],match

def blossom(graph):
 n=len(graph);match=[-1]*n;base=list(range(n));parent=[-1]*n
 def find_path(root):
  nonlocal base,parent
  used=[False]*n;parent=[-1]*n;base=list(range(n));q=[root];used[root]=True
  def get_lca(a,b):
   mark=[False]*n
   while True:
    a=base[a];mark[a]=True
    if match[a]==-1:break
    a=parent[match[a]]
   while True:
    b=base[b]
    if mark[b]:return b
    b=parent[match[b]]
  def mark_path(v,b,child,flower):
   while base[v]!=b:
    flower[base[v]]=flower[base[match[v]]]=True;parent[v]=child;child=match[v];v=parent[match[v]]
  for v in q:
   for u in graph[v]:
    if base[v]==base[u] or match[v]==u:continue
    if u==root or (match[u]!=-1 and parent[match[u]]!=-1):
     b=get_lca(v,u);flower=[False]*n;mark_path(v,b,u,flower);mark_path(u,b,v,flower)
     for x in range(n):
      if flower[base[x]]:base[x]=b
      if not used[x] and flower[base[x]]:used[x]=True;q.append(x)
    elif parent[u]==-1:
     parent[u]=v
     if match[u]==-1:return u
     u=match[u];used[u]=True;q.append(u)
  return -1
 for root in range(n):
  if match[root]!=-1:continue
  v=find_path(root)
  if v==-1:continue
  while v!=-1:
   pv=parent[v];nv=match[pv] if pv!=-1 else -1;match[v]=pv
   if pv!=-1:match[pv]=v
   v=nv
 return match
'''

PY_CUT=r'''import sys
from collections import deque
class Dinic:
 def __init__(self,n):self.g=[[] for _ in range(n)]
 def add(self,u,v,c):self.g[u].append([v,c,len(self.g[v])]);self.g[v].append([u,0,len(self.g[u])-1])
 def flow(self,s,t):
  answer=0;n=len(self.g)
  while True:
   level=[-1]*n;level[s]=0;q=deque([s])
   while q:
    u=q.popleft()
    for v,c,_ in self.g[u]:
     if c and level[v]<0:level[v]=level[u]+1;q.append(v)
   if level[t]<0:self.reachable=[x>=0 for x in level];return answer
   it=[0]*n
   def dfs(u,pushed):
    if u==t:return pushed
    while it[u]<len(self.g[u]):
     e=self.g[u][it[u]]
     if e[1] and level[e[0]]==level[u]+1:
      take=dfs(e[0],min(pushed,e[1]))
      if take:e[1]-=take;self.g[e[0]][e[2]][1]+=take;return take
     it[u]+=1
    return 0
   while True:
    pushed=dfs(s,10**30)
    if not pushed:break
    answer+=pushed

def gomory_hu(n,edges):
 parent=[0]*n;value=[0]*n
 for s in range(1,n):
  t=parent[s];d=Dinic(n)
  for u,v,c in edges:d.add(u,v,c);d.add(v,u,c)
  value[s]=d.flow(s,t);side=d.reachable
  for v in range(s+1,n):
   if parent[v]==t and side[v]:parent[v]=s
  if side[parent[t]]:
   parent[s]=parent[t];parent[t]=s;value[s],value[t]=value[t],value[s]
 tree=[[] for _ in range(n)]
 for v in range(1,n):tree[v].append((parent[v],value[v]));tree[parent[v]].append((v,value[v]))
 return tree
'''

PY_MATROID=r'''import sys
def forest_ok(n,edges,chosen):
 p=list(range(n))
 def find(x):
  while p[x]!=x:p[x]=p[p[x]];x=p[x]
  return x
 for i in chosen:
  u,v=edges[i];u=find(u);v=find(v)
  if u==v:return False
  p[u]=v
 return True
def partition_ok(colors,chosen):return len({colors[i] for i in chosen})==len(chosen)
def intersection(m,ok1,ok2):
 inside=set()
 while True:
  outside=[e for e in range(m) if e not in inside];parent={};q=[]
  for e in outside:
   if ok1(inside|{e}):parent[e]=-1;q.append(e)
  finish=-1
  for x in q:
   if x not in inside and ok2(inside|{x}):finish=x;break
   if x in inside:
    for e in outside:
     if e not in parent and ok1((inside-{x})|{e}):parent[e]=x;q.append(e)
   else:
    for y in list(inside):
     if y not in parent and ok2((inside-{y})|{x}):parent[y]=x;q.append(y)
  if finish<0:return inside
  x=finish
  while x!=-1:
   if x in inside:inside.remove(x)
   else:inside.add(x)
   x=parent[x]
'''

PY_ARB=r'''import sys
def arborescence(n,root,edges):
 answer=0
 while True:
  incoming=[10**30]*n;pre=[-1]*n
  for u,v,w in edges:
   if u!=v and w<incoming[v]:incoming[v]=w;pre[v]=u
  incoming[root]=0
  if any(x==10**30 for x in incoming):return None
  answer+=sum(incoming);component=[-1]*n;seen=[-1]*n;count=0
  for start in range(n):
   v=start
   while seen[v]!=start and component[v]<0 and v!=root:seen[v]=start;v=pre[v]
   if v!=root and component[v]<0:
    u=pre[v];component[v]=count
    while u!=v:component[u]=count;u=pre[u]
    count+=1
  if count==0:return answer
  for v in range(n):
   if component[v]<0:component[v]=count;count+=1
  edges=[(component[u],component[v],w-incoming[v]) for u,v,w in edges];root=component[root];n=count
'''

PY={}
PY["assignment"]=PY_MATCH+r'''def main():
 d=list(map(int,sys.stdin.buffer.read().split()));n=d[0];a=[d[1+i*n:1+(i+1)*n] for i in range(n)];print(hungarian(a)[0])
if __name__=='__main__':main()
'''
PY["profit_assignment"]=PY_MATCH+r'''def main():
 d=list(map(int,sys.stdin.buffer.read().split()));n,m=d[:2];raw=d[2:];inf=10**15;a=[[inf if raw[i*m+j]<0 else -raw[i*m+j] for j in range(m)] for i in range(n)];cost,match=hungarian(a)
 print('IMPOSSIBLE' if any(a[i][match[i]]>=inf for i in range(n)) else -cost)
if __name__=='__main__':main()
'''
def blossom_solution(kind):
 build="" if kind=='blossom' or kind=='roommates' else ""
 return PY_MATCH+f'''def main():
 d=list(map(int,sys.stdin.buffer.read().split()));n,m=d[:2];g=[[] for _ in range(n)]
 for i in range(2,2+2*m,2):u,v=d[i]-1,d[i+1]-1;g[u].append(v);g[v].append(u)
 matched=sum(x>=0 for x in blossom(g))//2
 print({"n-2*matched" if kind=="roommates" else "matched"})
if __name__=='__main__':main()
'''
PY["blossom"]=blossom_solution("blossom");PY["roommates"]=blossom_solution("roommates")
PY["compat_pairing"]=PY_MATCH+r'''def main():
 d=list(map(int,sys.stdin.buffer.read().split()));n,k=d[:2];a=d[2:2+n];allowed=set(d[2+n:]);g=[[] for _ in range(n)]
 for i in range(n):
  for j in range(i):
   if abs(a[i]-a[j]) in allowed:g[i].append(j);g[j].append(i)
 print(sum(x>=0 for x in blossom(g))//2)
if __name__=='__main__':main()
'''

TREE_MIN=r'''def tree_minimum(tree):
 n=len(tree);L=max(1,n.bit_length());up=[[0]*n for _ in range(L)];mn=[[10**30]*n for _ in range(L)];depth=[0]*n;stack=[(0,0)]
 while stack:
  u,p=stack.pop();up[0][u]=p
  for v,w in tree[u]:
   if v!=p:depth[v]=depth[u]+1;mn[0][v]=w;stack.append((v,u))
 for j in range(1,L):
  for v in range(n):mn[j][v]=min(mn[j-1][v],mn[j-1][up[j-1][v]]);up[j][v]=up[j-1][up[j-1][v]]
 def query(a,b):
  answer=10**30
  if depth[a]<depth[b]:a,b=b,a
  z=depth[a]-depth[b]
  for j in range(L):
   if z>>j&1:answer=min(answer,mn[j][a]);a=up[j][a]
  if a==b:return answer
  for j in range(L-1,-1,-1):
   if up[j][a]!=up[j][b]:answer=min(answer,mn[j][a],mn[j][b]);a,b=up[j][a],up[j][b]
  return min(answer,mn[0][a],mn[0][b])
 return query
'''
PY["gomory_queries"]=PY_CUT+TREE_MIN+r'''def main():
 d=list(map(int,sys.stdin.buffer.read().split()));n,m,q=d[:3];at=3;e=[]
 for _ in range(m):u,v,c=d[at:at+3];at+=3;e.append((u-1,v-1,c))
 query=tree_minimum(gomory_hu(n,e));print('\n'.join(str(query(d[i]-1,d[i+1]-1)) for i in range(at,at+2*q,2)))
if __name__=='__main__':main()
'''
PY["cut_pairs"]=PY_CUT+TREE_MIN+r'''def main():
 d=list(map(int,sys.stdin.buffer.read().split()));n,m,q=d[:3];at=3;e=[]
 for _ in range(m):u,v,c=d[at:at+3];at+=3;e.append((u-1,v-1,c))
 query=tree_minimum(gomory_hu(n,e));values=sorted(query(i,j) for i in range(n) for j in range(i));import bisect;print('\n'.join(str(bisect.bisect_right(values,d[i])) for i in range(at,at+q)))
if __name__=='__main__':main()
'''

def matroid_solution(kind):
 if kind in ('rainbow','rainbow_tree'):
  ending="print(len(answer))" if kind=='rainbow' else "print('YES' if len(answer)==n-1 else 'NO')"
  return PY_MATROID+f'''def main():
 d=list(map(int,sys.stdin.buffer.read().split()));n,m=d[:2];edges=[];colors=[]
 for i in range(2,2+3*m,3):edges.append((d[i]-1,d[i+1]-1));colors.append(d[i+2])
 answer=intersection(m,lambda chosen:forest_ok(n,edges,chosen),lambda chosen:partition_ok(colors,chosen));{ending}
if __name__=='__main__':main()
'''
 if kind=='dual_forest':ending='print(len(answer))';prefix='n1,n2,m=d[:3];at=3'
 else:ending="print('YES' if len(answer)==n-1 else 'NO')";prefix='n,m=d[:2];n1=n2=n;at=2'
 return PY_MATROID+f'''def main():
 d=list(map(int,sys.stdin.buffer.read().split()));{prefix};first=[];second=[]
 for i in range(m):a,b,c,e=d[at:at+4];at+=4;first.append((a-1,b-1));second.append((c-1,e-1))
 answer=intersection(m,lambda chosen:forest_ok(n1,first,chosen),lambda chosen:forest_ok(n2,second,chosen));{ending}
if __name__=='__main__':main()
'''
PY['rainbow']=matroid_solution('rainbow');PY['rainbow_tree']=matroid_solution('rainbow_tree');PY['dual_forest']=matroid_solution('dual_forest');PY['two_map']=matroid_solution('two_map')

def arb_solution():return PY_ARB+r'''def main():
 d=list(map(int,sys.stdin.buffer.read().split()));n,m,root=d[:3];edges=[]
 for i in range(3,3+3*m,3):edges.append((d[i]-1,d[i+1]-1,d[i+2]))
 answer=arborescence(n,root-1,edges);print('IMPOSSIBLE' if answer is None else answer)
if __name__=='__main__':main()
'''
PY['arborescence']=arb_solution();PY['broadcast']=arb_solution()
PY['bottleneck']=r'''import sys
def possible(a,x):
 n=len(a);match=[-1]*n
 def dfs(u,seen):
  for v in range(n):
   if a[u][v]<=x and not seen[v]:
    seen[v]=1
    if match[v]<0 or dfs(match[v],seen):match[v]=u;return True
  return False
 return all(dfs(u,[False]*n) for u in range(n))
def main():
 d=list(map(int,sys.stdin.buffer.read().split()));n=d[0];a=[d[1+i*n:1+(i+1)*n] for i in range(n)];values=sorted(set(d[1:]));l=-1;r=len(values)-1
 while r-l>1:
  m=(l+r)//2
  if possible(a,values[m]):r=m
  else:l=m
 print(values[r])
if __name__=='__main__':main()
'''

CPP_MATCH=r'''#include <bits/stdc++.h>
using namespace std;using ll=long long;pair<ll,vector<int>>hungarian(vector<vector<ll>>a){int n=a.size(),m=a[0].size();vector<ll>u(n+1),v(m+1);vector<int>p(m+1),way(m+1);for(int i=1;i<=n;i++){p[0]=i;int j0=0;vector<ll>mn(m+1,4e18);vector<char>used(m+1);do{used[j0]=1;int i0=p[j0],j1=0;ll delta=4e18;for(int j=1;j<=m;j++)if(!used[j]){ll cur=a[i0-1][j-1]-u[i0]-v[j];if(cur<mn[j])mn[j]=cur,way[j]=j0;if(mn[j]<delta)delta=mn[j],j1=j;}for(int j=0;j<=m;j++)if(used[j])u[p[j]]+=delta,v[j]-=delta;else mn[j]-=delta;j0=j1;}while(p[j0]);do{int j1=way[j0];p[j0]=p[j1];j0=j1;}while(j0);}vector<int>match(n);for(int j=1;j<=m;j++)if(p[j])match[p[j]-1]=j-1;return{-v[0],match};}
struct Blossom{int n;vector<vector<int>>g;vector<int>match,p,base,q;vector<char>used,flower;Blossom(vector<vector<int>>g):n(g.size()),g(g),match(n,-1),p(n),base(n),q(n),used(n),flower(n){}int lca(int a,int b){vector<char>mark(n);while(1){a=base[a];mark[a]=1;if(match[a]<0)break;a=p[match[a]];}while(1){b=base[b];if(mark[b])return b;b=p[match[b]];}}void mark_path(int v,int b,int child){while(base[v]!=b){flower[base[v]]=flower[base[match[v]]]=1;p[v]=child;child=match[v];v=p[match[v]];}}int path(int root){fill(used.begin(),used.end(),0);fill(p.begin(),p.end(),-1);iota(base.begin(),base.end(),0);int qh=0,qt=0;q[qt++]=root;used[root]=1;while(qh<qt){int v=q[qh++];for(int u:g[v])if(base[v]!=base[u]&&match[v]!=u){if(u==root||(match[u]>=0&&p[match[u]]>=0)){int b=lca(v,u);fill(flower.begin(),flower.end(),0);mark_path(v,b,u);mark_path(u,b,v);for(int x=0;x<n;x++)if(flower[base[x]]){base[x]=b;if(!used[x])used[x]=1,q[qt++]=x;}}else if(p[u]<0){p[u]=v;if(match[u]<0)return u;u=match[u];used[u]=1;q[qt++]=u;}}}return-1;}int solve(){for(int root=0;root<n;root++)if(match[root]<0){int v=path(root);while(v>=0){int pv=p[v],nv=pv<0?-1:match[pv];match[v]=pv;if(pv>=0)match[pv]=v;v=nv;}}return count_if(match.begin(),match.end(),[](int x){return x>=0;})/2;}};
'''

CPP_CUT=r'''#include <bits/stdc++.h>
using namespace std;using ll=long long;struct Dinic{struct E{int v,rev;ll c;};int n;vector<vector<E>>g;vector<int>level,it;vector<char>side;Dinic(int n):n(n),g(n),level(n),it(n),side(n){}void add(int u,int v,ll c){g[u].push_back({v,(int)g[v].size(),c});g[v].push_back({u,(int)g[u].size()-1,0});}ll dfs(int u,int t,ll f){if(u==t)return f;for(int&i=it[u];i<(int)g[u].size();i++){E&e=g[u][i];if(e.c&&level[e.v]==level[u]+1){ll z=dfs(e.v,t,min(f,e.c));if(z){e.c-=z;g[e.v][e.rev].c+=z;return z;}}}return 0;}ll flow(int s,int t){ll ans=0;while(1){fill(level.begin(),level.end(),-1);queue<int>q;q.push(s);level[s]=0;while(!q.empty()){int u=q.front();q.pop();for(auto&e:g[u])if(e.c&&level[e.v]<0)level[e.v]=level[u]+1,q.push(e.v);}if(level[t]<0){for(int i=0;i<n;i++)side[i]=level[i]>=0;return ans;}fill(it.begin(),it.end(),0);while(ll z=dfs(s,t,4e18))ans+=z;}}};vector<vector<pair<int,ll>>>gomory(int n,vector<tuple<int,int,ll>>e){vector<int>p(n);vector<ll>w(n);for(int s=1;s<n;s++){int t=p[s];Dinic d(n);for(auto[u,v,c]:e)d.add(u,v,c),d.add(v,u,c);w[s]=d.flow(s,t);for(int v=s+1;v<n;v++)if(p[v]==t&&d.side[v])p[v]=s;if(d.side[p[t]])p[s]=p[t],p[t]=s,swap(w[s],w[t]);}vector<vector<pair<int,ll>>>tree(n);for(int v=1;v<n;v++)tree[v].push_back({p[v],w[v]}),tree[p[v]].push_back({v,w[v]});return tree;}struct MinTree{int n,L;vector<int>dep;vector<vector<int>>up;vector<vector<ll>>mn;MinTree(vector<vector<pair<int,ll>>>t):n(t.size()),L(max(1,(int)bit_width((unsigned)n))),dep(n),up(L,vector<int>(n)),mn(L,vector<ll>(n,4e18)){vector<pair<int,int>>st={{0,0}};while(!st.empty()){auto[u,p]=st.back();st.pop_back();up[0][u]=p;for(auto[v,w]:t[u])if(v!=p)dep[v]=dep[u]+1,mn[0][v]=w,st.push_back({v,u});}for(int j=1;j<L;j++)for(int v=0;v<n;v++)mn[j][v]=min(mn[j-1][v],mn[j-1][up[j-1][v]]),up[j][v]=up[j-1][up[j-1][v]];}ll query(int a,int b){ll ans=4e18;if(dep[a]<dep[b])swap(a,b);int z=dep[a]-dep[b];for(int j=0;j<L;j++)if(z>>j&1)ans=min(ans,mn[j][a]),a=up[j][a];if(a==b)return ans;for(int j=L-1;j>=0;j--)if(up[j][a]!=up[j][b])ans=min({ans,mn[j][a],mn[j][b]}),a=up[j][a],b=up[j][b];return min({ans,mn[0][a],mn[0][b]});}};
'''

CPP_MATROID=r'''#include <bits/stdc++.h>
using namespace std;struct DSU{vector<int>p;DSU(int n):p(n){iota(p.begin(),p.end(),0);}int f(int x){return p[x]==x?x:p[x]=f(p[x]);}bool add(int a,int b){a=f(a);b=f(b);if(a==b)return 0;p[a]=b;return 1;}};bool forest_ok(int n,const vector<pair<int,int>>&e,const vector<char>&in){DSU d(n);for(int i=0;i<(int)e.size();i++)if(in[i]&&!d.add(e[i].first,e[i].second))return 0;return 1;}vector<char>intersect(int m,function<bool(const vector<char>&)>ok1,function<bool(const vector<char>&)>ok2){vector<char>in(m);while(1){vector<int>par(m,-2),q;for(int e=0;e<m;e++)if(!in[e]){in[e]=1;bool ok=ok1(in);in[e]=0;if(ok)par[e]=-1,q.push_back(e);}int finish=-1;for(int h=0;h<(int)q.size()&&finish<0;h++){int x=q[h];if(!in[x]){in[x]=1;bool sink=ok2(in);in[x]=0;if(sink){finish=x;break;}for(int y=0;y<m;y++)if(in[y]&&par[y]==-2){in[y]=0;in[x]=1;bool ok=ok2(in);in[x]=0;in[y]=1;if(ok)par[y]=x,q.push_back(y);}}else for(int e=0;e<m;e++)if(!in[e]&&par[e]==-2){in[x]=0;in[e]=1;bool ok=ok1(in);in[e]=0;in[x]=1;if(ok)par[e]=x,q.push_back(e);}}if(finish<0)return in;for(int x=finish;x>=0;x=par[x])in[x]^=1;}};
'''

CPP_ARB=r'''#include <bits/stdc++.h>
using namespace std;using ll=long long;struct Edge{int u,v;ll w;};optional<ll>arbo(int n,int root,vector<Edge>e){ll ans=0;while(1){vector<ll>in(n,4e18);vector<int>pre(n,-1);for(auto x:e)if(x.u!=x.v&&x.w<in[x.v])in[x.v]=x.w,pre[x.v]=x.u;in[root]=0;for(ll x:in)if(x==4e18)return{};for(ll x:in)ans+=x;vector<int>id(n,-1),seen(n,-1);int count=0;for(int s=0;s<n;s++){int v=s;while(seen[v]!=s&&id[v]<0&&v!=root)seen[v]=s,v=pre[v];if(v!=root&&id[v]<0){for(int u=pre[v];u!=v;u=pre[u])id[u]=count;id[v]=count++;}}if(!count)return ans;for(int v=0;v<n;v++)if(id[v]<0)id[v]=count++;vector<Edge>next;for(auto x:e)next.push_back({id[x.u],id[x.v],x.w-in[x.v]});root=id[root];n=count;e.swap(next);}};
'''

CPP={}
CPP['assignment']=CPP_MATCH+r'''int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;cin>>n;vector<vector<ll>>a(n,vector<ll>(n));for(auto&r:a)for(auto&x:r)cin>>x;cout<<hungarian(a).first<<'\n';}'''
CPP['profit_assignment']=CPP_MATCH+r'''int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,m;cin>>n>>m;const ll X=1e15;vector<vector<ll>>a(n,vector<ll>(m));for(auto&r:a)for(auto&x:r){cin>>x;x=x<0?X:-x;}auto[cost,match]=hungarian(a);for(int i=0;i<n;i++)if(a[i][match[i]]>=X){cout<<"IMPOSSIBLE\n";return 0;}cout<<-cost<<'\n';}'''
CPP['blossom']=CPP_MATCH+r'''int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,m;cin>>n>>m;vector<vector<int>>g(n);while(m--){int u,v;cin>>u>>v;--u;--v;g[u].push_back(v);g[v].push_back(u);}cout<<Blossom(g).solve()<<'\n';}'''
CPP['roommates']=CPP_MATCH+r'''int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,m;cin>>n>>m;vector<vector<int>>g(n);while(m--){int u,v;cin>>u>>v;--u;--v;g[u].push_back(v);g[v].push_back(u);}cout<<n-2*Blossom(g).solve()<<'\n';}'''
CPP['compat_pairing']=CPP_MATCH+r'''int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,k;cin>>n>>k;vector<int>a(n);for(int&x:a)cin>>x;set<int>ok;while(k--){int x;cin>>x;ok.insert(x);}vector<vector<int>>g(n);for(int i=0;i<n;i++)for(int j=0;j<i;j++)if(ok.count(abs(a[i]-a[j])))g[i].push_back(j),g[j].push_back(i);cout<<Blossom(g).solve()<<'\n';}'''
CPP['gomory_queries']=CPP_CUT+r'''int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,m,q;cin>>n>>m>>q;vector<tuple<int,int,ll>>e(m);for(auto&[u,v,c]:e)cin>>u>>v>>c,--u,--v;MinTree t(gomory(n,e));while(q--){int u,v;cin>>u>>v;cout<<t.query(u-1,v-1)<<'\n';}}'''
CPP['cut_pairs']=CPP_CUT+r'''int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,m,q;cin>>n>>m>>q;vector<tuple<int,int,ll>>e(m);for(auto&[u,v,c]:e)cin>>u>>v>>c,--u,--v;MinTree t(gomory(n,e));vector<ll>a;for(int i=0;i<n;i++)for(int j=0;j<i;j++)a.push_back(t.query(i,j));sort(a.begin(),a.end());while(q--){ll x;cin>>x;cout<<upper_bound(a.begin(),a.end(),x)-a.begin()<<'\n';}}'''

def cpp_matroid(kind):
    if kind in ('rainbow','rainbow_tree'):
        ending='cout<<count(in.begin(),in.end(),1)<<\'\\n\';' if kind=='rainbow' else 'cout<<(count(in.begin(),in.end(),1)==n-1?"YES\\n":"NO\\n");'
        return CPP_MATROID+f'''int main(){{ios::sync_with_stdio(false);cin.tie(nullptr);int n,m;cin>>n>>m;vector<pair<int,int>>e(m);vector<int>color(m);for(int i=0;i<m;i++)cin>>e[i].first>>e[i].second>>color[i],--e[i].first,--e[i].second;auto in=intersect(m,[&](auto&s){{return forest_ok(n,e,s);}},[&](auto&s){{set<int>z;for(int i=0;i<m;i++)if(s[i]&&!z.insert(color[i]).second)return false;return true;}});{ending}}}'''
    if kind=='dual_forest':head='int n1,n2,m;cin>>n1>>n2>>m;';ending="cout<<count(in.begin(),in.end(),1)<<'\\n';"
    else:head='int n,m;cin>>n>>m;int n1=n,n2=n;';ending='cout<<(count(in.begin(),in.end(),1)==n-1?"YES\\n":"NO\\n");'
    return CPP_MATROID+f'''int main(){{ios::sync_with_stdio(false);cin.tie(nullptr);{head}vector<pair<int,int>>a(m),b(m);for(int i=0;i<m;i++)cin>>a[i].first>>a[i].second>>b[i].first>>b[i].second,--a[i].first,--a[i].second,--b[i].first,--b[i].second;auto in=intersect(m,[&](auto&s){{return forest_ok(n1,a,s);}},[&](auto&s){{return forest_ok(n2,b,s);}});{ending}}}'''
CPP['rainbow']=cpp_matroid('rainbow');CPP['rainbow_tree']=cpp_matroid('rainbow_tree');CPP['dual_forest']=cpp_matroid('dual_forest');CPP['two_map']=cpp_matroid('two_map')

def cpp_arb():return CPP_ARB+r'''int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,m,r;cin>>n>>m>>r;vector<Edge>e(m);for(auto&x:e)cin>>x.u>>x.v>>x.w,--x.u,--x.v;auto ans=arbo(n,r-1,e);if(ans)cout<<*ans<<'\n';else cout<<"IMPOSSIBLE\n";}'''
CPP['arborescence']=cpp_arb();CPP['broadcast']=cpp_arb()
CPP['bottleneck']=r'''#include <bits/stdc++.h>
using namespace std;bool ok(vector<vector<int>>&a,int x){int n=a.size();vector<int>match(n,-1);function<bool(int,vector<char>&)>dfs=[&](int u,vector<char>&seen){for(int v=0;v<n;v++)if(a[u][v]<=x&&!seen[v]){seen[v]=1;if(match[v]<0||dfs(match[v],seen)){match[v]=u;return true;}}return false;};for(int u=0;u<n;u++){vector<char>seen(n);if(!dfs(u,seen))return false;}return true;}int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;cin>>n;vector<vector<int>>a(n,vector<int>(n));vector<int>v;for(auto&r:a)for(int&x:r)cin>>x,v.push_back(x);sort(v.begin(),v.end());v.erase(unique(v.begin(),v.end()),v.end());int l=-1,r=v.size()-1;while(r-l>1){int m=(l+r)/2;(ok(a,v[m])?r:l)=m;}cout<<v[r]<<'\n';}'''

SAMPLES={"assignment":("3\n4 1 3\n2 0 5\n3 2 2\n","5\n"),"profit_assignment":("2 3\n5 -1 4\n2 7 3\n","12\n"),"blossom":("5 5\n1 2\n2 3\n3 1\n3 4\n4 5\n","2\n"),"compat_pairing":("5 2\n1 4 6 7 10\n2 3\n","2\n"),"gomory_queries":("3 3 2\n1 2 4\n2 3 2\n1 3 3\n1 2\n1 3\n","6\n5\n"),"rainbow":("4 4\n1 2 1\n2 3 1\n3 4 2\n1 4 3\n","3\n"),"dual_forest":("3 3 3\n1 2 1 2\n2 3 2 3\n1 3 1 3\n","2\n"),"arborescence":("3 4 1\n1 2 5\n1 3 4\n2 3 1\n3 2 2\n","6\n"),"bottleneck":("3\n8 2 5\n6 4 7\n3 9 1\n","5\n"),"roommates":("5 4\n1 2\n2 3\n3 1\n4 5\n","1\n"),"cut_pairs":("3 3 3\n1 2 4\n2 3 2\n1 3 3\n4\n5\n6\n","0\n2\n3\n"),"rainbow_tree":("4 4\n1 2 1\n2 3 2\n3 4 3\n1 4 1\n","YES\n"),"broadcast":("3 4 1\n1 2 5\n1 3 4\n2 3 1\n3 2 2\n","6\n"),"two_map":("3 3\n1 2 1 2\n2 3 2 3\n1 3 1 3\n","YES\n")}

LESSONS={85:r'''---
title: "Section 85 — Weighted And General Matching"
format: pdf
geometry: margin=1.8cm
---

# Augmenting needs either a dual certificate or a contraction

This lesson develops A--C. Problem D is editorial-only.

# Problem A: Hungarian potentials

Assignment is perfect bipartite matching. Hungarian maintains row potentials `u`, column potentials `v`, and nonnegative reduced costs `cost-u-v`. Equality edges have zero reduced cost. While inserting one row, grow an alternating tree; the smallest slack changes potentials until a new equality edge appears. A free column ends an augmenting predecessor chain.

Weak duality makes `sum(u)+sum(v)` a lower bound. A perfect matching of equality edges reaches that bound, so complementary slackness proves optimality.

# Problem B: forbidden rectangular assignment

The same algorithm supports rows no more numerous than columns. Negate profit and replace forbidden pairs by an infinity larger than every feasible total. After optimization, explicitly reject a matching containing infinity; otherwise its negated cost is the maximum profit.

# Problem C: blossoms

In general graphs an edge between two even alternating-tree levels creates an odd alternating cycle. Contract that blossom: from outside, all alternating ways through it are interchangeable for finding an augmenting path. Continue BFS on bases, then use stored predecessor information to expand and flip the original path.

The invariant is that augmenting paths exist in the contracted graph exactly when they exist in the original graph.

# Exercises

A--C cover assignment duality and blossom contraction. D is a modeling transfer.
''',86:r'''---
title: "Section 86 — Cut Trees And Matroid Intersection"
format: pdf
geometry: margin=1.8cm
---

# Compress repeated optimization into a tree or an exchange graph

This lesson develops A--C. Problem D is editorial-only.

# Problem A: Gomory--Hu trees

For an undirected graph, one weighted tree represents every pair minimum cut: the answer for `u,v` is the minimum edge on their tree path. Build it using `n-1` maximum flows. Each residual source side reparents later vertices sharing the same current parent; the parent-swap correction preserves cuts nested through that parent.

# Problem B: exchange-graph augmentation

Maintain a set independent in two matroids. Outside elements addable to matroid 1 are BFS sources; elements addable to matroid 2 are sinks. Arcs alternate between exchanges preserving matroid 1 and exchanges preserving matroid 2. Flipping membership along a source-to-sink path grows the common set by one. The matroid-intersection theorem says no augmenting path is an optimality certificate.

# Problem C: graphic independence oracles

A graphic matroid declares an edge set independent exactly when it is a forest, testable by DSU. Two endpoint maps therefore give two graphic oracles on the same selectable elements. This remains polynomial for two matroids; an arbitrary third constraint would not be a harmless extension.

# Exercises

A--C develop cut-tree compression and matroid exchange. D requires directed cycle contraction.
''',87:r'''---
title: "Section 87 — Master Matching And Matroids Mixed Contest"
format: pdf
geometry: margin=1.8cm
---

# Contest contract

Six new problems combine threshold matching, blossom modeling, cut-tree aggregation, matroid intersection, and directed arborescence contraction.

| Problem | Main idea |
|---|---|
| A | binary search plus bipartite feasibility |
| B | unmatched vertices from general matching |
| C | all pair cuts represented by tree paths |
| D | graphic/partition matroid intersection |
| E | minimum incoming edges and cycle contraction |
| F | common spanning tree in two graphic matroids |

# Exercises

A--F form the complete mixed contest.
'''}

NOTES={"assignment":("Maintain feasible Hungarian potentials and augment only through equality edges.","Reduced costs stay nonnegative, giving a dual lower bound. The final perfect matching uses tight edges and reaches the bound."),"profit_assignment":("Negate profits and encode forbidden pairs by a dominant infinity.","Finite assignments preserve reversed objective order; an infinity edge occurs exactly when no complete allowed assignment exists."),"blossom":("Contract odd alternating cycles between even BFS vertices.","Blossom contraction preserves augmenting-path existence, and expansion of predecessors yields a valid original path whose flip grows the matching."),"compat_pairing":("Build exactly the allowed compatibility graph and run general matching.","Valid disjoint pair families are precisely graph matchings, so their optima coincide."),"gomory_queries":("Represent all pair minimum cuts by minimum edges on Gomory--Hu tree paths.","Residual cut-side reparenting preserves the tree-cut invariant at every construction step; path minima therefore equal original pair cuts."),"rainbow":("Intersect the graphic matroid with the color partition matroid.","Every exchange-path flip preserves both independences and grows the set; absence of a path certifies maximum cardinality."),"dual_forest":("Use two DSU forest oracles on different endpoint maps.","This is exactly two-matroid intersection, so the final common independent set is maximum."),"arborescence":("Select minimum incoming edges, contract their directed cycles, and subtract those minima from crossing costs.","Every solution pays the accumulated minima and replaces exactly one entry per contracted cycle; reduced costs preserve the remaining choice."),"bottleneck":("Binary-search the threshold at which a perfect bipartite matching first exists.","Feasibility is monotone and equivalent to an assignment with maximum cost at most the threshold."),"roommates":("Use a maximum matching in the compatibility graph.","Each matched edge covers exactly two participants, so maximum edge count minimizes the unmatched remainder."),"cut_pairs":("Enumerate and sort all Gomory--Hu path minima.","Each stored value is exactly one unordered pair cut, so upper bound answers every threshold count."),"rainbow_tree":("Seek common independent size `n-1` in graphic and color matroids.","A forest of `n-1` edges is spanning, making the size test necessary and sufficient."),"broadcast":("Apply directed minimum-arborescence contraction with signed reduced costs.","Loops and parallel or negative edges do not alter the minimum-incoming/cycle replacement proof."),"two_map":("Seek size `n-1` in two graphic matroids.","That size is a spanning tree on both n-vertex maps, and every common spanning tree is such a common independent set.")}

def editorial(section):
 out=[f'''---\ntitle: "Section {section} Editorial — {SECTIONS[section][1]}"\nformat: pdf\ngeometry: margin=1.65cm\nfontsize: 9pt\n---\n''']
 for i,(slug,title,kind) in enumerate(PROBLEMS[section]):
  find,proof=NOTES[kind];out.append(f'''# {chr(65+i)}. {title}\n\n## How to find it\n\n{find}\n\n## Correctness\n\n{proof}\n\n## Complexity\n\nThe reference follows the standard polynomial bound of the named augmentation, flow, or contraction algorithm; explicit problem limits keep oracle-based matroid intersection practical.\n\n## C++\n\n```cpp\n{{{{< include problems/{slug}/solution.cpp >}}}}\n```\n\n## Python\n\n```python\n{{{{< include problems/{slug}/solution.py >}}}}\n```\n''')
 return '\n'.join(out)
def generate():
 for section,(directory,title) in SECTIONS.items():
  base=ROOT/'sections'/f'{section:02d}_{directory}';base.mkdir(parents=True,exist_ok=True);(base/'lesson.qmd').write_text(LESSONS[section]);(base/'editorial.qmd').write_text(editorial(section));links=[];checks=[]
  for slug,name,kind in PROBLEMS[section]:
   links.append(f'- [{name}](problems/{slug}/README.md)');checks.append(f'- [ ] [{name}](problems/{slug}/README.md)');p=base/'problems'/slug;p.mkdir(parents=True,exist_ok=True);tests=p/'tests';tests.mkdir(exist_ok=True);(p/'README.md').write_text(f'# {name}\n\n{STATEMENTS[kind]}\n');(p/'solve.cpp').write_text(CPP_STUB);(p/'solve.py').write_text(PY_STUB);(p/'solution.cpp').write_text(CPP[kind]);(p/'solution.py').write_text(PY[kind]);(p/'manifest.json').write_text(json.dumps({'title':name,'checker':'tokens','time_limit_seconds':10})+'\n');x,y=SAMPLES[kind];(tests/'sample1.in').write_text(x);(tests/'sample1.out').write_text(y);(tests/'random_cases.py').write_text(f'''import subprocess,sys\nfrom pathlib import Path\nROOT=Path(__file__).resolve().parents[5]\nraise SystemExit(subprocess.call([sys.executable,str(ROOT/"tools"/"matching_matroids_random.py"),"{kind}",*sys.argv[1:]]))\n''')
  extra='The lesson derives A--C; D is explained only in the editorial.' if section<87 else 'Exactly six new problems form the mixed contest.';(base/'README.md').write_text(f'# Section {section}: {title}\n\n{extra}\n\n## Problems\n\n'+'\n'.join(links)+'\n');(base/'PRACTICE.md').write_text(f'# Section {section} Practice\n\n'+'\n'.join(checks)+'\n');names=',\n        '.join(repr(x[0]) for x in PROBLEMS[section]);(base/'check.py').write_text(f'''from pathlib import Path\nimport sys\nROOT=Path(__file__).resolve().parents[2]\nsys.path.insert(0,str(ROOT))\nfrom tools.section_checker import run_section_checks\nSECTION=Path(__file__).resolve().parent\nPROBLEMS=[SECTION/"problems"/x for x in (\n        {names},\n)]\nif __name__=="__main__":raise SystemExit(run_section_checks({section},PROBLEMS,ROOT))\n''')
 for section,(directory,_) in SECTIONS.items():
  for slug,name,kind in PROBLEMS[section]:
   if kind in TIME_LIMITS:
    manifest=ROOT/'sections'/f'{section:02d}_{directory}'/'problems'/slug/'manifest.json'
    manifest.write_text(json.dumps({'title':name,'checker':'tokens','time_limit_seconds':TIME_LIMITS[kind]})+'\n')
if __name__=='__main__':generate()
