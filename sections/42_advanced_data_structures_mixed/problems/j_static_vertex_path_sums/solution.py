import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data: return
    n, q = int(data[0]), int(data[1]); pos = 2
    original = list(map(int, data[pos:pos+n])); pos += n
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = int(data[pos]) - 1, int(data[pos + 1]) - 1; pos += 2
        g[u].append(v); g[v].append(u)
    tin = [0] * n; tout = [0] * n; order = []; stack = [(0, -1, False)]
    while stack:
        u, parent, leaving = stack.pop()
        if leaving:
            tout[u] = len(order); continue
        tin[u] = len(order); order.append(u)
        stack.append((u, parent, True))
        for v in reversed(g[u]):
            if v != parent: stack.append((v, u, False))
    parent=[0]*n;depth=[0]*n;sums=[0]*n;sums[0]=original[0]
    for u in order:
        for v in g[u]:
            if v!=parent[u]:parent[v]=u;depth[v]=depth[u]+1;sums[v]=sums[u]+original[v]
    up=[parent]
    for _ in range(1,n.bit_length()):
        previous=up[-1];up.append([previous[previous[u]] for u in range(n)])
    def lca(u,v):
        if depth[u]<depth[v]:u,v=v,u
        diff=depth[u]-depth[v]
        for k in range(len(up)):
            if diff>>k&1:u=up[k][u]
        if u==v:return u
        for k in range(len(up)-1,-1,-1):
            if up[k][u]!=up[k][v]:u,v=up[k][u],up[k][v]
        return parent[u]
    out=[]
    for _ in range(q):
        u,v=int(data[pos])-1,int(data[pos+1])-1;pos+=2;w=lca(u,v)
        out.append(sums[u]+sums[v]-2*sums[w]+original[w])
    print('\n'.join(map(str,out)))

if __name__ == "__main__": main()
