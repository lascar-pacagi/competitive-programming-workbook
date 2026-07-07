import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, q = data[0], data[1]
    a = data[2:2 + n]
    size = 1
    while size < n:
        size *= 2
    seg = [0] * (2 * size)
    lazy = [0] * (2 * size)
    for i, x in enumerate(a):
        seg[size + i] = x
    for i in range(size - 1, 0, -1):
        seg[i] = seg[2 * i] + seg[2 * i + 1]
    def apply(v, length, delta):
        seg[v] += delta * length
        lazy[v] += delta
    def push(v, length):
        if lazy[v] and v < size:
            half = length // 2
            apply(2 * v, half, lazy[v])
            apply(2 * v + 1, half, lazy[v])
            lazy[v] = 0
    def add(v, tl, tr, l, r, x):
        if l <= tl and tr <= r:
            apply(v, tr - tl + 1, x)
            return
        push(v, tr - tl + 1)
        tm = (tl + tr) // 2
        if l <= tm:
            add(2 * v, tl, tm, l, r, x)
        if tm < r:
            add(2 * v + 1, tm + 1, tr, l, r, x)
        seg[v] = seg[2 * v] + seg[2 * v + 1]
    def query(v, tl, tr, l, r):
        if l <= tl and tr <= r:
            return seg[v]
        push(v, tr - tl + 1)
        tm = (tl + tr) // 2
        ans = 0
        if l <= tm:
            ans += query(2 * v, tl, tm, l, r)
        if tm < r:
            ans += query(2 * v + 1, tm + 1, tr, l, r)
        return ans
    idx = 2 + n
    out = []
    for _ in range(q):
        typ = data[idx]
        idx += 1
        if typ == 1:
            l, r, x = data[idx], data[idx + 1], data[idx + 2]
            idx += 3
            add(1, 1, size, l, r, x)
        else:
            l, r = data[idx], data[idx + 1]
            idx += 2
            out.append(str(query(1, 1, size, l, r)))
    print("\n".join(out))

if __name__ == "__main__":
    main()
