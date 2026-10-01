import sys
from array import array
from bisect import bisect_left


def main():
    data = sys.stdin.buffer.read().split()
    s = data[0]
    n = len(s)
    q = int(data[1])

    # Suffix array by prefix doubling.
    rank = list(s)
    sa = list(range(n))
    k = 1
    width = max(n, 256) + 1  # ranks (and letter codes) stay below width
    while True:
        key = [r * width + (rank[i + k] + 1 if i + k < n else 0) for i, r in enumerate(rank)]
        sa.sort(key=key.__getitem__)
        new = [0] * n
        for idx in range(1, n):
            new[sa[idx]] = new[sa[idx - 1]] + (key[sa[idx - 1]] != key[sa[idx]])
        rank = new
        if rank[sa[-1]] == n - 1:
            break
        k *= 2
    lcp = [0] * n
    h = 0
    for i in range(n):
        r = rank[i]
        if r == 0:
            h = 0
            continue
        j = sa[r - 1]
        while i + h < n and j + h < n and s[i + h] == s[j + h]:
            h += 1
        lcp[r] = h
        if h:
            h -= 1

    # In suffix-array order, suffix sa[i] adds the distinct substrings of
    # lengths lcp[i]+1 .. n-sa[i], already lexicographically sorted.
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + n - sa[i] - lcp[i]
    mn_lcp = [array("i", lcp)]
    mn_sa = [array("i", sa)]
    step = 1
    while 2 * step <= n:
        a = mn_lcp[-1]
        b = mn_sa[-1]
        mn_lcp.append(array("i", [min(a[i], a[i + step]) for i in range(n - 2 * step + 1)]))
        mn_sa.append(array("i", [min(b[i], b[i + step]) for i in range(n - 2 * step + 1)]))
        step *= 2

    def range_min(table, l, r):
        k = (r - l + 1).bit_length() - 1
        row = table[k]
        x = row[l]
        y = row[r - (1 << k) + 1]
        return x if x < y else y

    total = prefix[n]
    out = []
    for token in data[2:2 + q]:
        k = int(token)
        if k > total:
            out.append("-1")
            continue
        i = bisect_left(prefix, k, 1) - 1
        length = lcp[i] + k - prefix[i]
        # Occurrences are suffixes i..hi, where lcp stays >= length.
        lo, hi = i, n - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if range_min(mn_lcp, i + 1, mid) >= length:
                lo = mid
            else:
                hi = mid - 1
        out.append(f"{range_min(mn_sa, i, lo) + 1} {length}")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
