import sys
from array import array
from bisect import bisect_left, insort
from functools import cmp_to_key


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, q = data[0], data[1]
    xs = data[2:2 + 2 * n:2]
    ys = data[3:3 + 2 * n:2]
    # below[i][j] (x_i < x_j): points strictly between them in x and strictly
    # below segment ij.  Around i, sort the points to its right by slope; k is
    # below segment ij iff slope(i,k) < slope(i,j) and x_k < x_j.
    order_x = sorted(range(n), key=xs.__getitem__)
    rank = [0] * n
    for r, i in enumerate(order_x):
        rank[i] = r
    below = [None] * n
    for i in range(n):
        xi, yi = xs[i], ys[i]
        right = [j for j in range(n) if xs[j] > xi]

        def cmp(a, b):
            # slope(i,a) < slope(i,b)  <=>  cross(a - i, b - i) > 0 (dx > 0)
            c = (xs[a] - xi) * (ys[b] - yi) - (ys[a] - yi) * (xs[b] - xi)
            return -1 if c > 0 else 1 if c < 0 else 0

        right.sort(key=cmp_to_key(cmp))
        row = array("i", bytes(4 * n))
        seen = []  # x-ranks of points with smaller slope, kept sorted
        for j in right:
            row[j] = bisect_left(seen, rank[j])
            insort(seen, rank[j])
        below[i] = row

    def under(a, b):
        return below[a][b] if xs[a] < xs[b] else below[b][a]

    out = []
    pos = 2 + 2 * n
    for _ in range(q):
        a, b, c = sorted((data[pos] - 1, data[pos + 1] - 1, data[pos + 2] - 1), key=xs.__getitem__)
        pos += 3
        # Is b above segment ac?
        cross = (xs[c] - xs[a]) * (ys[b] - ys[a]) - (ys[c] - ys[a]) * (xs[b] - xs[a])
        if cross > 0:
            out.append(under(a, b) + under(b, c) - under(a, c))
        else:
            out.append(under(a, c) - under(a, b) - under(b, c) - 1)
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
