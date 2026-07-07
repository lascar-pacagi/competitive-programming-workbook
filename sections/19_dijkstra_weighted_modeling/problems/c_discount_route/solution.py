import heapq
import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data); n = next(it); m = next(it)
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = next(it) - 1; v = next(it) - 1; w = next(it)
        adj[u].append((v, w))
    inf = 10**30
    dist = [[inf, inf] for _ in range(n)]
    dist[0][0] = 0
    heap = [(0, 0, 0)]
    while heap:
        d, u, used = heapq.heappop(heap)
        if d != dist[u][used]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v][used]:
                dist[v][used] = nd; heapq.heappush(heap, (nd, v, used))
            if used == 0:
                nd = d + w // 2
                if nd < dist[v][1]:
                    dist[v][1] = nd; heapq.heappush(heap, (nd, v, 1))
    ans = min(dist[n - 1])
    print(-1 if ans == inf else ans)


if __name__ == "__main__":
    main()

