import sys
from array import array


def main():
    t = sys.stdin.buffer.read().split()
    if not t:
        return
    z = 0
    n = int(t[z])
    q = int(t[z + 1])
    z += 2
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u = int(t[z]) - 1
        v = int(t[z + 1]) - 1
        z += 2
        g[u].append(v)
        g[v].append(u)
    blocked = [False] * n
    subtree = [0] * n
    paths = [array("i") for _ in range(n)]
    todo = [0]
    while todo:
        entry = todo.pop()
        nodes = [entry]
        parent = {entry: -1}
        for u in nodes:
            for v in g[u]:
                if not blocked[v] and v not in parent:
                    parent[v] = u
                    nodes.append(v)
        for u in reversed(nodes):
            subtree[u] = 1 + sum(subtree[v] for v in g[u] if parent.get(v) == u)
        total = len(nodes)
        centroid = entry
        for u in nodes:
            largest = total - subtree[u]
            for v in g[u]:
                if not blocked[v] and parent.get(v) == u:
                    largest = max(largest, subtree[v])
            if largest * 2 <= total:
                centroid = u
                break
        paths[centroid].extend((centroid, 0, -1))
        for first in g[centroid]:
            if not blocked[first]:
                stack = [(first, centroid, 1)]
                while stack:
                    u, p, d = stack.pop()
                    paths[u].extend((centroid, d, first))
                    for v in g[u]:
                        if v != p and not blocked[v]:
                            stack.append((v, u, d + 1))
        blocked[centroid] = True
        for v in g[centroid]:
            if not blocked[v]:
                todo.append(v)
    count = [0] * n
    distance_sum = [0] * n
    excluded = {}
    active = [False] * n
    out = []
    for _ in range(q):
        kind = t[z].decode()
        u = int(t[z + 1]) - 1
        z += 2
        if kind == "T":
            delta = -1 if active[u] else 1
            active[u] = not active[u]
            path = paths[u]
            for i in range(0, len(path), 3):
                c, d, b = path[i], path[i + 1], path[i + 2]
                count[c] += delta
                distance_sum[c] += delta * d
                if b != -1:
                    old_count, old_sum = excluded.get((c, b), (0, 0))
                    excluded[c, b] = (old_count + delta, old_sum + delta * d)
        else:
            answer = 0
            path = paths[u]
            for i in range(0, len(path), 3):
                c, d, b = path[i], path[i + 1], path[i + 2]
                answer += distance_sum[c] + count[c] * d
                if b != -1:
                    old_count, old_sum = excluded.get((c, b), (0, 0))
                    answer -= old_sum + old_count * d
            out.append(str(answer))
    print("\n".join(out))


if __name__ == "__main__":
    main()
