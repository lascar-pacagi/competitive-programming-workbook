import sys

sys.setrecursionlimit(1_000_000)


def scc(n, edges):
    graph = [[] for _ in range(n)]
    reverse = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        reverse[v].append(u)
    seen = [False] * n
    order = []
    for start in range(n):
        if seen[start]:
            continue
        stack = [(start, 0)]
        seen[start] = True
        while stack:
            node, index = stack[-1]
            if index < len(graph[node]):
                target = graph[node][index]
                stack[-1] = (node, index + 1)
                if not seen[target]:
                    seen[target] = True
                    stack.append((target, 0))
            else:
                order.append(node)
                stack.pop()
    component = [-1] * n
    count = 0
    for start in reversed(order):
        if component[start] != -1:
            continue
        component[start] = count
        stack = [start]
        while stack:
            node = stack.pop()
            for target in reverse[node]:
                if component[target] == -1:
                    component[target] = count
                    stack.append(target)
        count += 1
    return component, count


def undirected_lowlink(n, edges):
    graph = [[] for _ in range(n)]
    for edge_id, (u, v) in enumerate(edges):
        graph[u].append((v, edge_id))
        graph[v].append((u, edge_id))
    tin = [-1] * n
    low = [0] * n
    subtree = [0] * n
    bridges = [False] * len(edges)
    separating = [[] for _ in range(n)]
    timer = 0

    def dfs(node, parent_edge=-1):
        nonlocal timer
        tin[node] = low[node] = timer
        timer += 1
        subtree[node] = 1
        for target, edge_id in graph[node]:
            if edge_id == parent_edge:
                continue
            if tin[target] != -1:
                low[node] = min(low[node], tin[target])
            else:
                dfs(target, edge_id)
                subtree[node] += subtree[target]
                low[node] = min(low[node], low[target])
                if low[target] > tin[node]:
                    bridges[edge_id] = True
                if low[target] >= tin[node]:
                    separating[node].append(subtree[target])

    dfs(0)
    return graph, tin, low, subtree, bridges, separating


def bridge_tree(n, edges):
    graph, _, _, _, bridges, _ = undirected_lowlink(n, edges)
    component = [-1] * n
    count = 0
    for start in range(n):
        if component[start] != -1:
            continue
        component[start] = count
        stack = [start]
        while stack:
            node = stack.pop()
            for target, edge_id in graph[node]:
                if not bridges[edge_id] and component[target] == -1:
                    component[target] = count
                    stack.append(target)
        count += 1
    tree = [[] for _ in range(count)]
    for edge_id, (u, v) in enumerate(edges):
        if bridges[edge_id]:
            a, b = component[u], component[v]
            tree[a].append(b)
            tree[b].append(a)
    return component, tree


def tree_lca(tree):
    size = len(tree)
    levels = max(1, size.bit_length())
    up = [[0] * size for _ in range(levels)]
    depth = [0] * size
    stack = [(0, 0)]
    order = [0]
    while stack:
        node, parent = stack.pop()
        up[0][node] = parent
        for target in tree[node]:
            if target != parent:
                depth[target] = depth[node] + 1
                order.append(target)
                stack.append((target, node))
    for level in range(1, levels):
        previous = up[level - 1]
        up[level] = [previous[previous[node]] for node in range(size)]

    def lca(a, b):
        if depth[a] < depth[b]:
            a, b = b, a
        difference = depth[a] - depth[b]
        for level in range(levels):
            if difference >> level & 1:
                a = up[level][a]
        if a == b:
            return a
        for level in range(levels - 1, -1, -1):
            if up[level][a] != up[level][b]:
                a, b = up[level][a], up[level][b]
        return up[0][a]

    def distance(a, b):
        ancestor = lca(a, b)
        return depth[a] + depth[b] - 2 * depth[ancestor]

    return distance


def block_cut_tree(n, edges):
    graph = [[] for _ in range(n)]
    for edge_id, (u, v) in enumerate(edges):
        graph[u].append((v, edge_id))
        graph[v].append((u, edge_id))
    tin = [-1] * n
    low = [0] * n
    edge_stack = []
    tree = [[] for _ in range(n)]
    timer = 0

    def dfs(node, parent_edge=-1):
        nonlocal timer
        tin[node] = low[node] = timer
        timer += 1
        for target, edge_id in graph[node]:
            if edge_id == parent_edge:
                continue
            if tin[target] == -1:
                edge_stack.append(edge_id)
                dfs(target, edge_id)
                low[node] = min(low[node], low[target])
                if low[target] >= tin[node]:
                    vertices = set()
                    while True:
                        taken = edge_stack.pop()
                        vertices.update(edges[taken])
                        if taken == edge_id:
                            break
                    block = len(tree)
                    tree.append([])
                    for vertex in vertices:
                        tree[block].append(vertex)
                        tree[vertex].append(block)
            elif tin[target] < tin[node]:
                edge_stack.append(edge_id)
                low[node] = min(low[node], tin[target])

    dfs(0)
    return tree


def dominators(n, edges):
    predecessors = [[] for _ in range(n)]
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        predecessors[v].append(u)
    reachable = 1
    stack = [0]
    while stack:
        node = stack.pop()
        for target in graph[node]:
            if not (reachable >> target & 1):
                reachable |= 1 << target
                stack.append(target)
    dom = [reachable] * n
    dom[0] = 1
    changed = True
    while changed:
        changed = False
        for node in range(1, n):
            if not (reachable >> node & 1):
                continue
            value = reachable
            for parent in predecessors[node]:
                if reachable >> parent & 1:
                    value &= dom[parent]
            value |= 1 << node
            if value != dom[node]:
                dom[node] = value
                changed = True
    return dom


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m, q = data[:3]
    at = 3
    edges = [(data[i] - 1, data[i + 1] - 1) for i in range(at, at + 2 * m, 2)]
    at += 2 * m
    component, tree = bridge_tree(n, edges)
    distance = tree_lca(tree)
    print(
        "\n".join(
            str(distance(component[data[i] - 1], component[data[i + 1] - 1]))
            for i in range(at, at + 2 * q, 2)
        )
    )


if __name__ == "__main__":
    main()
