import sys,heapq
def main():
 d=list(map(int,sys.stdin.buffer.read().split()))
 if not d:return
 n,m=d[:2];g=[[] for _ in range(n)];i=2
 for _ in range(m):
  a,b,w=d[i]-1,d[i+1]-1,d[i+2];i+=3;g[a].append((b,w));g[b].append((a,w))
 inf=10**30;dist=[[inf]*n for _ in range(2)];dist[0][0]=0;pq=[(0,0,0)]
 while pq:
  cost,used,v=heapq.heappop(pq)
  if cost!=dist[used][v]:continue
  for to,w in g[v]:
   if cost+w<dist[used][to]:dist[used][to]=cost+w;heapq.heappush(pq,(cost+w,used,to))
   if not used and cost<dist[1][to]:dist[1][to]=cost;heapq.heappush(pq,(cost,1,to))
 print(min(dist[0][-1],dist[1][-1]))
if __name__=='__main__':main()
