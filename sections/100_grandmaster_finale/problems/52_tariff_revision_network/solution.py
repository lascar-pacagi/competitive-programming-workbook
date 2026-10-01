import sys


def main():
    data = sys.stdin.buffer.read().split()
    n, m, q = int(data[0]), int(data[1]), int(data[2])
    pos = 3
    weight = [0] * m
    eu = [0] * m
    ev = [0] * m
    for i in range(m):
        eu[i] = int(data[pos]) - 1
        ev[i] = int(data[pos + 1]) - 1
        weight[i] = int(data[pos + 2])
        pos += 3
    qe = [0] * q
    qw = [0] * q
    for i in range(q):
        qe[i] = int(data[pos]) - 1
        qw[i] = int(data[pos + 1])
        pos += 2
    answers = [0] * q
    stamp_of = [0] * m
    counter = [0]
    key = weight.__getitem__

    def find(parent, x):
        root = x
        while parent[root] != root:
            root = parent[root]
        while parent[x] != root:
            parent[x], x = root, parent[x]
        return root

    # Each edge list is three parallel lists: local endpoints and edge ids.
    def solve(l, r, vertices, us, vs, ids, base):
        if l == r:
            weight[qe[l]] = qw[l]
            order = sorted(range(len(ids)), key=lambda i: weight[ids[i]])
            parent = list(range(vertices))
            total = base
            for i in order:
                a = find(parent, us[i])
                b = find(parent, vs[i])
                if a != b:
                    parent[a] = b
                    total += weight[ids[i]]
            answers[l] = total
            return
        counter[0] += 1
        stamp = counter[0]
        for i in range(l, r + 1):
            stamp_of[qe[i]] = stamp
        dyn = []
        stat = []
        for i in range(len(ids)):
            (dyn if stamp_of[ids[i]] == stamp else stat).append(i)
        stat.sort(key=lambda i: weight[ids[i]])

        # Contraction: static edges still needed after all dynamic edges.
        parent = list(range(vertices))
        for i in dyn:
            a = find(parent, us[i])
            b = find(parent, vs[i])
            if a != b:
                parent[a] = b
        forced = list(range(vertices))
        for i in stat:
            a = find(parent, us[i])
            b = find(parent, vs[i])
            if a != b:
                parent[a] = b
                a = find(forced, us[i])
                b = find(forced, vs[i])
                forced[a] = b
                base += weight[ids[i]]
        label = [-1] * vertices
        count = 0
        for v in range(vertices):
            root = find(forced, v)
            if label[root] < 0:
                label[root] = count
                count += 1
            label[v] = label[root]

        # Reduction: static edges outside the static-only forest are useless.
        parent = list(range(count))
        nu = []
        nv = []
        nid = []
        for i in stat:
            a = label[us[i]]
            b = label[vs[i]]
            if a == b:
                continue
            ra = find(parent, a)
            rb = find(parent, b)
            if ra != rb:
                parent[ra] = rb
                nu.append(a)
                nv.append(b)
                nid.append(ids[i])
        for i in dyn:
            nu.append(label[us[i]])
            nv.append(label[vs[i]])
            nid.append(ids[i])
        mid = (l + r) // 2
        solve(l, mid, count, nu, nv, nid, base)
        solve(mid + 1, r, count, nu, nv, nid, base)

    sys.setrecursionlimit(10000)
    solve(0, q - 1, n, eu, ev, list(range(m)), 0)
    sys.stdout.write("\n".join(map(str, answers)) + "\n")


if __name__ == "__main__":
    main()
