import sys


def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n, m, wanted = int(next(it)), int(next(it)), int(next(it))
    edges = []
    for _ in range(m):
        u, v, w, color = (
            int(next(it)) - 1,
            int(next(it)) - 1,
            int(next(it)),
            next(it),
        )
        edges.append((u, v, w, color == b"R"))

    def run(lam, prefer_red):
        order = sorted(
            edges,
            key=lambda e: (e[2] + lam * e[3], -e[3] if prefer_red else e[3]),
        )
        parent = list(range(n))
        size = [1] * n

        def find(x):
            while x != parent[x]:
                x = parent[x]
            return x

        used = red = value = 0
        for u, v, w, is_red in order:
            u, v = find(u), find(v)
            if u == v:
                continue
            if size[u] < size[v]:
                u, v = v, u
            parent[v] = u
            size[u] += size[v]
            used += 1
            red += is_red
            value += w + lam * is_red
        return used, red, value

    bound = 400_000_000_000_000
    used, minimum, _ = run(bound, False)
    _, maximum, _ = run(-bound, True)
    if used != n - 1 or not minimum <= wanted <= maximum:
        print("IMPOSSIBLE")
        return
    lo, hi = -bound, bound
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if run(mid, True)[1] >= wanted:
            lo = mid
        else:
            hi = mid - 1
    _, _, modified = run(lo, True)
    print(modified - lo * wanted)


if __name__ == "__main__":
    main()
