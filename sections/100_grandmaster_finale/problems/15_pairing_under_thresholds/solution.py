import sys
from collections import defaultdict, deque


def maximum_matching(graph: list[list[int]]) -> int:
    n = len(graph)
    match = [-1] * n
    parent = [-1] * n
    base = list(range(n))
    used = [False] * n
    in_blossom = [False] * n

    def lca(a: int, b: int) -> int:
        seen = [False] * n
        while True:
            a = base[a]
            seen[a] = True
            if match[a] == -1:
                break
            a = parent[match[a]]
        while True:
            b = base[b]
            if seen[b]:
                return b
            b = parent[match[b]]

    def mark_path(v: int, blossom_base: int, child: int) -> None:
        while base[v] != blossom_base:
            in_blossom[base[v]] = True
            in_blossom[base[match[v]]] = True
            parent[v] = child
            child = match[v]
            v = parent[match[v]]

    def augment_from(root: int) -> bool:
        nonlocal parent, base, used, in_blossom
        used = [False] * n
        parent = [-1] * n
        base = list(range(n))
        queue = deque([root])
        used[root] = True
        while queue:
            v = queue.popleft()
            for u in graph[v]:
                if base[v] == base[u] or match[v] == u:
                    continue
                if u == root or (match[u] != -1 and parent[match[u]] != -1):
                    blossom_base = lca(v, u)
                    in_blossom = [False] * n
                    mark_path(v, blossom_base, u)
                    mark_path(u, blossom_base, v)
                    for x in range(n):
                        if in_blossom[base[x]]:
                            base[x] = blossom_base
                            if not used[x]:
                                used[x] = True
                                queue.append(x)
                elif parent[u] == -1:
                    parent[u] = v
                    if match[u] == -1:
                        x = u
                        while x != -1:
                            previous = parent[x]
                            next_x = -1 if previous == -1 else match[previous]
                            match[x] = previous
                            if previous != -1:
                                match[previous] = x
                            x = next_x
                        return True
                    u = match[u]
                    used[u] = True
                    queue.append(u)
        return False

    size = 0
    for v in range(n):
        if match[v] == -1 and augment_from(v):
            size += 1
    return size


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m, q = data[:3]
    index = 3
    edges = []
    for _ in range(m):
        u, v, difficulty = data[index:index + 3]
        index += 3
        edges.append((u - 1, v - 1, difficulty))
    queries = data[index:index + q]
    thresholds = sorted({difficulty for _, _, difficulty in edges})
    if not thresholds:
        print("\n".join("-1" for _ in queries))
        return

    requested = set(queries)
    low = {k: 0 for k in requested}
    high = {k: len(thresholds) for k in requested}
    rank_cache = {}

    def rank_at(threshold_index: int) -> int:
        if threshold_index not in rank_cache:
            graph = [[] for _ in range(n)]
            limit = thresholds[threshold_index]
            for u, v, difficulty in edges:
                if difficulty <= limit:
                    graph[u].append(v)
                    graph[v].append(u)
            rank_cache[threshold_index] = maximum_matching(graph)
        return rank_cache[threshold_index]

    while True:
        groups = defaultdict(list)
        for k in requested:
            if low[k] < high[k]:
                groups[(low[k] + high[k]) // 2].append(k)
        if not groups:
            break
        for middle, sizes in groups.items():
            rank = rank_at(middle)
            for k in sizes:
                if rank >= k:
                    high[k] = middle
                else:
                    low[k] = middle + 1

    answers = ["-1" if low[k] == len(thresholds)
               else str(thresholds[low[k]]) for k in queries]
    print("\n".join(answers))


if __name__ == "__main__":
    main()
