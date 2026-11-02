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
    n, m, k, q = next(it), next(it), next(it), next(it)
    costs = [next(it) for _ in range(n)]
    starts = [next(it) - 1 for _ in range(k)]
    targets = [next(it) - 1 for _ in range(q)]
    protected = set(starts + targets)
    inf = sum(c for c in costs if c >= 0) + 1
    s, t = 2 * n, 2 * n + 1
    flow = Dinic(t + 1)
    for v, cost in enumerate(costs):
        capacity = inf if cost < 0 or v in protected else cost
        flow.add_edge(2 * v, 2 * v + 1, capacity)
    for v in starts:
        flow.add_edge(s, 2 * v, inf)
    for v in targets:
        flow.add_edge(2 * v + 1, t, inf)
    for _ in range(m):
        u, v = next(it) - 1, next(it) - 1
        flow.add_edge(2 * u + 1, 2 * v, inf)
    answer = flow.max_flow(s, t)
    print(-1 if answer >= inf else answer)


if __name__ == '__main__':
    main()
