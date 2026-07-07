from collections import deque
import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it); m = next(it); s = next(it) - 1; qn = next(it)
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = next(it) - 1; v = next(it) - 1; w = next(it)
        adj[u].append((v, w))
    queries = [next(it) - 1 for _ in range(qn)]
    inf = 10**18
    dist = [inf] * n
    dist[s] = 0
    dq = deque([s])
    while dq:
        u = dq.popleft()
        du = dist[u]
        for v, w in adj[u]:
            nd = du + w
            if nd < dist[v]:
                dist[v] = nd
                if w == 0:
                    dq.appendleft(v)
                else:
                    dq.append(v)
    print(" ".join(str(-1 if dist[x] == inf else dist[x]) for x in queries))


if __name__ == "__main__":
    main()

