import sys


def main():
    data = sys.stdin.buffer.read().split()
    n, m, q = int(data[0]), int(data[1]), int(data[2])
    total = n + m + 1
    INF = 1 << 60
    L = [0] * total
    R = [0] * total
    P = [0] * total
    val = [INF] * total
    mn = list(range(total))
    rev = [False] * total

    def pull(x):
        best = x
        bv = val[x]
        c = L[x]
        if c and val[mn[c]] < bv:
            best = mn[c]
            bv = val[best]
        c = R[x]
        if c and val[mn[c]] < bv:
            best = mn[c]
        mn[x] = best

    def push(x):
        if rev[x]:
            a = L[x]
            b = R[x]
            if a:
                L[a], R[a] = R[a], L[a]
                rev[a] = not rev[a]
            if b:
                L[b], R[b] = R[b], L[b]
                rev[b] = not rev[b]
            rev[x] = False

    def is_root(x):
        p = P[x]
        return not p or (L[p] != x and R[p] != x)

    def rotate(x):
        p = P[x]
        g = P[p]
        if L[p] == x:
            b = R[x]
            L[p] = b
            R[x] = p
        else:
            b = L[x]
            R[p] = b
            L[x] = p
        if b:
            P[b] = p
        if g and (L[g] == p or R[g] == p):
            if L[g] == p:
                L[g] = x
            else:
                R[g] = x
        P[x] = g
        P[p] = x
        pull(p)
        pull(x)

    def splay(x):
        path = [x]
        y = x
        while not is_root(y):
            y = P[y]
            path.append(y)
        for y in reversed(path):
            push(y)
        while not is_root(x):
            p = P[x]
            if not is_root(p):
                g = P[p]
                if (L[g] == p) == (L[p] == x):
                    rotate(p)
                else:
                    rotate(x)
            rotate(x)

    def access(x):
        last = 0
        while x:
            splay(x)
            R[x] = last
            pull(x)
            last = x
            x = P[x]

    def make_root(x):
        access(x)
        splay(x)
        L[x], R[x] = R[x], L[x]
        rev[x] = not rev[x]

    def find_root(x):
        access(x)
        splay(x)
        while True:
            push(x)
            if not L[x]:
                break
            x = L[x]
        splay(x)
        return x

    def link(x, y):
        make_root(x)
        P[x] = y

    def cut(x, y):
        make_root(x)
        access(y)
        splay(y)
        L[y] = 0
        P[x] = 0
        pull(y)

    eu = [0] * (m + 1)
    ev = [0] * (m + 1)
    pre = [0] * (m + 1)
    pos = 3
    for i in range(1, m + 1):
        u = int(data[pos])
        v = int(data[pos + 1])
        pos += 2
        eu[i] = u
        ev[i] = v
        node = n + i
        val[node] = i
        mn[node] = node
        if u == v:
            pre[i] = i
            continue
        if find_root(u) == find_root(v):
            make_root(u)
            access(v)
            splay(v)
            oldest = mn[v]
            j = oldest - n
            pre[i] = j
            cut(eu[j], oldest)
            cut(oldest, ev[j])
        link(u, node)
        link(node, v)

    # Offline: count i in [l, r] with pre[i] < l, sweeping l upward.
    ql = [0] * q
    qr = [0] * q
    for i in range(q):
        ql[i] = int(data[pos])
        qr[i] = int(data[pos + 1])
        pos += 2
    order = sorted(range(q), key=ql.__getitem__)
    by_pre = sorted(range(1, m + 1), key=pre.__getitem__)
    bit = [0] * (m + 1)
    answer = [0] * q
    ptr = 0
    for qi in order:
        l = ql[qi]
        while ptr < m and pre[by_pre[ptr]] < l:
            k = by_pre[ptr]
            while k <= m:
                bit[k] += 1
                k += k & -k
            ptr += 1
        s = 0
        k = qr[qi]
        while k > 0:
            s += bit[k]
            k &= k - 1
        k = l - 1
        while k > 0:
            s -= bit[k]
            k &= k - 1
        answer[qi] = n - s
    sys.stdout.write("\n".join(map(str, answer)) + "\n")


if __name__ == "__main__":
    main()
