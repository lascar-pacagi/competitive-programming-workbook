import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, q = data[0], data[1]
    idx = 2
    LOG = max(1, n.bit_length())

    up = [[0] * (n + 1) for _ in range(LOG)]
    depth = [0] * (n + 1)
    root_sum = [0] * (n + 1)
    for v in range(2, n + 1):
        p, w = data[idx], data[idx + 1]
        idx += 2
        up[0][v] = p
        depth[v] = depth[p] + 1
        root_sum[v] = root_sum[p] + w
    for k in range(1, LOG):
        prev, cur = up[k - 1], up[k]
        for v in range(1, n + 1):
            cur[v] = prev[prev[v]]

    def lift(v, d):
        bit = 0
        while d:
            if d & 1:
                v = up[bit][v]
            d >>= 1
            bit += 1
        return v

    def lca(a, b):
        if depth[a] < depth[b]:
            a, b = b, a
        a = lift(a, depth[a] - depth[b])
        if a == b:
            return a
        for k in range(LOG - 1, -1, -1):
            if up[k][a] != up[k][b]:
                a = up[k][a]
                b = up[k][b]
        return up[0][a]

    out = []
    for _ in range(q):
        u, v = data[idx], data[idx + 1]
        idx += 2
        c = lca(u, v)
        out.append(str(root_sum[u] + root_sum[v] - 2 * root_sum[c]))
    print("\n".join(out))


if __name__ == "__main__":
    main()
