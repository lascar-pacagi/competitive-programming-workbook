import sys


def main():
    data = sys.stdin.buffer.read().split()
    n, q = map(int, data[:2])
    pos = 2
    values = list(map(int, data[pos : pos + n]))
    pos += n
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = int(data[pos]) - 1, int(data[pos + 1]) - 1
        pos += 2
        graph[u].append(v)
        graph[v].append(u)
    parent = [0] * n
    depth = [0] * n
    tin = [0] * n
    tout = [0] * n
    order = []
    stack = [(0, 0, False)]
    while stack:
        u, p, leaving = stack.pop()
        if leaving:
            tout[u] = len(order)
            continue
        parent[u] = p
        tin[u] = len(order)
        order.append(u)
        stack.append((u, p, True))
        for v in graph[u]:
            if v != p:
                depth[v] = depth[u] + 1
                stack.append((v, u, False))
    up = [parent]
    for _ in range(1, n.bit_length()):
        prev = up[-1]
        up.append([prev[prev[u]] for u in range(n)])
    bit = [0] * (n + 1)

    def add(i, x):
        i += 1
        while i <= n:
            bit[i] += x
            i += i & -i

    def prefix(i):
        result = 0
        while i:
            result += bit[i]
            i -= i & -i
        return result

    for u in range(n):
        add(tin[u], values[u])
    total = sum(values)
    root = 0
    out = []
    for _ in range(q):
        op, u = data[pos], int(data[pos + 1]) - 1
        pos += 2
        if op == b"R":
            root = u
        elif op == b"U":
            x = int(data[pos])
            pos += 1
            delta = x - values[u]
            values[u] = x
            total += delta
            add(tin[u], delta)
        elif u == root:
            out.append(total)
        elif not (tin[u] <= tin[root] < tout[u]):
            out.append(prefix(tout[u]) - prefix(tin[u]))
        else:
            child = root
            distance = depth[root] - depth[u] - 1
            k = 0
            while distance:
                if distance & 1:
                    child = up[k][child]
                distance >>= 1
                k += 1
            out.append(total - prefix(tout[child]) + prefix(tin[child]))
    print("\n".join(map(str, out)))


if __name__ == "__main__":
    main()
