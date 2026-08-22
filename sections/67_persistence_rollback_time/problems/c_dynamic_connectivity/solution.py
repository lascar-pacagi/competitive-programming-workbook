import sys


def main() -> None:
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    n, q = map(int, tokens[:2])
    idx = 2
    ops = []
    opened = {}
    seg = [[] for _ in range(4 * q + 4)]

    def add(node, lo, hi, ql, qr, edge):
        if ql >= hi or qr <= lo:
            return
        if ql <= lo and hi <= qr:
            seg[node].append(edge)
            return
        mid = (lo + hi) // 2
        add(node * 2, lo, mid, ql, qr, edge)
        add(node * 2 + 1, mid, hi, ql, qr, edge)

    for time in range(q):
        kind = tokens[idx].decode()
        u = int(tokens[idx + 1]) - 1
        v = int(tokens[idx + 2]) - 1
        idx += 3
        if u > v:
            u, v = v, u
        ops.append((kind, u, v))
        edge = (u, v)
        if kind == "+":
            opened[edge] = time
        elif kind == "-":
            add(1, 0, q, opened.pop(edge), time, edge)
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

    def rollback(snapshot):
        while len(history) > snapshot:
            b, old = history.pop()
            a = parent[b]
            size[a] = old
            parent[b] = b

    output = []

    def dfs(node, lo, hi):
        snapshot = len(history)
        for u, v in seg[node]:
            join(u, v)
        if hi - lo == 1:
            kind, u, v = ops[lo]
            if kind == "?":
                output.append("YES" if find(u) == find(v) else "NO")
        else:
            mid = (lo + hi) // 2
            dfs(node * 2, lo, mid)
            dfs(node * 2 + 1, mid, hi)
        rollback(snapshot)

    if q:
        dfs(1, 0, q)
    print("\n".join(output))


if __name__ == "__main__":
    main()
