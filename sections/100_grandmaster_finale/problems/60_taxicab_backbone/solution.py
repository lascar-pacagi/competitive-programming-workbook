import sys
from bisect import bisect_left


def main():
    data = sys.stdin.buffer.read().split()
    n, q = int(data[0]), int(data[1])
    x = [int(v) for v in data[2:2 + 2 * n:2]]
    y = [int(v) for v in data[3:3 + 2 * n:2]]
    pos = 2 + 2 * n

    # Nearest neighbour in each octant: four transforms, one Fenwick sweep each.
    # Candidate edges are packed as weight << 36 | i << 18 | j to save memory.
    edges = []
    px = x[:]
    py = y[:]
    for direction in range(4):
        if direction == 1 or direction == 3:
            px, py = py, px
        elif direction == 2:
            px = [-v for v in px]
        order = sorted(range(n), key=lambda i: (px[i], py[i]))
        keys = [b - a for a, b in zip(px, py)]
        sorted_keys = sorted(set(keys))
        K = len(sorted_keys)
        rank = {k: K - i for i, k in enumerate(sorted_keys)}
        del sorted_keys
        big = 1 << 62
        best_value = [big] * (K + 1)
        best_id = [-1] * (K + 1)
        for t in range(n - 1, -1, -1):
            i = order[t]
            r = rank[keys[i]]
            value = big
            j = -1
            k = r
            while k > 0:
                if best_value[k] < value:
                    value = best_value[k]
                    j = best_id[k]
                k &= k - 1
            if j >= 0:
                edges.append((abs(x[i] - x[j]) + abs(y[i] - y[j])) << 36 | i << 18 | j)
            mine = px[i] + py[i]
            k = r
            while k <= K:
                if mine < best_value[k]:
                    best_value[k] = mine
                    best_id[k] = i
                k += k & -k
    edges.sort()

    answer = [-1] * q
    qa = [0] * q
    qb = [0] * q
    pending = [[] for _ in range(n)]
    for i in range(q):
        a = int(data[pos]) - 1
        b = int(data[pos + 1]) - 1
        pos += 2
        qa[i] = a
        qb[i] = b
        if a == b:
            answer[i] = 0
        else:
            pending[a].append(i)
            pending[b].append(i)

    parent = list(range(n))

    def find(v):
        root = v
        while parent[root] != root:
            root = parent[root]
        while parent[v] != root:
            parent[v], v = root, parent[v]
        return root

    mask = (1 << 18) - 1
    for packed in edges:
        w = packed >> 36
        a = find(packed >> 18 & mask)
        b = find(packed & mask)
        if a == b:
            continue
        if len(pending[a]) > len(pending[b]):
            a, b = b, a
        target = pending[b]
        for i in pending[a]:
            if answer[i] >= 0:
                continue
            u = find(qa[i])
            other = find(qb[i]) if u == a else u
            if other == b:
                answer[i] = w
            else:
                target.append(i)
        pending[a] = []
        parent[a] = b
    sys.stdout.write("\n".join(map(str, answer)) + "\n")


if __name__ == "__main__":
    main()
