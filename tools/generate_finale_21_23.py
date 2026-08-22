"""Generate Section 100 problems 21--23."""
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'sections/100_grandmaster_finale/problems'
STUB_CPP='''#include <bits/stdc++.h>\nusing namespace std;\nint main(){ios::sync_with_stdio(false);cin.tie(nullptr);/* TODO */}\n'''
STUB_PY='''def main():\n    pass  # TODO\nif __name__ == "__main__": main()\n'''

R21=r'''# Persistent Text Occurrences

For every query pattern `p` and positive integer `k`, print the starting
position of the `k`-th occurrence of `p` in text `s`, ordered by position.
Print `-1` if fewer than `k` occurrences exist. Occurrences may overlap.

## Input
```text
s
q
q lines: p k
```
`s` and every `p` contain lowercase English letters. `1 <= |s|,q <= 100000`,
and the total pattern length is at most `200000`.

## Output
One answer per query. Positions are one-based.

## Sample input
```text
banana
4
ana 1
ana 2
na 2
apple 1
```
## Sample output
```text
2
4
5
-1
```
'''
CPP21=r'''#include <bits/stdc++.h>
using namespace std;struct N{int l=0,r=0,z=0;};
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);string s;if(!(cin>>s))return 0;int n=s.size();vector<int>sa(n),rk(n),t(n);iota(sa.begin(),sa.end(),0);for(int i=0;i<n;i++)rk[i]=s[i];for(int k=1;;k*=2){sort(sa.begin(),sa.end(),[&](int a,int b){return pair(rk[a],a+k<n?rk[a+k]:-1)<pair(rk[b],b+k<n?rk[b+k]:-1);});t[sa[0]]=0;for(int i=1;i<n;i++)t[sa[i]]=t[sa[i-1]]+(pair(rk[sa[i-1]],sa[i-1]+k<n?rk[sa[i-1]+k]:-1)<pair(rk[sa[i]],sa[i]+k<n?rk[sa[i]+k]:-1));rk=t;if(rk[sa.back()]==n-1)break;}
 vector<N>tr(1);function<int(int,int,int,int)>add=[&](int old,int l,int r,int x){int u=tr.size();tr.push_back(tr[old]);tr[u].z++;if(l<r){int m=(l+r)/2;if(x<=m)tr[u].l=add(tr[old].l,l,m,x);else tr[u].r=add(tr[old].r,m+1,r,x);}return u;};vector<int>root(n+1);for(int i=0;i<n;i++)root[i+1]=add(root[i],0,n-1,sa[i]);
 function<int(int,int,int,int,int)>kth=[&](int a,int b,int l,int r,int k){if(l==r)return l;int z=tr[tr[b].l].z-tr[tr[a].l].z,m=(l+r)/2;return k<=z?kth(tr[a].l,tr[b].l,l,m,k):kth(tr[a].r,tr[b].r,m+1,r,k-z);};
 auto cmp=[&](int pos,const string&p){int z=s.compare(pos,p.size(),p);return z<0?-1:z>0?1:0;};int q;cin>>q;while(q--){string p;int k;cin>>p>>k;int lo=0,hi=n;while(lo<hi){int m=(lo+hi)/2;if(cmp(sa[m],p)<0)lo=m+1;else hi=m;}int L=lo;lo=0;hi=n;while(lo<hi){int m=(lo+hi)/2;if(cmp(sa[m],p)<=0)lo=m+1;else hi=m;}int R=lo;if(R-L<k)cout<<-1<<'\n';else cout<<kth(root[L],root[R],0,n-1,k)+1<<'\n';}}
'''
PY21=r'''import sys
def main():
 d=sys.stdin.buffer.read().split();s=d[0];n=len(s);q=int(d[1]);sa=list(range(n));r=list(s);k=1
 while True:
  sa.sort(key=lambda i:(r[i],r[i+k] if i+k<n else -1));nr=[0]*n
  for j in range(1,n):nr[sa[j]]=nr[sa[j-1]]+((r[sa[j-1]],r[sa[j-1]+k] if sa[j-1]+k<n else -1)<(r[sa[j]],r[sa[j]+k] if sa[j]+k<n else -1))
  r=nr
  if r[sa[-1]]==n-1:break
  k*=2
 left=[0];right=[0];cnt=[0];roots=[0]
 def add(old,l,h,x):
  u=len(cnt);left.append(left[old]);right.append(right[old]);cnt.append(cnt[old]+1)
  if l<h:
   m=(l+h)//2
   if x<=m:left[u]=add(left[old],l,m,x)
   else:right[u]=add(right[old],m+1,h,x)
  return u
 for x in sa:roots.append(add(roots[-1],0,n-1,x))
 def kth(a,b,l,h,z):
  while l<h:
   m=(l+h)//2;c=cnt[left[b]]-cnt[left[a]]
   if z<=c:a,b,h=left[a],left[b],m
   else:a,b,l,z=right[a],right[b],m+1,z-c
  return l
 out=[];at=2
 for _ in range(q):
  p=d[at];z=int(d[at+1]);at+=2;lo=0;hi=n
  while lo<hi:
   m=(lo+hi)//2
   if s[sa[m]:sa[m]+len(p)]<p:lo=m+1
   else:hi=m
  L=lo;lo=0;hi=n
  while lo<hi:
   m=(lo+hi)//2
   if s[sa[m]:sa[m]+len(p)]<=p:lo=m+1
   else:hi=m
  out.append(str(kth(roots[L],roots[lo],0,n-1,z)+1) if lo-L>=z else '-1')
 print('\n'.join(out))
if __name__=='__main__':main()
'''
RAND21=r'''import argparse,random
from pathlib import Path
def case(r):
 n=r.randint(1,22);s=''.join(r.choice('abc') for _ in range(n));q=r.randint(1,25);qs=[];ans=[]
 for _ in range(q):
  p=''.join(r.choice('abc') for _ in range(r.randint(1,6)));k=r.randint(1,8);a=[i+1 for i in range(n-len(p)+1) if s[i:i+len(p)]==p];qs.append((p,k));ans.append(str(a[k-1] if len(a)>=k else -1))
 return s+'\n'+str(q)+'\n'+''.join(f'{p} {k}\n' for p,k in qs),'\n'.join(ans)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--count',type=int,default=25);p.add_argument('--seed',type=int,default=1);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);r=random.Random(a.seed)
 for i in range(a.count):x,y=case(r);z=a.out_dir/f'case{i:03d}';z.with_suffix('.in').write_text(x);z.with_suffix('.out').write_text(y)
if __name__=='__main__':main()
'''

R22=r'''# Multi-Archive Common Substrings

Given `k` nonempty lowercase strings, determine:

1. the length of their longest common substring;
2. the number of **distinct** nonempty strings that occur as substrings of
   every archive.

## Input
```text
k
s[1]
...
s[k]
```
`1 <= k <= 20`; total input length is at most `200000`.

## Output
Print `longest count`.

## Sample input
```text
3
ababa
babab
caba
```
## Sample output
```text
3 5
```
'''
CPP22=r'''#include <bits/stdc++.h>
using namespace std;struct S{int link=-1,len=0;array<int,26>to{};S(){to.fill(-1);}};int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int k;if(!(cin>>k))return 0;string a;cin>>a;vector<S>st(1);int last=0;for(char cc:a){int c=cc-'a',cur=st.size();st.push_back(S());st[cur].len=st[last].len+1;int p=last;while(p>=0&&st[p].to[c]<0)st[p].to[c]=cur,p=st[p].link;if(p<0)st[cur].link=0;else{int q=st[p].to[c];if(st[p].len+1==st[q].len)st[cur].link=q;else{int z=st.size();st.push_back(st[q]);st[z].len=st[p].len+1;while(p>=0&&st[p].to[c]==q)st[p].to[c]=z,p=st[p].link;st[q].link=st[cur].link=z;}}last=cur;}int n=st.size();vector<int>ord(n);iota(ord.begin(),ord.end(),0);sort(ord.begin(),ord.end(),[&](int x,int y){return st[x].len<st[y].len;});vector<int>common(n);for(int i=0;i<n;i++)common[i]=st[i].len;for(int z=1;z<k;z++){string s;cin>>s;vector<int>best(n);int v=0,l=0;for(char cc:s){int c=cc-'a';while(v&&st[v].to[c]<0)v=st[v].link,l=min(l,st[v].len);if(st[v].to[c]>=0)v=st[v].to[c],l++;else v=l=0;best[v]=max(best[v],l);}for(int ii=n-1;ii>0;ii--){int x=ord[ii],p=st[x].link;best[p]=max(best[p],min(best[x],st[p].len));}for(int i=1;i<n;i++)common[i]=min(common[i],best[i]);}long long cnt=0;int longest=0;for(int i=1;i<n;i++)cnt+=max(0,common[i]-st[st[i].link].len),longest=max(longest,common[i]);cout<<longest<<' '<<cnt<<'\n';}
'''
PY22=r'''import sys
def main():
 d=sys.stdin.buffer.read().split();k=int(d[0]);text=d[1];link=[-1];ln=[0];to=[{}];last=0
 for c in text:
  cur=len(link);link.append(0);ln.append(ln[last]+1);to.append({});p=last
  while p>=0 and c not in to[p]:to[p][c]=cur;p=link[p]
  if p<0:link[cur]=0
  else:
   q=to[p][c]
   if ln[p]+1==ln[q]:link[cur]=q
   else:
    z=len(link);link.append(link[q]);ln.append(ln[p]+1);to.append(to[q].copy())
    while p>=0 and to[p].get(c)==q:to[p][c]=z;p=link[p]
    link[q]=link[cur]=z
  last=cur
 order=sorted(range(len(link)),key=ln.__getitem__);common=ln.copy()
 for s in d[2:]:
  best=[0]*len(link);v=l=0
  for c in s:
   while v and c not in to[v]:v=link[v];l=min(l,ln[v])
   if c in to[v]:v=to[v][c];l+=1
   else:v=l=0
   best[v]=max(best[v],l)
  for x in reversed(order[1:]):p=link[x];best[p]=max(best[p],min(best[x],ln[p]))
  for i in range(1,len(link)):common[i]=min(common[i],best[i])
 vals=[max(0,common[i]-ln[link[i]]) for i in range(1,len(link))];print(max(common),sum(vals))
if __name__=='__main__':main()
'''
RAND22=r'''import argparse,random
from pathlib import Path
def case(r):
 k=r.randint(1,5);ss=[''.join(r.choice('abc') for _ in range(r.randint(1,9))) for _ in range(k)];sets=[]
 for s in ss:sets.append({s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1)})
 z=set.intersection(*sets);return str(k)+'\n'+'\n'.join(ss)+'\n',f'{max(map(len,z),default=0)} {len(z)}\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--count',type=int,default=25);p.add_argument('--seed',type=int,default=1);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);r=random.Random(a.seed)
 for i in range(a.count):x,y=case(r);z=a.out_dir/f'case{i:03d}';z.with_suffix('.in').write_text(x);z.with_suffix('.out').write_text(y)
if __name__=='__main__':main()
'''

R23=r'''# Palindromic Range Census

Every distinct palindromic substring of `s` has one **discovery interval**:
its leftmost occurrence `[start,end]`. For each query `[l,r]`, count discovery
intervals wholly contained in `[l,r]`.

## Input
```text
s
q
q lines: l r
```
`s` is lowercase; `1 <= |s|,q <= 200000`.

## Output
One count per query.

## Sample input
```text
ababa
3
1 5
2 5
3 4
```
## Sample output
```text
5
2
0
```
'''
CPP23=r'''#include <bits/stdc++.h>
using namespace std;struct N{int len,link,end;array<int,26>to{};N(int l=0):len(l),link(0),end(0){to.fill(0);}};int main(){ios::sync_with_stdio(false);cin.tie(nullptr);string s;if(!(cin>>s))return 0;vector<N>t={N(-1),N(0)};t[0].link=0;t[1].link=0;int last=1;vector<vector<int>>at(s.size()+1);for(int i=0;i<(int)s.size();i++){int c=s[i]-'a',p=last;while(i-1-t[p].len<0||s[i-1-t[p].len]!=s[i])p=t[p].link;if(!t[p].to[c]){int u=t.size();t.push_back(N(t[p].len+2));t[u].end=i+1;if(t[u].len==1)t[u].link=1;else{int q=t[p].link;while(i-1-t[q].len<0||s[i-1-t[q].len]!=s[i])q=t[q].link;t[u].link=t[q].to[c];}t[p].to[c]=u;at[i+1].push_back(i+2-t[u].len);}last=t[p].to[c];}int q;cin>>q;vector<vector<pair<int,int>>>qs(s.size()+1);for(int i=0,l,r;i<q;i++){cin>>l>>r;qs[r].push_back({l,i});}vector<int>bit(s.size()+1),ans(q);auto add=[&](int x){for(;x<(int)bit.size();x+=x&-x)bit[x]++;};auto sum=[&](int x){int z=0;for(;x;x-=x&-x)z+=bit[x];return z;};int total=0;for(int r=1;r<=(int)s.size();r++){for(int x:at[r])add(x),total++;for(auto [l,id]:qs[r])ans[id]=total-sum(l-1);}for(int x:ans)cout<<x<<'\n';}
'''
PY23=r'''import sys
def main():
 d=sys.stdin.buffer.read().split();s=d[0];n=len(s);ln=[-1,0];link=[0,0];to=[{},{}];last=1;events=[[] for _ in range(n+1)]
 for i,c in enumerate(s):
  p=last
  while i-1-ln[p]<0 or s[i-1-ln[p]]!=c:p=link[p]
  if c not in to[p]:
   u=len(ln);ln.append(ln[p]+2);link.append(1);to.append({})
   if ln[u]>1:
    q=link[p]
    while i-1-ln[q]<0 or s[i-1-ln[q]]!=c:q=link[q]
    link[u]=to[q][c]
   to[p][c]=u;events[i+1].append(i+2-ln[u])
  last=to[p][c]
 q=int(d[1]);queries=[[] for _ in range(n+1)];at=2
 for z in range(q):l=int(d[at]);r=int(d[at+1]);at+=2;queries[r].append((l,z))
 bit=[0]*(n+1);ans=[0]*q;total=0
 for r in range(1,n+1):
  for x in events[r]:
   total+=1;y=x
   while y<=n:bit[y]+=1;y+=y&-y
  for l,z in queries[r]:
   y=l-1;v=0
   while y:v+=bit[y];y-=y&-y
   ans[z]=total-v
 print('\n'.join(map(str,ans)))
if __name__=='__main__':main()
'''
RAND23=r'''import argparse,random
from pathlib import Path
def case(r):
 n=r.randint(1,18);s=''.join(r.choice('abc') for _ in range(n));seen=set();iv=[]
 for e in range(n):
  for st in range(e+1):
   x=s[st:e+1]
   if x==x[::-1] and x not in seen:seen.add(x);iv.append((st+1,e+1))
 q=r.randint(1,25);qs=[];ans=[]
 for _ in range(q):l=r.randint(1,n);h=r.randint(l,n);qs.append((l,h));ans.append(str(sum(l<=a and b<=h for a,b in iv)))
 return s+'\n'+str(q)+'\n'+''.join(f'{l} {h}\n' for l,h in qs),'\n'.join(ans)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--count',type=int,default=25);p.add_argument('--seed',type=int,default=1);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);r=random.Random(a.seed)
 for i in range(a.count):x,y=case(r);z=a.out_dir/f'case{i:03d}';z.with_suffix('.in').write_text(x);z.with_suffix('.out').write_text(y)
if __name__=='__main__':main()
'''

P={
'21_persistent_text_occurrences':('Persistent Text Occurrences',R21,CPP21,PY21,RAND21,'banana\n4\nana 1\nana 2\nna 2\napple 1\n','2\n4\n5\n-1\n'),
'22_multi_archive_common_substrings':('Multi-Archive Common Substrings',R22,CPP22,PY22,RAND22,'3\nababa\nbabab\ncaba\n','3 5\n'),
'23_palindromic_range_census':('Palindromic Range Census',R23,CPP23,PY23,RAND23,'ababa\n3\n1 5\n2 5\n3 4\n','5\n2\n0\n')}
def main():
 for slug,(title,readme,cpp,py,rand,si,so) in P.items():
  d=BASE/slug;t=d/'tests';t.mkdir(parents=True,exist_ok=True)
  (d/'README.md').write_text(readme);(d/'manifest.json').write_text(f'{{"title":"{title}","checker":"tokens","time_limit_seconds":20}}\n');(d/'solution.cpp').write_text(cpp);(d/'solution.py').write_text(py);(d/'solve.cpp').write_text(STUB_CPP);(d/'solve.py').write_text(STUB_PY);(t/'sample1.in').write_text(si);(t/'sample1.out').write_text(so);(t/'random_cases.py').write_text(rand)
if __name__=='__main__':main()
