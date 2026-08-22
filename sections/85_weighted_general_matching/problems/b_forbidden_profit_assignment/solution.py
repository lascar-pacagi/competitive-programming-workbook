import sys


def hungarian(cost):
    n = len(cost)
    m = len(cost[0])
    u = [0] * (n + 1)
    v = [0] * (m + 1)
    p = [0] * (m + 1)
    way = [0] * (m + 1)
    for i in range(1, n + 1):
        p[0] = i
        j0 = 0
        minimum = [10**30] * (m + 1)
        used = [False] * (m + 1)
        while True:
            used[j0] = True
            i0 = p[j0]
            delta = 10**30
            j1 = 0
            for j in range(1, m + 1):
                if not used[j]:
                    cur = cost[i0 - 1][j - 1] - u[i0] - v[j]
                    if cur < minimum[j]:
                        minimum[j] = cur
                        way[j] = j0
                    if minimum[j] < delta:
                        delta = minimum[j]
                        j1 = j
            for j in range(m + 1):
                if used[j]:
                    u[p[j]] += delta
                    v[j] -= delta
                else:
                    minimum[j] -= delta
            j0 = j1
            if p[j0] == 0:
                break
        while True:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1
            if j0 == 0:
                break
    match = [-1] * n
    for j in range(1, m + 1):
        if p[j]:
            match[p[j] - 1] = j - 1
    return -v[0], match


def blossom(graph):
    n = len(graph)
    match = [-1] * n
    base = list(range(n))
    parent = [-1] * n

    def find_path(root):
        nonlocal base, parent
        used = [False] * n
        parent = [-1] * n
        base = list(range(n))
        q = [root]
        used[root] = True

        def get_lca(a, b):
            mark = [False] * n
            while True:
                a = base[a]
                mark[a] = True
                if match[a] == -1:
                    break
                a = parent[match[a]]
            while True:
                b = base[b]
                if mark[b]:
                    return b
                b = parent[match[b]]

        def mark_path(v, b, child, flower):
            while base[v] != b:
                flower[base[v]] = flower[base[match[v]]] = True
                parent[v] = child
                child = match[v]
                v = parent[match[v]]

        for v in q:
            for u in graph[v]:
                if base[v] == base[u] or match[v] == u:
                    continue
                if u == root or (match[u] != -1 and parent[match[u]] != -1):
                    b = get_lca(v, u)
                    flower = [False] * n
                    mark_path(v, b, u, flower)
                    mark_path(u, b, v, flower)
                    for x in range(n):
                        if flower[base[x]]:
                            base[x] = b
                        if not used[x] and flower[base[x]]:
                            used[x] = True
                            q.append(x)
                elif parent[u] == -1:
                    parent[u] = v
                    if match[u] == -1:
                        return u
                    u = match[u]
                    used[u] = True
                    q.append(u)
        return -1

    for root in range(n):
        if match[root] != -1:
            continue
        v = find_path(root)
        if v == -1:
            continue
        while v != -1:
            pv = parent[v]
            nv = match[pv] if pv != -1 else -1
            match[v] = pv
            if pv != -1:
                match[pv] = v
            v = nv
    return match


def main():
    d = list(map(int, sys.stdin.buffer.read().split()))
    n, m = d[:2]
    raw = d[2:]
    inf = 10**15
    a = [
        [inf if raw[i * m + j] < 0 else -raw[i * m + j] for j in range(m)]
        for i in range(n)
    ]
    cost, match = hungarian(a)
    print(
        "IMPOSSIBLE"
        if any(a[i][match[i]] >= inf for i in range(n))
        else -cost
    )


if __name__ == "__main__":
    main()
