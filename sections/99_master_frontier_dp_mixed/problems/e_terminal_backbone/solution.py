import sys, heapq

def main():
    d = list(map(int, sys.stdin.buffer.read().split()))
    n, m, k, queries = d[:4]
    at = 4
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = d[at:at + 3]
        at += 3
        u -= 1
        v -= 1
        g[u].append((v, w))
        g[v].append((u, w))
    terminals = [x - 1 for x in d[at:at + k]]
    inf = 10 ** 30
    dp = [[inf] * n for _ in range(1 << k)]
    for i, v in enumerate(terminals):
        dp[1 << i][v] = 0
    for mask in range(1, 1 << k):
        sub = mask - 1 & mask
        while sub:
            other = mask ^ sub
            if sub < other:
                for v in range(n):
                    dp[mask][v] = min(dp[mask][v], dp[sub][v] + dp[other][v])
            sub = sub - 1 & mask
        q = [(x, v) for v, x in enumerate(dp[mask]) if x < inf]
        heapq.heapify(q)
        while q:
            cost, u = heapq.heappop(q)
            if cost != dp[mask][u]:
                continue
            for v, w in g[u]:
                if cost + w < dp[mask][v]:
                    dp[mask][v] = cost + w
                    heapq.heappush(q, (cost + w, v))
    out = []
    for mask in d[at + k:at + k + queries]:
        ans = min(dp[mask])
        out.append('IMPOSSIBLE' if ans == inf else str(ans))
    print('\n'.join(out))
if __name__ == '__main__':
    main()
