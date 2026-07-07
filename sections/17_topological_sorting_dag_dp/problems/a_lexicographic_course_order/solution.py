import heapq
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
        a = next(it) - 1
        b = next(it) - 1
        adj[a].append(b)
        indeg[b] += 1

    heap = [i for i in range(n) if indeg[i] == 0]
    heapq.heapify(heap)
    order: list[int] = []
    while heap:
        u = heapq.heappop(heap)
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                heapq.heappush(heap, v)

    if len(order) != n:
        print("IMPOSSIBLE")
    else:
        print(" ".join(str(x + 1) for x in order))


if __name__ == "__main__":
    main()

