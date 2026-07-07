import sys

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 2)
    def add(self, i, delta):
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i
    def sum(self, i):
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, q = data[0], data[1]
    a = data[2:2 + n]
    bit = Fenwick(n + 1)
    prev = 0
    for i, x in enumerate(a, 1):
        bit.add(i, x - prev)
        prev = x
    idx = 2 + n
    out = []
    for _ in range(q):
        typ = data[idx]
        idx += 1
        if typ == 1:
            l, r, x = data[idx], data[idx + 1], data[idx + 2]
            idx += 3
            bit.add(l, x)
            bit.add(r + 1, -x)
        else:
            i = data[idx]
            idx += 1
            out.append(str(bit.sum(i)))
    print("\n".join(out))

if __name__ == "__main__":
    main()
