import sys

def main():
    d = list(map(int, sys.stdin.buffer.read().split()))
    if not d:
        return
    n, q = d[:2]
    z = 1
    while z < n:
        z *= 2
    neg = -10 ** 30
    t = [(0, neg, neg, neg)] * (2 * z)

    def one(x):
        return (x, x, x, x)

    def join(a, b):
        return (
            a[0] + b[0],
            max(a[1], a[0] + b[1]),
            max(b[2], b[0] + a[2]),
            max(a[3], b[3], a[2] + b[1]),
        )
    for i, x in enumerate(d[2:2 + n]):
        t[z + i] = one(x)
    for i in range(z - 1, 0, -1):
        t[i] = join(t[2 * i], t[2 * i + 1])
    j = 2 + n
    out = []
    for _ in range(q):
        p, x = d[j:j + 2]
        j += 2
        p = z + p - 1
        t[p] = one(x)
        p //= 2
        while p:
            t[p] = join(t[2 * p], t[2 * p + 1])
            p //= 2
        out.append(str(t[1][3]))
    print('\n'.join(out))
if __name__ == '__main__':
    main()
