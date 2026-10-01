import sys


def main():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    total = n + m
    # Subdivide link i (u -> v) as u -> n+i -> v.
    adj_start = [0] * (total + 1)
    src = [0] * (2 * m)
    dst = [0] * (2 * m)
    for i in range(m):
        u = int(data[2 + 2 * i]) - 1
        v = int(data[3 + 2 * i]) - 1
        x = n + i
        src[2 * i] = u
        dst[2 * i] = x
        src[2 * i + 1] = x
        dst[2 * i + 1] = v
    for a in src:
        adj_start[a + 1] += 1
    for i in range(total):
        adj_start[i + 1] += adj_start[i]
    adj = [0] * (2 * m)
    fill = adj_start[:]
    for a, b in zip(src, dst):
        adj[fill[a]] = b
        fill[a] += 1

    # Iterative preorder DFS from station 1.
    dfn = [-1] * total
    vertex_at = [0]
    parent = [-1]
    dfn[0] = 0
    stack_v = [0]
    stack_e = [adj_start[0]]
    while stack_v:
        v = stack_v[-1]
        e = stack_e[-1]
        if e == adj_start[v + 1]:
            stack_v.pop()
            stack_e.pop()
            continue
        stack_e[-1] = e + 1
        w = adj[e]
        if dfn[w] < 0:
            dfn[w] = len(vertex_at)
            vertex_at.append(w)
            parent.append(dfn[v])
            stack_v.append(w)
            stack_e.append(adj_start[w])
    T = len(vertex_at)
    # Predecessor lists in preorder numbering, stored contiguously.
    pred_start = [0] * (T + 1)
    for a, b in zip(src, dst):
        if dfn[a] >= 0:
            pred_start[dfn[b] + 1] += 1
    for i in range(T):
        pred_start[i + 1] += pred_start[i]
    pred = [0] * pred_start[T]
    fill = pred_start[:]
    for a, b in zip(src, dst):
        da = dfn[a]
        if da >= 0:
            db = dfn[b]
            pred[fill[db]] = da
            fill[db] += 1
    del fill, src, dst, adj, adj_start

    sdom = list(range(T))
    idom = [0] * T
    anc = [-1] * T
    best = list(range(T))
    bucket_head = [-1] * T
    bucket_next = [-1] * T

    def evaluate(v):
        if anc[v] < 0:
            return v
        path = []
        x = v
        while anc[anc[x]] >= 0:
            path.append(x)
            x = anc[x]
        for y in reversed(path):
            a = anc[y]
            if sdom[best[a]] < sdom[best[y]]:
                best[y] = best[a]
            anc[y] = anc[a]
        return best[v]

    for w in range(T - 1, 0, -1):
        s = sdom[w]
        for i in range(pred_start[w], pred_start[w + 1]):
            v = pred[i]
            u = evaluate(v) if anc[v] >= 0 else v
            if sdom[u] < s:
                s = sdom[u]
        sdom[w] = s
        bucket_next[w] = bucket_head[s]
        bucket_head[s] = w
        p = parent[w]
        anc[w] = p
        v = bucket_head[p]
        while v >= 0:
            u = evaluate(v)
            idom[v] = u if sdom[u] < sdom[v] else p
            v = bucket_next[v]
        bucket_head[p] = -1
    for w in range(1, T):
        if idom[w] != sdom[w]:
            idom[w] = idom[idom[w]]

    below = [1 if vertex_at[w] < n else 0 for w in range(T)]
    for w in range(T - 1, 0, -1):
        below[idom[w]] += below[w]
    out = []
    for i in range(m):
        x = dfn[n + i]
        out.append(below[x] if x >= 0 else 0)
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
