from collections import deque
import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    duration = [next(it) for _ in range(n)]
    adj = [[] for _ in range(n)]
    indeg = [0] * n
    for _ in range(m):
        a = next(it) - 1
        b = next(it) - 1
        adj[a].append(b)
        indeg[b] += 1

    earliest_start = [0] * n
    finish = duration[:]
    q = deque(i for i in range(n) if indeg[i] == 0)
    processed = 0
    while q:
        u = q.popleft()
        processed += 1
        finish[u] = earliest_start[u] + duration[u]
        for v in adj[u]:
            if earliest_start[v] < finish[u]:
                earliest_start[v] = finish[u]
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    if processed != n:
        print("IMPOSSIBLE")
    else:
        print(" ".join(map(str, finish)))


if __name__ == "__main__":
    main()

