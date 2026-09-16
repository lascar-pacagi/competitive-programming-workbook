import collections
import sys


class MinCostFlow:
    def __init__(self, n):
        self.graph = [[] for _ in range(n)]

    def add_edge(self, u, v, capacity, cost):
        self.graph[u].append([v, len(self.graph[v]), capacity, cost])
        self.graph[v].append([u, len(self.graph[u]) - 1, 0, -cost])

    def flow(self, source, sink, required):
        sent = total_cost = 0
        n = len(self.graph)
        while sent < required:
            distance = [None] * n
            parent = [None] * n
            queued = [False] * n
            queue = collections.deque([source])
            distance[source] = 0
            queued[source] = True
            while queue:
                u = queue.popleft()
                queued[u] = False
                for index, edge in enumerate(self.graph[u]):
                    v, _, capacity, cost = edge
                    if not capacity:
                        continue
                    candidate = distance[u] + cost
                    if distance[v] is not None and candidate >= distance[v]:
                        continue
                    distance[v] = candidate
                    parent[v] = (u, index)
                    if not queued[v]:
                        queued[v] = True
                        queue.append(v)
            if distance[sink] is None:
                break
            add = required - sent
            vertex = sink
            while vertex != source:
                u, index = parent[vertex]
                add = min(add, self.graph[u][index][2])
                vertex = u
            vertex = sink
            while vertex != source:
                u, index = parent[vertex]
                edge = self.graph[u][index]
                total_cost += add * edge[3]
                edge[2] -= add
                self.graph[vertex][edge[1]][2] += add
                vertex = u
            sent += add
        return sent, total_cost


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m, exact = data[:3]
    source, sink = data[3] - 1, data[4] - 1
    at = 5
    network = MinCostFlow(n + 2)
    balance = [0] * n
    mandatory_cost = 0

    def add_bounded(u, v, low, high, cost):
        nonlocal mandatory_cost
        balance[u] -= low
        balance[v] += low
        mandatory_cost += low * cost
        network.add_edge(u, v, high - low, cost)

    for _ in range(m):
        u, v, low, high, cost = data[at:at + 5]
        at += 5
        add_bounded(u - 1, v - 1, low, high, cost)
    add_bounded(sink, source, exact, exact, 0)

    super_source, super_sink = n, n + 1
    required = 0
    for vertex, value in enumerate(balance):
        if value > 0:
            network.add_edge(super_source, vertex, value, 0)
            required += value
        elif value < 0:
            network.add_edge(vertex, super_sink, -value, 0)

    sent, extra_cost = network.flow(super_source, super_sink, required)
    if sent != required:
        print("IMPOSSIBLE")
    else:
        print(mandatory_cost + extra_cost)


if __name__ == '__main__':
    main()
