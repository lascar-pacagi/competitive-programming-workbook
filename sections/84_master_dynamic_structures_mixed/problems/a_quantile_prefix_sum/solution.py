import sys
from array import array


class Wavelet:
    def __init__(self, a):
        self.values = sorted(set(a))
        rank = {x: i for i, x in enumerate(self.values)}
        r = [rank[x] for x in a]
        self.bits = max(1, (len(self.values) - 1).bit_length())
        self.zero = []
        self.zero_sum = []
        self.mid = []
        v = a[:]
        for bit in range(self.bits - 1, -1, -1):
            pc = array("I", [0])
            ps = array("q", [0])
            zr = []
            zv = []
            orank = []
            oval = []
            for x, y in zip(r, v):
                z = not (x >> bit & 1)
                pc.append(pc[-1] + z)
                ps.append(ps[-1] + (y if z else 0))
                (zr if z else orank).append(x)
                (zv if z else oval).append(y)
            self.zero.append(pc)
            self.zero_sum.append(ps)
            self.mid.append(len(zr))
            r = zr + orank
            v = zv + oval

    def kth(self, l, r, k):
        rank = 0
        for level in range(self.bits):
            bit = self.bits - 1 - level
            p = self.zero[level]
            zl = p[r] - p[l]
            if k <= zl:
                l, r = p[l], p[r]
            else:
                k -= zl
                rank |= 1 << bit
                l, r = self.mid[level] + l - p[l], self.mid[level] + r - p[r]
        return self.values[rank]

    def lte(self, l, r, x):
        import bisect

        limit = bisect.bisect_right(self.values, x)
        if limit >= len(self.values):
            return r - l
        ans = 0
        for level in range(self.bits):
            bit = self.bits - 1 - level
            p = self.zero[level]
            if limit >> bit & 1:
                ans += p[r] - p[l]
                l, r = self.mid[level] + l - p[l], self.mid[level] + r - p[r]
            else:
                l, r = p[l], p[r]
        return ans

    def sum_k(self, l, r, k):
        ans = 0
        rank = 0
        for level in range(self.bits):
            bit = self.bits - 1 - level
            p = self.zero[level]
            s = self.zero_sum[level]
            zl = p[r] - p[l]
            if k <= zl:
                l, r = p[l], p[r]
            else:
                ans += s[r] - s[l]
                k -= zl
                rank |= 1 << bit
                l, r = self.mid[level] + l - p[l], self.mid[level] + r - p[r]
        return ans + self.values[rank] * k


def main():
    d = list(map(int, sys.stdin.buffer.read().split()))
    n, q = d[:2]
    a = d[2 : 2 + n]
    w = Wavelet(a)
    at = 2 + n
    print(
        "\n".join(
            str(w.sum_k(d[i] - 1, d[i + 1], d[i + 2]))
            for i in range(at, at + 3 * q, 3)
        )
    )


if __name__ == "__main__":
    main()
