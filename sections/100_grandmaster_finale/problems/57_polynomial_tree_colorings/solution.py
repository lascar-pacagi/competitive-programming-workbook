import sys

MOD = 998244353
ROOT = 3


def ntt(values, inverse):
    n = len(values)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j:
            values[i], values[j] = values[j], values[i]
    length = 2
    while length <= n:
        step = pow(ROOT, (MOD - 1) // length, MOD)
        if inverse:
            step = pow(step, MOD - 2, MOD)
        half = length // 2
        for start in range(0, n, length):
            root = 1
            for offset in range(half):
                u = values[start + offset]
                v = values[start + offset + half] * root % MOD
                values[start + offset] = (u + v) % MOD
                values[start + offset + half] = (u - v) % MOD
                root = root * step % MOD
        length *= 2
    if inverse:
        inverse_n = pow(n, MOD - 2, MOD)
        for i in range(n):
            values[i] = values[i] * inverse_n % MOD


def convolution(first, second):
    if not first or not second:
        return []
    total = len(first) + len(second) - 1
    if min(len(first), len(second)) < 35:
        result = [0] * total
        for i, x in enumerate(first):
            for j, y in enumerate(second):
                result[i + j] = (result[i + j] + x * y) % MOD
        return result
    size = 1
    while size < total:
        size *= 2
    a = first + [0] * (size - len(first))
    b = second + [0] * (size - len(second))
    ntt(a, False)
    ntt(b, False)
    for i in range(size):
        a[i] = a[i] * b[i] % MOD
    ntt(a, True)
    return a[:total]


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    colors = data[1:1 + n]
    graph = [[] for _ in range(n)]
    index = 1 + n
    for _ in range(n - 1):
        u, v = data[index] - 1, data[index + 1] - 1
        index += 2
        graph[u].append(v)
        graph[v].append(u)

    blocked = [False] * n
    parent = [-1] * n
    subtree = [0] * n
    answer = [0] * n

    def find_centroid(start):
        nodes = [start]
        parent[start] = -1
        for u in nodes:
            for v in graph[u]:
                if not blocked[v] and v != parent[u]:
                    parent[v] = u
                    nodes.append(v)
        for u in reversed(nodes):
            size = 1
            for v in graph[u]:
                if not blocked[v] and parent[v] == u:
                    size += subtree[v]
            subtree[u] = size
        total = len(nodes)
        centroid = start
        best = total + 1
        for u in nodes:
            largest = total - subtree[u]
            for v in graph[u]:
                if not blocked[v] and parent[v] == u:
                    largest = max(largest, subtree[v])
            if largest < best:
                best = largest
                centroid = u
        return centroid

    def add_square(polynomial, sign):
        product = convolution(polynomial, polynomial)
        for distance, contribution in enumerate(product[:n]):
            answer[distance] = (answer[distance] + sign * contribution) % MOD

    sys.setrecursionlimit(1_000_000)

    def decompose(start):
        centroid = find_centroid(start)
        all_colors = [[], []]
        all_colors[colors[centroid]] = [1]
        for neighbor in graph[centroid]:
            if blocked[neighbor]:
                continue
            branch = [[], []]
            stack = [(neighbor, centroid, 1)]
            while stack:
                u, p, distance = stack.pop()
                bucket = branch[colors[u]]
                if len(bucket) <= distance:
                    bucket.extend([0] * (distance + 1 - len(bucket)))
                bucket[distance] += 1
                for v in graph[u]:
                    if not blocked[v] and v != p:
                        stack.append((v, u, distance + 1))
            for color in range(2):
                add_square(branch[color], -1)
                if len(all_colors[color]) < len(branch[color]):
                    all_colors[color].extend(
                        [0] * (len(branch[color]) - len(all_colors[color])))
                for distance, count in enumerate(branch[color]):
                    all_colors[color][distance] += count
        add_square(all_colors[0], 1)
        add_square(all_colors[1], 1)
        blocked[centroid] = True
        for neighbor in graph[centroid]:
            if not blocked[neighbor]:
                decompose(neighbor)

    decompose(0)
    answer[0] = 0
    inverse_two = (MOD + 1) // 2
    for distance in range(1, n):
        answer[distance] = answer[distance] * inverse_two % MOD
    print(*answer)


if __name__ == "__main__":
    main()
