import sys

INF = 10**40


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    index = 0
    n, query_count = data[index], data[index + 1]
    index += 2
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v, cost = data[index] - 1, data[index + 1] - 1, data[index + 2]
        index += 3
        graph[u].append((v, cost))
        graph[v].append((u, cost))

    log = max(1, n.bit_length())
    up = [[0] * n for _ in range(log)]
    minimum = [[INF] * n for _ in range(log)]
    depth = [0] * n
    tin = [0] * n
    tout = [0] * n
    timer = 0
    events = [(0, 0, INF, 0)]
    while events:
        u, parent, weight, phase = events.pop()
        if phase:
            tout[u] = timer
            continue
        tin[u] = timer
        timer += 1
        up[0][u] = parent
        minimum[0][u] = weight
        if u:
            depth[u] = depth[parent] + 1
        for bit in range(1, log):
            middle = up[bit - 1][u]
            up[bit][u] = up[bit - 1][middle]
            minimum[bit][u] = min(minimum[bit - 1][u], minimum[bit - 1][middle])
        events.append((u, parent, weight, 1))
        for v, cost in reversed(graph[u]):
            if v != parent:
                events.append((v, u, cost, 0))

    def is_ancestor(u, v):
        return tin[u] <= tin[v] and tout[v] <= tout[u]

    def lca(u, v):
        if is_ancestor(u, v):
            return u
        if is_ancestor(v, u):
            return v
        for bit in range(log - 1, -1, -1):
            if not is_ancestor(up[bit][u], v):
                u = up[bit][u]
        return up[0][u]

    def path_minimum(ancestor, vertex):
        difference = depth[vertex] - depth[ancestor]
        result = INF
        bit = 0
        while difference:
            if difference & 1:
                result = min(result, minimum[bit][vertex])
                vertex = up[bit][vertex]
            difference >>= 1
            bit += 1
        return result

    marked = [0] * n
    output = []
    for token in range(1, query_count + 1):
        k = data[index]
        index += 1
        terminals = [value - 1 for value in data[index:index + k]]
        index += k
        for vertex in terminals:
            marked[vertex] = token
        if k <= 1:
            output.append("0 0")
            continue
        terminals.sort(key=tin.__getitem__)
        nodes = terminals + [lca(terminals[i - 1], terminals[i]) for i in range(1, k)]
        nodes = sorted(set(nodes), key=tin.__getitem__)
        children = [[] for _ in nodes]
        stack = []
        for i, vertex in enumerate(nodes):
            while stack and not is_ancestor(nodes[stack[-1]], vertex):
                stack.pop()
            if stack:
                parent_index = stack[-1]
                children[parent_index].append(
                    (i, path_minimum(nodes[parent_index], vertex)))
            stack.append(i)

        dp_zero = [None] * len(nodes)
        dp_one = [None] * len(nodes)
        for i in range(len(nodes) - 1, -1, -1):
            if marked[nodes[i]] == token:
                zero, one = (INF, INF), (0, 0)
            else:
                zero, one = (0, 0), (INF, INF)
            for child, edge_cost in children[i]:
                cut_child = (dp_one[child][0] + edge_cost,
                             dp_one[child][1] + 1)
                separated = min(dp_zero[child], cut_child)
                new_zero = (zero[0] + separated[0], zero[1] + separated[1])
                new_one = min((one[0] + separated[0], one[1] + separated[1]),
                              (zero[0] + dp_one[child][0],
                               zero[1] + dp_one[child][1]))
                zero, one = new_zero, new_one
            dp_zero[i], dp_one[i] = zero, one
        answer = min(dp_zero[0], dp_one[0])
        output.append(f"{answer[0]} {answer[1]}")
    print("\n".join(output))


if __name__ == "__main__":
    main()
