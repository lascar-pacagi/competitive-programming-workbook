import sys
from array import array


def main():
    data = sys.stdin.buffer.read().split()
    n, q = int(data[0]), int(data[1])
    adj = [[] for _ in range(n + 1)]
    ptr = 2
    for _ in range(n - 1):
        u = int(data[ptr])
        v = int(data[ptr + 1])
        w = int(data[ptr + 2])
        ptr += 3
        adj[u].append((v, w))
        adj[v].append((u, w))
    ql = array("i", map(int, data[ptr:ptr + 2 * q:2]))
    qr = array("i", map(int, data[ptr + 1:ptr + 2 * q:2]))
    del data

    parent = [0] * (n + 1)
    up = [0] * (n + 1)
    depth = [0] * (n + 1)
    level = [0] * (n + 1)
    order = []
    seen = [False] * (n + 1)
    seen[1] = True
    stack = [1]
    while stack:
        v = stack.pop()
        order.append(v)
        for w, length in adj[v]:
            if not seen[w]:
                seen[w] = True
                parent[w] = v
                up[w] = length
                depth[w] = depth[v] + length
                level[w] = level[v] + 1
                stack.append(w)
    size = [1] * (n + 1)
    heavy = [0] * (n + 1)
    for v in reversed(order):
        p = parent[v]
        if p:
            size[p] += size[v]
    for v in reversed(order):
        p = parent[v]
        if p and (not heavy[p] or size[v] > size[heavy[p]]):
            heavy[p] = v

    # Heavy chains get contiguous positions, head first.
    head = [0] * (n + 1)
    pos = [0] * (n + 1)
    head[1] = 1
    cur = 0
    stack = [1]
    while stack:
        v = stack.pop()
        x = v
        while x:
            head[x] = v
            pos[x] = cur
            cur += 1
            for w, _ in adj[x]:
                if w != parent[x] and w != heavy[x]:
                    stack.append(w)
            x = heavy[x]
    # Preorder entry times (any DFS order works for the range-LCA trick).
    tin = [0] * (n + 1)
    for t, v in enumerate(order):
        tin[v] = t
    del order, size, adj

    def lca(a, b):
        while head[a] != head[b]:
            if level[head[a]] < level[head[b]]:
                a, b = b, a
            a = parent[head[a]]
        return a if pos[a] < pos[b] else b

    prefix = [0] * (n + 1)
    by_pos = [0] * n
    for v in range(1, n + 1):
        by_pos[pos[v]] = up[v]
    for k in range(n):
        prefix[k + 1] = prefix[k] + by_pos[k]

    # Sparse tables over labels: vertex with min / max entry time.  Rows are
    # compact int arrays to keep memory low.
    mn = [array("i", range(n + 1))]
    mx = [array("i", range(n + 1))]
    k = 1
    while (1 << k) <= n:
        pm = mn[-1]
        px = mx[-1]
        half = 1 << (k - 1)
        cm = list(pm)
        cx = list(px)
        for v in range(1, n - (1 << k) + 2):
            a = pm[v]
            b = pm[v + half]
            cm[v] = a if tin[a] < tin[b] else b
            a = px[v]
            b = px[v + half]
            cx[v] = a if tin[a] > tin[b] else b
        mn.append(array("i", cm))
        mx.append(array("i", cx))
        del cm, cx
        k += 1

    def range_lca(l, r):
        k = (r - l + 1).bit_length() - 1
        a = mn[k][l]
        b = mn[k][r - (1 << k) + 1]
        lo = a if tin[a] < tin[b] else b
        a = mx[k][l]
        b = mx[k][r - (1 << k) + 1]
        hi = a if tin[a] > tin[b] else b
        return lca(lo, hi)

    bit = [0] * (n + 1)

    def bit_add(i, x):
        while i <= n:
            bit[i] += x
            i += i & -i

    def bit_sum(i):
        s = 0
        while i > 0:
            s += bit[i]
            i &= i - 1
        return s

    # Per chain: stack of blocks [from, to, colour]; the top block is nearest
    # to the chain head.
    blocks = [[] for _ in range(n + 1)]

    def paint(v, colour):
        while v:
            h = head[v]
            a = pos[h]
            b = pos[v]
            st = blocks[h]
            while st and st[-1][1] <= b:
                blk = st.pop()
                bit_add(blk[2], prefix[blk[0]] - prefix[blk[1] + 1])
            if st and st[-1][0] <= b:
                blk = st[-1]
                bit_add(blk[2], prefix[blk[0]] - prefix[b + 1])
                blk[0] = b + 1
            st.append([a, b, colour])
            bit_add(colour, prefix[b + 1] - prefix[a])
            v = parent[h]

    answer = [0] * q
    painted = 0
    for i in sorted(range(q), key=qr.__getitem__):
        r = qr[i]
        while painted < r:
            painted += 1
            paint(painted, painted)
        l = ql[i]
        answer[i] = bit_sum(n) - bit_sum(l - 1) - depth[range_lca(l, r)]
    sys.stdout.write("\n".join(map(str, answer)) + "\n")


if __name__ == "__main__":
    main()
