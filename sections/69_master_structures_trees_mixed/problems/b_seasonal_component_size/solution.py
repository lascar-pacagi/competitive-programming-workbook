import sys


def main():
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    idx = 0
    n = int(tokens[idx])
    q = int(tokens[idx + 1])
    idx += 2
    ops = []
    opened = {}
    seg = [[] for _ in range(4 * q + 4)]

    def add(x, l, r, ql, qr, e):
        if ql >= r or qr <= l:
            return
        if ql <= l and r <= qr:
            seg[x].append(e)
            return
        m = (l + r) // 2
        add(2 * x, l, m, ql, qr, e)
        add(2 * x + 1, m, r, ql, qr, e)

    for time in range(q):
        kind = tokens[idx].decode()
        u = int(tokens[idx + 1]) - 1
        idx += 2
        v = -1
        if kind != "S":
            v = int(tokens[idx]) - 1
            idx += 1
            if u > v:
                u, v = v, u
            if kind == "+":
                opened[(u, v)] = time
            else:
                add(1, 0, q, opened.pop((u, v)), time, (u, v))
        ops.append((kind, u, v))
    for edge, start in opened.items():
        add(1, 0, q, start, q, edge)
    parent = list(range(n))
    size = [1] * n
    history = []

    def find(x):
        while x != parent[x]:
            x = parent[x]
        return x

    def join(a, b):
        a = find(a)
        b = find(b)
        if a == b:
            return
        if size[a] < size[b]:
            a, b = b, a
        history.append((b, size[a]))
        parent[b] = a
        size[a] += size[b]

    def dfs(x, l, r):
        snap = len(history)
        for u, v in seg[x]:
            join(u, v)
        if r - l == 1:
            if ops[l][0] == "S":
                output.append(str(size[find(ops[l][1])]))
        else:
            m = (l + r) // 2
            dfs(2 * x, l, m)
            dfs(2 * x + 1, m, r)
        while len(history) > snap:
            b, old = history.pop()
            a = parent[b]
            size[a] = old
            parent[b] = b

    output = []
    if q:
        dfs(1, 0, q)
    print("\n".join(output))


if __name__ == "__main__":
    main()
