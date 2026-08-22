import heapq, sys
from array import array


def main():
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    idx = 0
    n = int(tokens[idx])
    q = int(tokens[idx + 1])
    idx += 2
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        u = int(tokens[idx]) - 1
        v = int(tokens[idx + 1]) - 1
        idx += 2
        graph[u].append(v)
        graph[v].append(u)
    blocked = [False] * n
    paths = [array("i") for _ in range(n)]
    subtree = [0] * n
    todo = [0]
    while todo:
        entry = todo.pop()
        nodes = [entry]
        parent = {entry: -1}
        for u in nodes:
            for v in graph[u]:
                if not blocked[v] and v not in parent:
                    parent[v] = u
                    nodes.append(v)
        for u in reversed(nodes):
            subtree[u] = 1 + sum(
                subtree[v]
                for v in graph[u]
                if not blocked[v] and parent.get(v) != None and parent.get(v) == u
            )
        total = len(nodes)
        centroid = entry
        for u in nodes:
            largest = total - subtree[u]
            for v in graph[u]:
                if not blocked[v] and parent.get(v) == u:
                    largest = max(largest, subtree[v])
            if largest * 2 <= total:
                centroid = u
                break
        stack = [(centroid, -1, 0)]
        while stack:
            u, p, d = stack.pop()
            paths[u].extend((centroid, d))
            for v in graph[u]:
                if v != p and not blocked[v]:
                    stack.append((v, u, d + 1))
        blocked[centroid] = True
        for v in graph[centroid]:
            if not blocked[v]:
                todo.append(v)
    added = [[] for _ in range(n)]
    removed = [[] for _ in range(n)]
    active = [False] * n

    def clean(c):
        while added[c] and removed[c] and added[c][0] == removed[c][0]:
            heapq.heappop(added[c])
            heapq.heappop(removed[c])

    out = []
    for _ in range(q):
        kind = tokens[idx].decode()
        u = int(tokens[idx + 1]) - 1
        idx += 2
        if kind == "T":
            active[u] = not active[u]
            path = paths[u]
            for i in range(0, len(path), 2):
                c, d = path[i], path[i + 1]
                heapq.heappush(added[c] if active[u] else removed[c], d)
                if not active[u]:
                    clean(c)
        else:
            answer = 10**18
            path = paths[u]
            for i in range(0, len(path), 2):
                c, d = path[i], path[i + 1]
                clean(c)
                answer = min(answer, d + added[c][0]) if added[c] else answer
            out.append(str(-1 if answer == 10**18 else answer))
    print("\n".join(out))


if __name__ == "__main__":
    main()
