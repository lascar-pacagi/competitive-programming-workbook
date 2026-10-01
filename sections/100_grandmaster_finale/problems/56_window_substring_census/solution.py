import sys


def main():
    data = sys.stdin.buffer.read().split()
    s = data[0]
    n = len(s)
    q = int(data[1])

    # Suffix automaton with dict transitions.
    size = 2 * n + 1
    length = [0] * size
    link = [-1] * size
    trans = [None] * size
    trans[0] = {}
    prefix_state = [0] * (n + 1)
    states = 1
    last = 0
    for i in range(n):
        c = s[i]
        cur = states
        states += 1
        length[cur] = length[last] + 1
        trans[cur] = {}
        p = last
        while p != -1 and c not in trans[p]:
            trans[p][c] = cur
            p = link[p]
        if p == -1:
            link[cur] = 0
        else:
            qq = trans[p][c]
            if length[p] + 1 == length[qq]:
                link[cur] = qq
            else:
                clone = states
                states += 1
                length[clone] = length[p] + 1
                trans[clone] = dict(trans[qq])
                link[clone] = link[qq]
                while p != -1 and trans[p].get(c) == qq:
                    trans[p][c] = clone
                    p = link[p]
                link[qq] = clone
                link[cur] = clone
        last = cur
        prefix_state[i + 1] = cur
    del trans

    # Link-cut tree over suffix links; node id = state + 1, 0 is null.
    N = states + 1
    L = [0] * N
    R = [0] * N
    fa = [0] * N
    colour = [0] * N
    tag = [0] * N
    leftmost = list(range(N))
    low_len = [0] * N  # len(link(state)) or 0 for the root
    node_len = [0] * N
    for v in range(1, N):
        st = v - 1
        node_len[v] = length[st]
        if link[st] >= 0:
            fa[v] = link[st] + 1
            low_len[v] = length[link[st]]

    def is_root(x):
        p = fa[x]
        return not p or (L[p] != x and R[p] != x)

    def push(x):
        t = tag[x]
        if t:
            a = L[x]
            if a:
                colour[a] = tag[a] = t
            b = R[x]
            if b:
                colour[b] = tag[b] = t
            tag[x] = 0

    def rotate(x):
        p = fa[x]
        g = fa[p]
        if g and (L[g] == p or R[g] == p):
            if L[g] == p:
                L[g] = x
            else:
                R[g] = x
        fa[x] = g
        if R[p] == x:
            b = L[x]
            R[p] = b
            if b:
                fa[b] = p
            L[x] = p
        else:
            b = R[x]
            L[p] = b
            if b:
                fa[b] = p
            R[x] = p
        fa[p] = x
        leftmost[p] = leftmost[L[p]] if L[p] else p
        leftmost[x] = leftmost[L[x]] if L[x] else x

    def splay(x):
        path = [x]
        y = x
        while not is_root(y):
            y = fa[y]
            path.append(y)
        for y in reversed(path):
            push(y)
        while not is_root(x):
            p = fa[x]
            if not is_root(p):
                g = fa[p]
                if (L[g] == p) == (L[p] == x):
                    rotate(p)
                else:
                    rotate(x)
            rotate(x)

    # Fenwick trees for range add / range sum over start positions.
    A = [0] * (n + 2)
    B = [0] * (n + 2)
    top_index = n + 1

    def range_add(l, r, v):
        if l > r:
            return
        i = l
        vb = v * (l - 1)
        while i <= top_index:
            A[i] += v
            B[i] += vb
            i += i & -i
        i = r + 1
        vb = v * r
        while i <= top_index:
            A[i] -= v
            B[i] -= vb
            i += i & -i

    def prefix(i):
        sa = 0
        sb = 0
        k = i
        while k > 0:
            sa += A[k]
            sb += B[k]
            k &= k - 1
        return sa * i - sb

    def access(start, r):
        x = start
        y = 0
        while x:
            splay(x)
            c = colour[x]
            if c:
                top = leftmost[L[x]] if L[x] else x
                range_add(c - node_len[x] + 1, c - low_len[top], -1)
            R[x] = y
            leftmost[x] = leftmost[L[x]] if L[x] else x
            y = x
            x = fa[x]
        splay(start)
        colour[start] = tag[start] = r
        range_add(1, r, 1)

    ql = [0] * q
    qr = [0] * q
    for i in range(q):
        ql[i] = int(data[2 + 2 * i])
        qr[i] = int(data[3 + 2 * i])
    answer = [0] * q
    done = 0
    for i in sorted(range(q), key=qr.__getitem__):
        r = qr[i]
        while done < r:
            done += 1
            access(prefix_state[done] + 1, done)
        answer[i] = prefix(r) - prefix(ql[i] - 1)
    sys.stdout.write("\n".join(map(str, answer)) + "\n")


if __name__ == "__main__":
    main()
