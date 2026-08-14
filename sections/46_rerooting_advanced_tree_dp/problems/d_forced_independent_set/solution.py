import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    graph = [[] for _ in range(n)]
    for index in range(1, 2 * n - 1, 2):
        left, right = data[index] - 1, data[index + 1] - 1
        graph[left].append(right)
        graph[right].append(left)

    parent = [-1] * n
    order = [0]
    for vertex in order:
        for neighbor in graph[vertex]:
            if neighbor != parent[vertex]:
                parent[neighbor] = vertex
                order.append(neighbor)

    down_without = [0] * n
    down_with = [1] * n
    for vertex in reversed(order):
        for neighbor in graph[vertex]:
            if parent[neighbor] == vertex:
                down_without[vertex] += max(down_without[neighbor], down_with[neighbor])
                down_with[vertex] += down_without[neighbor]

    outside_without = [0] * n
    outside_with = [0] * n
    answer = [0] * n
    for vertex in order:
        answer[vertex] = down_with[vertex] + outside_with[vertex]
        for child in graph[vertex]:
            if parent[child] != vertex:
                continue
            siblings_free = down_without[vertex] - max(down_without[child], down_with[child])
            siblings_without = down_with[vertex] - 1 - down_without[child]
            outside_with[child] = outside_without[vertex] + siblings_free
            outside_without[child] = max(
                outside_without[vertex] + siblings_free,
                outside_with[vertex] + 1 + siblings_without,
            )

    print(" ".join(map(str, answer)))


if __name__ == "__main__":
    main()
