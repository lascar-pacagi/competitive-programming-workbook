import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    pos = 0
    n = int(data[pos]); q = int(data[pos + 1]); pos += 2
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        a[i] = int(data[pos]); pos += 1

    size = 4 * n + 4
    sm = [0] * size
    addv = [0] * size
    asgv = [0] * size
    hasa = [False] * size

    def put_assign(x, ln, v):
        sm[x] = v * ln; asgv[x] = v; hasa[x] = True; addv[x] = 0

    def put_add(x, ln, v):
        sm[x] += v * ln
        if hasa[x]:
            asgv[x] += v
        else:
            addv[x] += v

    def push(x, l, r):
        m = (l + r) // 2; lc = 2 * x; rc = 2 * x + 1
        if hasa[x]:
            put_assign(lc, m - l + 1, asgv[x])
            put_assign(rc, r - m, asgv[x])
            hasa[x] = False; asgv[x] = 0
        if addv[x]:
            put_add(lc, m - l + 1, addv[x])
            put_add(rc, r - m, addv[x])
            addv[x] = 0

    def build(x, l, r):
        if l == r:
            sm[x] = a[l]; return
        m = (l + r) // 2
        build(2 * x, l, m); build(2 * x + 1, m + 1, r)
        sm[x] = sm[2 * x] + sm[2 * x + 1]

    def upd(x, l, r, ql, qr, v, is_assign):
        if qr < l or r < ql:
            return
        if ql <= l and r <= qr:
            if is_assign:
                put_assign(x, r - l + 1, v)
            else:
                put_add(x, r - l + 1, v)
            return
        push(x, l, r)
        m = (l + r) // 2
        upd(2 * x, l, m, ql, qr, v, is_assign)
        upd(2 * x + 1, m + 1, r, ql, qr, v, is_assign)
        sm[x] = sm[2 * x] + sm[2 * x + 1]

    def qry(x, l, r, ql, qr):
        if qr < l or r < ql:
            return 0
        if ql <= l and r <= qr:
            return sm[x]
        push(x, l, r)
        m = (l + r) // 2
        return (qry(2 * x, l, m, ql, qr)
                + qry(2 * x + 1, m + 1, r, ql, qr))

    sys.setrecursionlimit(300000)
    build(1, 1, n)
    out = []
    for _ in range(q):
        t = int(data[pos]); pos += 1
        if t == 3:
            l = int(data[pos]); r = int(data[pos + 1]); pos += 2
            out.append(qry(1, 1, n, l, r))
        else:
            l = int(data[pos]); r = int(data[pos + 1])
            x = int(data[pos + 2]); pos += 3
            upd(1, 1, n, l, r, x, t == 1)
    sys.stdout.write("\n".join(map(str, out)) + ("\n" if out else ""))

if __name__ == "__main__":
    main()
