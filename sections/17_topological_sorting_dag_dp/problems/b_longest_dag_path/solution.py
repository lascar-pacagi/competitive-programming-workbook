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
    indeg = [0] * n
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        adj[u].append(v)
        indeg[v] += 1

    q = deque(i for i in range(n) if indeg[i] == 0)
    dp = [0] * n
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dp[v] < dp[u] + 1:
                dp[v] = dp[u] + 1
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    print(max(dp, default=0))


if __name__ == "__main__":
    main()

