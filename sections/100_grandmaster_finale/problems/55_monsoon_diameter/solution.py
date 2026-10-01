import sys


def useful_hull(points):
    """Upper hull part that matters for t >= 0 (A up, B down, concave)."""
    points.sort()
    h = []
    for p in points:
        pa, pb = p
        while h and h[-1][0] == pa:
            h.pop()
        while len(h) >= 2:
            oa, ob = h[-2]
            aa, ab = h[-1]
            if (aa - oa) * (pb - ob) - (ab - ob) * (pa - oa) >= 0:
                h.pop()
            else:
                break
        h.append(p)
    best = 0
    for i in range(1, len(h)):
        if h[i][1] >= h[best][1]:
            best = i
    return h[best:]


def minkowski(a, b, shift_a, shift_b):
    x = a[0][0] + b[0][0] + shift_a
    y = a[0][1] + b[0][1] + shift_b
    out = [(x, y)]
    i = j = 0
    la = len(a) - 1
    lb = len(b) - 1
    while i < la or j < lb:
        if i == la:
            take_a = False
        elif j == lb:
            take_a = True
        else:
            dax = a[i + 1][0] - a[i][0]
            day = a[i + 1][1] - a[i][1]
            dbx = b[j + 1][0] - b[j][0]
            dby = b[j + 1][1] - b[j][1]
            take_a = day * dbx >= dby * dax
        if take_a:
            x += a[i + 1][0] - a[i][0]
            y += a[i + 1][1] - a[i][1]
            i += 1
        else:
            x += b[j + 1][0] - b[j][0]
            y += b[j + 1][1] - b[j][1]
            j += 1
        out.append((x, y))
    return out


def main():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    raw = [[] for _ in range(n)]
    ptr = 2
    for _ in range(n - 1):
        u = int(data[ptr]) - 1
        v = int(data[ptr + 1]) - 1
        a = int(data[ptr + 2])
        b = int(data[ptr + 3])
        ptr += 4
        raw[u].append((v, a, b))
        raw[v].append((u, a, b))
    del data

    # Binarize with zero-cost dummy vertices.
    eu = []
    ev = []
    ea = []
    eb = []
    V = n
    parent = [-1] * n
    parent[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        kids = []
        for e in raw[v]:
            if parent[e[0]] < 0:
                parent[e[0]] = v
                kids.append(e)
                stack.append(e[0])
        cur = v
        k = len(kids)
        for i, (w, a, b) in enumerate(kids):
            eu.append(cur)
            ev.append(w)
            ea.append(a)
            eb.append(b)
            if k - i > 2:
                eu.append(cur)
                ev.append(V)
                ea.append(0)
                eb.append(0)
                cur = V
                V += 1
    del raw, parent
    E = len(eu)
    adj = [[] for _ in range(V)]
    for e in range(E):
        adj[eu[e]].append(e)
        adj[ev[e]].append(e)
    removed = [False] * E
    parent_edge = [-1] * V
    size = [0] * V
    acc_a = [0] * V
    acc_b = [0] * V

    def collect(root):
        out = [root]
        parent_edge[root] = -1
        for v in out:
            pe = parent_edge[v]
            for e in adj[v]:
                if e != pe and not removed[e]:
                    w = eu[e] ^ ev[e] ^ v
                    parent_edge[w] = e
                    out.append(w)
        return out

    def side_hull(root):
        vs = collect(root)
        acc_a[root] = 0
        acc_b[root] = 0
        pts = [(0, 0)]
        for idx in range(1, len(vs)):
            v = vs[idx]
            e = parent_edge[v]
            p = eu[e] ^ ev[e] ^ v
            x = acc_a[p] + ea[e]
            y = acc_b[p] + eb[e]
            acc_a[v] = x
            acc_b[v] = y
            pts.append((x, y))
        return useful_hull(pts)

    candidates = [(0, 0)]
    work = [0]
    while work:
        root = work.pop()
        vs = collect(root)
        total = len(vs)
        if total == 1:
            continue
        for idx in range(total - 1, -1, -1):
            v = vs[idx]
            s = 1
            pe = parent_edge[v]
            for e in adj[v]:
                if e != pe and not removed[e]:
                    s += size[eu[e] ^ ev[e] ^ v]
            size[v] = s
        best_value = total + 1
        child = -1
        for idx in range(1, total):
            v = vs[idx]
            s = size[v]
            value = s if s > total - s else total - s
            if value < best_value:
                best_value = value
                child = v
        edge = parent_edge[child]
        other = eu[edge] ^ ev[edge] ^ child
        removed[edge] = True
        h1 = side_hull(child)
        h2 = side_hull(other)
        candidates.extend(minkowski(h1, h2, ea[edge], eb[edge]))
        work.append(child)
        work.append(other)

    hull = useful_hull(candidates)
    del candidates, adj, eu, ev, ea, eb
    write = sys.stdout.write
    out = []
    k = 0
    last = len(hull) - 1
    ha, hb = hull[0]
    for t in range(m):
        while k < last:
            na, nb = hull[k + 1]
            if na * t + nb >= ha * t + hb:
                k += 1
                ha, hb = na, nb
            else:
                break
        out.append(ha * t + hb)
        if len(out) == 65536:
            write(" ".join(map(str, out)) + " ")
            out = []
    write(" ".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
