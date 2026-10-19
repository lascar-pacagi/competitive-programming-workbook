import sys


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
    vertices = sorted(range(n), key=lambda u: original[u])
    events = []
    out = [0] * q
    for i in range(q):
        u, lo, hi = map(int, data[pos : pos + 3])
        pos += 3
        u -= 1
        events.append((hi, u, i, 1))
        events.append((lo - 1, u, i, -1))
    bit = [0] * (n + 1)

    def prefix(i):
        total = 0
        while i:
            total += bit[i]
            i -= i & -i
        return total

    current = 0
    for bound, u, i, sign in sorted(events):
        while current < n and original[vertices[current]] <= bound:
            j = tin[vertices[current]] + 1
            while j <= n:
                bit[j] += 1
                j += j & -j
            current += 1
        out[i] += sign * (prefix(tout[u]) - prefix(tin[u]))
    print("\n".join(map(str, out)))


if __name__ == "__main__":
    main()
