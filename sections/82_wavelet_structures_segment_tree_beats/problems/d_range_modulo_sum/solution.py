import sys

INF = 10**30


class Beats:
    def __init__(self, a):
        n = len(a)
        z = 4 * n
        self.n = n
        self.sum = [0] * z
        self.mx = [-INF] * z
        self.smx = [-INF] * z
        self.mxc = [0] * z
        self.mn = [INF] * z
        self.smn = [INF] * z
        self.mnc = [0] * z
        self._build(1, 0, n, a)

    def _build(self, p, l, r, a):
        if r - l == 1:
            self.sum[p] = self.mx[p] = self.mn[p] = a[l]
            self.mxc[p] = self.mnc[p] = 1
            return
        m = (l + r) // 2
        self._build(p * 2, l, m, a)
        self._build(p * 2 + 1, m, r, a)
        self._pull(p)

    def _pull(self, p):
        a, b = p * 2, p * 2 + 1
        self.sum[p] = self.sum[a] + self.sum[b]
        if self.mx[a] > self.mx[b]:
            self.mx[p], self.mxc[p], self.smx[p] = (
                self.mx[a],
                self.mxc[a],
                max(self.smx[a], self.mx[b]),
            )
        elif self.mx[a] < self.mx[b]:
            self.mx[p], self.mxc[p], self.smx[p] = (
                self.mx[b],
                self.mxc[b],
                max(self.mx[a], self.smx[b]),
            )
        else:
            self.mx[p], self.mxc[p], self.smx[p] = (
                self.mx[a],
                self.mxc[a] + self.mxc[b],
                max(self.smx[a], self.smx[b]),
            )
        if self.mn[a] < self.mn[b]:
            self.mn[p], self.mnc[p], self.smn[p] = (
                self.mn[a],
                self.mnc[a],
                min(self.smn[a], self.mn[b]),
            )
        elif self.mn[a] > self.mn[b]:
            self.mn[p], self.mnc[p], self.smn[p] = (
                self.mn[b],
                self.mnc[b],
                min(self.mn[a], self.smn[b]),
            )
        else:
            self.mn[p], self.mnc[p], self.smn[p] = (
                self.mn[a],
                self.mnc[a] + self.mnc[b],
                min(self.smn[a], self.smn[b]),
            )

    def _upper_node(self, p, x):
        if self.mx[p] <= x:
            return
        self.sum[p] += (x - self.mx[p]) * self.mxc[p]
        if self.mn[p] == self.mx[p]:
            self.mn[p] = x
        elif self.smn[p] == self.mx[p]:
            self.smn[p] = x
        self.mx[p] = x

    def _lower_node(self, p, x):
        if self.mn[p] >= x:
            return
        self.sum[p] += (x - self.mn[p]) * self.mnc[p]
        if self.mx[p] == self.mn[p]:
            self.mx[p] = x
        elif self.smx[p] == self.mn[p]:
            self.smx[p] = x
        self.mn[p] = x

    def _push(self, p):
        for c in (p * 2, p * 2 + 1):
            self._upper_node(c, self.mx[p])
            self._lower_node(c, self.mn[p])

    def upper(self, ql, qr, x, p=1, l=0, r=None):
        if r is None:
            r = self.n
        if qr <= l or r <= ql or self.mx[p] <= x:
            return
        if ql <= l and r <= qr and self.smx[p] < x:
            self._upper_node(p, x)
            return
        self._push(p)
        m = (l + r) // 2
        self.upper(ql, qr, x, p * 2, l, m)
        self.upper(ql, qr, x, p * 2 + 1, m, r)
        self._pull(p)

    def lower(self, ql, qr, x, p=1, l=0, r=None):
        if r is None:
            r = self.n
        if qr <= l or r <= ql or self.mn[p] >= x:
            return
        if ql <= l and r <= qr and self.smn[p] > x:
            self._lower_node(p, x)
            return
        self._push(p)
        m = (l + r) // 2
        self.lower(ql, qr, x, p * 2, l, m)
        self.lower(ql, qr, x, p * 2 + 1, m, r)
        self._pull(p)

    def query(self, ql, qr, p=1, l=0, r=None):
        if r is None:
            r = self.n
        if qr <= l or r <= ql:
            return 0
        if ql <= l and r <= qr:
            return self.sum[p]
        self._push(p)
        m = (l + r) // 2
        return self.query(ql, qr, p * 2, l, m) + self.query(
            ql, qr, p * 2 + 1, m, r
        )


class ModTree:
    def __init__(self, a):
        self.n = len(a)
        self.s = [0] * (4 * self.n)
        self.mx = [0] * (4 * self.n)
        self._build(1, 0, self.n, a)

    def _build(self, p, l, r, a):
        if r - l == 1:
            self.s[p] = self.mx[p] = a[l]
            return
        m = (l + r) // 2
        self._build(p * 2, l, m, a)
        self._build(p * 2 + 1, m, r, a)
        self._pull(p)

    def _pull(self, p):
        self.s[p] = self.s[p * 2] + self.s[p * 2 + 1]
        self.mx[p] = max(self.mx[p * 2], self.mx[p * 2 + 1])

    def mod(self, ql, qr, x, p=1, l=0, r=None):
        if r is None:
            r = self.n
        if qr <= l or r <= ql or self.mx[p] < x:
            return
        if r - l == 1:
            self.s[p] %= x
            self.mx[p] = self.s[p]
            return
        m = (l + r) // 2
        self.mod(ql, qr, x, p * 2, l, m)
        self.mod(ql, qr, x, p * 2 + 1, m, r)
        self._pull(p)

    def set(self, i, x, p=1, l=0, r=None):
        if r is None:
            r = self.n
        if r - l == 1:
            self.s[p] = self.mx[p] = x
            return
        m = (l + r) // 2
        if i < m:
            self.set(i, x, p * 2, l, m)
        else:
            self.set(i, x, p * 2 + 1, m, r)
        self._pull(p)

    def query(self, ql, qr, p=1, l=0, r=None):
        if r is None:
            r = self.n
        if qr <= l or r <= ql:
            return 0
        if ql <= l and r <= qr:
            return self.s[p]
        m = (l + r) // 2
        return self.query(ql, qr, p * 2, l, m) + self.query(
            ql, qr, p * 2 + 1, m, r
        )


def main():
    d = sys.stdin.buffer.read().split()
    n, q = map(int, d[:2])
    t = ModTree(list(map(int, d[2 : 2 + n])))
    at = 2 + n
    out = []
    for _ in range(q):
        op = d[at]
        at += 1
        if op == b"SET":
            t.set(int(d[at]) - 1, int(d[at + 1]))
            at += 2
        else:
            l = int(d[at]) - 1
            r = int(d[at + 1])
            at += 2
            if op == b"MOD":
                t.mod(l, r, int(d[at]))
                at += 1
            else:
                out.append(str(t.query(l, r)))
    print("\n".join(out))


if __name__ == "__main__":
    main()
