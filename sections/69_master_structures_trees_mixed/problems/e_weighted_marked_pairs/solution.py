import sys


def main():
    t = sys.stdin.buffer.read().split()
    if not t:
        return
    z = 0
    n = int(t[z])
    q = int(t[z + 1])
    z += 2
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u = int(t[z]) - 1
        v = int(t[z + 1]) - 1
        w = int(t[z + 2])
        z += 3
        g[u].append((v, w))
        g[v].append((u, w))
    log = n.bit_length()
    up = [[0] * n for _ in range(log)]
    tin = [0] * n
    tout = [0] * n
    dist = [0] * n
    timer = 0
    stack = [(0, 0, 0)]
    while stack:
        u, p, state = stack.pop()
        if not state:
            tin[u] = timer
            timer += 1
            up[0][u] = p
            for j in range(1, log):
                up[j][u] = up[j - 1][up[j - 1][u]]
            stack.append((u, p, 1))
            for v, w in reversed(g[u]):
                if v != p:
                    dist[v] = dist[u] + w
                    stack.append((v, u, 0))
        else:
            tout[u] = timer - 1

    def anc(u, v):
        return tin[u] <= tin[v] <= tout[u]

    def lca(u, v):
        if anc(u, v):
            return u
        if anc(v, u):
            return v
        for j in range(log - 1, -1, -1):
            if not anc(up[j][u], v):
                u = up[j][u]
        return up[0][u]

    weight = [0] * n
    sub = [0] * n
    parent = [-1] * n
    out = []
    for _ in range(q):
        k = int(t[z])
        z += 1
        nodes = []
        total = 0
        for _ in range(k):
            u = int(t[z]) - 1
            c = int(t[z + 1])
            z += 2
            nodes.append(u)
            weight[u] = c
            total += c
        nodes.sort(key=tin.__getitem__)
        nodes += [lca(nodes[i - 1], nodes[i]) for i in range(1, k)]
        nodes = sorted(set(nodes), key=tin.__getitem__)
        st = []
        for u in nodes:
            while st and not anc(st[-1], u):
                st.pop()
            parent[u] = st[-1] if st else -1
            st.append(u)
            sub[u] = weight[u]
        answer = 0
        for u in reversed(nodes):
            p = parent[u]
            if p != -1:
                answer += (dist[u] - dist[p]) * sub[u] * (total - sub[u])
                sub[p] += sub[u]
        out.append(str(answer))
        for u in nodes:
            weight[u] = 0
    print("\n".join(out))


if __name__ == "__main__":
    main()
