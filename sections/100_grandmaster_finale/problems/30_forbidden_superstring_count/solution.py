import sys,collections
M=998244353
def mul(a,b):
 n=len(a);c=[[0]*n for _ in range(n)]
 for i in range(n):
  for k,x in enumerate(a[i]):
   if x:
    for j,y in enumerate(b[k]):
     if y:c[i][j]=(c[i][j]+x*y)%M
 return c
def main():
 d=sys.stdin.buffer.read().split();R=int(d[0]);F=int(d[1]);L=int(d[2]);p=d[3:3+R+F];to=[{}];fail=[0];mask=[0];bad=[0]
 for i,s in enumerate(p):
  v=0
  for c in s:
   if c not in to[v]:to[v][c]=len(to);to.append({});fail.append(0);mask.append(0);bad.append(0)
   v=to[v][c]
  if i<R:mask[v]|=1<<i
  else:bad[v]=1
 q=collections.deque()
 for c in b'abc':
  if c in to[0]:q.append(to[0][c])
  else:to[0][c]=0
 while q:
  v=q.popleft();mask[v]|=mask[fail[v]];bad[v]|=bad[fail[v]]
  for c in b'abc':
   if c in to[v]:fail[to[v][c]]=to[fail[v]][c];q.append(to[v][c])
   else:to[v][c]=to[fail[v]][c]
 ans=0;n=len(to)
 for ban in range(1<<R):
  ok=[not bad[i] and not(mask[i]&ban) for i in range(n)];a=[[0]*n for _ in range(n)]
  for i in range(n):
   if ok[i]:
    for c in b'abc':
     j=to[i][c]
     if ok[j]:a[i][j]+=1
  v=[[0]*n for _ in range(n)]
  for i in range(n):v[i][i]=1
  e=L
  while e:
   if e&1:v=mul(v,a)
   a=mul(a,a);e//=2
  z=sum(v[0])%M;ans+=( -z if ban.bit_count()&1 else z)
 print(ans%M)
if __name__=='__main__':main()
