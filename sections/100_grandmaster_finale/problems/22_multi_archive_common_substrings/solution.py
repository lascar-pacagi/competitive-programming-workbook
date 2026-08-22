import sys
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
