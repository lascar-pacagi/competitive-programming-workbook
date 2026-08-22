import sys

MOD1 = 1_000_000_007
MOD2 = 1_000_000_009
BASE = 911382323


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    index = 0
    n, q = int(data[index]), int(data[index + 1])
    labels = data[index + 2]
    index += 3
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = int(data[index]) - 1, int(data[index + 1]) - 1
        index += 2
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
        if heavy[p] == -1 or size[u] > size[heavy[p]]:
            heavy[p] = u

    head = [0] * n
    position = [0] * n
    vertex_at = [0] * n
    tasks = [(0, 0)]
    timer = 0
    while tasks:
        u, chain_head = tasks.pop()
        while u != -1:
            head[u] = chain_head
            position[u] = timer
            vertex_at[timer] = u
            timer += 1
            for v in graph[u]:
                if parent[v] == u and v != heavy[u]:
                    tasks.append((v, v))
            u = heavy[u]

    def lca(u, v):
        while head[u] != head[v]:
            if depth[head[u]] > depth[head[v]]:
                u = parent[head[u]]
            else:
                v = parent[head[v]]
        return u if depth[u] < depth[v] else v

    def path_segments(u, v):
        ancestor = lca(u, v)
        result = []
        down = []
        while head[u] != head[ancestor]:
            result.append((position[head[u]], position[u] + 1, 1))
            u = parent[head[u]]
        result.append((position[ancestor], position[u] + 1, 1))
        while head[v] != head[ancestor]:
            down.append((position[head[v]], position[v] + 1, 0))
            v = parent[head[v]]
        if position[ancestor] + 1 <= position[v]:
            down.append((position[ancestor] + 1, position[v] + 1, 0))
        result.extend(reversed(down))
        return result

    base = [labels[vertex_at[i]] - 96 for i in range(n)]
    reversed_base = base[::-1]
    powers = []
    prefixes = []
    reverse_prefixes = []
    for mod in (MOD1, MOD2):
        power = [1] * (n + 1)
        prefix = [0] * (n + 1)
        reverse_prefix = [0] * (n + 1)
        for i in range(n):
            power[i + 1] = power[i] * BASE % mod
            prefix[i + 1] = (prefix[i] * BASE + base[i]) % mod
            reverse_prefix[i + 1] = (reverse_prefix[i] * BASE + reversed_base[i]) % mod
        powers.append(power)
        prefixes.append(prefix)
        reverse_prefixes.append(reverse_prefix)

    def range_hash(source, left, right):
        length = right - left
        return tuple((source[h][right] - source[h][left] * powers[h][length]) % mod
                     for h, mod in enumerate((MOD1, MOD2)))

    def segment_hash(segment, offset, length):
        left, right, reversed_flag = segment
        if not reversed_flag:
            return range_hash(prefixes, left + offset, left + offset + length)
        original_left = right - offset - length
        original_right = right - offset
        return range_hash(reverse_prefixes, n - original_right, n - original_left)

    def character(segment, offset):
        left, right, reversed_flag = segment
        return base[right - 1 - offset if reversed_flag else left + offset]

    output = []
    for _ in range(q):
        u, v, x, y = (int(data[index]) - 1, int(data[index + 1]) - 1,
                      int(data[index + 2]) - 1, int(data[index + 3]) - 1)
        index += 4
        first = path_segments(u, v)
        second = path_segments(x, y)
        i = j = offset_first = offset_second = common = 0
        comparison = 0
        while i < len(first) and j < len(second):
            remaining_first = first[i][1] - first[i][0] - offset_first
            remaining_second = second[j][1] - second[j][0] - offset_second
            take = min(remaining_first, remaining_second)
            if (segment_hash(first[i], offset_first, take)
                    == segment_hash(second[j], offset_second, take)):
                common += take
                offset_first += take
                offset_second += take
                if offset_first == first[i][1] - first[i][0]:
                    i += 1
                    offset_first = 0
                if offset_second == second[j][1] - second[j][0]:
                    j += 1
                    offset_second = 0
                continue
            low, high = 0, take
            while low < high:
                middle = (low + high + 1) // 2
                if (segment_hash(first[i], offset_first, middle)
                        == segment_hash(second[j], offset_second, middle)):
                    low = middle
                else:
                    high = middle - 1
            common += low
            a = character(first[i], offset_first + low)
            b = character(second[j], offset_second + low)
            comparison = -1 if a < b else 1
            break
        if comparison == 0 and (i == len(first)) != (j == len(second)):
            comparison = -1 if i == len(first) else 1
        output.append(f"{common} {comparison}")
    print("\n".join(output))


if __name__ == "__main__":
    main()
