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

    data = sys.stdin.buffer.read().split()
    s = data[0].decode()
    sa = suffix_array(s)
    output = []
    for raw in data[2:]:
        pattern = raw.decode()

        def compare(start):
            piece = s[start : start + len(pattern)]
            return (piece > pattern) - (piece < pattern)

        left, right = 0, len(sa)
        while left < right:
            middle = (left + right) // 2
            if compare(sa[middle]) < 0:
                left = middle + 1
            else:
                right = middle
        first = left
        left, right = 0, len(sa)
        while left < right:
            middle = (left + right) // 2
            if compare(sa[middle]) <= 0:
                left = middle + 1
            else:
                right = middle
        output.append(str(left - first))
    print("\n".join(output))


if __name__ == "__main__":
    main()
