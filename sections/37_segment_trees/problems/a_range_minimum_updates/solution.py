import sys

INF = 10**30

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, q = data[0], data[1]
    a = data[2:2 + n]
    size = 1
    while size < n:
        size *= 2
    seg = [INF] * (2 * size)
    for i, x in enumerate(a):
        seg[size + i] = x
    for i in range(size - 1, 0, -1):
        seg[i] = min(seg[2 * i], seg[2 * i + 1])
    idx = 2 + n
    out = []
    for _ in range(q):
        typ, x, y = data[idx], data[idx + 1], data[idx + 2]
        idx += 3
        if typ == 1:
            p = size + x - 1
            seg[p] = y
            p //= 2
            while p:
                seg[p] = min(seg[2 * p], seg[2 * p + 1])
                p //= 2
        else:
            l, r = x - 1 + size, y + size
            ans = INF
            while l < r:
                if l & 1:
                    ans = min(ans, seg[l])
                    l += 1
                if r & 1:
                    r -= 1
                    ans = min(ans, seg[r])
                l //= 2
                r //= 2
            out.append(str(ans))
    print("\n".join(out))

if __name__ == "__main__":
    main()
