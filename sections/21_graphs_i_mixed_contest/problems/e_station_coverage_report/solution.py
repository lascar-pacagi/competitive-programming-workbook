import sys
from collections import deque


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m, k = data[:3]
    graph = [[] for _ in range(n)]
    index = 3
    for _ in range(m):
        u, v = data[index] - 1, data[index + 1] - 1
        index += 2
        graph[u].append(v)
        graph[v].append(u)
    distance = [-1] * n
    queue = deque()
    for station in data[index:index + k]:
        station -= 1
        if distance[station] == -1:
            distance[station] = 0
            queue.append(station)
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if distance[v] == -1:
                distance[v] = distance[u] + 1
                queue.append(v)
    unreachable = distance.count(-1)
    farthest = max(distance)
    vertex = distance.index(farthest) + 1
    print(unreachable, vertex, farthest)


if __name__ == "__main__":
    main()
