import bisect
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    index = 0
    n, q = int(data[index]), int(data[index + 1])
    index += 2
    current = list(map(int, data[index:index + n]))
    index += n
    possible = [[value] for value in current]
    all_values = current.copy()
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = int(data[index]) - 1, int(data[index + 1]) - 1
        index += 2
        graph[u].append(v)
        graph[v].append(u)

    parent = [-1] * n
    order = []
    stack = [0]
    while stack:
        u = stack.pop()
        order.append(u)
        for v in reversed(graph[u]):
            if v != parent[u]:
                parent[v] = u
                stack.append(v)
    tin = [0] * n
    subtree_size = [1] * n
    for position, vertex in enumerate(order):
        tin[vertex] = position
    for vertex in reversed(order[1:]):
        subtree_size[parent[vertex]] += subtree_size[vertex]
    tout = [tin[v] + subtree_size[v] for v in range(n)]

    operations = []
    for _ in range(q):
        kind = data[index]
        vertex, argument = int(data[index + 1]) - 1, int(data[index + 2])
        index += 3
        operations.append((kind, vertex, argument))
        if kind == b"U":
            possible[vertex].append(argument)
            all_values.append(argument)
    all_values = sorted(set(all_values))

    candidates = [[] for _ in range(n + 1)]
    for vertex in range(n):
        for value in set(possible[vertex]):
            outer = tin[vertex] + 1
            while outer <= n:
                candidates[outer].append(value)
                outer += outer & -outer
    counts = [None] * (n + 1)
    for outer in range(1, n + 1):
        candidates[outer] = sorted(set(candidates[outer]))
        counts[outer] = [0] * (len(candidates[outer]) + 1)

    def modify(vertex, value, delta):
        outer = tin[vertex] + 1
        while outer <= n:
            inner = bisect.bisect_left(candidates[outer], value) + 1
            bucket = counts[outer]
            while inner < len(bucket):
                bucket[inner] += delta
                inner += inner & -inner
            outer += outer & -outer

    def prefix_count(position, value):
        result = 0
        outer = position
        while outer:
            inner = bisect.bisect_right(candidates[outer], value)
            bucket = counts[outer]
            while inner:
                result += bucket[inner]
                inner -= inner & -inner
            outer -= outer & -outer
        return result

    for vertex, value in enumerate(current):
        modify(vertex, value, 1)
    output = []
    for kind, vertex, argument in operations:
        if kind == b"U":
            modify(vertex, current[vertex], -1)
            current[vertex] = argument
            modify(vertex, current[vertex], 1)
        else:
            k = argument
            left, right = 0, len(all_values) - 1
            while left < right:
                middle = (left + right) // 2
                count = (prefix_count(tout[vertex], all_values[middle])
                         - prefix_count(tin[vertex], all_values[middle]))
                if count >= k:
                    right = middle
                else:
                    left = middle + 1
            output.append(str(all_values[left]))
    print("\n".join(output))


if __name__ == "__main__":
    main()
