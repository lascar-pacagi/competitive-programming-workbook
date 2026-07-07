import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    adj = [[] for _ in range(n)]
    for _ in range(n - 1):
        u = next(it) - 1
        v = next(it) - 1
        adj[u].append(v)
        adj[v].append(u)
    parent = [-1] * n
    parent[0] = 0
    order = [0]
    for u in order:
        for v in adj[u]:
            if parent[v] == -1:
                parent[v] = u
                order.append(v)
    free = [0] * n
    used = [0] * n
    for u in reversed(order):
        base = 0
        children = []
        for v in adj[u]:
            if parent[v] == u:
                children.append(v)
                base += max(free[v], used[v])
        free[u] = base
        best = base
        for v in children:
            cand = base - max(free[v], used[v]) + free[v] + 1
            if cand > best:
                best = cand
        used[u] = best
    print(max(free[0], used[0]))


if __name__ == "__main__":
    main()

