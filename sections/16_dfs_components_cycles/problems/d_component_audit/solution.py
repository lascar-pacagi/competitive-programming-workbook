import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = data[0], data[1]
    graph = [[] for _ in range(n)]
    index = 2
    for _ in range(m):
        u = data[index] - 1
        v = data[index + 1] - 1
        index += 2
        graph[u].append(v)
        graph[v].append(u)

    seen = [False] * n
    tree_components = 0
    cyclic_components = 0
    for start in range(n):
        if seen[start]:
            continue

        vertices = 0
        degree_sum = 0
        stack = [start]
        seen[start] = True
        while stack:
            u = stack.pop()
            vertices += 1
            degree_sum += len(graph[u])
            for v in graph[u]:
                if not seen[v]:
                    seen[v] = True
                    stack.append(v)

        if degree_sum // 2 == vertices - 1:
            tree_components += 1
        else:
            cyclic_components += 1

    print(tree_components, cyclic_components)


if __name__ == "__main__":
    main()
