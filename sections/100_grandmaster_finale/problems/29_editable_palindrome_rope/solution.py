import sys,random
sys.setrecursionlimit(1000000);M1=1000000007;M2=1000000009;B=911382323
def main():
 d=sys.stdin.buffer.read().split();s=d[0];n=len(s);q=int(d[1]);pw1=[1]*(n+2);pw2=[1]*(n+2)
 for i in range(1,n+2):pw1[i]=pw1[i-1]*B%M1;pw2[i]=pw2[i-1]*B%M2
 L=[0];R=[0];P=[0];V=[0];Z=[0];F1=[0];F2=[0];G1=[0];G2=[0];REV=[0];rng=random.Random(712367)
 def node(v):L.append(0);R.append(0);P.append(rng.randrange(1<<30));V.append(v);Z.append(1);F1.append(v);F2.append(v);G1.append(v);G2.append(v);REV.append(0);return len(L)-1
 def rv(x):
  if x:L[x],R[x]=R[x],L[x];F1[x],G1[x]=G1[x],F1[x];F2[x],G2[x]=G2[x],F2[x];REV[x]^=1
 def push(x):
  if REV[x]:rv(L[x]);rv(R[x]);REV[x]=0
 def pull(x):
  l=L[x];r=R[x];Z[x]=Z[l]+Z[r]+1;F1[x]=(F1[l]*pw1[Z[r]+1]+V[x]*pw1[Z[r]]+F1[r])%M1;F2[x]=(F2[l]*pw2[Z[r]+1]+V[x]*pw2[Z[r]]+F2[r])%M2;G1[x]=(G1[r]*pw1[Z[l]+1]+V[x]*pw1[Z[l]]+G1[l])%M1;G2[x]=(G2[r]*pw2[Z[l]+1]+V[x]*pw2[Z[l]]+G2[l])%M2
 def split(x,k):
  if not x:return 0,0
  push(x)
  if Z[L[x]]>=k:a,L[x]=split(L[x],k);pull(x);return a,x
  R[x],b=split(R[x],k-Z[L[x]]-1);pull(x);return x,b
 def merge(a,b):
  if not a or not b:return a or b
  if P[a]<P[b]:push(a);R[a]=merge(R[a],b);pull(a);return a
  push(b);L[b]=merge(a,L[b]);pull(b);return b
 root=0
 for c in s:root=merge(root,node(c-96))
 out=[];at=2
 for _ in range(q):
  o=d[at];l=int(d[at+1]);at+=2;a,b=split(root,l-1)
  if o==b'SET':x,b=split(b,1);V[x]=d[at][0]-96;at+=1;pull(x)
  else:
   r=int(d[at]);at+=1;x,b=split(b,r-l+1)
   if o==b'REV':rv(x)
   else:out.append('YES' if F1[x]==G1[x] and F2[x]==G2[x] else 'NO')
  root=merge(a,merge(x,b))
 print('\n'.join(out))
if __name__=='__main__':main()
