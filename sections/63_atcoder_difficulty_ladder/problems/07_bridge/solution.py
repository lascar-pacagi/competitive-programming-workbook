import sys
from collections import deque


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[:2]
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    index = 2
    for _ in range(m):
        a, b = data[index], data[index + 1]
        index += 2
        graph[a].append(b)
        indegree[b] += 1

    available = deque(step for step in range(1, n + 1) if indegree[step] == 0)
    ambiguous = False
    order = []

    while available:
        if len(available) > 1:
            ambiguous = True

        u = available.popleft()
        order.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                available.append(v)

    if len(order) != n:
        print("IMPOSSIBLE")
    elif ambiguous:
        print("AMBIGUOUS")
    else:
        print("UNIQUE")
        print(*order)


if __name__ == "__main__":
    main()
