import sys


class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

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

    n, m = data[:2]
    edges = []
    total_cost = 0
    index = 2
    for _ in range(m):
        u, v, w = data[index:index + 3]
        index += 3
        edges.append((w, u, v))
        total_cost += w

    edges.sort()
    dsu = DSU(n)
    kept_cost = 0
    for w, u, v in edges:
        if dsu.union(u, v):
            kept_cost += w

    print(total_cost - kept_cost)


if __name__ == "__main__":
    main()
