import heapq
import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    values = data[1:1 + n]
    graph = [[] for _ in range(n)]
    index = 1 + n
    for _ in range(n - 1):
        u, v = data[index] - 1, data[index + 1] - 1
        index += 2
        graph[u].append(v)
        graph[v].append(u)

    parent = [-1] * n
    order = [0]
    for u in order:
        for v in graph[u]:
            if v != parent[u]:
                parent[v] = u
                order.append(v)

    heaps = [None] * n
    answer = 0
    for u in reversed(order):
        current = []
        for v in graph[u]:
            if parent[v] != u:
                continue
            child = heaps[v]
            if len(current) < len(child):
                current, child = child, current
            for breakpoint in child:
                heapq.heappush(current, breakpoint)
            heaps[v] = None
        heapq.heappush(current, values[u])
        heapq.heappush(current, values[u])
        first_breakpoint = heapq.heappop(current)
        answer += values[u] - first_breakpoint
        heaps[u] = current
    print(answer)


if __name__ == "__main__":
    main()
