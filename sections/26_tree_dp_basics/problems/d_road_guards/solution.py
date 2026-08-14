import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    cost = data[1:1 + n]
    graph = [[] for _ in range(n)]
    index = 1 + n
    for _ in range(n - 1):
        u = data[index] - 1
        v = data[index + 1] - 1
        index += 2
        graph[u].append(v)
        graph[v].append(u)

    parent = [-1] * n
    parent[0] = 0
    order = [0]
    for u in order:
        for v in graph[u]:
            if parent[v] == -1:
                parent[v] = u
                order.append(v)

    active = cost[:]
    inactive = [0] * n
    for u in reversed(order):
        for v in graph[u]:
            if parent[v] == u:
                active[u] += min(active[v], inactive[v])
                inactive[u] += active[v]

    print(min(active[0], inactive[0]))


if __name__ == "__main__":
    main()
