import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m, q = data[:3]
    pos = 3
    edges = []
    for _ in range(m):
        u, v, w = data[pos : pos + 3]
        pos += 3
        edges.append((w, u - 1, v - 1))
    leader = list(range(n))
    size = [1] * n

    def find(u):
        while leader[u] != u:
            leader[u] = leader[leader[u]]
            u = leader[u]
        return u

    graph = [[] for _ in range(n)]
    for w, u, v in sorted(edges):
        a, b = find(u), find(v)
        if a == b:
            continue
        if size[a] < size[b]:
            a, b = b, a
        leader[b] = a
        size[a] += size[b]
        graph[u].append((v, w))
        graph[v].append((u, w))
    parent = list(range(n))
    depth = [-1] * n
    weight = [0] * n
    for root in range(n):
        if depth[root] != -1:
            continue
        depth[root] = 0
        stack = [root]
        while stack:
            u = stack.pop()
            for v, w in graph[u]:
                if depth[v] == -1:
                    depth[v] = depth[u] + 1
                    parent[v] = u
                    weight[v] = w
                    stack.append(v)
    up = [parent]
    high = [weight]
    for _ in range(1, n.bit_length()):
        previous, maxima = up[-1], high[-1]
        up.append([previous[previous[u]] for u in range(n)])
        high.append(
            [max(maxima[u], maxima[previous[u]]) for u in range(n)]
        )
    out = []
    for _ in range(q):
        u, v = data[pos] - 1, data[pos + 1] - 1
        pos += 2
        if find(u) != find(v):
            out.append(-1)
            continue
        result = 0
        if depth[u] < depth[v]:
            u, v = v, u
        d = depth[u] - depth[v]
        k = 0
        while d:
            if d & 1:
                result = max(result, high[k][u])
                u = up[k][u]
            d >>= 1
            k += 1
        if u != v:
            for k in range(len(up) - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    result = max(result, high[k][u], high[k][v])
                    u, v = up[k][u], up[k][v]
            result = max(result, high[0][u], high[0][v])
        out.append(result)
    print("\n".join(map(str, out)))


if __name__ == "__main__":
    main()
