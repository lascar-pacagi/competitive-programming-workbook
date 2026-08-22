import sys


class LinkCut:
    def __init__(self, values, mode="sum", mod=None):
        n = len(values)
        self.n = n
        self.ch = [[0, 0] for _ in range(n + 1)]
        self.p = [0] * (n + 1)
        self.rev = [0] * (n + 1)
        self.val = [0] + values[:]
        self.agg = [0] + values[:]
        self.sz = [0] + [1] * n
        self.mode = mode
        self.mod = mod
        self.mul = [1] * (n + 1)
        self.add = [0] * (n + 1)

    def root(self, x):
        p = self.p[x]
        return not p or (self.ch[p][0] != x and self.ch[p][1] != x)

    def pull(self, x):
        l, r = self.ch[x]
        self.sz[x] = 1 + self.sz[l] + self.sz[r]
        self.agg[x] = (
            (self.agg[l] ^ self.val[x] ^ self.agg[r])
            if self.mode == "xor"
            else self.agg[l] + self.val[x] + self.agg[r]
        )
        if self.mod:
            self.agg[x] %= self.mod

    def reverse(self, x):
        if x:
            self.ch[x].reverse()
            self.rev[x] ^= 1

    def affine(self, x, a, b):
        if not x:
            return
        mod = self.mod
        self.val[x] = (a * self.val[x] + b) % mod
        self.agg[x] = (a * self.agg[x] + b * self.sz[x]) % mod
        self.mul[x] = a * self.mul[x] % mod
        self.add[x] = (a * self.add[x] + b) % mod

    def push(self, x):
        if self.rev[x]:
            self.reverse(self.ch[x][0])
            self.reverse(self.ch[x][1])
            self.rev[x] = 0
        if self.mul[x] != 1 or self.add[x]:
            a, b = self.mul[x], self.add[x]
            self.affine(self.ch[x][0], a, b)
            self.affine(self.ch[x][1], a, b)
            self.mul[x] = 1
            self.add[x] = 0

    def rotate(self, x):
        p = self.p[x]
        g = self.p[p]
        side = self.ch[p][1] == x
        b = self.ch[x][side ^ 1]
        if not self.root(p):
            self.ch[g][self.ch[g][1] == p] = x
        self.p[x] = g
        self.ch[x][side ^ 1] = p
        self.p[p] = x
        self.ch[p][side] = b
        if b:
            self.p[b] = p
        self.pull(p)
        self.pull(x)

    def splay(self, x):
        path = [x]
        y = x
        while not self.root(y):
            y = self.p[y]
            path.append(y)
        for y in reversed(path):
            self.push(y)
        while not self.root(x):
            p = self.p[x]
            g = self.p[p]
            if not self.root(p):
                self.rotate(
                    p if (self.ch[p][1] == x) == (self.ch[g][1] == p) else x
                )
            self.rotate(x)

    def access(self, x):
        last = 0
        y = x
        while y:
            self.splay(y)
            self.ch[y][1] = last
            self.pull(y)
            last = y
            y = self.p[y]
        self.splay(x)

    def makeroot(self, x):
        self.access(x)
        self.reverse(x)

    def findroot(self, x):
        self.access(x)
        while self.push(x) is None and self.ch[x][0]:
            x = self.ch[x][0]
        self.splay(x)
        return x

    def link(self, u, v):
        self.makeroot(u)
        self.p[u] = v

    def cut(self, u, v):
        self.makeroot(u)
        self.access(v)
        self.ch[v][0] = 0
        self.p[u] = 0
        self.pull(v)

    def path(self, u, v):
        self.makeroot(u)
        self.access(v)
        return v

    def set(self, u, x):
        self.access(u)
        self.val[u] = x
        self.pull(u)


def main():
    d = sys.stdin.buffer.read().split()
    n, q = map(int, d[:2])
    t = LinkCut(list(map(int, d[2 : 2 + n])), "sum", None)
    at = 2 + n
    out = []
    for _ in range(q):
        op = d[at]
        at += 1
        if op == b"LINK":
            u, v = map(int, d[at : at + 2])
            at += 2
            t.link(u, v)
        elif op == b"CUT":
            u, v = map(int, d[at : at + 2])
            at += 2
            t.cut(u, v)
        elif op == b"SET":
            u, x = map(int, d[at : at + 2])
            at += 2
            t.set(u, x)
        elif op == b"AFFINE":
            u, v, a, b = map(int, d[at : at + 4])
            at += 4
            x = t.path(u, v)
            t.affine(x, a, b)
        else:
            u, v = map(int, d[at : at + 2])
            at += 2
            out.append(str(t.agg[t.path(u, v)]))
    print("\n".join(out))


if __name__ == "__main__":
    main()
