import sys


def main():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(data)
    alarm = [next(data) for _ in range(n)]
    adj = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v, delay = next(data) - 1, next(data) - 1, next(data)
        adj[u].append((v, delay))
        adj[v].append((u, delay))

    parent = [-1] * n
    order = [0]
    for u in order:
        for v, _ in adj[u]:
            if v != parent[u]:
                parent[v] = u
                order.append(v)

    down = alarm.copy()
    for u in reversed(order):
        for v, delay in adj[u]:
            if parent[v] == u:
                down[u] = max(down[u], down[v] + delay)

    up = [-1] * n
    answer = [0] * n
    for u in order:
        answer[u] = max(down[u], up[u])
        best = second = -1
        best_child = -1
        for v, delay in adj[u]:
            if parent[v] != u:
                continue
            candidate = down[v] + delay
            if candidate > best:
                second, best = best, candidate
                best_child = v
            elif candidate > second:
                second = candidate
        for v, delay in adj[u]:
            if parent[v] == u:
                other = second if v == best_child else best
                up[v] = delay + max(alarm[u], up[u], other)
    print(' '.join(map(str, answer)))


if __name__ == '__main__':
    main()
