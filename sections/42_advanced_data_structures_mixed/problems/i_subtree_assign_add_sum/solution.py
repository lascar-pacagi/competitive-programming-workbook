import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    pos = 0
    n = int(data[pos]); q = int(data[pos + 1]); pos += 2
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
    a = [0] + [original[u] for u in order]

    size = 4 * n + 4
    sm = [0] * size
    addv = [0] * size
    asgv = [0] * size
    hasa = [False] * size

    def put_assign(x, ln, v):
        sm[x] = v * ln; asgv[x] = v; hasa[x] = True; addv[x] = 0

    def put_add(x, ln, v):
        sm[x] += v * ln
        if hasa[x]:
            asgv[x] += v
        else:
            addv[x] += v

    def push(x, l, r):
        m = (l + r) // 2; lc = 2 * x; rc = 2 * x + 1
        if hasa[x]:
            put_assign(lc, m - l + 1, asgv[x])
            put_assign(rc, r - m, asgv[x])
            hasa[x] = False; asgv[x] = 0
        if addv[x]:
            put_add(lc, m - l + 1, addv[x])
            put_add(rc, r - m, addv[x])
            addv[x] = 0

    def build(x, l, r):
        if l == r:
            sm[x] = a[l]; return
        m = (l + r) // 2
        build(2 * x, l, m); build(2 * x + 1, m + 1, r)
        sm[x] = sm[2 * x] + sm[2 * x + 1]

    def upd(x, l, r, ql, qr, v, is_assign):
        if qr < l or r < ql:
            return
        if ql <= l and r <= qr:
            if is_assign:
                put_assign(x, r - l + 1, v)
            else:
                put_add(x, r - l + 1, v)
            return
        push(x, l, r)
        m = (l + r) // 2
        upd(2 * x, l, m, ql, qr, v, is_assign)
        upd(2 * x + 1, m + 1, r, ql, qr, v, is_assign)
        sm[x] = sm[2 * x] + sm[2 * x + 1]

    def qry(x, l, r, ql, qr):
        if qr < l or r < ql:
            return 0
        if ql <= l and r <= qr:
            return sm[x]
        push(x, l, r)
        m = (l + r) // 2
        return (qry(2 * x, l, m, ql, qr)
                + qry(2 * x + 1, m + 1, r, ql, qr))

    sys.setrecursionlimit(300000)
    build(1, 1, n)
    out = []
    for _ in range(q):
        t = int(data[pos]); pos += 1
        u = int(data[pos]) - 1; pos += 1
        l, r = tin[u]+1, tout[u]
        if t == 3: out.append(qry(1,1,n,l,r))
        else:
            x = int(data[pos]); pos += 1
            upd(1,1,n,l,r,x,t == 1)
    sys.stdout.write("\n".join(map(str, out)) + ("\n" if out else ""))

if __name__ == "__main__":
    main()
