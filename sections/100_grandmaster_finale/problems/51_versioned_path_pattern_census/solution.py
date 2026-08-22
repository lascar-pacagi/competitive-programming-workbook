import sys,collections
def main():
 d=sys.stdin.buffer.read().split();n=int(d[0]);q=int(d[1]);to=[{}];fail=[0];ends=[];at=2
 for s in d[at:at+n]:
  v=0
  for c in s:
   if c not in to[v]:to[v][c]=len(to);to.append({});fail.append(0)
   v=to[v][c]
  ends.append(v)
 at+=n;qq=collections.deque(to[0].values());order=[0]
 while qq:
  v=qq.popleft();order.append(v)
  for c,u in to[v].items():
   f=fail[v]
   while f and c not in to[f]:f=fail[f]
   fail[u]=to[f].get(c,0);qq.append(u)
 child=[[] for _ in to]
 for v in range(1,len(to)):child[fail[v]].append(v)
 tin=[0]*len(to);tout=[0]*len(to);tm=0;st=[(0,0)]
 while st:
  v,i=st[-1]
  if i==0:tm+=1;tin[v]=tm
  if i<len(child[v]):st[-1]=(v,i+1);st.append((child[v][i],0))
  else:tout[v]=tm;st.pop()
 bit=[0]*(len(to)+2)
 def add(x,z):
  while x<len(bit):bit[x]+=z;x+=x&-x
 def get(x):
  z=0
  while x:z+=bit[x];x-=x&-x
  return z
 out=[]
 for _ in range(q):
  op=d[at];x=d[at+1];at+=2
  if op==b'?':
   v=0;ans=0
   for c in x:
    while v and c not in to[v]:v=fail[v]
    v=to[v].get(c,0);ans+=get(tin[v])
   out.append(str(ans))
  else:v=ends[int(x)-1];z=1 if op==b'+' else -1;add(tin[v],z);add(tout[v]+1,-z)
 print('\n'.join(out))
if __name__=='__main__':main()
