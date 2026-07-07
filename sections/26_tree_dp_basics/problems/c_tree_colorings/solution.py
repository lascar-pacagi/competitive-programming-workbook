import sys


MOD = 1_000_000_007


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
    white = [1] * n
    black = [1] * n
    for u in reversed(order):
        for v in adj[u]:
            if parent[v] == u:
                white[u] = white[u] * (white[v] + black[v]) % MOD
                black[u] = black[u] * white[v] % MOD
    print((white[0] + black[0]) % MOD)


if __name__ == "__main__":
    main()

