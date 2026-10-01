import sys
from array import array


def main():
    data = sys.stdin.buffer.read().split()
    n, q = int(data[0]), int(data[1])
    label = data[2]
    adj = [[] for _ in range(n + 1)]
    ptr = 3
    for _ in range(n - 1):
        u = int(data[ptr])
        v = int(data[ptr + 1])
        ptr += 2
        adj[u].append(v)
        adj[v].append(u)
    qu = [0] * q
    qv = [0] * q
    pats = [b""] * q
    for i in range(q):
        qu[i] = int(data[ptr])
        qv[i] = int(data[ptr + 1])
        pats[i] = data[ptr + 2]
        ptr += 3
    del data

    # Rooted tree, depths, binary lifting.
    parent = [0] * (n + 1)
    depth = [0] * (n + 1)
    order = [1]
    parent[1] = 0
    seen = [False] * (n + 1)
    seen[1] = True
    for v in order:
        for w in adj[v]:
            if not seen[w]:
                seen[w] = True
                parent[w] = v
                depth[w] = depth[v] + 1
                order.append(w)
    LOG = max(1, (n).bit_length())
    up = [array("i", parent)]
    for k in range(1, LOG):
        prev = up[-1]
        up.append(array("i", [prev[prev[v]] for v in range(n + 1)]))

    def ancestor_at_depth(v, d):
        diff = depth[v] - d
        k = 0
        while diff:
            if diff & 1:
                v = up[k][v]
            diff >>= 1
            k += 1
        return v

    def lca(a, b):
        if depth[a] < depth[b]:
            a, b = b, a
        a = ancestor_at_depth(a, depth[b])
        if a == b:
            return a
        for k in range(LOG - 1, -1, -1):
            if up[k][a] != up[k][b]:
                a = up[k][a]
                b = up[k][b]
        return parent[a]

    # Aho--Corasick automaton of every pattern and its reversal.
    child = [{}]
    def insert(word):
        s = 0
        for c in word:
            nxt = child[s].get(c)
            if nxt is None:
                nxt = len(child)
                child.append({})
                child[s][c] = nxt
            s = nxt
        return s

    node_fwd = [insert(p) for p in pats]
    node_rev = [insert(p[::-1]) for p in pats]
    T = len(child)
    fail = [0] * T
    bfs = [0]
    for s in bfs:
        for c, t in child[s].items():
            if s:
                f = fail[s]
                while f and c not in child[f]:
                    f = fail[f]
                g = child[f].get(c, 0)
                fail[t] = g if g != t else 0
            bfs.append(t)
    # Euler tour of the fail tree.
    fchildren = [[] for _ in range(T)]
    for t in range(1, T):
        fchildren[fail[t]].append(t)
    tin = [0] * T
    tout = [0] * T
    timer = 0
    stack = [(0, False)]
    while stack:
        s, done = stack.pop()
        if done:
            tout[s] = timer
            continue
        timer += 1
        tin[s] = timer
        stack.append((s, True))
        for t in fchildren[s]:
            stack.append((t, False))
    del fchildren

    memo = [None] * T

    def goto(s, c):
        path = []
        t = s
        while True:
            nxt = child[t].get(c)
            if nxt is not None:
                break
            m = memo[t]
            if m is not None and c in m:
                nxt = m[c]
                break
            if t == 0:
                nxt = 0
                break
            path.append(t)
            t = fail[t]
        for x in path:
            if memo[x] is None:
                memo[x] = {}
            memo[x][c] = nxt
        return nxt

    # Occurrences are counted by their bottom vertex x on a vertical segment:
    # the root-to-x string must end with the pattern (downward half) or with
    # its reversal (upward half).  Events: (vertex, automaton node, sign, id).
    events = [[] for _ in range(n + 1)]
    answer = [0] * q
    for i in range(q):
        u, v, p = qu[i], qv[i], pats[i]
        L = len(p)
        l = lca(u, v)
        dl = depth[l]
        if depth[u] >= dl + L - 1:
            w = ancestor_at_depth(u, dl + L - 1)
            events[u].append((node_rev[i], 1, i))
            if parent[w]:
                events[parent[w]].append((node_rev[i], -1, i))
        if v != l and depth[v] >= dl + L:
            w = ancestor_at_depth(v, dl + L)
            events[v].append((node_fwd[i], 1, i))
            events[parent[w]].append((node_fwd[i], -1, i))
        if L >= 2 and v != l:
            a = min(L - 1, depth[u] - dl + 1)
            b = min(L - 1, depth[v] - dl)
            if a + b >= L:
                x = ancestor_at_depth(u, dl + a - 1)
                left = []
                while True:
                    left.append(label[x - 1])
                    if x == l:
                        break
                    x = parent[x]
                y = ancestor_at_depth(v, dl + b)
                right = []
                while y != l:
                    right.append(label[y - 1])
                    y = parent[y]
                right.reverse()
                text = left + right
                # KMP: occurrences starting before the junction and ending after it.
                fail_p = [0] * L
                k = 0
                for idx in range(1, L):
                    while k and p[idx] != p[k]:
                        k = fail_p[k - 1]
                    if p[idx] == p[k]:
                        k += 1
                    fail_p[idx] = k
                k = 0
                count = 0
                for idx, c in enumerate(text):
                    while k and c != p[k]:
                        k = fail_p[k - 1]
                    if c == p[k]:
                        k += 1
                    if k == L:
                        start = idx - L + 1
                        if start < a <= idx:
                            count += 1
                        k = fail_p[k - 1]
                answer[i] += count

    # DFS down the tree with a Fenwick tree over fail-tree Euler positions.
    bit = [0] * (T + 1)

    def bit_add(i, x):
        while i <= T:
            bit[i] += x
            i += i & -i

    def bit_sum(i):
        s = 0
        while i > 0:
            s += bit[i]
            i &= i - 1
        return s

    state = [0] * (n + 1)
    stack = [(1, False)]
    while stack:
        v, done = stack.pop()
        if done:
            bit_add(tin[state[v]], -1)
            continue
        st = goto(state[parent[v]] if v != 1 else 0, label[v - 1])
        state[v] = st
        bit_add(tin[st], 1)
        for node, sign, i in events[v]:
            answer[i] += sign * (bit_sum(tout[node]) - bit_sum(tin[node] - 1))
        stack.append((v, True))
        for w in adj[v]:
            if w != parent[v]:
                stack.append((w, False))
    sys.stdout.write("\n".join(map(str, answer)) + "\n")


if __name__ == "__main__":
    main()
