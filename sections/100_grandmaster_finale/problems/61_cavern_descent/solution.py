import sys

LIM = 100000


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    a = [int(v) for v in data[1:1 + n]]
    b = [int(v) for v in data[1 + n:1 + 2 * n]]
    adj = [[] for _ in range(n)]
    pos = 1 + 2 * n
    for _ in range(n - 1):
        u = int(data[pos]) - 1
        v = int(data[pos + 1]) - 1
        pos += 2
        adj[u].append(v)
        adj[v].append(u)

    # Li Chao node pool; index 0 is the null node.  Nodes emptied by a merge
    # are recycled, so the pool never holds more than n + 1 nodes.
    K = [0]
    M = [0]
    L = [0]
    R = [0]
    free = []

    def new_node(k, m):
        if free:
            t = free.pop()
            K[t] = k
            M[t] = m
            L[t] = 0
            R[t] = 0
            return t
        K.append(k)
        M.append(m)
        L.append(0)
        R.append(0)
        return len(K) - 1

    def insert(t, lo, hi, k, m):
        if not t:
            return new_node(k, m)
        root = t
        while True:
            mid = (lo + hi) >> 1
            tk = K[t]
            tm = M[t]
            left_better = k * lo + m < tk * lo + tm
            mid_better = k * mid + m < tk * mid + tm
            if mid_better:
                K[t] = k
                M[t] = m
                k = tk
                m = tm
            if lo == hi:
                return root
            if left_better != mid_better:
                child = L[t]
                if not child:
                    L[t] = new_node(k, m)
                    return root
                t = child
                hi = mid
            else:
                child = R[t]
                if not child:
                    R[t] = new_node(k, m)
                    return root
                t = child
                lo = mid + 1

    def merge(x, y, lo, hi):
        if not x or not y:
            return x or y
        x = insert(x, lo, hi, K[y], M[y])
        yl = L[y]
        yr = R[y]
        free.append(y)
        if lo == hi:
            return x
        mid = (lo + hi) >> 1
        L[x] = merge(L[x], yl, lo, mid)
        R[x] = merge(R[x], yr, mid + 1, hi)
        return x

    def query(t, x):
        best = None
        lo = -LIM
        hi = LIM
        while t:
            value = K[t] * x + M[t]
            if best is None or value < best:
                best = value
            mid = (lo + hi) >> 1
            if x <= mid:
                t = L[t]
                hi = mid
            else:
                t = R[t]
                lo = mid + 1
        return best

    parent = [-1] * n
    parent[0] = 0
    order = []
    stack = [0]
    while stack:
        v = stack.pop()
        order.append(v)
        for w in adj[v]:
            if parent[w] < 0:
                parent[w] = v
                stack.append(w)
    tree = [0] * n
    dp = [0] * n
    for v in reversed(order):
        t = tree[v]
        value = query(t, a[v]) if t else 0
        dp[v] = value
        t = insert(t, -LIM, LIM, b[v], value)
        if v:
            p = parent[v]
            tree[p] = merge(tree[p], t, -LIM, LIM)
        tree[v] = 0
    sys.stdout.write(" ".join(map(str, dp)) + "\n")


if __name__ == "__main__":
    main()
