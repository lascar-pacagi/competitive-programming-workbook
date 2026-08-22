import sys
from array import array


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    iterator = iter(data)
    n = next(iterator)
    q = next(iterator)
    values = [next(iterator) for _ in range(n)]
    coordinates = sorted(set(values))
    rank = {value: index for index, value in enumerate(coordinates)}

    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        u = next(iterator) - 1
        v = next(iterator) - 1
        graph[u].append(v)
        graph[v].append(u)

    levels = n.bit_length()
    up = [array("i", [0]) * n for _ in range(levels)]
    depth = array("i", [0]) * n
    order = [0]
    for u in order:
        for v in graph[u]:
            if v == up[0][u] or v == 0:
                continue
            up[0][v] = u
            depth[v] = depth[u] + 1
            order.append(v)
    for level in range(1, levels):
        previous = up[level - 1]
        current = up[level]
        for u in range(n):
            current[u] = previous[previous[u]]

    left = array("i", [0])
    right = array("i", [0])
    count = array("i", [0])

    def insert(old: int, low: int, high: int, position: int) -> int:
        current = len(count)
        left.append(left[old])
        right.append(right[old])
        count.append(count[old] + 1)
        if low != high:
            middle = (low + high) // 2
            if position <= middle:
                left[current] = insert(left[old], low, middle, position)
            else:
                right[current] = insert(right[old], middle + 1, high, position)
        return current

    roots = array("i", [0]) * n
    maximum = len(coordinates) - 1
    for u in order:
        parent_root = 0 if u == 0 else roots[up[0][u]]
        roots[u] = insert(parent_root, 0, maximum, rank[values[u]])

    def lca(u: int, v: int) -> int:
        if depth[u] < depth[v]:
            u, v = v, u
        difference = depth[u] - depth[v]
        for level in range(levels):
            if difference >> level & 1:
                u = up[level][u]
        if u == v:
            return u
        for level in range(levels - 1, -1, -1):
            if up[level][u] != up[level][v]:
                u = up[level][u]
                v = up[level][v]
        return up[0][u]

    def kth(a: int, b: int, c: int, d: int, k: int) -> int:
        low = 0
        high = maximum
        while low != high:
            left_count = (
                count[left[a]] + count[left[b]]
                - count[left[c]] - count[left[d]]
            )
            middle = (low + high) // 2
            if k <= left_count:
                a, b, c, d = left[a], left[b], left[c], left[d]
                high = middle
            else:
                k -= left_count
                a, b, c, d = right[a], right[b], right[c], right[d]
                low = middle + 1
        return low

    answer = []
    for _ in range(q):
        u = next(iterator) - 1
        v = next(iterator) - 1
        k = next(iterator)
        ancestor = lca(u, v)
        before = 0 if ancestor == 0 else roots[up[0][ancestor]]
        answer.append(str(coordinates[kth(
            roots[u], roots[v], roots[ancestor], before, k
        )]))
    print("\n".join(answer))


if __name__ == "__main__":
    main()
