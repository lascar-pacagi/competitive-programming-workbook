import sys

MOD = 998_244_353
IDENTITY = (1, 0, 0, 1)


def mul(x, y):
    return (
        (x[0] * y[0] + x[1] * y[2]) % MOD,
        (x[0] * y[1] + x[1] * y[3]) % MOD,
        (x[2] * y[0] + x[3] * y[2]) % MOD,
        (x[2] * y[1] + x[3] * y[3]) % MOD,
    )


def merge(x, y):
    return mul(x[0], y[0]), mul(y[1], x[1])


def main():
    t = sys.stdin.buffer.read().split()
    if not t:
        return
    z = 0
    n = int(t[z])
    q = int(t[z + 1])
    z += 2
    values = []
    for _ in range(n):
        values.append(tuple(map(int, t[z : z + 4])))
        z += 4
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u = int(t[z]) - 1
        v = int(t[z + 1]) - 1
        z += 2
        g[u].append(v)
        g[v].append(u)
    parent = [-1] * n
    depth = [0] * n
    order = [0]
    for u in order:
        for v in g[u]:
            if v != parent[u]:
                parent[v] = u
                depth[v] = depth[u] + 1
                order.append(v)
    size = [1] * n
    heavy = [-1] * n
    for u in reversed(order[1:]):
        p = parent[u]
        size[p] += size[u]
        heavy[p] = u if heavy[p] < 0 or size[u] > size[heavy[p]] else heavy[p]
    head = [0] * n
    pos = [0] * n
    timer = 0
    todo = [(0, 0)]
    while todo:
        u, h = todo.pop()
        while u != -1:
            head[u] = h
            pos[u] = timer
            timer += 1
            for v in g[u]:
                if parent[v] == u and v != heavy[u]:
                    todo.append((v, v))
            u = heavy[u]
    base = 1
    while base < n:
        base *= 2
    tree = [(IDENTITY, IDENTITY) for _ in range(2 * base)]
    for u, m in enumerate(values):
        tree[base + pos[u]] = (m, m)
    for p in range(base - 1, 0, -1):
        tree[p] = merge(tree[2 * p], tree[2 * p + 1])

    def query(l, r):
        x = y = (IDENTITY, IDENTITY)
        l += base
        r += base + 1
        while l < r:
            if l & 1:
                x = merge(x, tree[l])
                l += 1
            if r & 1:
                r -= 1
                y = merge(tree[r], y)
            l //= 2
            r //= 2
        return merge(x, y)

    out = []
    for _ in range(q):
        kind = t[z].decode()
        u = int(t[z + 1]) - 1
        z += 2
        if kind == "U":
            m = tuple(map(int, t[z : z + 4]))
            z += 4
            p = base + pos[u]
            tree[p] = (m, m)
            p //= 2
            while p:
                tree[p] = merge(tree[2 * p], tree[2 * p + 1])
                p //= 2
        else:
            v = int(t[z]) - 1
            z += 1
            left = right = IDENTITY
            while head[u] != head[v]:
                if depth[head[u]] >= depth[head[v]]:
                    left = mul(left, query(pos[head[u]], pos[u])[1])
                    u = parent[head[u]]
                else:
                    right = mul(query(pos[head[v]], pos[v])[0], right)
                    v = parent[head[v]]
            middle = (
                query(pos[u], pos[v])[0]
                if pos[u] <= pos[v]
                else query(pos[v], pos[u])[1]
            )
            out.append(" ".join(map(str, mul(mul(left, middle), right))))
    print("\n".join(out))


if __name__ == "__main__":
    main()
