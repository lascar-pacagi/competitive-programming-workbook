import sys


def main():
    d = list(map(int, sys.stdin.buffer.read().split()))
    if not d:
        return
    n = d[0]
    colors = d[1 : n + 1]
    z = n + 1
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u = d[z] - 1
        v = d[z + 1] - 1
        z += 2
        g[u].append(v)
        g[v].append(u)
    parent = [-1] * n
    order = [0]
    for u in order:
        for v in g[u]:
            if v != parent[u]:
                parent[v] = u
                order.append(v)
    maps = [None] * n
    best = [0] * n
    ways = [0] * n
    for u in reversed(order):
        children = [v for v in g[u] if parent[v] == u]
        base = max(children, key=lambda v: len(maps[v]), default=-1)
        if base < 0:
            current = {}
            maximum = count = 0
        else:
            current = maps[base]
            maximum = best[base]
            count = ways[base]

        def add(color, amount):
            nonlocal maximum, count
            value = current.get(color, 0) + amount
            current[color] = value
            if value > maximum:
                maximum = value
                count = 1
            elif value == maximum:
                count += 1

        for v in children:
            if v != base:
                for color, amount in maps[v].items():
                    add(color, amount)
                maps[v].clear()
        add(colors[u], 1)
        maps[u] = current
        best[u] = maximum
        ways[u] = count
    print("\n".join(f"{best[u]} {ways[u]}" for u in range(n)))


if __name__ == "__main__":
    main()
