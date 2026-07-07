import sys,collections
def bfs(s,g):
    d=[-1]*len(g); d[s]=0; q=collections.deque([s])
    while q:
        u=q.popleft()
        for v in g[u]:
            if d[v]<0: d[v]=d[u]+1; q.append(v)
    return d
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n=data[0]; g=[[] for _ in range(n)]; idx=1
    for _ in range(n-1):
        a,b=data[idx]-1,data[idx+1]-1; idx+=2; g[a].append(b); g[b].append(a)
    d0=bfs(0,g); a=max(range(n),key=d0.__getitem__); da=bfs(a,g); b=max(range(n),key=da.__getitem__); db=bfs(b,g)
    print(" ".join(str(max(da[i],db[i])) for i in range(n)))
if __name__=="__main__": main()
