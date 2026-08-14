import heapq
import sys


def main():
    tokens = sys.stdin.buffer.read().split()
    n, m = map(int, tokens[:2])
    graph = [[] for _ in range(n)]
    index = 2
    for _ in range(m):
        u = int(tokens[index]) - 1
        v = int(tokens[index + 1]) - 1
        cost = int(tokens[index + 2])
        color = 0 if tokens[index + 3] == b"R" else 1
        index += 4
        graph[u].append((v, cost, color))
    if n == 1:
        print(0)
        return
    inf = 10**30
    dist = [[inf, inf] for _ in range(n)]
    heap = []
    for v, cost, color in graph[0]:
        if cost < dist[v][color]:
            dist[v][color] = cost
            heapq.heappush(heap, (cost, v, color))
    while heap:
        cost, u, last = heapq.heappop(heap)
        if cost != dist[u][last]:
            continue
        for v, weight, color in graph[u]:
            if color == last:
                continue
            new = cost + weight
            if new < dist[v][color]:
                dist[v][color] = new
                heapq.heappush(heap, (new, v, color))
    answer = min(dist[-1])
    print(-1 if answer == inf else answer)


if __name__ == "__main__":
    main()
