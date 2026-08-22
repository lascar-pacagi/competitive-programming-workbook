import sys

MOD = 998_244_353
IDENTITY = (1, 0)


def compose(first, second):
    return second[0] * first[0] % MOD, (second[0] * first[1] + second[1]) % MOD


def merge(left, right):
    return compose(left[0], right[0]), compose(right[1], left[1])


def main():
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    idx = 0
    n = int(tokens[idx])
    q = int(tokens[idx + 1])
    idx += 2
    functions = []
    for _ in range(n):
        functions.append((int(tokens[idx]), int(tokens[idx + 1])))
        idx += 2
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        u = int(tokens[idx]) - 1
        v = int(tokens[idx + 1]) - 1
        idx += 2
        graph[u].append(v)
        graph[v].append(u)
    parent = [-1] * n
    depth = [0] * n
    order = [0]
    for u in order:
        for v in graph[u]:
            if v != parent[u]:
                parent[v] = u
                depth[v] = depth[u] + 1
                order.append(v)
    size = [1] * n
    heavy = [-1] * n
    for u in reversed(order[1:]):
        p = parent[u]
        size[p] += size[u]
        if heavy[p] < 0 or size[u] > size[heavy[p]]:
            heavy[p] = u
    head = [0] * n
    position = [0] * n
    timer = 0
    chains = [(0, 0)]
    while chains:
        start, h = chains.pop()
        u = start
        while u != -1:
            head[u] = h
            position[u] = timer
            timer += 1
            for v in graph[u]:
                if parent[v] == u and v != heavy[u]:
                    chains.append((v, v))
            u = heavy[u]
    base = 1
    while base < n:
        base *= 2
    identity = (IDENTITY, IDENTITY)
    tree = [identity for _ in range(2 * base)]
    for u, f in enumerate(functions):
        tree[base + position[u]] = (f, f)
    for p in range(base - 1, 0, -1):
        tree[p] = merge(tree[2 * p], tree[2 * p + 1])

    def range_query(left, right):
        a = b = identity
        left += base
        right += base + 1
        while left < right:
            if left & 1:
                a = merge(a, tree[left])
                left += 1
            if right & 1:
                right -= 1
                b = merge(tree[right], b)
            left //= 2
            right //= 2
        return merge(a, b)

    out = []
    for _ in range(q):
        kind = tokens[idx].decode()
        idx += 1
        if kind == "U":
            u = int(tokens[idx]) - 1
            f = (int(tokens[idx + 1]), int(tokens[idx + 2]))
            idx += 3
            p = base + position[u]
            tree[p] = (f, f)
            p //= 2
            while p:
                tree[p] = merge(tree[2 * p], tree[2 * p + 1])
                p //= 2
        else:
            u = int(tokens[idx]) - 1
            v = int(tokens[idx + 1]) - 1
            x = int(tokens[idx + 2])
            idx += 3
            left = right = IDENTITY
            while head[u] != head[v]:
                if depth[head[u]] >= depth[head[v]]:
                    left = compose(left, range_query(position[head[u]], position[u])[1])
                    u = parent[head[u]]
                else:
                    right = compose(
                        range_query(position[head[v]], position[v])[0], right
                    )
                    v = parent[head[v]]
            middle = (
                range_query(position[u], position[v])[0]
                if position[u] <= position[v]
                else range_query(position[v], position[u])[1]
            )
            whole = compose(compose(left, middle), right)
            out.append(str((whole[0] * x + whole[1]) % MOD))
    print("\n".join(out))


if __name__ == "__main__":
    main()
