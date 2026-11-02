import sys
from collections import deque


class BipartiteMatching:
    """Independent 0-based IDs on each side. -1 means unmatched."""

    def __init__(self, left_count, right_count):
        self.adj = [[] for _ in range(left_count)]
        self.left = [-1] * left_count
        self.right = [-1] * right_count

    def add_edge(self, u, v):
        assert 0 <= u < len(self.left) and 0 <= v < len(self.right)
        self.adj[u].append(v)

    def _augment(self, root):
        previous = [-1] * len(self.right)
        seen = [False] * len(self.left)
        seen[root] = True
        queue = deque([root])
        while queue:
            u = queue.popleft()
            for v in self.adj[u]:
                if previous[v] != -1:
                    continue
                previous[v] = u
                owner = self.right[v]
                if owner == -1:
                    # Follow predecessors and flip the entire path.
                    while v != -1:
                        u = previous[v]
                        old = self.left[u]
                        self.left[u] = v
                        self.right[v] = u
                        v = old
                    return True
                if not seen[owner]:
                    seen[owner] = True
                    queue.append(owner)
        return False

    def maximum_matching(self):
        for root in range(len(self.left)):
            if self.left[root] == -1:
                self._augment(root)
        return [(u, v) for u, v in enumerate(self.left) if v != -1]


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n, m, e = next(it), next(it), next(it)
    matching = BipartiteMatching(n, m)
    for _ in range(e):
        u, v = next(it), next(it)
        matching.add_edge(u - 1, v - 1)
    print(len(matching.maximum_matching()))


if __name__ == '__main__':
    main()
