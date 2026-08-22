import sys


def main():
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    idx = 0
    n = int(tokens[idx])
    q = int(tokens[idx + 1])
    idx += 2
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        u = int(tokens[idx]) - 1
        v = int(tokens[idx + 1]) - 1
        w = int(tokens[idx + 2])
        idx += 3
        graph[u].append((v, w))
        graph[v].append((u, w))
    log = n.bit_length()
    up = [[0] * n for _ in range(log)]
    tin = [0] * n
    tout = [0] * n
    distance = [0] * n
    timer = 0
    stack = [(0, 0, 0)]
    while stack:
        u, p, state = stack.pop()
        if state == 0:
            tin[u] = timer
            timer += 1
            up[0][u] = p
            for j in range(1, log):
                up[j][u] = up[j - 1][up[j - 1][u]]
            stack.append((u, p, 1))
            for v, w in reversed(graph[u]):
                if v != p:
                    distance[v] = distance[u] + w
                    stack.append((v, u, 0))
        else:
            tout[u] = timer - 1

    def ancestor(u, v):
        return tin[u] <= tin[v] <= tout[u]

    def lca(u, v):
        if ancestor(u, v):
            return u
        if ancestor(v, u):
            return v
        for j in range(log - 1, -1, -1):
            if not ancestor(up[j][u], v):
                u = up[j][u]
        return up[0][u]

    marked = [False] * n
    count = [0] * n
    parent = [-1] * n
    out = []
    for _ in range(q):
        k = int(tokens[idx])
        idx += 1
        nodes = [int(x) - 1 for x in tokens[idx : idx + k]]
        idx += k
        for u in nodes:
            marked[u] = True
        nodes.sort(key=tin.__getitem__)
        nodes += [lca(nodes[i - 1], nodes[i]) for i in range(1, k)]
        nodes = sorted(set(nodes), key=tin.__getitem__)
        st = []
        for u in nodes:
            while st and not ancestor(st[-1], u):
                st.pop()
            parent[u] = st[-1] if st else -1
            st.append(u)
            count[u] = int(marked[u])
        answer = 0
        for u in reversed(nodes):
            p = parent[u]
            if p != -1:
                answer += (distance[u] - distance[p]) * count[u] * (k - count[u])
                count[p] += count[u]
        out.append(str(answer))
        for u in nodes:
            marked[u] = False
    print("\n".join(out))


if __name__ == "__main__":
    main()
