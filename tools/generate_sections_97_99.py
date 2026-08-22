"""Generate Sections 97--99: digit, profile, connectivity, and treewidth DP."""
from __future__ import annotations
import ast,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];MOD=1_000_000_007
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
SECTIONS={97:("digit_broken_profile_dp","Digit And Broken-Profile DP"),98:("plug_treewidth_frontiers","Plug DP And Treewidth Frontiers"),99:("master_frontier_dp_mixed","Master Frontier DP Mixed Contest")}
PROBLEMS={97:[("a_digit_sum_range","Digit Sum Range","digitsum"),("b_forbidden_decimal_pattern","Forbidden Decimal Pattern","digitpattern"),("c_obstacle_domino_tilings","Obstacle Domino Tilings","domino"),("d_grid_independent_sets","Grid Independent Sets","gridset")],98:[("a_tower_domino_tilings","Tower Domino Tilings","tower"),("b_connected_cell_sets","Connected Cell Sets","connected"),("c_terminal_steiner_network","Terminal Steiner Network","steiner"),("d_nice_decomposition_independent_set","Nice-Decomposition Independent Set","treewidth")],99:[("a_checksum_digit_sum","Checksum Digit Sum","digitsum_story"),("b_serial_filter","Serial Filter","digitpattern_story"),("c_repeating_domino_tower","Repeating Domino Tower","tower_story"),("d_connected_reserve","Connected Reserve","connected_story"),("e_terminal_backbone","Terminal Backbone","steiner_story"),("f_decomposition_profit","Decomposition Profit","treewidth_story")]}
STATEMENTS={
'digitsum':'''For each query `[L,R,S]`, count integers `x` with `L <= x <= R` whose decimal digit sum is exactly `S`. `0 <= L <= R <= 10^18`, `0 <= S <= 171`, and `q <= 10000`. Count zero with digit sum zero.

Sample input
```text
2
0 20 2
10 15 6
```
Sample output
```text
3
1
```''',
'digitpattern':'''For each `N` and nonempty decimal pattern `P`, count integers `x` in `[0,N]` whose usual decimal representation does not contain `P` as a substring. The representation of zero is `0`; positive representations have no leading zeroes. `N <= 10^18`, `|P| <= 18`, `q <= 1000`.

Sample input
```text
2
20 1
105 05
```
Sample output
```text
10
105
```''',
'domino':'''Count tilings of an `n by m` board by `1 by 2` dominoes modulo `1000000007`. `#` cells are blocked and `.` cells must be covered exactly once. `n,m <= 12`.

Sample input
```text
2 3
...
...
```
Sample output
```text
3
```''',
'gridset':'''Count independent sets of unblocked cells in an `n by m` grid modulo `1000000007`: no two chosen cells may share an edge. `n,m <= 14`.

Sample input
```text
2 2
..
..
```
Sample output
```text
7
```''',
'tower':'''Count domino tilings of an `H by W` empty rectangle modulo `1000000007`, where `0 <= H <= 10^18` and `1 <= W <= 6`.

Sample input
```text
3 2
```
Sample output
```text
3
```''',
'connected':'''Count nonempty connected subsets of open cells in an `H by W` grid modulo `1000000007`. Connectivity uses shared edges. `H <= 30`, `W <= 7`; blocked cells are `#`.

Sample input
```text
1 3
...
```
Sample output
```text
6
```''',
'steiner':'''An undirected weighted graph has `n <= 60`, `m <= 500`, and `k <= 10` terminals. Print the minimum weight of a connected subgraph containing every terminal, or `IMPOSSIBLE`.

Sample input
```text
4 4 3
1 2 1
2 3 1
3 4 1
1 4 10
1 3 4
```
Sample output
```text
3
```''',
'treewidth':'''Find a maximum-weight independent set using a supplied valid nice tree decomposition of width at most 15. Vertices are `1..n`; weights may be negative. Decomposition nodes are topologically ordered and the root is node `t` with empty bag.

Node formats are `L`, `I child vertex`, `F child vertex`, and `J left right`. `I` adds the vertex to its child's bag, `F` removes it, and `J` has two children with identical bags. The input guarantees the nice-decomposition properties and that every graph edge appears together in some bag. `n <= 60`, `t <= 200000`, and the aggregate state budget `sum(2^|bag|)` over all decomposition nodes is at most `2000000`.

Sample input
```text
2 1
5 7
1 2
5
L
I 1 1
I 2 2
F 3 1
F 4 2
```
Sample output
```text
7
```'''}
STATEMENTS.update({
'digitsum_story':'''For each query, count integers `x` in `[L,R]` whose decimal digit sum is exactly `S` and whose remainder modulo `M` is zero. `0 <= L <= R <= 10^18`, `0 <= S <= 171`, `1 <= M <= 50`, and `q <= 1000`.

Sample input
```text
2
0 30 3 3
10 20 2 2
```
Sample output
```text
4
1
```''',
'digitpattern_story':'''For each query, count integers in `[0,N]` whose usual decimal representation avoids `P` as a substring and has digit sum exactly `S`. Zero is represented by `0`; positive representations have no leading zeroes. `N <= 10^18`, `|P| <= 18`, `0 <= S <= 171`, and `q <= 500`.

Sample input
```text
2
20 1 2
30 9 3
```
Sample output
```text
2
4
```''',
'tower_story':'''A block of `P` obstacle rows is repeated exactly `H` times. Count domino tilings of the resulting `(P*H) by W` board modulo `1000000007`. Dots must be covered and `#` cells are blocked. `0 <= H <= 10^18`, `1 <= P,W <= 5`.

Sample input
```text
2 1 2
..
```
Sample output
```text
2
```''',
'connected_story':'''Count connected subsets of grid cells that contain every required cell `T`. Cells `.` are optional and `#` are blocked. Connectivity uses shared edges. There is at least one `T`; `H <= 30`, `W <= 7`. Print the count modulo `1000000007`.

Sample input
```text
1 3
T.T
```
Sample output
```text
1
```''',
'steiner_story':'''A weighted undirected graph has `k <= 10` distinguished terminals. For each query mask, print the minimum weight of a connected subgraph containing the terminals whose bits occur in the mask. `n <= 60`, `m <= 500`, `q <= 1000`; masks are nonzero.

Input gives `n m k q`, the edges, one line of `k` terminal vertices, then the `q` masks.

Sample input
```text
4 4 3 2
1 2 1
2 3 1
3 4 1
1 4 10
1 3 4
3
7
```
Sample output
```text
2
3
```''',
'treewidth_story':'''Find the minimum weight of a vertex cover using a supplied valid nice tree decomposition of width at most 15. Vertex weights are nonnegative. The decomposition format and guarantees are the same as in Nice-Decomposition Independent Set: `L`, `I child vertex`, `F child vertex`, and `J left right`; nodes are topologically ordered and node `t` is an empty-bag root. `n <= 60`, `t <= 200000`, and `sum(2^|bag|) <= 2000000` over all decomposition nodes.

Sample input
```text
2 1
5 7
1 2
5
L
I 1 1
I 2 2
F 3 1
F 4 2
```
Sample output
```text
5
```'''
})

PY={}
PY['digitsum']=r'''import sys
MAX_SUM=171
WAYS=[[0]*(MAX_SUM+1) for _ in range(20)]
WAYS[0][0]=1
for length in range(1,20):
 for total in range(MAX_SUM+1):WAYS[length][total]=sum(WAYS[length-1][total-digit] for digit in range(10) if digit<=total)
def count(n,target):
 if n<0:return 0
 digits=list(map(int,str(n)));answer=0;prefix=0
 for pos,limit in enumerate(digits):
  remaining=len(digits)-pos-1
  for digit in range(limit):
   needed=target-prefix-digit
   if 0<=needed<=MAX_SUM:answer+=WAYS[remaining][needed]
  prefix+=limit
 return answer+int(prefix==target)
def main():
 d=list(map(int,sys.stdin.buffer.read().split()));print('\n'.join(str(count(d[i+1],d[i+2])-count(d[i]-1,d[i+2])) for i in range(1,len(d),3)))
if __name__=='__main__':main()
'''
PY['digitpattern']=r'''import sys
from functools import lru_cache
def count(n,pattern):
 digits=list(map(int,str(n)));p=list(map(int,pattern));fail=[0]*len(p)
 for i in range(1,len(p)):
  j=fail[i-1]
  while j and p[i]!=p[j]:j=fail[j-1]
  if p[i]==p[j]:j+=1
  fail[i]=j
 def step(j,d):
  while j and p[j]!=d:j=fail[j-1]
  if p[j]==d:j+=1
  return j
 @lru_cache(None)
 def dp(pos,j,tight,started):
  if pos==len(digits):return int(started or pattern!='0')
  limit=digits[pos] if tight else 9;answer=0
  for d in range(limit+1):
   nt=tight and d==limit
   if not started and d==0:answer+=dp(pos+1,0,nt,False)
   else:
    nj=step(j,d)
    if nj<len(p):answer+=dp(pos+1,nj,nt,True)
  return answer
 return dp(0,0,True,False)
def main():
 data=sys.stdin.buffer.read().split();out=[]
 for i in range(1,len(data),2):out.append(str(count(int(data[i]),data[i+1].decode())))
 print('\n'.join(out))
if __name__=='__main__':main()
'''
PY['domino']=r'''import sys
MOD=1000000007
def main():
 data=sys.stdin.buffer.read().split();n,m=map(int,data[:2]);grid=[x.decode() for x in data[2:]];dp={0:1}
 for row in range(n):
  blocked=sum((grid[row][c]=='#')<<c for c in range(m));nd={}
  for incoming,value in dp.items():
   if incoming&blocked:continue
   def fill(c,used,out):
    if c==m:nd[out]=(nd.get(out,0)+value)%MOD;return
    bit=1<<c
    if (used|blocked)&bit:fill(c+1,used,out)
    else:
     if c+1<m and not((used|blocked)>>(c+1)&1):fill(c+2,used|bit|(bit<<1),out)
     if row+1<n and grid[row+1][c]=='.':fill(c+1,used|bit,out|bit)
   fill(0,incoming,0)
  dp=nd
 print(dp.get(0,0))
if __name__=='__main__':main()
'''
PY['gridset']=r'''import sys
MOD=1000000007
def main():
 data=sys.stdin.buffer.read().split();n,m=map(int,data[:2]);grid=[x.decode() for x in data[2:]];valid=[x for x in range(1<<m) if not(x&(x<<1))];dp={0:1}
 for row in grid:
  blocked=sum((row[c]=='#')<<c for c in range(m));nd={}
  for mask in valid:
   if mask&blocked:continue
   nd[mask]=sum(value for old,value in dp.items() if not(mask&old))%MOD
  dp=nd
 print(sum(dp.values())%MOD)
if __name__=='__main__':main()
'''
PY['tower']=r'''import sys
MOD=1000000007
def mul(a,b):
 n=len(a);c=[[0]*n for _ in range(n)]
 for i in range(n):
  for k,x in enumerate(a[i]):
   if x:
    for j,y in enumerate(b[k]):c[i][j]=(c[i][j]+x*y)%MOD
 return c
def main():
 h,w=map(int,sys.stdin.buffer.read().split());size=1<<w;mat=[[0]*size for _ in range(size)]
 for incoming in range(size):
  def fill(c,used,out):
   if c==w:mat[incoming][out]+=1;return
   bit=1<<c
   if used&bit:fill(c+1,used,out)
   else:
    if c+1<w and not(used&(bit<<1)):fill(c+2,used|bit|(bit<<1),out)
    fill(c+1,used|bit,out|bit)
  fill(0,incoming,0)
 result=[[int(i==j) for j in range(size)] for i in range(size)]
 while h:
  if h&1:result=mul(result,mat)
  mat=mul(mat,mat);h//=2
 print(result[0][0])
if __name__=='__main__':main()
'''
PY['connected']=r'''import sys
MOD=1000000007
def canon(a):
 mp={};nxt=1;out=[]
 for x in a:
  if x and x not in mp:mp[x]=nxt;nxt+=1
  out.append(mp.get(x,0))
 return tuple(out)
def main():
 data=sys.stdin.buffer.read().split();h,w=map(int,data[:2]);g=[x.decode() for x in data[2:]];dp={(tuple([0]*w),False):1}
 for r in range(h):
  for c in range(w):
   nd={}
   for (labels,closed),value in dp.items():
    old=list(labels);up=old[c];left=old[c-1] if c else 0
    new=old[:];new[c]=0;vanished=up and up not in new
    if not vanished or (not any(new) and not closed):
     key=(canon(new),closed or bool(vanished));nd[key]=(nd.get(key,0)+value)%MOD
    if g[r][c]=='.' and not closed:
     new=old[:]
     if left and up and left!=up:new=[left if x==up else x for x in new]
     new[c]=left or up or max(new,default=0)+1;key=(canon(new),False);nd[key]=(nd.get(key,0)+value)%MOD
   dp=nd
 answer=0
 for (labels,closed),value in dp.items():
  if closed or len(set(labels)-{0})==1:answer=(answer+value)%MOD
 print(answer)
if __name__=='__main__':main()
'''
PY['steiner']=r'''import sys,heapq
def main():
 d=list(map(int,sys.stdin.buffer.read().split()));n,m,k=d[:3];at=3;g=[[] for _ in range(n)]
 for _ in range(m):u,v,w=d[at:at+3];at+=3;u-=1;v-=1;g[u].append((v,w));g[v].append((u,w))
 terminals=[x-1 for x in d[at:at+k]];inf=10**30;dp=[[inf]*n for _ in range(1<<k)]
 for i,v in enumerate(terminals):dp[1<<i][v]=0
 for mask in range(1,1<<k):
  sub=(mask-1)&mask
  while sub:
   other=mask^sub
   if sub<other:
    for v in range(n):dp[mask][v]=min(dp[mask][v],dp[sub][v]+dp[other][v])
   sub=(sub-1)&mask
  q=[(x,v) for v,x in enumerate(dp[mask]) if x<inf];heapq.heapify(q)
  while q:
   cost,u=heapq.heappop(q)
   if cost!=dp[mask][u]:continue
   for v,w in g[u]:
    if cost+w<dp[mask][v]:dp[mask][v]=cost+w;heapq.heappush(q,(cost+w,v))
 ans=min(dp[-1]);print('IMPOSSIBLE' if ans==inf else ans)
if __name__=='__main__':main()
'''
PY['treewidth']=r'''import sys
def main():
 lines=sys.stdin.buffer.readlines();n,m=map(int,lines[0].split());weight=list(map(int,lines[1].split()));adj=[0]*n
 for line in lines[2:2+m]:u,v=map(int,line.split());u-=1;v-=1;adj[u]|=1<<v;adj[v]|=1<<u
 t=int(lines[2+m]);dp=[];bags=[]
 for line in lines[3+m:3+m+t]:
  z=line.split();kind=z[0]
  if kind==b'L':bags.append(0);dp.append({0:0})
  elif kind==b'I':
   child=int(z[1])-1;v=int(z[2])-1;bags.append(bags[child]|1<<v);cur=dict(dp[child])
   for mask,val in dp[child].items():
    if not(mask&adj[v]):cur[mask|1<<v]=max(cur.get(mask|1<<v,-10**30),val+weight[v])
   dp.append(cur)
  elif kind==b'F':
   child=int(z[1])-1;v=int(z[2])-1;bags.append(bags[child]&~(1<<v));cur={}
   for mask,val in dp[child].items():key=mask&~(1<<v);cur[key]=max(cur.get(key,-10**30),val)
   dp.append(cur)
  else:
   a=int(z[1])-1;b=int(z[2])-1;bags.append(bags[a]);cur={}
   for mask,val in dp[a].items():
    if mask in dp[b]:cur[mask]=val+dp[b][mask]-sum(weight[v] for v in range(n) if mask>>v&1)
   dp.append(cur)
 print(dp[-1].get(0,max(dp[-1].values())))
if __name__=='__main__':main()
'''
PY['digitsum_story']=r'''import sys
MAX_SUM=171
def suffix_ways(mod):
 ways=[[[0]*mod for _ in range(MAX_SUM+1)] for _ in range(20)];ways[0][0][0]=1
 for length in range(1,20):
  previous=ways[length-1];current=ways[length]
  for total in range(MAX_SUM+1):
   row=current[total]
   for digit in range(min(9,total)+1):
    for remainder,value in enumerate(previous[total-digit]):
     if value:row[(remainder*10+digit)%mod]+=value
 return ways
def count(n,target,mod,ways):
 if n<0:return 0
 digits=list(map(int,str(n)));answer=0;prefix_sum=0;prefix_rem=0;powers=[pow(10,length,mod) for length in range(20)]
 for pos,limit in enumerate(digits):
  remaining=len(digits)-pos-1
  for digit in range(limit):
   needed_sum=target-prefix_sum-digit
   if 0<=needed_sum<=MAX_SUM:
    next_rem=(prefix_rem*10+digit)%mod;needed_rem=(-next_rem*powers[remaining])%mod
    answer+=ways[remaining][needed_sum][needed_rem]
  prefix_sum+=limit;prefix_rem=(prefix_rem*10+limit)%mod
 return answer+int(prefix_sum==target and prefix_rem==0)
def main():
 d=list(map(int,sys.stdin.buffer.read().split()));queries=[tuple(d[i:i+4]) for i in range(1,len(d),4)];out=[0]*len(queries);groups={}
 for index,query in enumerate(queries):groups.setdefault(query[3],[]).append(index)
 for mod,indices in groups.items():
  ways=suffix_ways(mod)
  for index in indices:
   left,right,target,_=queries[index];out[index]=count(right,target,mod,ways)-count(left-1,target,mod,ways)
 print('\n'.join(map(str,out)))
if __name__=='__main__':main()
'''
PY['digitpattern_story']=r'''import sys
from functools import lru_cache
def count(n,pattern,target):
 digits=list(map(int,str(n)));p=list(map(int,pattern));fail=[0]*len(p)
 for i in range(1,len(p)):
  j=fail[i-1]
  while j and p[i]!=p[j]:j=fail[j-1]
  if p[i]==p[j]:j+=1
  fail[i]=j
 def step(j,d):
  while j and p[j]!=d:j=fail[j-1]
  if p[j]==d:j+=1
  return j
 @lru_cache(None)
 def dp(pos,j,total,tight,started):
  if total>target:return 0
  if pos==len(digits):return int(total==target and (started or pattern!='0'))
  limit=digits[pos] if tight else 9;answer=0
  for d in range(limit+1):
   nt=tight and d==limit
   if not started and d==0:answer+=dp(pos+1,0,total,nt,False)
   else:
    nj=step(j,d)
    if nj<len(p):answer+=dp(pos+1,nj,total+d,nt,True)
  return answer
 return dp(0,0,0,True,False)
def main():
 data=sys.stdin.buffer.read().split();out=[]
 for i in range(1,len(data),3):out.append(str(count(int(data[i]),data[i+1].decode(),int(data[i+2]))))
 print('\n'.join(out))
if __name__=='__main__':main()
'''
PY['tower_story']=r'''import sys
MOD=1000000007
def mul(a,b):
 n=len(a);c=[[0]*n for _ in range(n)]
 for i in range(n):
  for k,x in enumerate(a[i]):
   if x:
    for j,y in enumerate(b[k]):c[i][j]=(c[i][j]+x*y)%MOD
 return c
def main():
 data=sys.stdin.buffer.read().split();h,p,w=map(int,data[:3]);rows=[x.decode() for x in data[3:]];size=1<<w
 block=[[int(i==j) for j in range(size)] for i in range(size)]
 for row in rows:
  blocked=sum((row[c]=='#')<<c for c in range(w));mat=[[0]*size for _ in range(size)]
  for incoming in range(size):
   if incoming&blocked:continue
   def fill(c,used,out):
    if c==w:mat[incoming][out]+=1;return
    bit=1<<c
    if (used|blocked)&bit:fill(c+1,used,out)
    else:
     if c+1<w and not((used|blocked)&(bit<<1)):fill(c+2,used|bit|(bit<<1),out)
     fill(c+1,used|bit,out|bit)
   fill(0,incoming,0)
  block=mul(block,mat)
 result=[[int(i==j) for j in range(size)] for i in range(size)]
 while h:
  if h&1:result=mul(result,block)
  block=mul(block,block);h//=2
 print(result[0][0])
if __name__=='__main__':main()
'''
PY['connected_story']=PY['connected'].replace("if not vanished or (not any(new) and not closed):","if g[r][c]!='T' and (not vanished or (not any(new) and not closed)):").replace("if g[r][c]=='.' and not closed:","if g[r][c]!='#' and not closed:")
PY['steiner_story']=PY['steiner'].replace("n,m,k=d[:3];at=3","n,m,k,queries=d[:4];at=4").replace("ans=min(dp[-1]);print('IMPOSSIBLE' if ans==inf else ans)","out=[]\n for mask in d[at+k:at+k+queries]:\n  ans=min(dp[mask]);out.append('IMPOSSIBLE' if ans==inf else str(ans))\n print('\\n'.join(out))")
PY['treewidth_story']=PY['treewidth'].replace("print(dp[-1].get(0,max(dp[-1].values())))","print(sum(weight)-dp[-1].get(0,max(dp[-1].values())))")

CPP={}
CPP['digitsum']=r'''#include <bits/stdc++.h>
using namespace std;using ll=long long;ll ways[20][172];ll count_to(ll n,int target){if(n<0)return 0;string digits=to_string(n);ll answer=0;int prefix=0;for(int pos=0;pos<(int)digits.size();pos++){int limit=digits[pos]-'0',remaining=digits.size()-pos-1;for(int digit=0;digit<limit;digit++){int needed=target-prefix-digit;if(0<=needed&&needed<=171)answer+=ways[remaining][needed];}prefix+=limit;}return answer+(prefix==target);}int main(){ios::sync_with_stdio(false);cin.tie(nullptr);ways[0][0]=1;for(int length=1;length<20;length++)for(int total=0;total<=171;total++)for(int digit=0;digit<=9&&digit<=total;digit++)ways[length][total]+=ways[length-1][total-digit];int q;cin>>q;while(q--){ll l,r;int target;cin>>l>>r>>target;cout<<count_to(r,target)-count_to(l-1,target)<<'\n';}}'''
CPP['digitpattern']=r'''#include <bits/stdc++.h>
using namespace std;using ll=long long;string digits,pat;vector<int>fail;map<tuple<int,int,bool,bool>,ll>memo;int step(int j,int d){char c='0'+d;while(j&&pat[j]!=c)j=fail[j-1];if(pat[j]==c)j++;return j;}ll dfs(int pos,int j,bool tight,bool started){if(pos==(int)digits.size())return started||pat!="0";auto key=tuple{pos,j,tight,started};if(!tight&&memo.count(key))return memo[key];int lim=tight?digits[pos]-'0':9;ll ans=0;for(int d=0;d<=lim;d++){bool nt=tight&&d==lim;if(!started&&d==0)ans+=dfs(pos+1,0,nt,0);else{int nj=step(j,d);if(nj<(int)pat.size())ans+=dfs(pos+1,nj,nt,1);}}if(!tight)memo[key]=ans;return ans;}ll solve(ll n,string p){digits=to_string(n);pat=p;fail.assign(p.size(),0);for(int i=1;i<(int)p.size();i++){int j=fail[i-1];while(j&&p[i]!=p[j])j=fail[j-1];if(p[i]==p[j])j++;fail[i]=j;}memo.clear();return dfs(0,0,1,0);}int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int q;cin>>q;while(q--){ll n;string p;cin>>n>>p;cout<<solve(n,p)<<'\n';}}'''
CPP['domino']=r'''#include <bits/stdc++.h>
using namespace std;const int MOD=1e9+7;int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,m;cin>>n>>m;vector<string>g(n);for(auto&s:g)cin>>s;vector<int>dp(1<<m);dp[0]=1;for(int r=0;r<n;r++){int blocked=0;for(int c=0;c<m;c++)if(g[r][c]=='#')blocked|=1<<c;vector<int>nd(1<<m);for(int in=0;in<1<<m;in++)if(dp[in]&&!(in&blocked)){function<void(int,int,int)>fill=[&](int c,int used,int out){if(c==m){nd[out]=(nd[out]+dp[in])%MOD;return;}int bit=1<<c;if((used|blocked)&bit)fill(c+1,used,out);else{if(c+1<m&&!((used|blocked)&(bit<<1)))fill(c+2,used|bit|(bit<<1),out);if(r+1<n&&g[r+1][c]=='.')fill(c+1,used|bit,out|bit);}};fill(0,in,0);}dp.swap(nd);}cout<<dp[0]<<'\n';}'''
CPP['gridset']=r'''#include <bits/stdc++.h>
using namespace std;const int MOD=1e9+7;int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,m;cin>>n>>m;vector<string>g(n);for(auto&s:g)cin>>s;vector<int>valid;for(int x=0;x<1<<m;x++)if(!(x&(x<<1)))valid.push_back(x);vector<int>dp(1<<m);dp[0]=1;for(auto row:g){int blocked=0;for(int c=0;c<m;c++)if(row[c]=='#')blocked|=1<<c;vector<int>nd(1<<m);for(int x:valid)if(!(x&blocked))for(int y:valid)if(!(x&y))nd[x]=(nd[x]+dp[y])%MOD;dp.swap(nd);}cout<<accumulate(dp.begin(),dp.end(),0LL)%MOD<<'\n';}'''
CPP['tower']=r'''#include <bits/stdc++.h>
using namespace std;using ll=long long;const int MOD=1e9+7;using Mat=vector<vector<int>>;Mat mul(const Mat&a,const Mat&b){int n=a.size();Mat c(n,vector<int>(n));for(int i=0;i<n;i++)for(int k=0;k<n;k++)if(a[i][k])for(int j=0;j<n;j++)c[i][j]=(c[i][j]+(ll)a[i][k]*b[k][j])%MOD;return c;}int main(){ios::sync_with_stdio(false);cin.tie(nullptr);unsigned long long h;int w;cin>>h>>w;int n=1<<w;Mat a(n,vector<int>(n));for(int in=0;in<n;in++){function<void(int,int,int)>fill=[&](int c,int used,int out){if(c==w){a[in][out]++;return;}int bit=1<<c;if(used&bit)fill(c+1,used,out);else{if(c+1<w&&!(used&(bit<<1)))fill(c+2,used|bit|(bit<<1),out);fill(c+1,used|bit,out|bit);}};fill(0,in,0);}Mat r(n,vector<int>(n));for(int i=0;i<n;i++)r[i][i]=1;while(h){if(h&1)r=mul(r,a);a=mul(a,a);h>>=1;}cout<<r[0][0]<<'\n';}'''
CPP['connected']=r'''#include <bits/stdc++.h>
using namespace std;using ll=long long;const int MOD=1e9+7;using State=pair<vector<int>,bool>;vector<int>canon(vector<int>a){map<int,int>mp;int nxt=1;for(int&x:a)if(x){if(!mp.count(x))mp[x]=nxt++;x=mp[x];}return a;}int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int h,w;cin>>h>>w;vector<string>g(h);for(auto&s:g)cin>>s;map<State,int>dp;dp[{vector<int>(w),false}]=1;for(int r=0;r<h;r++)for(int c=0;c<w;c++){map<State,int>nd;for(auto[state,value]:dp){auto labels=state.first;bool closed=state.second;int up=labels[c],left=c?labels[c-1]:0;auto z=labels;z[c]=0;bool vanished=up&&find(z.begin(),z.end(),up)==z.end();if(!vanished||(!closed&&count_if(z.begin(),z.end(),[](int x){return x;})==0)){State key={canon(z),closed||vanished};nd[key]=(nd[key]+value)%MOD;}if(g[r][c]=='.'&&!closed){z=labels;if(left&&up&&left!=up)for(int&x:z)if(x==up)x=left;z[c]=left?left:(up?up:*max_element(z.begin(),z.end())+1);State key={canon(z),false};nd[key]=(nd[key]+value)%MOD;}}dp.swap(nd);}ll answer=0;for(auto[state,value]:dp){set<int>s(state.first.begin(),state.first.end());s.erase(0);if(state.second||s.size()==1)answer+=value;}cout<<answer%MOD<<'\n';}'''
CPP['steiner']=r'''#include <bits/stdc++.h>
using namespace std;using ll=long long;const ll INF=4e18;int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,m,k;cin>>n>>m>>k;vector<vector<pair<int,int>>>g(n);while(m--){int u,v,w;cin>>u>>v>>w;--u;--v;g[u].push_back({v,w});g[v].push_back({u,w});}vector<vector<ll>>dp(1<<k,vector<ll>(n,INF));for(int i=0,v;i<k;i++)cin>>v,dp[1<<i][v-1]=0;for(int mask=1;mask<1<<k;mask++){for(int sub=(mask-1)&mask;sub;sub=(sub-1)&mask){int other=mask^sub;if(sub<other)for(int v=0;v<n;v++)dp[mask][v]=min(dp[mask][v],dp[sub][v]+dp[other][v]);}priority_queue<pair<ll,int>,vector<pair<ll,int>>,greater<pair<ll,int>>>q;for(int v=0;v<n;v++)if(dp[mask][v]<INF)q.push({dp[mask][v],v});while(!q.empty()){auto[d,u]=q.top();q.pop();if(d!=dp[mask][u])continue;for(auto[v,w]:g[u])if(d+w<dp[mask][v])dp[mask][v]=d+w,q.push({d+w,v});}}ll ans=*min_element(dp.back().begin(),dp.back().end());if(ans==INF)cout<<"IMPOSSIBLE\n";else cout<<ans<<'\n';}'''
CPP['treewidth']=r'''#include <bits/stdc++.h>
using namespace std;using ll=long long;int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,m;cin>>n>>m;vector<ll>w(n);for(ll&x:w)cin>>x;vector<unsigned long long>adj(n);while(m--){int u,v;cin>>u>>v;--u;--v;adj[u]|=1ULL<<v;adj[v]|=1ULL<<u;}int t;cin>>t;vector<unsigned long long>bag(t);vector<map<unsigned long long,ll>>dp(t);for(int i=0;i<t;i++){char type;cin>>type;if(type=='L')dp[i][0]=0;else if(type=='I'){int child,v;cin>>child>>v;--child;--v;bag[i]=bag[child]|1ULL<<v;dp[i]=dp[child];for(auto[mask,val]:dp[child])if(!(mask&adj[v])){auto nextmask=mask|1ULL<<v;ll candidate=val+w[v];if(!dp[i].count(nextmask)||candidate>dp[i][nextmask])dp[i][nextmask]=candidate;}}else if(type=='F'){int child,v;cin>>child>>v;--child;--v;bag[i]=bag[child]&~(1ULL<<v);for(auto[mask,val]:dp[child]){auto nextmask=mask&~(1ULL<<v);if(!dp[i].count(nextmask)||val>dp[i][nextmask])dp[i][nextmask]=val;}}else{int a,b;cin>>a>>b;--a;--b;bag[i]=bag[a];for(auto[mask,val]:dp[a])if(dp[b].count(mask)){ll duplicate=0;for(int v=0;v<n;v++)if(mask>>v&1)duplicate+=w[v];dp[i][mask]=val+dp[b][mask]-duplicate;}}}cout<<dp.back()[0]<<'\n';}'''
CPP['digitsum_story']=r'''#include <bits/stdc++.h>
using namespace std;using ll=long long;struct Query{ll left,right;int target,mod;};using Ways=vector<vector<vector<ll>>>;Ways build(int mod){Ways ways(20,vector<vector<ll>>(172,vector<ll>(mod)));ways[0][0][0]=1;for(int length=1;length<20;length++)for(int total=0;total<=171;total++)for(int digit=0;digit<=9&&digit<=total;digit++)for(int remainder=0;remainder<mod;remainder++)ways[length][total][(remainder*10+digit)%mod]+=ways[length-1][total-digit][remainder];return ways;}ll count_to(ll n,int target,int mod,const Ways&ways){if(n<0)return 0;string digits=to_string(n);vector<int>power(20,1%mod);for(int i=1;i<20;i++)power[i]=power[i-1]*10%mod;ll answer=0;int prefix_sum=0,prefix_rem=0;for(int pos=0;pos<(int)digits.size();pos++){int limit=digits[pos]-'0',remaining=digits.size()-pos-1;for(int digit=0;digit<limit;digit++){int needed_sum=target-prefix_sum-digit;if(0<=needed_sum&&needed_sum<=171){int next_rem=(prefix_rem*10+digit)%mod;int needed_rem=(mod-(ll)next_rem*power[remaining]%mod)%mod;answer+=ways[remaining][needed_sum][needed_rem];}}prefix_sum+=limit;prefix_rem=(prefix_rem*10+limit)%mod;}return answer+(prefix_sum==target&&prefix_rem==0);}int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int q;cin>>q;vector<Query>queries(q);map<int,vector<int>>groups;for(int i=0;i<q;i++){auto&x=queries[i];cin>>x.left>>x.right>>x.target>>x.mod;groups[x.mod].push_back(i);}vector<ll>answer(q);for(auto&[mod,indices]:groups){Ways ways=build(mod);for(int index:indices){auto x=queries[index];answer[index]=count_to(x.right,x.target,mod,ways)-count_to(x.left-1,x.target,mod,ways);}}for(ll value:answer)cout<<value<<'\n';}'''
CPP['digitpattern_story']=r'''#include <bits/stdc++.h>
using namespace std;using ll=long long;string digits,pattern;vector<int>failure;int target;map<tuple<int,int,int,bool,bool>,ll>memo;int step(int j,int d){char c='0'+d;while(j&&pattern[j]!=c)j=failure[j-1];if(pattern[j]==c)j++;return j;}ll dfs(int pos,int j,int sum,bool tight,bool started){if(sum>target)return 0;if(pos==(int)digits.size())return sum==target&&(started||pattern!="0");auto key=tuple{pos,j,sum,tight,started};if(!tight&&memo.count(key))return memo[key];int limit=tight?digits[pos]-'0':9;ll answer=0;for(int d=0;d<=limit;d++){bool next_tight=tight&&d==limit;if(!started&&d==0)answer+=dfs(pos+1,0,sum,next_tight,false);else{int next=step(j,d);if(next<(int)pattern.size())answer+=dfs(pos+1,next,sum+d,next_tight,true);}}if(!tight)memo[key]=answer;return answer;}ll solve(ll n,string p,int s){digits=to_string(n);pattern=p;target=s;failure.assign(p.size(),0);for(int i=1;i<(int)p.size();i++){int j=failure[i-1];while(j&&p[i]!=p[j])j=failure[j-1];if(p[i]==p[j])j++;failure[i]=j;}memo.clear();return dfs(0,0,0,true,false);}int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int q;cin>>q;while(q--){ll n;string p;int s;cin>>n>>p>>s;cout<<solve(n,p,s)<<'\n';}}'''
CPP['tower_story']=r'''#include <bits/stdc++.h>
using namespace std;using ll=long long;const int MOD=1e9+7;using Matrix=vector<vector<int>>;Matrix multiply(const Matrix&a,const Matrix&b){int n=a.size();Matrix c(n,vector<int>(n));for(int i=0;i<n;i++)for(int k=0;k<n;k++)if(a[i][k])for(int j=0;j<n;j++)c[i][j]=(c[i][j]+(ll)a[i][k]*b[k][j])%MOD;return c;}int main(){ios::sync_with_stdio(false);cin.tie(nullptr);unsigned long long h;int p,w;cin>>h>>p>>w;vector<string>rows(p);for(auto&row:rows)cin>>row;int size=1<<w;Matrix block(size,vector<int>(size));for(int i=0;i<size;i++)block[i][i]=1;for(auto row:rows){int blocked=0;for(int c=0;c<w;c++)if(row[c]=='#')blocked|=1<<c;Matrix transition(size,vector<int>(size));for(int incoming=0;incoming<size;incoming++)if(!(incoming&blocked)){function<void(int,int,int)>fill=[&](int c,int used,int outgoing){if(c==w){transition[incoming][outgoing]++;return;}int bit=1<<c;if((used|blocked)&bit)fill(c+1,used,outgoing);else{if(c+1<w&&!((used|blocked)&(bit<<1)))fill(c+2,used|bit|(bit<<1),outgoing);fill(c+1,used|bit,outgoing|bit);}};fill(0,incoming,0);}block=multiply(block,transition);}Matrix answer(size,vector<int>(size));for(int i=0;i<size;i++)answer[i][i]=1;while(h){if(h&1)answer=multiply(answer,block);block=multiply(block,block);h>>=1;}cout<<answer[0][0]<<'\n';}'''
CPP['connected_story']=CPP['connected'].replace("if(!vanished||(!closed&&count_if(z.begin(),z.end(),[](int x){return x;})==0))","if(g[r][c]!='T'&&(!vanished||(!closed&&count_if(z.begin(),z.end(),[](int x){return x;})==0)))").replace("if(g[r][c]=='.'&&!closed)","if(g[r][c]!='#'&&!closed)")
CPP['steiner_story']=CPP['steiner'].replace("int n,m,k;cin>>n>>m>>k;","int n,m,k,queries;cin>>n>>m>>k>>queries;").replace("ll ans=*min_element(dp.back().begin(),dp.back().end());if(ans==INF)cout<<\"IMPOSSIBLE\\n\";else cout<<ans<<'\\n';","while(queries--){int mask;cin>>mask;ll ans=*min_element(dp[mask].begin(),dp[mask].end());if(ans==INF)cout<<\"IMPOSSIBLE\\n\";else cout<<ans<<'\\n';}")
CPP['treewidth_story']=CPP['treewidth'].replace("for(ll&x:w)cin>>x;","ll total=0;for(ll&x:w){cin>>x;total+=x;}").replace("cout<<dp.back()[0]","cout<<total-dp.back()[0]")

LESSONS={97:r'''---
title: "Section 97 — Digit And Broken-Profile DP"
format: pdf
geometry: margin=1.75cm
---

# Remember only the boundary between fixed and unknown choices

This lesson derives A--C. Problem D is editorial-only.

# A. Tight digit DP

Process digits from most significant to least. `tight` says whether the chosen prefix still equals the bound; if false, every remaining digit may range through nine. For a digit-sum target, the other state is the accumulated sum. The base case accepts exactly the target.

To answer `[L,R]`, compute `count(R)-count(L-1)`. Leading zeroes are harmless for digit sums and naturally make zero one fixed-length representation. The state boundary is the prefix summary: the future depends on its exact digits only through `tight` and the sum.

# B. Digit DP with an automaton

For a forbidden substring, compile the pattern with KMP failure links. The automaton state is the longest pattern prefix matching a suffix of the digits already emitted. A transition reaching the full pattern is rejected. Add `started` so padding zeroes are not mistaken for representation digits; handle the number zero explicitly at the base case.

This is a general product construction: digit-bound automaton times property automaton. The same method supports remainders, occurrence counts, and any finite-state language.

# C. Broken-profile tiling

Scan one row while a mask records cells already occupied from the previous row. At the first free cell, every valid tiling makes exactly one local choice: a horizontal domino if its neighbor is free, or a vertical domino that sets a bit in the next-row mask. Blocked cells behave as already occupied but may never overlap incoming bits.

Induction on the first unprocessed cell proves that the recursion enumerates every tiling exactly once. The important ordering fact is that after a cell leaves the profile, no future domino can touch it.

# Exercises

A--C build tight, automaton, and occupancy profiles. D transfers the row profile to local exclusion rather than covering.
''',98:r'''---
title: "Section 98 — Plug DP And Treewidth Frontiers"
format: pdf
geometry: margin=1.75cm
---

# A frontier may need connectivity, not just occupancy

This lesson derives A--C. Problem D is editorial-only.

# A. Transfer matrices for repeated profiles

The one-row domino transition is a matrix indexed by incoming and outgoing masks. Repeating an identical row `H` times is matrix exponentiation; the empty-to-empty entry is the answer. This separates local geometry from repetition and changes linear dependence on huge `H` into `O(log H)` matrix products.

# B. Canonical connectivity labels

For connected cell subsets, each nonzero frontier label names a currently open connected component. Selecting a cell creates a label or merges its left and upper labels. Skipping a cell may make a label disappear; if another component remains open, the vanished component can never reconnect and the state is invalid. If it is the last component, mark the solution closed and prohibit future selections.

Relabel components by first appearance after every transition: `(7,0,7,4)` becomes `(1,0,1,2)`. Labels are names, not information; canonicalization merges equivalent states.

# C. Steiner subset merging

Let `dp[mask][v]` be the minimum cost of a connected subgraph containing terminals in `mask` and ending at `v`. Combine two proper submasks at the same `v`, then run multi-source Dijkstra to move the meeting point through graph edges. Every Steiner tree can be split at a branching vertex, while every transition joins connected valid subgraphs.

# Boundary-design checklist

Ask which facts can still interact with unseen input. Occupancy needs bits; connectivity needs an equivalence relation; a bounded-width graph decomposition needs the choices on the active bag. Prove that forgotten objects have no edge or path to the future before dropping them.

# Exercises

A--C cover repeated, connected, and terminal-subset frontiers. D applies introduce/forget/join transitions on a supplied nice tree decomposition.
''',99:r'''---
title: "Section 99 — Master Frontier DP Mixed Contest"
format: pdf
geometry: margin=1.75cm
---

# Final contest contract

Six original problems cover the complete frontier-DP block.

| Problem | State boundary |
|---|---|
| A | tight prefix, digit sum, and remainder |
| B | tight prefix, digit sum, and KMP state |
| C | periodic obstacle-profile transfer matrix |
| D | canonical component labels with forced cells |
| E | reusable answers for every terminal subset |
| F | vertex-cover complement on a tree decomposition |

The final habit is explicit forgetting: state compression is correct only after proving that discarded information cannot affect any future transition.

# Exercises

A--F form the complete mixed contest.
'''}
NOTES={'digitsum':('Use a tight digit DP and range subtraction.','The state enumerates every bound-respecting prefix once, and the base accepts exactly the desired sum. Subtracting prefixes leaves precisely the interval.','`O(19 * S * 10)` per query.'),'digitpattern':('Take the product of digit-bound state and a KMP prefix automaton.','The KMP state exactly summarizes every suffix relevant to a future pattern occurrence; rejecting the terminal state is necessary and sufficient.','`O(19 * |P| * 10)` per query.'),'domino':('Scan the first uncovered cell under an incoming occupancy mask.','Every tiling covers that cell horizontally or vertically exactly once, and each legal transition preserves nonoverlap and complete coverage.','`O(n * 2^m * m)` up to transition constants.'),'gridset':('Enumerate horizontally valid row masks and reject overlap with blocked cells or the previous row.','These tests are exactly the horizontal and vertical adjacency constraints, so row induction is bijective.','`O(n * V^2)`, where `V` is the number of horizontally valid masks.'),'tower':('Build the one-row mask transition matrix and exponentiate it.','Matrix multiplication composes consecutive row transitions; binary exponentiation therefore represents exactly `H` rows.','`O(2^(3W) log H)` with dense matrices.'),'connected':('Store canonical labels for open frontier components and reject premature component disappearance.','Labels encode exactly future-connectable components. A vanished component cannot meet future cells; the closure rule is therefore necessary and sufficient for one final component.','Exponential in width and polynomial in height.'),'steiner':('Merge terminal submasks at a vertex, then relax locations with multi-source Dijkstra.','Every transition joins connected structures, and splitting an optimum at its last merge yields a represented transition.','`O(3^k n + 2^k m log n)`.'),'treewidth':('DP over selected active-bag vertices through leaf, introduce, forget, and join nodes.','Introduce checks all newly visible edges; forget is safe by decomposition connectivity; join combines independent subtrees and subtracts duplicated bag weights.','`O(t * 2^w * w)` expected map work.')}
NOTES.update({
'digitsum_story':('Take the product of tight digit DP with a digit-sum counter and a remainder automaton.','Decimal append updates the remainder exactly, so accepted paths are precisely the numbers satisfying both conditions.','`O(19 * S * M * 10)` per bound.'),
'digitpattern_story':('Combine the KMP automaton with a bounded digit-sum dimension.','KMP remembers exactly the suffix relevant to a future forbidden match, while the sum dimension is exact.','`O(19 * |P| * S * 10)` per query.'),
'tower_story':('Compose one matrix per obstacle row into a period matrix, then exponentiate it.','Row matrices enforce local obstacles; composition represents one period and exponentiation represents exactly `H` periods.','`O(P * 2^(3W) + 2^(3W) log H)` with dense matrices.'),
'connected_story':('Use connectivity labels, but prohibit skipping every `T` cell.','Every required cell is selected, and the disappearance rule accepts exactly selections ending in one component.','Exponential in `W` and polynomial in `H`.'),
'steiner_story':('Compute every terminal-mask Steiner row once and answer queries from those rows.','The subset-merge and shortest-path proof applies independently to every queried mask.','`O(3^k n + 2^k m log n + qn)`.'),
'treewidth_story':('A vertex cover is the complement of an independent set.','The complement covers every edge exactly when the chosen set contains no edge, so the answer is total weight minus maximum independent-set weight.','`O(t * 2^w * w)` expected map work.')})
NOTES['digitsum']=(
    'Precompute suffix counts by length and sum, then scan each tight prefix.',
    'Every smaller prefix digit is paired with all suffixes having the one required remaining sum; the bound itself is added exactly when its sum matches. Range subtraction leaves precisely the interval.',
    '`O(19 * 171 * 10)` preprocessing and `O(19 * 10)` per bound.',
)
NOTES['digitsum_story']=(
    'Group queries by modulus, precompute fixed-length suffix counts by sum and remainder, then scan tight prefixes.',
    'For each smaller prefix digit, the required suffix sum and remainder are uniquely determined; the table counts exactly those suffixes.',
    'For each distinct modulus `M`: `O(19 * 171 * M * 10)` preprocessing, then `O(19 * 10)` per bound.',
)
NOTES['treewidth']=(
    'DP over selected active-bag vertices through leaf, introduce, forget, and join nodes.',
    'Introduce checks all newly visible edges; forget is safe by decomposition connectivity; join combines independent subtrees and subtracts duplicated bag weights.',
    'Let `B = sum(2^|bag|)` over the supplied nodes. The reference uses `O(nB)` time and `O(B)` memory.',
)
NOTES['treewidth_story']=(
    'A vertex cover is the complement of an independent set.',
    'The complement covers every edge exactly when the chosen set contains no edge, so the answer is total weight minus maximum independent-set weight.',
    'Let `B = sum(2^|bag|)` over the supplied nodes. The reference uses `O(nB)` time and `O(B)` memory.',
)
SAMPLES={'digitsum':('2\n0 20 2\n10 15 6\n','3\n1\n'),'digitpattern':('2\n20 1\n105 05\n','10\n105\n'),'domino':('2 3\n...\n...\n','3\n'),'gridset':('2 2\n..\n..\n','7\n'),'tower':('3 2\n','3\n'),'connected':('1 3\n...\n','6\n'),'steiner':('4 4 3\n1 2 1\n2 3 1\n3 4 1\n1 4 10\n1 3 4\n','3\n'),'treewidth':('2 1\n5 7\n1 2\n5\nL\nI 1 1\nI 2 2\nF 3 1\nF 4 2\n','7\n')}
SAMPLES.update({'digitsum_story':('2\n0 30 3 3\n10 20 2 2\n','4\n1\n'),'digitpattern_story':('2\n20 1 2\n30 9 3\n','2\n4\n'),'tower_story':('2 1 2\n..\n','2\n'),'connected_story':('1 3\nT.T\n','1\n'),'steiner_story':('4 4 3 2\n1 2 1\n2 3 1\n3 4 1\n1 4 10\n1 3 4\n3\n7\n','2\n3\n'),'treewidth_story':('2 1\n5 7\n1 2\n5\nL\nI 1 1\nI 2 2\nF 3 1\nF 4 2\n','5\n')})

def editorial(section):
 out=[f'---\ntitle: "Section {section} Editorial — {SECTIONS[section][1]}"\nformat:\n  pdf:\n    code-overflow: wrap\ngeometry: margin=1.6cm\nfontsize: 9pt\n---\n']
 for i,(slug,title,kind) in enumerate(PROBLEMS[section]):
  idea,proof,complexity=NOTES[kind];out.append(f'''# {chr(65+i)}. {title}\n\n## How to find it\n\n{idea}\n\n## Correctness\n\n{proof}\n\n## Complexity\n\n{complexity}\n\n## C++\n\n```cpp\n{{{{< include problems/{slug}/solution.cpp >}}}}\n```\n\n## Python\n\n```python\n{{{{< include problems/{slug}/solution.py >}}}}\n```\n''')
 return '\n'.join(out)

def fmt_py(s):return ast.unparse(ast.parse(s))+'\n'
def fmt_cpp(source):
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
   links.append(f'- [{name}](problems/{slug}/README.md)');checks.append(f'- [ ] [{name}](problems/{slug}/README.md)');p=base/'problems'/slug;p.mkdir(parents=True,exist_ok=True);tests=p/'tests';tests.mkdir(exist_ok=True);(p/'README.md').write_text(f'# {name}\n\n{STATEMENTS[kind]}\n');(p/'solve.cpp').write_text(CPP_STUB);(p/'solve.py').write_text(PY_STUB);(p/'solution.cpp').write_text(fmt_cpp(CPP[kind]));(p/'solution.py').write_text(fmt_py(PY[kind]));(p/'manifest.json').write_text(json.dumps({'title':name,'checker':'tokens','time_limit_seconds':15})+'\n');x,y=SAMPLES[kind];(tests/'sample1.in').write_text(x);(tests/'sample1.out').write_text(y);(tests/'random_cases.py').write_text(f'''import subprocess,sys\nfrom pathlib import Path\nROOT=Path(__file__).resolve().parents[5]\nraise SystemExit(subprocess.call([sys.executable,str(ROOT/"tools"/"frontier_dp_random.py"),"{kind}",*sys.argv[1:]]))\n''')
  note='The lesson derives A--C; D is editorial-only.' if section<99 else 'Exactly six new problems form the mixed contest.';(base/'README.md').write_text(f'# Section {section}: {title}\n\n{note}\n\n## Problems\n\n'+'\n'.join(links)+'\n');(base/'PRACTICE.md').write_text(f'# Section {section} Practice\n\n'+'\n'.join(checks)+'\n');names=',\n        '.join(repr(x[0]) for x in PROBLEMS[section]);(base/'check.py').write_text(f'''from pathlib import Path\nimport sys\nROOT=Path(__file__).resolve().parents[2]\nsys.path.insert(0,str(ROOT))\nfrom tools.section_checker import run_section_checks\nSECTION=Path(__file__).resolve().parent\nPROBLEMS=[SECTION/"problems"/x for x in (\n        {names},\n)]\nif __name__=="__main__":raise SystemExit(run_section_checks({section},PROBLEMS,ROOT))\n''')
if __name__=='__main__':generate()
