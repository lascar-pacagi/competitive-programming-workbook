import sys


def postorder(adj: list[list[int]], root: int = 0) -> tuple[list[int], list[int]]:
    n = len(adj)
    parent = [-1] * n
    order = [root]
    parent[root] = root
    for u in order:
        for v in adj[u]:
            if parent[v] == -1:
                parent[v] = u
                order.append(v)
    return parent, order[::-1]


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    h = [next(it) for _ in range(n)]
    adj = [[] for _ in range(n)]
    for _ in range(n - 1):
        u = next(it) - 1
        v = next(it) - 1
        adj[u].append(v)
        adj[v].append(u)
    parent, order = postorder(adj)
    take = h[:]
    skip = [0] * n
    for u in order:
        for v in adj[u]:
            if parent[v] == u:
                take[u] += skip[v]
                skip[u] += max(take[v], skip[v])
    print(max(take[0], skip[0]))


if __name__ == "__main__":
    main()

