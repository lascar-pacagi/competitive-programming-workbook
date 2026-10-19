import sys


class SegmentTree:
    def __init__(self, values):
        self.n = len(values)
        self.tree = [0] * (4 * self.n)
        self._build(1, 0, self.n, values)

    def _build(self, node, left, right, values):
        if right - left == 1:
            self.tree[node] = values[left]
            return
        mid = (left + right) // 2
        self._build(2 * node, left, mid, values)
        self._build(2 * node + 1, mid, right, values)
        self.tree[node] = max(
            self.tree[2 * node], self.tree[2 * node + 1]
        )

    def assign(self, i, x):
        self._assign(1, 0, self.n, i, x)

    def _assign(self, node, left, right, i, x):
        if right - left == 1:
            self.tree[node] = x
            return
        mid = (left + right) // 2
        if i < mid:
            self._assign(2 * node, left, mid, i, x)
        else:
            self._assign(2 * node + 1, mid, right, i, x)
        self.tree[node] = max(
            self.tree[2 * node], self.tree[2 * node + 1]
        )

    def query(self, l, r):
        return self._query(1, 0, self.n, l, r)

    def _query(self, node, left, right, l, r):
        if r <= left or right <= l:
            return -(10**30)
        if l <= left and right <= r:
            return self.tree[node]
        mid = (left + right) // 2
        return max(
            self._query(2 * node, left, mid, l, r),
            self._query(2 * node + 1, mid, right, l, r),
        )


def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n, q = int(data[0]), int(data[1])
    pos = 2
    original = list(map(int, data[pos : pos + n]))
    pos += n
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = int(data[pos]) - 1, int(data[pos + 1]) - 1
        pos += 2
        g[u].append(v)
        g[v].append(u)
    tin = [0] * n
    tout = [0] * n
    order = []
    stack = [(0, -1, False)]
    while stack:
        u, parent, leaving = stack.pop()
        if leaving:
            tout[u] = len(order)
            continue
        tin[u] = len(order)
        order.append(u)
        stack.append((u, parent, True))
        for v in reversed(g[u]):
            if v != parent:
                stack.append((v, u, False))
    tree = SegmentTree([original[u] for u in order])

    out = []
    for _ in range(q):
        op = data[pos]
        u = int(data[pos + 1]) - 1
        pos += 2
        if op == b"Q":
            out.append(tree.query(tin[u], tout[u]))
        else:
            x = int(data[pos])
            pos += 1
            tree.assign(tin[u], x)
    sys.stdout.write("\n".join(map(str, out)) + ("\n" if out else ""))


if __name__ == "__main__":
    main()
