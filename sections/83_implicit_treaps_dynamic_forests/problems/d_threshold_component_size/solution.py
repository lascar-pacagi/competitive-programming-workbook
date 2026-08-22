import sys
from array import array


class KRT:
    def __init__(self, n, edges):
        z = 2 * n + 5
        self.parent = list(range(z))
        self.tree = [[] for _ in range(z)]
        self.weight = [-1] * z
        self.size = [1] * z
        self.next = n
        dsu = list(range(z))

        def find(x):
            while dsu[x] != x:
                dsu[x] = dsu[dsu[x]]
                x = dsu[x]
            return x

        for w, u, v in sorted(edges):
            a, b = find(u), find(v)
            if a == b:
                continue
            x = self.next
            self.next += 1
            self.weight[x] = w
            self.size[x] = self.size[a] + self.size[b]
            self.tree[x] = [a, b]
            self.parent[a] = self.parent[b] = x
            dsu[a] = dsu[b] = dsu[x] = x
        roots = [v for v in range(self.next) if self.parent[v] == v]
        self.depth = [0] * self.next
        order = []
        for root in roots:
            st = [root]
            while st:
                x = st.pop()
                order.append(x)
                for y in self.tree[x]:
                    self.depth[y] = self.depth[x] + 1
                    st.append(y)
        self.L = max(1, self.next.bit_length())
        self.up = [[0] * self.next for _ in range(self.L)]
        self.up[0] = self.parent[: self.next]
        for j in range(1, self.L):
            self.up[j] = [
                self.up[j - 1][self.up[j - 1][x]] for x in range(self.next)
            ]
        self.component = [self.up[-1][v] for v in range(n)]

    def climb(self, v, x):
        for j in range(self.L - 1, -1, -1):
            p = self.up[j][v]
            if p != v and self.weight[p] <= x:
                v = p
        return v

    def lca(self, a, b):
        if self.component[a] != self.component[b]:
            return -1
        if self.depth[a] < self.depth[b]:
            a, b = b, a
        d = self.depth[a] - self.depth[b]
        for j in range(self.L):
            if d >> j & 1:
                a = self.up[j][a]
        if a == b:
            return a
        for j in range(self.L - 1, -1, -1):
            if self.up[j][a] != self.up[j][b]:
                a, b = self.up[j][a], self.up[j][b]
        return self.up[0][a]


def main():
    d = array("i", map(int, sys.stdin.buffer.read().split()))
    n, m, q = d[:3]
    at = 3
    e = []
    for i in range(m):
        u, v, w = d[at : at + 3]
        at += 3
        e.append((w, u - 1, v - 1))
    t = KRT(n, e)
    print(
        "\n".join(
            str(t.size[t.climb(d[i] - 1, d[i + 1])])
            for i in range(at, at + 2 * q, 2)
        )
    )


if __name__ == "__main__":
    main()
