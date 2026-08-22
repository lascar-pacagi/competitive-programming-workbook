import sys
def main():
 d=sys.stdin.buffer.read().split();s=d[0];ln=[0];link=[-1];to=[{}];last=0
 for c in s:
  u=len(ln);ln.append(ln[last]+1);link.append(0);to.append({});p=last
  while p>=0 and c not in to[p]:to[p][c]=u;p=link[p]
  if p<0:link[u]=0
  else:
   q=to[p][c]
   if ln[p]+1==ln[q]:link[u]=q
   else:
    z=len(ln);ln.append(ln[p]+1);link.append(link[q]);to.append(to[q].copy())
    while p>=0 and to[p].get(c)==q:to[p][c]=z;p=link[p]
    link[q]=link[u]=z
  last=u
 cnt=[1]*len(ln);CAP=4*10**18
 for v in sorted(range(len(ln)),key=ln.__getitem__,reverse=True):cnt[v]=min(CAP,1+sum(cnt[u] for u in to[v].values()))
 out=[]
 for x in d[2:]:
  k=int(x)
  if k>=cnt[0]:out.append('-1');continue
  v=0;z=[]
  while k:
   for c,u in sorted(to[v].items()):
    if k>cnt[u]:k-=cnt[u]
    else:z.append(chr(c));k-=1;v=u;break
  out.append(''.join(z))
 print('\n'.join(out))
if __name__=='__main__':main()
