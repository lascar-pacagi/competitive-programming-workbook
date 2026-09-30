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
    values = [original[u] for u in order]
    mx = [0] * (4*n); lazy = [0] * (4*n)
    def build(node, left, right):
        if right-left == 1: mx[node] = values[left]; return
        mid = (left+right)//2
        build(2*node,left,mid); build(2*node+1,mid,right)
        mx[node] = max(mx[2*node],mx[2*node+1])
    def apply(node, delta):
        mx[node] += delta; lazy[node] += delta
    def push(node):
        if lazy[node]:
            apply(2*node,lazy[node]); apply(2*node+1,lazy[node]); lazy[node] = 0
    def update(node,left,right,ql,qr,x,assignment=False):
        if qr<=left or right<=ql: return
        if ql<=left and right<=qr:
            if assignment: mx[node]=x; lazy[node]=0
            else: apply(node,x)
            return
        push(node); mid=(left+right)//2
        update(2*node,left,mid,ql,qr,x,assignment)
        update(2*node+1,mid,right,ql,qr,x,assignment)
        mx[node]=max(mx[2*node],mx[2*node+1])
    def query(node,left,right,ql,qr):
        if qr<=left or right<=ql: return -10**30
        if ql<=left and right<=qr: return mx[node]
        push(node); mid=(left+right)//2
        return max(query(2*node,left,mid,ql,qr),query(2*node+1,mid,right,ql,qr))
    build(1,0,n); out=[]
    for _ in range(q):
        op=data[pos]; u=int(data[pos+1])-1; pos+=2
        if op == b'Q': out.append(query(1,0,n,tin[u],tout[u]))
        else:
            x=int(data[pos]); pos+=1
            update(1,0,n,tin[u],tout[u],x)
    sys.stdout.write('\n'.join(map(str,out)) + ('\n' if out else ''))

if __name__ == "__main__": main()
