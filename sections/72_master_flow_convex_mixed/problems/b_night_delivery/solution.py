import heapq
import sys


class MCF:
    def __init__(self, n):
        self.g = [[] for _ in range(n)]

    def add_edge(self, u, v, cap, cost):
        ref = (u, len(self.g[u]))
        self.g[u].append([v, cap, cost, len(self.g[v]), cap])
        self.g[v].append([u, 0, -cost, len(self.g[u]) - 1, 0])
        return ref

    def flow(self, s, t, limit):
        n = len(self.g)
        inf = 10**40
        potential = [inf] * n
        potential[s] = 0
        for _ in range(n):
            changed = False
            for u in range(n):
                if potential[u] == inf:
                    continue
                for v, cap, cost, _, _ in self.g[u]:
                    if cap and potential[v] > potential[u] + cost:
                        potential[v] = potential[u] + cost
                        changed = True
            if not changed:
                break
        potential = [0 if x == inf else x for x in potential]
        sent = total = 0
        while sent < limit:
            dist = [inf] * n
            prev = [None] * n
            dist[s] = 0
            pq = [(0, s)]
            while pq:
                d, u = heapq.heappop(pq)
                if d != dist[u]:
                    continue
                for i, (v, cap, cost, _, _) in enumerate(self.g[u]):
                    nd = d + cost + potential[u] - potential[v]
                    if cap and nd < dist[v]:
                        dist[v] = nd
                        prev[v] = (u, i)
                        heapq.heappush(pq, (nd, v))
            if dist[t] == inf:
                break
            for v in range(n):
                if dist[v] < inf:
                    potential[v] += dist[v]
            add = limit - sent
            v = t
            while v != s:
                u, i = prev[v]
                add = min(add, self.g[u][i][1])
                v = u
            v = t
            while v != s:
                u, i = prev[v]
                e = self.g[u][i]
                total += add * e[2]
                e[1] -= add
                self.g[v][e[3]][1] += add
                v = u
            sent += add
        return sent, total


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m, need, s, t = data[:5]
    mcf = MCF(n)
    at = 5
    for _ in range(m):
        u, v, cap, cost = data[at : at + 4]
        at += 4
        mcf.add_edge(u - 1, v - 1, cap, cost)
    sent, cost = mcf.flow(s - 1, t - 1, need)
    print(cost if sent == need else "IMPOSSIBLE")


if __name__ == "__main__":
    main()
