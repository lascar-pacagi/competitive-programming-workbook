import sys

class Fenwick:

    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, delta):
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def kth(self, k):
        pos = 0
        bit = 1 << self.n.bit_length()
        while bit:
            nxt = pos + bit
            if nxt <= self.n and self.bit[nxt] < k:
                pos = nxt
                k -= self.bit[nxt]
            bit //= 2
        return pos + 1

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    a = data[1:1 + n]
    positions = data[1 + n:1 + 2 * n]
    bit = Fenwick(n)
    for i in range(1, n + 1):
        bit.add(i, 1)
    out = []
    for k in positions:
        idx = bit.kth(k)
        out.append(str(a[idx - 1]))
        bit.add(idx, -1)
    print(' '.join(out))
if __name__ == '__main__':
    main()
