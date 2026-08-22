import sys
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
