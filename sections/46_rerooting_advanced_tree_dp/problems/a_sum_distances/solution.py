import sys
sys.setrecursionlimit(1_000_000)
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n=data[0]; g=[[] for _ in range(n)]; idx=1
    for _ in range(n-1):
        a,b=data[idx]-1,data[idx+1]-1; idx+=2; g[a].append(b); g[b].append(a)
    sub=[1]*n; down=[0]*n
    def dfs(u,p):
        for v in g[u]:
            if v!=p: dfs(v,u); sub[u]+=sub[v]; down[u]+=down[v]+sub[v]
    ans=[0]*n
    def reroot(u,p):
        for v in g[u]:
            if v!=p:
                ans[v]=ans[u]+n-2*sub[v]; reroot(v,u)
    dfs(0,-1); ans[0]=down[0]; reroot(0,-1); print(" ".join(map(str,ans)))
if __name__=="__main__": main()
