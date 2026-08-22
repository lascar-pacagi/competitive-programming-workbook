def suffix_array(s):
    n = len(s)
    sa = list(range(n))
    rank = list(map(ord, s))
    step = 1
    while True:
        sa.sort(
            key=lambda i: (rank[i], rank[i + step] if i + step < n else -1)
        )
        new_rank = [0] * n
        for j in range(1, n):
            a, b = sa[j - 1], sa[j]
            left = (rank[a], rank[a + step] if a + step < n else -1)
            right = (rank[b], rank[b + step] if b + step < n else -1)
            new_rank[b] = new_rank[a] + (left < right)
        rank = new_rank
        if rank[sa[-1]] == n - 1:
            return sa
        step *= 2


def lcp_array(s, sa):
    n = len(s)
    rank = [0] * n
    for i, start in enumerate(sa):
        rank[start] = i
    lcp = [0] * (n - 1)
    height = 0
    for i in range(n):
        place = rank[i]
        if place == 0:
            continue
        j = sa[place - 1]
        while (
            i + height < n
            and j + height < n
            and s[i + height] == s[j + height]
        ):
            height += 1
        lcp[place - 1] = height
        height = max(0, height - 1)
    return lcp


def main():
    import sys

    s = sys.stdin.buffer.readline().decode().strip()
    n = len(s)
    sa = suffix_array(s)
    edges = sorted(
        ((w, i, i + 1) for i, w in enumerate(lcp_array(s, sa))), reverse=True
    )
    parent = list(range(n))
    size = [1] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    answer = [0] * (n + 1)
    answer[1] = n
    for weight, a, b in edges:
        a, b = find(a), find(b)
        if a != b:
            if size[a] < size[b]:
                a, b = b, a
            parent[b] = a
            size[a] += size[b]
        answer[size[a]] = max(answer[size[a]], weight)
    for k in range(n - 1, 0, -1):
        answer[k] = max(answer[k], answer[k + 1])
    print(*answer[1:])


if __name__ == "__main__":
    main()
