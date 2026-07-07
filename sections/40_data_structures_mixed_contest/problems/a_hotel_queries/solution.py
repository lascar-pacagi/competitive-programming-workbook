import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, q = data[0], data[1]
    a = data[2:2 + n]
    req = data[2 + n:2 + n + q]
    size = 1
    while size < n:
        size *= 2
    seg = [0] * (2 * size)
    for i, x in enumerate(a):
        seg[size + i] = x
    for i in range(size - 1, 0, -1):
        seg[i] = max(seg[2 * i], seg[2 * i + 1])
    out = []
    for x in req:
        if seg[1] < x:
            out.append("0")
            continue
        v = 1
        while v < size:
            if seg[2 * v] >= x:
                v *= 2
            else:
                v = 2 * v + 1
        pos = v - size
        seg[v] -= x
        v //= 2
        while v:
            seg[v] = max(seg[2 * v], seg[2 * v + 1])
            v //= 2
        out.append(str(pos + 1))
    print(" ".join(out))

if __name__ == "__main__":
    main()
