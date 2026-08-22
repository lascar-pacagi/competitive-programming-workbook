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
    n, p, m = data[:3]
    at = 3
    projects = []
    for _ in range(p):
        projects.append(tuple(data[at : at + 3]))
        at += 3
    choices = []
    max_profit = 0
    for _ in range(m):
        w, j, profit = data[at : at + 3]
        at += 3
        choices.append((w - 1, j - 1, profit))
        max_profit = max(max_profit, profit)
    s, t = n + p, n + p + 1
    mcf = MCF(t + 1)
    for w in range(n):
        mcf.add_edge(s, w, 1, 0)
    for w, j, profit in choices:
        mcf.add_edge(w, n + j, 1, -profit)
    max_a = max(a for _, _, a in projects)
    big = (n + 1) * (max_profit + 2 * max_a * n + 1)
    mandatory = []
    for j, (low, high, a) in enumerate(projects):
        for k in range(1, high + 1):
            ref = mcf.add_edge(
                n + j, t, 1, a * (2 * k - 1) - (big if k <= low else 0)
            )
            if k <= low:
                mandatory.append(ref)
    sent, cost = mcf.flow(s, t, n)
    ok = sent == n and all(mcf.g[u][i][1] == 0 for u, i in mandatory)
    print(
        -cost - big * sum(low for low, _, _ in projects)
        if ok
        else "IMPOSSIBLE"
    )


if __name__ == "__main__":
    main()
