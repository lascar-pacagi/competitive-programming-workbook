import sys
def main():
 s=sys.stdin.buffer.readline().strip();n=len(s);sa=list(range(n));r=list(s);k=1
 while True:
  sa.sort(key=lambda i:(r[i],r[i+k] if i+k<n else -1));z=[0]*n
  for i in range(1,n):z[sa[i]]=z[sa[i-1]]+((r[sa[i-1]],r[sa[i-1]+k] if sa[i-1]+k<n else -1)<(r[sa[i]],r[sa[i]+k] if sa[i]+k<n else -1))
  r=z
  if r[sa[-1]]==n-1:break
  k*=2
 e=[];k=0
 for i in range(n):
  x=r[i]
  if x:
   j=sa[x-1]
   while i+k<n and j+k<n and s[i+k]==s[j+k]:k+=1
   e.append((k,x-1,x));k=max(0,k-1)
 p=list(range(n));sz=[1]*n
 def f(x):
  while p[x]!=x:p[x]=p[p[x]];x=p[x]
  return x
 ans=0
 for w,x,y in sorted(e,reverse=True):x=f(x);y=f(y);ans+=w*sz[x]*sz[y];p[y]=x;sz[x]+=sz[y]
 print(ans)
if __name__=='__main__':main()
