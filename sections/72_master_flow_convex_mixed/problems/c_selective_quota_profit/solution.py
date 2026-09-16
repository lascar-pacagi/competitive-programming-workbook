import heapq
import sys


class MCF:
    def __init__(self, n):
        self.graph = [[] for _ in range(n)]

    def add_edge(self, u, v, capacity, cost):
        reference = (u, len(self.graph[u]))
        self.graph[u].append([v, capacity, cost, len(self.graph[v])])
        self.graph[v].append([u, 0, -cost, len(self.graph[u]) - 1])
        return reference

    def flow(self, source, sink, limit):
        n = len(self.graph)
        infinity = 10**40
        potential = [infinity] * n
        potential[source] = 0
        for _ in range(n):
            changed = False
            for u in range(n):
                if potential[u] == infinity:
                    continue
                for v, capacity, cost, _ in self.graph[u]:
                    if capacity and potential[v] > potential[u] + cost:
                        potential[v] = potential[u] + cost
                        changed = True
            if not changed:
                break
        potential = [0 if value == infinity else value for value in potential]

        sent = total_cost = 0
        while sent < limit:
            distance = [infinity] * n
            parent = [None] * n
            distance[source] = 0
            queue = [(0, source)]
            while queue:
                current, u = heapq.heappop(queue)
                if current != distance[u]:
                    continue
                for index, edge in enumerate(self.graph[u]):
                    v, capacity, cost, _ = edge
                    if not capacity:
                        continue
                    candidate = current + cost + potential[u] - potential[v]
                    if candidate < distance[v]:
                        distance[v] = candidate
                        parent[v] = (u, index)
                        heapq.heappush(queue, (candidate, v))
            if distance[sink] == infinity:
                break
            for v in range(n):
                if distance[v] < infinity:
                    potential[v] += distance[v]
            add = limit - sent
            vertex = sink
            while vertex != source:
                u, index = parent[vertex]
                add = min(add, self.graph[u][index][1])
                vertex = u
            vertex = sink
            while vertex != source:
                u, index = parent[vertex]
                edge = self.graph[u][index]
                total_cost += add * edge[2]
                edge[1] -= add
                self.graph[vertex][edge[3]][1] += add
                vertex = u
            sent += add
        return sent, total_cost


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, projects, m, chosen = data[:4]
    at = 4
    bounds = []
    for _ in range(projects):
        bounds.append(tuple(data[at:at + 2]))
        at += 2
    choices = []
    maximum_profit = 0
    for _ in range(m):
        worker, project, profit = data[at:at + 3]
        at += 3
        choices.append((worker - 1, project - 1, profit))
        maximum_profit = max(maximum_profit, profit)

    source = n + projects
    sink = source + 1
    network = MCF(sink + 1)
    for worker in range(n):
        network.add_edge(source, worker, 1, 0)
    for worker, project, profit in choices:
        network.add_edge(worker, n + project, 1, -profit)

    big = (chosen + 1) * (maximum_profit + 1)
    mandatory = []
    for project, (low, high) in enumerate(bounds):
        mandatory.append(
            network.add_edge(n + project, sink, low, -big)
        )
        network.add_edge(n + project, sink, high - low, 0)

    sent, cost = network.flow(source, sink, chosen)
    possible = sent == chosen and all(
        network.graph[u][index][1] == 0 for u, index in mandatory
    )
    if possible:
        print(-cost - big * sum(low for low, _ in bounds))
    else:
        print("IMPOSSIBLE")


if __name__ == '__main__':
    main()
