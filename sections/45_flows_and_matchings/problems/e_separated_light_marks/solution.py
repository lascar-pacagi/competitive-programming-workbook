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
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    h, w = map(int, data[:2])
    grid = data[2:]
    row = [[-1] * w for _ in range(h)]
    col = [[-1] * w for _ in range(h)]
    a = b = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 35:
                continue
            if j == 0 or grid[i][j - 1] == 35:
                a += 1
            row[i][j] = a - 1
    for j in range(w):
        for i in range(h):
            if grid[i][j] == 35:
                continue
            if i == 0 or grid[i - 1][j] == 35:
                b += 1
            col[i][j] = b - 1
    matching = BipartiteMatching(a, b)
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 46:
                matching.add_edge(row[i][j], col[i][j])
    print(len(matching.maximum_matching()))


if __name__ == '__main__':
    main()
