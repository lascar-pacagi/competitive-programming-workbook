import sys
def main():
 d=list(map(int,sys.stdin.buffer.read().split()));n,m,k=d[:3];i=3;g=[[] for _ in range(n+1)]
 for _ in range(m):u,v=d[i],d[i+1];i+=2;g[u].append(v);g[v].append(u)
 dist=[-1]*(n+1);q=[]
 for s in d[i:i+k]:
  if dist[s]<0:dist[s]=0;q.append(s)
 for h,u in enumerate(q):
  for v in g[u]:
   if dist[v]<0:dist[v]=dist[u]+1;q.append(v)
 print(*dist[1:])
if __name__=='__main__':main()
