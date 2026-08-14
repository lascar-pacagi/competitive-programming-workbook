import heapq
import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = data[:2]
    graph = [[] for _ in range(n)]
    index = 2
    for _ in range(m):
        u, v, weight = data[index:index + 3]
        index += 3
        graph[u - 1].append((v - 1, weight))

    inf = 10**30
    dist = [[inf, inf] for _ in range(n)]
    dist[0][0] = 0
    heap = [(0, 0, 0)]
    while heap:
        cost, u, parity = heapq.heappop(heap)
        if cost != dist[u][parity]:
            continue
        for v, weight in graph[u]:
            next_parity = parity ^ 1
            next_cost = cost + weight
            if next_cost < dist[v][next_parity]:
                dist[v][next_parity] = next_cost
                heapq.heappush(heap, (next_cost, v, next_parity))

    print(-1 if dist[n - 1][0] == inf else dist[n - 1][0])


if __name__ == "__main__":
    main()
