import sys


def main():
    data = sys.stdin.buffer.read().split()
    iterator = iter(data)
    n = int(next(iterator))
    m = int(next(iterator))
    components = int(next(iterator))
    wanted = int(next(iterator))
    edges = []
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        weight = int(next(iterator))
        red = next(iterator) == b'R'
        edges.append((u, v, weight, red))
    edge_count = n - components
    if edge_count == 0:
        print(0 if wanted == 0 else "IMPOSSIBLE")
        return

    def run(penalty, prefer_red):
        order = sorted(
            edges,
            key=lambda edge: (
                edge[2] + penalty * edge[3],
                -edge[3] if prefer_red else edge[3],
            ),
        )
        parent = list(range(n))
        size = [1] * n

        def find(value):
            while value != parent[value]:
                value = parent[value]
            return value

        used = red_count = value = 0
        for u, v, weight, red in order:
            u, v = find(u), find(v)
            if u == v:
                continue
            if size[u] < size[v]:
                u, v = v, u
            parent[v] = u
            size[u] += size[v]
            used += 1
            red_count += red
            value += weight + penalty * red
            if used == edge_count:
                break
        return used, red_count, value

    bound = 400_000_000_000_000
    minimum_used, minimum_red, _ = run(bound, False)
    maximum_used, maximum_red, _ = run(-bound, True)
    if (minimum_used != edge_count or maximum_used != edge_count
            or not minimum_red <= wanted <= maximum_red):
        print("IMPOSSIBLE")
        return

    low, high = -bound, bound
    while low < high:
        middle = (low + high + 1) // 2
        if run(middle, True)[1] >= wanted:
            low = middle
        else:
            high = middle - 1
    _, _, modified = run(low, True)
    print(modified - low * wanted)


if __name__ == '__main__':
    main()
