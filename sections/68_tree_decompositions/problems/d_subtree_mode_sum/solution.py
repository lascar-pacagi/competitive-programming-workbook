import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    colors = data[1 : n + 1]
    idx = n + 1
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        u = data[idx] - 1
        v = data[idx + 1] - 1
        idx += 2
        graph[u].append(v)
        graph[v].append(u)
    parent = [-1] * n
    order = [0]
    for u in order:
        for v in graph[u]:
            if v != parent[u]:
                parent[v] = u
                order.append(v)
    maps = [None] * n
    maximum = [0] * n
    answer = [0] * n
    for u in reversed(order):
        children = [v for v in graph[u] if parent[v] == u]
        base = max(children, key=lambda v: len(maps[v]), default=-1)
        if base < 0:
            current = {}
            best = total = 0
        else:
            current = maps[base]
            best = maximum[base]
            total = answer[base]

        def add(color, amount):
            nonlocal best, total
            value = current.get(color, 0) + amount
            current[color] = value
            if value > best:
                best = value
                total = color
            elif value == best:
                total += color

        for v in children:
            if v != base:
                for color, amount in maps[v].items():
                    add(color, amount)
                maps[v].clear()
        add(colors[u], 1)
        maps[u] = current
        maximum[u] = best
        answer[u] = total
    print(*answer)


if __name__ == "__main__":
    main()
