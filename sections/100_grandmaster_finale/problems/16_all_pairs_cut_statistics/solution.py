import sys
from collections import deque


class Dinic:
    def __init__(self, n: int) -> None:
        self.graph = [[] for _ in range(n)]

    def add_undirected(self, u: int, v: int, capacity: int) -> None:
        forward = [v, len(self.graph[v]), capacity]
        backward = [u, len(self.graph[u]), capacity]
        self.graph[u].append(forward)
        self.graph[v].append(backward)

    def max_flow(self, source: int, sink: int) -> int:
        answer = 0
        n = len(self.graph)
        while True:
            level = [-1] * n
            level[source] = 0
            queue = deque([source])
            while queue:
                u = queue.popleft()
                for v, _, capacity in self.graph[u]:
                    if capacity and level[v] == -1:
                        level[v] = level[u] + 1
                        queue.append(v)
            if level[sink] == -1:
                break
            next_edge = [0] * n

            def send(u: int, pushed: int) -> int:
                if u == sink:
                    return pushed
                while next_edge[u] < len(self.graph[u]):
                    edge = self.graph[u][next_edge[u]]
                    v, reverse, capacity = edge
                    if capacity and level[v] == level[u] + 1:
                        flow = send(v, min(pushed, capacity))
                        if flow:
                            edge[2] -= flow
                            self.graph[v][reverse][2] += flow
                            return flow
                    next_edge[u] += 1
                return 0

            while True:
                pushed = send(source, 10**30)
                if not pushed:
                    break
                answer += pushed
        return answer

    def source_side(self, source: int) -> list[bool]:
        seen = [False] * len(self.graph)
        seen[source] = True
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for v, _, capacity in self.graph[u]:
                if capacity and not seen[v]:
                    seen[v] = True
                    queue.append(v)
        return seen


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m, q = data[:3]
    index = 3
    edges = []
    for _ in range(m):
        u, v, capacity = data[index:index + 3]
        index += 3
        edges.append((u - 1, v - 1, capacity))
    queries = data[index:index + q]

    parent = [0] * n
    cut_value = [0] * n
    for s in range(1, n):
        t = parent[s]
        flow = Dinic(n)
        for u, v, capacity in edges:
            flow.add_undirected(u, v, capacity)
        value = flow.max_flow(s, t)
        side = flow.source_side(s)
        for v in range(s + 1, n):
            if parent[v] == t and side[v]:
                parent[v] = s
        if side[parent[t]]:
            parent[s] = parent[t]
            parent[t] = s
            cut_value[s] = cut_value[t]
            cut_value[t] = value
        else:
            cut_value[s] = value

    tree_edges = sorted(((cut_value[v], v, parent[v]) for v in range(1, n)),
                        reverse=True)
    ordered_queries = sorted(((threshold, i) for i, threshold in enumerate(queries)),
                             reverse=True)
    dsu_parent = list(range(n))
    dsu_size = [1] * n

    def find(x: int) -> int:
        while dsu_parent[x] != x:
            dsu_parent[x] = dsu_parent[dsu_parent[x]]
            x = dsu_parent[x]
        return x

    answers = [0] * q
    pairs = 0
    edge_index = 0
    for threshold, query_index in ordered_queries:
        while edge_index < len(tree_edges) and tree_edges[edge_index][0] >= threshold:
            _, u, v = tree_edges[edge_index]
            edge_index += 1
            u, v = find(u), find(v)
            if u != v:
                if dsu_size[u] < dsu_size[v]:
                    u, v = v, u
                pairs += dsu_size[u] * dsu_size[v]
                dsu_parent[v] = u
                dsu_size[u] += dsu_size[v]
        answers[query_index] = pairs
    print("\n".join(map(str, answers)))


if __name__ == "__main__":
    main()
