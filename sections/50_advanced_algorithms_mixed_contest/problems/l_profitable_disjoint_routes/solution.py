from collections import deque
import sys
def main():
    d=list(map(int,sys.stdin.buffer.read().split()))
    if not d:return
    n,m,k=d[:3];g=[[]for _ in range(n)];j=3
    def add(u,v,c):
        g[u].append([v,len(g[v]),1,c]);g[v].append([u,len(g[u])-1,0,-c])
    for _ in range(m):u,v,p=d[j:j+3];j+=3;add(u-1,v-1,-p)
    flow=0;cost=0;inf=10**30
    while flow<k:
        dist=[inf]*n;pv=[-1]*n;pe=[-1]*n;inside=[False]*n;dist[0]=0;q=deque([0]);inside[0]=True
        while q:
            u=q.popleft();inside[u]=False
            for i,e in enumerate(g[u]):
                v,rev,cap,c=e
                if cap and dist[v]>dist[u]+c:
                    dist[v]=dist[u]+c;pv[v]=u;pe[v]=i
                    if not inside[v]:inside[v]=True;q.append(v)
        if dist[-1]==inf:break
        flow+=1;cost+=dist[-1];v=n-1
        while v:
            u=pv[v];i=pe[v];rev=g[u][i][1];g[u][i][2]-=1;g[v][rev][2]+=1;v=u
    print(-cost if flow==k else 'IMPOSSIBLE')
if __name__=="__main__":main()
