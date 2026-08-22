import sys,heapq
def main():
 d=list(map(int,sys.stdin.buffer.read().split()));it=iter(d);n=next(it);w=next(it);par=[-1]+[next(it)-1 for _ in range(n-1)];offers=[]
 for _ in range(w):offers.append([(next(it)-1,next(it)) for _ in range(next(it))])
 N=1+w+n+1;S=0;T=N-1;g=[[] for _ in range(N)]
 def add(u,v,cap,c):g[u].append([v,cap,c,len(g[v])]);g[v].append([u,0,-c,len(g[u])-1])
 for i,o in enumerate(offers):
  add(S,1+i,1,0)
  for v,c in o:add(1+i,1+w+v,1,c)
 child=[0]*n
 for v in range(1,n):add(1+w+par[v],1+w+v,w,0);child[par[v]]+=1
 for v in range(n):
  if not child[v]:add(1+w+v,T,1,0)
 pot=[0]*N;cost=flow=0;INF=10**30
 while flow<w:
  dist=[INF]*N;dist[S]=0;prev=[None]*N;pq=[(0,S)]
  while pq:
   du,u=heapq.heappop(pq)
   if du!=dist[u]:continue
   for ei,e in enumerate(g[u]):
    if e[1] and du+e[2]+pot[u]-pot[e[0]]<dist[e[0]]:dist[e[0]]=du+e[2]+pot[u]-pot[e[0]];prev[e[0]]=(u,ei);heapq.heappush(pq,(dist[e[0]],e[0]))
  if dist[T]==INF:print('IMPOSSIBLE');return
  for v in range(N):
   if dist[v]<INF:pot[v]+=dist[v]
  v=T
  while v!=S:u,ei=prev[v];e=g[u][ei];e[1]-=1;g[v][e[3]][1]+=1;cost+=e[2];v=u
  flow+=1
 print(cost)
if __name__=='__main__':main()
