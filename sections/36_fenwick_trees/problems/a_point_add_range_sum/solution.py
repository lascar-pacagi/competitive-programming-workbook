import sys

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)
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
    def range_sum(self, l, r):
        return self.sum(r) - self.sum(l - 1)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, q = data[0], data[1]
    a = data[2:2 + n]
    bit = Fenwick(n)
    for i, x in enumerate(a, 1):
        bit.add(i, x)
    idx = 2 + n
    out = []
    for _ in range(q):
        typ = data[idx]
        idx += 1
        if typ == 1:
            i, x = data[idx], data[idx + 1]
            idx += 2
            bit.add(i, x)
        else:
            l, r = data[idx], data[idx + 1]
            idx += 2
            out.append(str(bit.range_sum(l, r)))
    print("\n".join(out))

if __name__ == "__main__":
    main()
