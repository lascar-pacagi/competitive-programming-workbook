from collections import deque
import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    qn = next(it)
    duration = [next(it) for _ in range(n)]
    adj = [[] for _ in range(n)]
    indeg = [0] * n
    for _ in range(m):
        a = next(it) - 1
        b = next(it) - 1
        adj[a].append(b)
        indeg[b] += 1
    queries = [next(it) - 1 for _ in range(qn)]
    start = [0] * n
    finish = duration[:]
    dq = deque(i for i in range(n) if indeg[i] == 0)
    processed = 0
    while dq:
        u = dq.popleft()
        processed += 1
        finish[u] = start[u] + duration[u]
        for v in adj[u]:
            if finish[u] > start[v]:
                start[v] = finish[u]
            indeg[v] -= 1
            if indeg[v] == 0:
                dq.append(v)
    if processed != n:
        print("IMPOSSIBLE")
    else:
        print(" ".join(str(finish[x]) for x in queries))


if __name__ == "__main__":
    main()

