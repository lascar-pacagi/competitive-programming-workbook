from collections import deque
import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        adj[u].append((v, 0))
        adj[v].append((u, 1))
    inf = 10**9
    dist = [inf] * n
    dist[0] = 0
    dq = deque([0])
    while dq:
        u = dq.popleft()
        for v, w in adj[u]:
            nd = dist[u] + w
            if nd < dist[v]:
                dist[v] = nd
                if w == 0:
                    dq.appendleft(v)
                else:
                    dq.append(v)
    print(-1 if dist[n - 1] == inf else dist[n - 1])


if __name__ == "__main__":
    main()

