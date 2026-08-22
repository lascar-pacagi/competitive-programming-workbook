import collections
import sys


class Dinic:
    def __init__(self, n):
        self.g = [[] for _ in range(n)]

    def add_edge(self, u, v, cap):
        self.g[u].append([v, cap, len(self.g[v])])
        self.g[v].append([u, 0, len(self.g[u]) - 1])

    def flow(self, s, t):
        answer = 0
        while True:
            level = [-1] * len(self.g)
            level[s] = 0
            q = collections.deque([s])
            while q:
                u = q.popleft()
                for v, cap, _ in self.g[u]:
                    if cap and level[v] < 0:
                        level[v] = level[u] + 1
                        q.append(v)
            if level[t] < 0:
                return answer
            it = [0] * len(self.g)

            def dfs(u, pushed):
                if u == t:
                    return pushed
                while it[u] < len(self.g[u]):
                    e = self.g[u][it[u]]
                    v, cap, rev = e
                    if cap and level[v] == level[u] + 1:
                        take = dfs(v, min(pushed, cap))
                        if take:
                            e[1] -= take
                            self.g[v][rev][1] += take
                            return take
                    it[u] += 1
                return 0

            while pushed := dfs(s, 10**30):
                answer += pushed


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    rows, cols, m = data[:3]
    at = 3
    demands = data[at : at + rows]
    at += rows
    bounds = []
    for _ in range(cols):
        bounds.append(tuple(data[at : at + 2]))
        at += 2
    n = rows + cols + 2
    source, sink, ss, tt = rows + cols, rows + cols + 1, n, n + 1
    dinic = Dinic(n + 2)
    balance = [0] * n

    def bounded(u, v, low, high):
        dinic.add_edge(u, v, high - low)
        balance[u] -= low
        balance[v] += low

    total = sum(demands)
    for r, demand in enumerate(demands):
        bounded(source, r, demand, demand)
    for c, (low, high) in enumerate(bounds):
        bounded(rows + c, sink, low, high)
    for _ in range(m):
        r, c = data[at : at + 2]
        at += 2
        bounded(r - 1, rows + c - 1, 0, 1)
    bounded(sink, source, total, total)
    need = 0
    for v, value in enumerate(balance):
        if value > 0:
            dinic.add_edge(ss, v, value)
            need += value
        elif value < 0:
            dinic.add_edge(v, tt, -value)
    print("YES" if dinic.flow(ss, tt) == need else "NO")


if __name__ == "__main__":
    main()
