import sys
from array import array


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    index = 0
    n, q = data[index], data[index + 1]
    index += 2
    values = data[index:index + n]
    index += n
    coordinates = sorted(set(values))
    compressed = {x: i for i, x in enumerate(coordinates)}

    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = data[index] - 1, data[index + 1] - 1
        index += 2
        graph[u].append(v)
        graph[v].append(u)

    log = n.bit_length()
    parent = array("i", [0]) * n
    depth = array("i", [0]) * n
    order = [0]
    for u in order:
        for v in graph[u]:
            if v == parent[u] and u != 0:
                continue
            parent[v] = u
            depth[v] = depth[u] + 1
            order.append(v)
    up = [parent]
    for _ in range(1, log):
        previous = up[-1]
        up.append(array("i", (previous[previous[v]] for v in range(n))))

    left_child = array("i", [0])
    right_child = array("i", [0])
    count = array("i", [0])
    sums = array("q", [0])

    def clone(node: int) -> int:
        left_child.append(left_child[node])
        right_child.append(right_child[node])
        count.append(count[node])
        sums.append(sums[node])
        return len(count) - 1

    def insert(previous: int, position: int, x: int) -> int:
        new_root = clone(previous)
        current = new_root
        old = previous
        low, high = 0, len(coordinates)
        while True:
            count[current] += 1
            sums[current] += x
            if high - low == 1:
                return new_root
            middle = (low + high) // 2
            if position < middle:
                old_child = left_child[old]
                new_child = clone(old_child)
                left_child[current] = new_child
                old, current, high = old_child, new_child, middle
            else:
                old_child = right_child[old]
                new_child = clone(old_child)
                right_child[current] = new_child
                old, current, low = old_child, new_child, middle

    roots = array("i", [0]) * n
    for v in order:
        previous = 0 if v == 0 else roots[parent[v]]
        roots[v] = insert(previous, compressed[values[v]], values[v])

    def lca(u: int, v: int) -> int:
        if depth[u] < depth[v]:
            u, v = v, u
        difference = depth[u] - depth[v]
        bit = 0
        while difference:
            if difference & 1:
                u = up[bit][u]
            difference >>= 1
            bit += 1
        if u == v:
            return u
        for bit in range(log - 1, -1, -1):
            if up[bit][u] != up[bit][v]:
                u, v = up[bit][u], up[bit][v]
        return parent[u]

    output = []
    for _ in range(q):
        u, v = data[index] - 1, data[index + 1] - 1
        index += 2
        ancestor = lca(u, v)
        before = 0 if ancestor == 0 else roots[parent[ancestor]]
        a, b, c, d = roots[u], roots[v], roots[ancestor], before

        length = count[a] + count[b] - count[c] - count[d]
        total = sums[a] + sums[b] - sums[c] - sums[d]
        wanted = (length + 1) // 2
        low, high = 0, len(coordinates)
        lower_count = 0
        lower_sum = 0
        while high - low > 1:
            al, bl = left_child[a], left_child[b]
            cl, dl = left_child[c], left_child[d]
            count_left = count[al] + count[bl] - count[cl] - count[dl]
            middle = (low + high) // 2
            if wanted <= count_left:
                a, b, c, d = al, bl, cl, dl
                high = middle
            else:
                wanted -= count_left
                lower_count += count_left
                lower_sum += sums[al] + sums[bl] - sums[cl] - sums[dl]
                a, b = right_child[a], right_child[b]
                c, d = right_child[c], right_child[d]
                low = middle

        lower_count += count[a] + count[b] - count[c] - count[d]
        lower_sum += sums[a] + sums[b] - sums[c] - sums[d]
        median = coordinates[low]
        cost = (median * lower_count - lower_sum
                + total - lower_sum - median * (length - lower_count))
        output.append(f"{median} {cost}")
    print("\n".join(output))


if __name__ == "__main__":
    main()
