import sys
INF=10**30
def main():
 d=list(map(int,sys.stdin.buffer.read().split()));
 if not d:return
 q=d[0];i=1;ops=[];xs=[]
 for _ in range(q):
  t=d[i];a=d[i+1];i+=2
  if t==1:b=d[i];i+=1;ops.append((t,a,b))
  else:ops.append((t,a,0));xs.append(a)
 xs=sorted(set(xs));where={x:i for i,x in enumerate(xs)};tree=[None]*(4*len(xs))
 def val(line,x):return (line[0]*x+line[1],line[2]) if line else (INF,10**9)
 def add(line,p,l,r):
  if tree[p] is None:tree[p]=line;return
  m=(l+r)//2
  if val(line,xs[m])<val(tree[p],xs[m]):tree[p],line=line,tree[p]
  if l==r:return
  if val(line,xs[l])<val(tree[p],xs[l]):add(line,p*2,l,m)
  elif val(line,xs[r])<val(tree[p],xs[r]):add(line,p*2+1,m+1,r)
 def get(p,l,r,k):
  ans=val(tree[p],xs[k]);
  if l==r:return ans
  m=(l+r)//2;return min(ans,get(p*2,l,m,k) if k<=m else get(p*2+1,m+1,r,k))
 out=[];id=0
 for t,a,b in ops:
  if t==1:id+=1;add((a,b,id),1,0,len(xs)-1)
  else:out.append('%d %d'%get(1,0,len(xs)-1,where[a]))
 print('\n'.join(out))
if __name__=='__main__':main()
