import sys
def main():
 d=sys.stdin.buffer.read().split();s=d[0];n=len(s);sa=list(range(n));rank=list(s);k=1
 while True:
  sa.sort(key=lambda i:(rank[i],rank[i+k] if i+k<n else -1));nr=[0]*n
  for j in range(1,n):nr[sa[j]]=nr[sa[j-1]]+((rank[sa[j-1]],rank[sa[j-1]+k] if sa[j-1]+k<n else -1)<(rank[sa[j]],rank[sa[j]+k] if sa[j]+k<n else -1))
  rank=nr
  if rank[sa[-1]]==n-1:break
  k*=2
 h=[0]*n;k=0
 for i in range(n):
  x=rank[i]
  if x:
   j=sa[x-1]
   while i+k<n and j+k<n and s[i+k]==s[j+k]:k+=1
   h[x]=k;k=max(0,k-1)
 size=1
 while size<n:size*=2
 seg=[n*2]*(2*size);seg[size:size+n]=h
 for i in range(size-1,0,-1):seg[i]=min(seg[i*2],seg[i*2+1])
 def lcp(a,b):
  if a==b:return n-sa[a]
  if a>b:a,b=b,a
  a+=1;v=n*2;a+=size;b+=size+1
  while a<b:
   if a&1:v=min(v,seg[a]);a+=1
   if b&1:b-=1;v=min(v,seg[b])
   a//=2;b//=2
  return v
 levels=max(1,(n-1).bit_length());prefs=[];zeros=[];cur=rank
 for bit in range(levels-1,-1,-1):
  pref=[0];z=[];o=[]
  for x in cur:
   iszero=not (x>>bit&1);pref.append(pref[-1]+iszero);(z if iszero else o).append(x)
  prefs.append(pref);zeros.append(len(z));cur=z+o
 def kth(l,r,k):
  value=0
  for lev,bit in enumerate(range(levels-1,-1,-1)):
   p=prefs[lev];zl=p[l];zr=p[r];cnt=zr-zl
   if k<=cnt:l=zl;r=zr
   else:k-=cnt;value|=1<<bit;l=zeros[lev]+l-zl;r=zeros[lev]+r-zr
  return value
 q=int(d[1]);out=[];at=2
 for _ in range(q):
  l=int(d[at])-1;r=int(d[at+1]);k=int(d[at+2]);at+=3;a=kth(l,r,k);v=0 if k==r-l else lcp(a,kth(l,r,k+1));out.append(f'{sa[a]+1} {v}')
 print('\n'.join(out))
if __name__=='__main__':main()
