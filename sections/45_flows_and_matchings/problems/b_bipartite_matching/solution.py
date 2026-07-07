import sys, collections
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n,m,e=data[0],data[1],data[2]; adj=[[] for _ in range(n)]; idx=3
    for _ in range(e): adj[data[idx]-1].append(data[idx+1]-1); idx+=2
    match=[-1]*m
    def dfs(u,vis):
        for v in adj[u]:
            if vis[v]: continue
            vis[v]=1
            if match[v]==-1 or dfs(match[v],vis): match[v]=u; return True
        return False
    ans=0
    for u in range(n): ans+=dfs(u,[0]*m)
    print(ans)
if __name__=="__main__": main()
