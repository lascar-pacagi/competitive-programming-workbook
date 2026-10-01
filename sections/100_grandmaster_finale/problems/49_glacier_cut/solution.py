import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, q = data[0], data[1]
    xs = data[2:2 + 2 * n:2]
    ys = data[3:3 + 2 * n:2]
    if sum(xs[i] * ys[(i + 1) % n] - xs[(i + 1) % n] * ys[i] for i in range(n)) < 0:
        xs.reverse()
        ys.reverse()

    def half(x, y):
        return 0 if y > 0 or (y == 0 and x > 0) else 1

    # Rotate so that edge directions increase in angle over [0, 2*pi).
    ex = [xs[(i + 1) % n] - xs[i] for i in range(n)]
    ey = [ys[(i + 1) % n] - ys[i] for i in range(n)]
    best = 0
    for i in range(n):
        if half(ex[i], ey[i]) < half(ex[best], ey[best]) or (
                half(ex[i], ey[i]) == half(ex[best], ey[best]) and ex[best] * ey[i] - ey[best] * ex[i] < 0):
            best = i
    xs = xs[best:] + xs[:best]
    ys = ys[best:] + ys[:best]
    ex = ex[best:] + ex[:best]
    ey = ey[best:] + ey[:best]
    eh = [half(ex[i], ey[i]) for i in range(n)]
    # prefix[k] = sum of cross(p_i, p_{i+1}) for i < k over the doubled cycle
    prefix = [0] * (2 * n + 1)
    for k in range(2 * n):
        i = k % n
        j = (k + 1) % n
        prefix[k + 1] = prefix[k] + xs[i] * ys[j] - xs[j] * ys[i]
    total2 = prefix[n]

    def first_edge_not_before(tx, ty):
        """Index of the first edge whose angle is >= angle(t) (cyclic)."""
        th = half(tx, ty)
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) // 2
            h = eh[mid]
            before = h < th or (h == th and ex[mid] * ty - ey[mid] * tx > 0)
            if before:
                lo = mid + 1
            else:
                hi = mid
        return lo % n

    out = []
    pos = 2 + 2 * n
    for _ in range(q):
        ax, ay, bx, by = data[pos:pos + 4]
        pos += 4
        dx, dy = bx - ax, by - ay

        def f(i):
            return dx * (ys[i] - ay) - dy * (xs[i] - ax)

        # f is the dot product with the left normal (-dy, dx); its maximum is
        # at the start of the first edge pointing past (-dy, dx) rotated by +90.
        imax = first_edge_not_before(-dx, -dy)
        imin = first_edge_not_before(dx, dy)
        fmax = f(imax)
        fmin = f(imin)
        if fmax <= 0:
            out.append("0")
            continue
        if fmin >= 0:
            out.append(str(total2 / 2))
            continue
        # chain imin -> imax: f increases; last vertex with f <= 0
        lo, hi = 0, (imax - imin) % n
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if f((imin + mid) % n) <= 0:
                lo = mid
            else:
                hi = mid - 1
        i = (imin + lo) % n
        # chain imax -> imin: f decreases; last vertex with f > 0
        lo, hi = 0, (imin - imax) % n
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if f((imax + mid) % n) > 0:
                lo = mid
            else:
                hi = mid - 1
        j = (imax + lo) % n
        i1 = (i + 1) % n
        j1 = (j + 1) % n
        # X on edge (i, i1), Y on edge (j, j1), as exact fractions
        fi, fi1, fj, fj1 = f(i), f(i1), f(j), f(j1)
        d1 = fi1 - fi
        d2 = fj - fj1
        X0 = xs[i] * d1 + (xs[i1] - xs[i]) * (-fi)
        X1 = ys[i] * d1 + (ys[i1] - ys[i]) * (-fi)
        Y0 = xs[j] * d2 + (xs[j1] - xs[j]) * fj
        Y1 = ys[j] * d2 + (ys[j1] - ys[j]) * fj
        k0 = i1
        k1 = j if j >= i1 else j + n
        inner = prefix[k1] - prefix[k0]
        num = ((X0 * ys[i1] - X1 * xs[i1]) * d2
               + inner * d1 * d2
               + (xs[j] * Y1 - ys[j] * Y0) * d1
               + (Y0 * X1 - Y1 * X0))
        out.append(repr(num / (2 * d1 * d2)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
