import sys

NEG = -10**30

def merge(a, b):
    total = a[0] + b[0]
    pref = max(a[1], a[0] + b[1])
    suff = max(b[2], b[0] + a[2])
    best = max(a[3], b[3], a[2] + b[1])
    return (total, pref, suff, best)

def leaf(x):
    return (x, x, x, x)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, q = data[0], data[1]
    a = data[2:2 + n]
    size = 1
    while size < n:
        size *= 2
    neutral = (0, NEG, NEG, NEG)
    seg = [neutral] * (2 * size)
    for i, x in enumerate(a):
        seg[size + i] = leaf(x)
    for i in range(size - 1, 0, -1):
        seg[i] = merge(seg[2 * i], seg[2 * i + 1])
    idx = 2 + n
    out = []
    for _ in range(q):
        pos, val = data[idx], data[idx + 1]
        idx += 2
        p = size + pos - 1
        seg[p] = leaf(val)
        p //= 2
        while p:
            seg[p] = merge(seg[2 * p], seg[2 * p + 1])
            p //= 2
        out.append(str(seg[1][3]))
    print("\n".join(out))

if __name__ == "__main__":
    main()
