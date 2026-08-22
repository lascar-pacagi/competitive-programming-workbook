import sys

sys.setrecursionlimit(1_000_000)
MOD = 1_000_000_007
BASE = 911382323
POW = [1]
seed = 712367821


def rnd():
    global seed
    seed ^= seed << 13 & 0xFFFFFFFF
    seed ^= seed >> 17
    seed ^= seed << 5 & 0xFFFFFFFF
    return seed & 0xFFFFFFFF


class Node:
    __slots__ = "v", "p", "l", "r", "z", "sum", "add", "rev", "hf", "hr"

    def __init__(self, v):
        self.v = v
        self.p = rnd()
        self.l = self.r = None
        self.z = 1
        self.sum = v
        self.add = 0
        self.rev = False
        self.hf = self.hr = v % MOD


def size(t):
    return t.z if t else 0


def total(t):
    return t.sum if t else 0


def ensure(n):
    while len(POW) <= n:
        POW.append(POW[-1] * BASE % MOD)


def pull(t):
    if not t:
        return
    ensure(size(t.l) + size(t.r) + 1)
    t.z = 1 + size(t.l) + size(t.r)
    t.sum = t.v + total(t.l) + total(t.r)
    ll = size(t.l)
    rr = size(t.r)
    lf = t.l.hf if t.l else 0
    rf = t.r.hf if t.r else 0
    lr = t.l.hr if t.l else 0
    rrh = t.r.hr if t.r else 0
    t.hf = (lf + t.v * POW[ll] + rf * POW[ll + 1]) % MOD
    t.hr = (rrh + t.v * POW[rr] + lr * POW[rr + 1]) % MOD


def apply_add(t, x):
    if t:
        t.v += x
        t.sum += x * t.z
        t.add += x


def apply_rev(t):
    if t:
        t.l, t.r = t.r, t.l
        t.hf, t.hr = t.hr, t.hf
        t.rev ^= True


def push(t):
    if not t:
        return
    if t.rev:
        apply_rev(t.l)
        apply_rev(t.r)
        t.rev = False
    if t.add:
        apply_add(t.l, t.add)
        apply_add(t.r, t.add)
        t.add = 0


def split(t, k):
    if not t:
        return None, None
    push(t)
    if size(t.l) >= k:
        a, t.l = split(t.l, k)
        pull(t)
        return a, t
    t.r, b = split(t.r, k - size(t.l) - 1)
    pull(t)
    return t, b


def merge(a, b):
    if not a or not b:
        return a or b
    if a.p > b.p:
        push(a)
        a.r = merge(a.r, b)
        pull(a)
        return a
    push(b)
    b.l = merge(a, b.l)
    pull(b)
    return b


def build(values):
    root = None
    for x in values:
        root = merge(root, Node(x))
    return root


def values(t, out):
    if not t:
        return
    push(t)
    values(t.l, out)
    out.append(t.v)
    values(t.r, out)


def main():
    d = sys.stdin.buffer.read().split()
    n, q = map(int, d[:2])
    root = build(range(1, n + 1))
    at = 2
    for _ in range(q):
        l, r, p = map(int, d[at + 1 : at + 4])
        at += 4
        a, b = split(root, l - 1)
        b, c = split(b, r - l + 1)
        root = merge(a, c)
        a, c = split(root, p - 1)
        root = merge(merge(a, b), c)
    out = []
    values(root, out)
    print(*out)


if __name__ == "__main__":
    main()
