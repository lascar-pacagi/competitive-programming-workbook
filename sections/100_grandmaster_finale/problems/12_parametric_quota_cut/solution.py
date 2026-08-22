import collections
import sys

INF = 10**30


class Dinic:
    def __init__(self, n):
        self.graph = [[] for _ in range(n)]
        self.level = [-1] * n
        self.next_edge = [0] * n

    def add_edge(self, u, v, capacity):
        self.graph[u].append([v, len(self.graph[v]), capacity])
        self.graph[v].append([u, len(self.graph[u]) - 1, 0])

    def max_flow(self, source, sink):
        total = 0
        n = len(self.graph)
        while True:
            self.level[:] = [-1] * n
            self.level[source] = 0
            queue = collections.deque([source])
            while queue:
                u = queue.popleft()
                for v, _, capacity in self.graph[u]:
                    if capacity and self.level[v] == -1:
                        self.level[v] = self.level[u] + 1
                        queue.append(v)
            if self.level[sink] == -1:
                return total
            self.next_edge[:] = [0] * n

            def send(u, pushed):
                if u == sink:
                    return pushed
                while self.next_edge[u] < len(self.graph[u]):
                    edge_index = self.next_edge[u]
                    edge = self.graph[u][edge_index]
                    v, reverse, capacity = edge
                    if capacity and self.level[v] == self.level[u] + 1:
                        sent = send(v, min(pushed, capacity))
                        if sent:
                            edge[2] -= sent
                            self.graph[v][reverse][2] += sent
                            return sent
                    self.next_edge[u] += 1
                return 0

            while True:
                pushed = send(source, INF)
                if not pushed:
                    break
                total += pushed


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    index = 0
    n, m, target = data[index:index + 3]
    index += 3
    profits = data[index:index + n]
    index += n
    dependencies = []
    for _ in range(m):
        dependencies.append((data[index] - 1, data[index + 1] - 1))
        index += 2

    def solve(penalty):
        source, sink = n, n + 1
        flow = Dinic(n + 2)
        for vertex, profit in enumerate(profits):
            adjusted = profit - penalty
            if adjusted > 0:
                flow.add_edge(source, vertex, adjusted)
            elif adjusted < 0:
                flow.add_edge(vertex, sink, -adjusted)
        for u, v in dependencies:
            flow.add_edge(u, v, INF)
        flow.max_flow(source, sink)
        reachable = [False] * (n + 2)
        reachable[source] = True
        queue = [source]
        for u in queue:
            for v, _, capacity in flow.graph[u]:
                if capacity and not reachable[v]:
                    reachable[v] = True
                    queue.append(v)
        size = 0
        original_profit = 0
        for vertex in range(n):
            if reachable[vertex]:
                size += 1
                original_profit += profits[vertex]
        return size, original_profit

    low, high = -1_000_000_001, 1_000_000_001
    while low < high:
        middle = (low + high) // 2
        if solve(middle)[0] <= target:
            high = middle
        else:
            low = middle + 1
    size, answer = solve(low)
    if size != target:
        raise RuntimeError("input violates the promised attainable cardinality")
    print(answer)


if __name__ == "__main__":
    sys.setrecursionlimit(1_000_000)
    main()
