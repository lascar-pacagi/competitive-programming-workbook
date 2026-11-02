import sys
from collections import deque


class Dinic:
    """0-based vertices; integer capacities; paired residual edge IDs."""

    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]
        self.to = []
        self.cap = []

    def add_edge(self, u, v, capacity):
        assert 0 <= u < self.n and 0 <= v < self.n
        assert capacity >= 0
        edge = len(self.to)
        self.adj[u].append(edge)
        self.to.append(v)
        self.cap.append(capacity)
        self.adj[v].append(edge ^ 1)
        self.to.append(u)
        self.cap.append(0)
        return edge

    def _bfs(self, s, t):
        self.level = [-1] * self.n
        self.level[s] = 0
        queue = deque([s])
        while queue:
            u = queue.popleft()
            for edge in self.adj[u]:
                v = self.to[edge]
                if self.cap[edge] > 0 and self.level[v] == -1:
                    self.level[v] = self.level[u] + 1
                    queue.append(v)
        return self.level[t] != -1

    def _send(self, s, t, limit):
        vertices = [s]
        path = []
        bottleneck = [limit]
        while vertices:
            u = vertices[-1]
            if u == t:
                delta = bottleneck[-1]
                for edge in path:
                    self.cap[edge] -= delta
                    self.cap[edge ^ 1] += delta
                return delta
            while self.ptr[u] < len(self.adj[u]):
                edge = self.adj[u][self.ptr[u]]
                v = self.to[edge]
                if (self.cap[edge] > 0
                        and self.level[v] == self.level[u] + 1):
                    break
                self.ptr[u] += 1
            if self.ptr[u] == len(self.adj[u]):
                vertices.pop()
                bottleneck.pop()
                if path:
                    path.pop()
                    self.ptr[vertices[-1]] += 1
            else:
                edge = self.adj[u][self.ptr[u]]
                path.append(edge)
                vertices.append(self.to[edge])
                bottleneck.append(min(bottleneck[-1], self.cap[edge]))
        return 0

    def max_flow(self, s, t):
        assert 0 <= s < self.n and 0 <= t < self.n and s != t
        added = 0
        # A finite upper bound on every possible augmentation.
        limit = sum(self.cap[edge] for edge in self.adj[s])
        while self._bfs(s, t):
            self.ptr = [0] * self.n
            while True:
                delta = self._send(s, t, limit)
                if delta == 0:
                    break
                added += delta
        return added

    def reachable(self, s):
        seen = [False] * self.n
        seen[s] = True
        queue = deque([s])
        while queue:
            u = queue.popleft()
            for edge in self.adj[u]:
                v = self.to[edge]
                if self.cap[edge] > 0 and not seen[v]:
                    seen[v] = True
                    queue.append(v)
        return seen


def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    if not values:
        return
    it = iter(values)
    n, p = next(it), next(it)
    calendar = [(next(it), next(it), next(it)) for _ in range(p)]
    jobs = [(next(it), next(it), next(it)) for _ in range(n)]
    if any(work > r - l for l, r, work in jobs):
        print(-1)
        return
    points = sorted({x for l, r, c in calendar + jobs for x in (l, r)})
    blocks = len(points) - 1
    base = []
    current = 0
    for x in points[:-1]:
        while x >= calendar[current][1]:
            current += 1
        base.append(calendar[current][2])
    total = sum(work for l, r, work in jobs)
    def feasible(extra):
        s, t = n + blocks, n + blocks + 1
        flow = Dinic(t + 1)
        for i, (l, r, work) in enumerate(jobs):
            flow.add_edge(s, i, work)
            for j in range(blocks):
                if l <= points[j] and points[j + 1] <= r:
                    flow.add_edge(i, n + j, points[j + 1] - points[j])
        for j in range(blocks):
            length = points[j + 1] - points[j]
            flow.add_edge(n + j, t, min(total, (base[j] + extra) * length))
        return flow.max_flow(s, t) == total
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    print(lo)


if __name__ == '__main__':
    main()
