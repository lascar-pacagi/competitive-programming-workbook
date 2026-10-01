import sys

MOD = (1 << 61) - 1
BASE = 1000003


def main():
    s = sys.stdin.buffer.read().split()[0]
    n = len(s)
    # Forward prefix hashes, and prefix hashes of the reversed string for
    # longest-common-suffix queries.
    pw = [1] * (n + 1)
    for i in range(n):
        pw[i + 1] = pw[i] * BASE % MOD
    h = [0] * (n + 1)
    for i in range(n):
        h[i + 1] = (h[i] * BASE + s[i]) % MOD
    rs = s[::-1]
    rh = [0] * (n + 1)
    for i in range(n):
        rh[i + 1] = (rh[i] * BASE + rs[i]) % MOD

    def fwd(i, length):
        return (h[i + length] - h[i] * pw[length]) % MOD

    def lce(i, j):
        """Longest common prefix of suffixes i and j (galloping + binary search)."""
        if i == j:
            return n - i
        limit = n - max(i, j)
        if limit == 0 or s[i] != s[j]:
            return 0
        step = 1
        good = 1
        while True:
            nxt = good + step
            if nxt > limit or fwd(i, nxt) != fwd(j, nxt):
                hi = min(nxt, limit + 1)
                break
            good = nxt
            step *= 2
        lo = good
        while hi - lo > 1:
            mid = (lo + hi) >> 1
            if fwd(i, mid) == fwd(j, mid):
                lo = mid
            else:
                hi = mid
        return lo

    def lcs(i, j):
        """Longest common suffix of prefixes ending at i and j (inclusive)."""
        if i < 0 or j < 0:
            return 0
        if s[i] != s[j]:
            return 0
        a = n - 1 - i
        b = n - 1 - j
        limit = n - max(a, b)
        step = 1
        good = 1
        while True:
            nxt = good + step
            if nxt > limit or (rh[a + nxt] - rh[a] * pw[nxt]) % MOD != (rh[b + nxt] - rh[b] * pw[nxt]) % MOD:
                hi = min(nxt, limit + 1)
                break
            good = nxt
            step *= 2
        lo = good
        while hi - lo > 1:
            mid = (lo + hi) >> 1
            if (rh[a + mid] - rh[a] * pw[mid]) % MOD == (rh[b + mid] - rh[b] * pw[mid]) % MOD:
                lo = mid
            else:
                hi = mid
        return lo

    runs = set()
    for flip in (False, True):
        # Lyndon array under the letter order (reversed when flip), with the
        # end of the string smaller than every letter in both orders.
        lyn = [1] * n
        for i in range(n - 1, -1, -1):
            j = i + 1
            while j < n:
                l = lce(i, j)
                if j + l == n:
                    break  # suffix j is a prefix of suffix i: suffix j is smaller
                smaller = s[i + l] < s[j + l]
                if smaller != flip:
                    j += lyn[j]  # suffix i < suffix j: extend the Lyndon word
                else:
                    break
            lyn[i] = j - i
        for i in range(n):
            p = lyn[i]
            j = i + p
            if j > n:
                continue
            r = lce(i, j) if j < n else 0
            l = lcs(i - 1, j - 1)
            if l + r >= p:
                runs.add((i - l, j + r, p))

    squares = set()
    for a, b, p in runs:
        length = b - a
        L = p
        while 2 * L <= length:
            last_start = b - 2 * L
            for x in range(a, min(last_start, a + p - 1) + 1):
                squares.add(fwd(x, 2 * L) * (n + 1) + L)
            L += p
    print(len(squares))


if __name__ == "__main__":
    main()
