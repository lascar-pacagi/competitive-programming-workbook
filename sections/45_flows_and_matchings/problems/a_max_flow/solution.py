import sys
from collections import deque
def dinic(n,edges,s,t,cut=False):
    g=[[] for _ in range(n)]
    def add(u,v,c):
        g[u].append([v,c,len(g[v])]); g[v].append([u,0,len(g[u])-1])
    for u,v,c in edges: add(u,v,c)
    flow=0
    while True:
        level=[-1]*n; level[s]=0; dq=deque([s])
        while dq:
            u=dq.popleft()
            for v,c,rev in g[u]:
                if c and level[v]<0: level[v]=level[u]+1; dq.append(v)
        if level[t]<0: break
        it=[0]*n
        def dfs(u,f):
            if u==t: return f
            for i in range(it[u],len(g[u])):
                it[u]=i; v,c,rev=g[u][i]
                if c and level[v]==level[u]+1:
                    ret=dfs(v,min(f,c))
                    if ret: g[u][i][1]-=ret; g[v][rev][1]+=ret; return ret
            return 0
        while True:
            pushed=dfs(s,10**18)
            if not pushed: break
            flow+=pushed
    if cut:
        seen=[False]*n; dq=deque([s]); seen[s]=True
        while dq:
            u=dq.popleft()
            for v,c,rev in g[u]:
                if c and not seen[v]: seen[v]=True; dq.append(v)
        return flow,seen
    return flow,None
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n,m=data[0],data[1]; idx=2; edges=[]
    for _ in range(m): edges.append((data[idx]-1,data[idx+1]-1,data[idx+2])); idx+=3
    print(dinic(n,edges,0,n-1)[0])
if __name__=="__main__": main()
