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

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    a = data[1:1 + n]
    values = {x: i + 1 for i, x in enumerate(sorted(set(a)))}
    bit = Fenwick(len(values))
    inv = 0
    seen = 0
    for x in a:
        rank = values[x]
        inv += seen - bit.sum(rank)
        bit.add(rank, 1)
        seen += 1
    print(inv)

if __name__ == "__main__":
    main()
