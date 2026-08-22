import sys


def forest_ok(n, edges, chosen):
    p = list(range(n))

    def find(x):
        while p[x] != x:
            p[x] = p[p[x]]
            x = p[x]
        return x

    for i in chosen:
        u, v = edges[i]
        u = find(u)
        v = find(v)
        if u == v:
            return False
        p[u] = v
    return True


def partition_ok(colors, chosen):
    return len({colors[i] for i in chosen}) == len(chosen)


def intersection(m, ok1, ok2):
    inside = set()
    while True:
        outside = [e for e in range(m) if e not in inside]
        parent = {}
        q = []
        for e in outside:
            if ok1(inside | {e}):
                parent[e] = -1
                q.append(e)
        finish = -1
        for x in q:
            if x not in inside and ok2(inside | {x}):
                finish = x
                break
            if x in inside:
                for e in outside:
                    if e not in parent and ok1((inside - {x}) | {e}):
                        parent[e] = x
                        q.append(e)
            else:
                for y in list(inside):
                    if y not in parent and ok2((inside - {y}) | {x}):
                        parent[y] = x
                        q.append(y)
        if finish < 0:
            return inside
        x = finish
        while x != -1:
            if x in inside:
                inside.remove(x)
            else:
                inside.add(x)
            x = parent[x]


def main():
    d = list(map(int, sys.stdin.buffer.read().split()))
    n, m = d[:2]
    edges = []
    colors = []
    for i in range(2, 2 + 3 * m, 3):
        edges.append((d[i] - 1, d[i + 1] - 1))
        colors.append(d[i + 2])
    answer = intersection(
        m,
        lambda chosen: forest_ok(n, edges, chosen),
        lambda chosen: partition_ok(colors, chosen),
    )
    print("YES" if len(answer) == n - 1 else "NO")


if __name__ == "__main__":
    main()
