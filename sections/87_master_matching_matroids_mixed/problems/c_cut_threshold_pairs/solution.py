import sys
from collections import deque


class Dinic:
    def __init__(self, n):
        self.g = [[] for _ in range(n)]

    def add(self, u, v, c):
        self.g[u].append([v, c, len(self.g[v])])
        self.g[v].append([u, 0, len(self.g[u]) - 1])

    def flow(self, s, t):
        answer = 0
        n = len(self.g)
        while True:
            level = [-1] * n
            level[s] = 0
            q = deque([s])
            while q:
                u = q.popleft()
                for v, c, _ in self.g[u]:
                    if c and level[v] < 0:
                        level[v] = level[u] + 1
                        q.append(v)
            if level[t] < 0:
                self.reachable = [x >= 0 for x in level]
                return answer
            it = [0] * n

            def dfs(u, pushed):
                if u == t:
                    return pushed
                while it[u] < len(self.g[u]):
                    e = self.g[u][it[u]]
                    if e[1] and level[e[0]] == level[u] + 1:
                        take = dfs(e[0], min(pushed, e[1]))
                        if take:
                            e[1] -= take
                            self.g[e[0]][e[2]][1] += take
                            return take
                    it[u] += 1
                return 0

            while True:
                pushed = dfs(s, 10**30)
                if not pushed:
                    break
                answer += pushed


def gomory_hu(n, edges):
    parent = [0] * n
    value = [0] * n
    for s in range(1, n):
        t = parent[s]
        d = Dinic(n)
        for u, v, c in edges:
            d.add(u, v, c)
            d.add(v, u, c)
        value[s] = d.flow(s, t)
        side = d.reachable
        for v in range(s + 1, n):
            if parent[v] == t and side[v]:
                parent[v] = s
        if side[parent[t]]:
            parent[s] = parent[t]
            parent[t] = s
            value[s], value[t] = value[t], value[s]
    tree = [[] for _ in range(n)]
    for v in range(1, n):
        tree[v].append((parent[v], value[v]))
        tree[parent[v]].append((v, value[v]))
    return tree


def tree_minimum(tree):
    n = len(tree)
    L = max(1, n.bit_length())
    up = [[0] * n for _ in range(L)]
    mn = [[10**30] * n for _ in range(L)]
    depth = [0] * n
    stack = [(0, 0)]
    while stack:
        u, p = stack.pop()
        up[0][u] = p
        for v, w in tree[u]:
            if v != p:
                depth[v] = depth[u] + 1
                mn[0][v] = w
                stack.append((v, u))
    for j in range(1, L):
        for v in range(n):
            mn[j][v] = min(mn[j - 1][v], mn[j - 1][up[j - 1][v]])
            up[j][v] = up[j - 1][up[j - 1][v]]

    def query(a, b):
        answer = 10**30
        if depth[a] < depth[b]:
            a, b = b, a
        z = depth[a] - depth[b]
        for j in range(L):
            if z >> j & 1:
                answer = min(answer, mn[j][a])
                a = up[j][a]
        if a == b:
            return answer
        for j in range(L - 1, -1, -1):
            if up[j][a] != up[j][b]:
                answer = min(answer, mn[j][a], mn[j][b])
                a, b = up[j][a], up[j][b]
        return min(answer, mn[0][a], mn[0][b])

    return query


def main():
    d = list(map(int, sys.stdin.buffer.read().split()))
    n, m, q = d[:3]
    at = 3
    e = []
    for _ in range(m):
        u, v, c = d[at : at + 3]
        at += 3
        e.append((u - 1, v - 1, c))
    query = tree_minimum(gomory_hu(n, e))
    values = sorted(query(i, j) for i in range(n) for j in range(i))
    import bisect

    print(
        "\n".join(
            str(bisect.bisect_right(values, d[i])) for i in range(at, at + q)
        )
    )


if __name__ == "__main__":
    main()
