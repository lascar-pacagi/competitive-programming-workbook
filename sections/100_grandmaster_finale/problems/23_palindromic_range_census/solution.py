import sys
def main():
 d=sys.stdin.buffer.read().split();s=d[0];n=len(s);ln=[-1,0];link=[0,0];to=[{},{}];last=1;events=[[] for _ in range(n+1)]
 for i,c in enumerate(s):
  p=last
  while i-1-ln[p]<0 or s[i-1-ln[p]]!=c:p=link[p]
  if c not in to[p]:
   u=len(ln);ln.append(ln[p]+2);link.append(1);to.append({})
   if ln[u]>1:
    q=link[p]
    while i-1-ln[q]<0 or s[i-1-ln[q]]!=c:q=link[q]
    link[u]=to[q][c]
   to[p][c]=u;events[i+1].append(i+2-ln[u])
  last=to[p][c]
 q=int(d[1]);queries=[[] for _ in range(n+1)];at=2
 for z in range(q):l=int(d[at]);r=int(d[at+1]);at+=2;queries[r].append((l,z))
 bit=[0]*(n+1);ans=[0]*q;total=0
 for r in range(1,n+1):
  for x in events[r]:
   total+=1;y=x
   while y<=n:bit[y]+=1;y+=y&-y
  for l,z in queries[r]:
   y=l-1;v=0
   while y:v+=bit[y];y-=y&-y
   ans[z]=total-v
 print('\n'.join(map(str,ans)))
if __name__=='__main__':main()
