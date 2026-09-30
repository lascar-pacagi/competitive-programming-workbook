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
    size = 1
    while size < n: size *= 2
    tree = [-10**30] * (2*size)
    for i,u in enumerate(order): tree[size+i] = original[u]
    for node in range(size-1,0,-1):
        tree[node] = max(tree[2*node],tree[2*node+1])
    def assign(i,x):
        node=size+i;tree[node]=x;node//=2
        while node:
            tree[node]=max(tree[2*node],tree[2*node+1]);node//=2
    def query(left,right):
        left+=size;right+=size;answer=-10**30
        while left<right:
            if left&1:answer=max(answer,tree[left]);left+=1
            if right&1:right-=1;answer=max(answer,tree[right])
            left//=2;right//=2
        return answer
    out=[]
    for _ in range(q):
        op=data[pos];u=int(data[pos+1])-1;pos+=2
        if op==b'Q':out.append(query(tin[u],tout[u]))
        else:x=int(data[pos]);pos+=1;assign(tin[u],x)
    sys.stdout.write('\n'.join(map(str,out))+('\n' if out else ''))

if __name__ == "__main__": main()
