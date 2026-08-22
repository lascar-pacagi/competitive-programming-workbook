import heapq
import sys


class MinCostFlow:
    def __init__(self, n: int):
        self.graph = [[] for _ in range(n)]

    def add_edge(self, u: int, v: int, capacity: int, cost: int) -> None:
        self.graph[u].append([v, capacity, cost, len(self.graph[v])])
        self.graph[v].append([u, 0, -cost, len(self.graph[u]) - 1])

    def flow(self, source: int, sink: int, required: int):
        n = len(self.graph)
        potential = [0] * n
        sent = total_cost = 0
        infinity = 10**30

        while sent < required:
            distance = [infinity] * n
            previous = [None] * n
            distance[source] = 0
            queue = [(0, source)]
            while queue:
                current_distance, u = heapq.heappop(queue)
                if current_distance != distance[u]:
                    continue
                for index, edge in enumerate(self.graph[u]):
                    v, capacity, cost, _ = edge
                    if not capacity:
                        continue
                    candidate = current_distance + cost + potential[u] - potential[v]
                    if candidate < distance[v]:
                        distance[v] = candidate
                        previous[v] = (u, index)
                        heapq.heappush(queue, (candidate, v))
            if distance[sink] == infinity:
                break
            for v in range(n):
                if distance[v] < infinity:
                    potential[v] += distance[v]

            add = required - sent
            v = sink
            while v != source:
                u, index = previous[v]
                add = min(add, self.graph[u][index][1])
                v = u
            v = sink
            while v != source:
                u, index = previous[v]
                edge = self.graph[u][index]
                total_cost += add * edge[2]
                edge[1] -= add
                self.graph[v][edge[3]][1] += add
                v = u
            sent += add
        return sent, total_cost


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = data[:2]
    source, sink = n, n + 1
    network = MinCostFlow(n + 2)
    balance = [0] * n
    mandatory_cost = 0
    at = 2
    for _ in range(m):
        u, v, low, high, cost = data[at : at + 5]
        at += 5
        u -= 1
        v -= 1
        balance[u] -= low
        balance[v] += low
        mandatory_cost += low * cost
        network.add_edge(u, v, high - low, cost)

    required = 0
    for v, amount in enumerate(balance):
        if amount > 0:
            network.add_edge(source, v, amount, 0)
            required += amount
        elif amount < 0:
            network.add_edge(v, sink, -amount, 0)

    sent, extra_cost = network.flow(source, sink, required)
    print(mandatory_cost + extra_cost if sent == required else "IMPOSSIBLE")


if __name__ == "__main__":
    main()
