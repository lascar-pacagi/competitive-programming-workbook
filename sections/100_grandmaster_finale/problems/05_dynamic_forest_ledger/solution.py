import sys

MOD = 1_000_000_007


class LinkCutTree:
    def __init__(self, values):
        n = len(values)
        self.child = [[0, 0] for _ in range(n + 1)]
        self.parent = [0] * (n + 1)
        self.reversed = [0] * (n + 1)
        self.size = [0] + [1] * n
        self.value = [0] + values
        self.total = [0] + values.copy()
        self.lazy_mul = [1] * (n + 1)
        self.lazy_add = [0] * (n + 1)

    def is_auxiliary_root(self, x):
        p = self.parent[x]
        return not p or (self.child[p][0] != x and self.child[p][1] != x)

    def pull(self, x):
        left, right = self.child[x]
        self.size[x] = 1 + self.size[left] + self.size[right]
        self.total[x] = (self.total[left] + self.value[x] + self.total[right]) % MOD

    def apply_reverse(self, x):
        if x:
            self.child[x].reverse()
            self.reversed[x] ^= 1

    def apply_affine(self, x, multiplier, addition):
        if not x:
            return
        self.value[x] = (multiplier * self.value[x] + addition) % MOD
        self.total[x] = (multiplier * self.total[x] + addition * self.size[x]) % MOD
        self.lazy_mul[x] = multiplier * self.lazy_mul[x] % MOD
        self.lazy_add[x] = (multiplier * self.lazy_add[x] + addition) % MOD

    def push(self, x):
        if self.reversed[x]:
            self.apply_reverse(self.child[x][0])
            self.apply_reverse(self.child[x][1])
            self.reversed[x] = 0
        if self.lazy_mul[x] != 1 or self.lazy_add[x]:
            multiplier, addition = self.lazy_mul[x], self.lazy_add[x]
            self.apply_affine(self.child[x][0], multiplier, addition)
            self.apply_affine(self.child[x][1], multiplier, addition)
            self.lazy_mul[x] = 1
            self.lazy_add[x] = 0

    def rotate(self, x):
        p = self.parent[x]
        g = self.parent[p]
        side = self.child[p][1] == x
        middle = self.child[x][side ^ 1]
        if not self.is_auxiliary_root(p):
            self.child[g][self.child[g][1] == p] = x
        self.parent[x] = g
        self.child[x][side ^ 1] = p
        self.parent[p] = x
        self.child[p][side] = middle
        if middle:
            self.parent[middle] = p
        self.pull(p)
        self.pull(x)

    def splay(self, x):
        ancestors = [x]
        y = x
        while not self.is_auxiliary_root(y):
            y = self.parent[y]
            ancestors.append(y)
        for y in reversed(ancestors):
            self.push(y)
        while not self.is_auxiliary_root(x):
            p = self.parent[x]
            g = self.parent[p]
            if not self.is_auxiliary_root(p):
                self.rotate(p if ((self.child[p][1] == x)
                                  == (self.child[g][1] == p)) else x)
            self.rotate(x)

    def access(self, x):
        previous = 0
        current = x
        while current:
            self.splay(current)
            self.child[current][1] = previous
            self.pull(current)
            previous = current
            current = self.parent[current]
        self.splay(x)

    def make_root(self, x):
        self.access(x)
        self.apply_reverse(x)

    def link(self, u, v):
        self.make_root(u)
        self.parent[u] = v

    def cut(self, u, v):
        self.make_root(u)
        self.access(v)
        self.child[v][0] = 0
        self.parent[u] = 0
        self.pull(v)

    def expose_path(self, u, v):
        self.make_root(u)
        self.access(v)
        return v


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n, q = map(int, data[:2])
    tree = LinkCutTree(list(map(int, data[2:2 + n])))
    index = 2 + n
    output = []
    for _ in range(q):
        operation = data[index]
        u, v = int(data[index + 1]), int(data[index + 2])
        index += 3
        if operation == b"LINK":
            tree.link(u, v)
        elif operation == b"CUT":
            tree.cut(u, v)
        elif operation == b"AFFINE":
            multiplier, addition = int(data[index]), int(data[index + 1])
            index += 2
            tree.apply_affine(tree.expose_path(u, v), multiplier, addition)
        else:
            output.append(str(tree.total[tree.expose_path(u, v)]))
    print("\n".join(output))


if __name__ == "__main__":
    main()
