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

    def union(self, a: int, b: int) -> int:
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return self.size[ra]
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return self.size[ra]


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    dsu = DSU(n)
    components = n
    largest = 1
    out: list[str] = []
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        ru = dsu.find(u)
        rv = dsu.find(v)
        if ru != rv:
            merged = dsu.union(ru, rv)
            components -= 1
            largest = max(largest, merged)
        out.append(f"{components} {largest}")
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

