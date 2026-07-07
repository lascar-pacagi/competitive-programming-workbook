import heapq
import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data); n = next(it); m = next(it)
    cost = [[next(it) for _ in range(m)] for _ in range(n)]
    inf = 10**30
    dist = [[inf] * m for _ in range(n)]
    dist[0][0] = cost[0][0]
    heap = [(cost[0][0], 0, 0)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    while heap:
        d, r, c = heapq.heappop(heap)
        if d != dist[r][c]:
            continue
        if r == n - 1 and c == m - 1:
            break
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m:
                nd = d + cost[nr][nc]
                if nd < dist[nr][nc]:
                    dist[nr][nc] = nd
                    heapq.heappush(heap, (nd, nr, nc))
    print(dist[n - 1][m - 1])


if __name__ == "__main__":
    main()

