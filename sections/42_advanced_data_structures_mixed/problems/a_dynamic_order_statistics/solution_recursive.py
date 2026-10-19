import sys


class SegmentTree:
    def __init__(self, size):
        self.n = size
        self.count = [0] * (4 * size)

    def change(self, score, delta):
        self._change(1, 0, self.n, score - 1, delta)

    def _change(self, node, left, right, x, delta):
        if right - left == 1:
            self.count[node] = max(0, self.count[node] + delta)
            return
        mid = (left + right) // 2
        if x < mid:
            self._change(2 * node, left, mid, x, delta)
        else:
            self._change(2 * node + 1, mid, right, x, delta)
        self.count[node] = (
            self.count[2 * node] + self.count[2 * node + 1]
        )

    def prefix(self, score):
        return self._prefix(1, 0, self.n, score)

    def _prefix(self, node, left, right, end):
        if end <= left:
            return 0
        if right <= end:
            return self.count[node]
        mid = (left + right) // 2
        return self._prefix(2 * node, left, mid, end) + self._prefix(
            2 * node + 1, mid, right, end
        )

    def kth(self, k):
        if k > self.count[1]:
            return -1
        return self._kth(1, 0, self.n, k)

    def _kth(self, node, left, right, k):
        if right - left == 1:
            return left + 1
        mid = (left + right) // 2
        if k <= self.count[2 * node]:
            return self._kth(2 * node, left, mid, k)
        return self._kth(
            2 * node + 1, mid, right, k - self.count[2 * node]
        )


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    m, q = data[:2]
    tree = SegmentTree(m)
    out = []
    pos = 2
    for _ in range(q):
        op, x = data[pos : pos + 2]
        pos += 2
        if op == 1:
            tree.change(x, 1)
        elif op == 2:
            tree.change(x, -1)
        elif op == 3:
            out.append(tree.kth(x))
        else:
            out.append(tree.prefix(x))
    sys.stdout.write("\n".join(map(str, out)) + ("\n" if out else ""))


if __name__ == "__main__":
    main()
