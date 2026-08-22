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
    sa = suffix_array(s)
    lcp = lcp_array(s, sa)

    def possible(length):
        low = high = sa[0]
        for i, common in enumerate(lcp):
            if common < length:
                low = high = sa[i + 1]
            else:
                low = min(low, sa[i + 1])
                high = max(high, sa[i + 1])
                if high - low >= length:
                    return True
        return False

    low, high = 0, len(s) // 2 + 1
    while high - low > 1:
        middle = (low + high) // 2
        if possible(middle):
            low = middle
        else:
            high = middle
    print(low)


if __name__ == "__main__":
    main()
