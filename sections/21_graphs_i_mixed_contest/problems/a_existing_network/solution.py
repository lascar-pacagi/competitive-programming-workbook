import sys


class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]
        return True


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    f = next(it)
    p = next(it)
    dsu = DSU(n)
    components = n
    for _ in range(f):
        u = next(it) - 1
        v = next(it) - 1
        if dsu.union(u, v):
            components -= 1
    edges = []
    for _ in range(p):
        u = next(it) - 1
        v = next(it) - 1
        w = next(it)
        edges.append((w, u, v))
    edges.sort()
    total = 0
    for w, u, v in edges:
        if components == 1:
            break
        if dsu.union(u, v):
            total += w
            components -= 1
    print(total if components == 1 else "IMPOSSIBLE")


if __name__ == "__main__":
    main()

