import sys
INF=10**80
def run(xs,lam,prefer_max):
 n=len(xs)-1; tree=[None]*(4*(n+1))
 def better(a,b,x):
  if b is None:return True
  va=a[0]*x+a[1];vb=b[0]*x+b[1]
  return va<vb or (va==vb and ((a[2]>b[2]) if prefer_max else (a[2]<b[2])))
 def add(line,p=1,l=0,r=n):
  mid=(l+r)//2
  if tree[p] is None:tree[p]=line;return
  left=better(line,tree[p],xs[l]);middle=better(line,tree[p],xs[mid])
  if middle:tree[p],line=line,tree[p]
  if l==r:return
  if left!=middle:add(line,p*2,l,mid)
  elif better(line,tree[p],xs[r])!=better(line,tree[p],xs[mid]):add(line,p*2+1,mid+1,r)
 def query(idx,p=1,l=0,r=n):
  line=tree[p];best=line
  if l==r:return best
  mid=(l+r)//2;child=p*2 if idx<=mid else p*2+1
  if tree[child] is None:return best
  other=query(idx,child,l,mid) if idx<=mid else query(idx,child,mid+1,r)
  return other if better(other,best,xs[idx]) else best
 add((0,0,0)); val=cnt=0
 for i in range(1,n+1):
  z=query(i);val=z[0]*xs[i]+z[1]+xs[i]*xs[i]+lam;cnt=z[2]+1;add((-2*xs[i],val+xs[i]*xs[i],cnt))
 return val,cnt
def main():
 d=list(map(int,sys.stdin.buffer.read().split()));n,k=d[:2];xs=[0]
 for a in d[2:]:xs.append(xs[-1]+a)
 if k==1:print(xs[-1]*xs[-1]);return
 if k==n:print(sum(a*a for a in d[2:]));return
 B=xs[-1]*xs[-1]+1;lo=-B;hi=B
 while lo<hi:
  mid=(lo+hi+1)//2
  if run(xs,mid,True)[1]>=k:lo=mid
  else:hi=mid-1
 value,maxc=run(xs,lo,True);_,minc=run(xs,lo,False)
 if not minc<=k<=maxc:raise RuntimeError("convexity invariant failed")
 print(value-lo*k)
if __name__=="__main__":main()
