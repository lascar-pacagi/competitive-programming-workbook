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
    n, m = data[:2]
    dinic = Dinic(n + 2)
    balance = [0] * n
    at = 2
    for _ in range(m):
        u, v, low, high = data[at : at + 4]
        at += 4
        u -= 1
        v -= 1
        dinic.add_edge(u, v, high - low)
        balance[u] -= low
        balance[v] += low
    need = 0
    for v, value in enumerate(balance):
        if value > 0:
            dinic.add_edge(n, v, value)
            need += value
        elif value < 0:
            dinic.add_edge(v, n + 1, -value)
    print("YES" if dinic.flow(n, n + 1) == need else "NO")


if __name__ == "__main__":
    main()
