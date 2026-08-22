import heapq
import sys

INF = 10**40


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    index = 0
    n, m = data[index], data[index + 1]
    index += 2
    source, sink = n, n + 1
    graph = [[] for _ in range(n + 2)]

    def add_edge(u, v, capacity, cost):
        graph[u].append([v, len(graph[v]), capacity, cost])
        graph[v].append([u, len(graph[u]) - 1, 0, -cost])

    balance = [0] * n
    base_cost = 0
    for _ in range(m):
        u, v, lower, upper, c, d = data[index:index + 6]
        index += 6
        u -= 1
        v -= 1
        balance[u] -= lower
        balance[v] += lower
        base_cost += c * lower + d * lower * (lower - 1) // 2
        for amount in range(lower, upper):
            add_edge(u, v, 1, c + d * amount)
    required = 0
    for vertex, value in enumerate(balance):
        if value > 0:
            add_edge(source, vertex, value, 0)
            required += value
        elif value < 0:
            add_edge(vertex, sink, -value, 0)

    potential = [0] * (n + 2)
    sent = extra_cost = 0
    while sent < required:
        distance = [INF] * (n + 2)
        previous = [None] * (n + 2)
        distance[source] = 0
        queue = [(0, source)]
        while queue:
            current_distance, u = heapq.heappop(queue)
            if current_distance != distance[u]:
                continue
            for edge_index, edge in enumerate(graph[u]):
                v, _, capacity, cost = edge
                if not capacity:
                    continue
                candidate = current_distance + cost + potential[u] - potential[v]
                if candidate < distance[v]:
                    distance[v] = candidate
                    previous[v] = (u, edge_index)
                    heapq.heappush(queue, (candidate, v))
        if distance[sink] == INF:
            break
        for vertex in range(n + 2):
            if distance[vertex] != INF:
                potential[vertex] += distance[vertex]
        pushed = required - sent
        vertex = sink
        while vertex != source:
            u, edge_index = previous[vertex]
            pushed = min(pushed, graph[u][edge_index][2])
            vertex = u
        vertex = sink
        while vertex != source:
            u, edge_index = previous[vertex]
            edge = graph[u][edge_index]
            extra_cost += pushed * edge[3]
            edge[2] -= pushed
            graph[vertex][edge[1]][2] += pushed
            vertex = u
        sent += pushed
    print("IMPOSSIBLE" if sent != required else base_cost + extra_cost)


if __name__ == "__main__":
    main()
