import sys


def cross(a, b, c=None):
    if c is None:
        return a[0] * b[1] - a[1] * b[0]
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    lower = []
    for point in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    upper = []
    for point in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]


def locate(p, q):
    n = len(p)
    if n == 1:
        return 0 if p[0] == q else -1
    if n == 2:
        return (
            0
            if cross(p[0], p[1], q) == 0
            and min(p[0][0], p[1][0]) <= q[0] <= max(p[0][0], p[1][0])
            and min(p[0][1], p[1][1]) <= q[1] <= max(p[0][1], p[1][1])
            else -1
        )
    a, b = cross(p[0], p[1], q), cross(p[0], p[-1], q)
    if a < 0 or b > 0:
        return -1
    if a == 0:
        return (
            0
            if (q[0] - p[0][0]) ** 2 + (q[1] - p[0][1]) ** 2
            <= (p[1][0] - p[0][0]) ** 2 + (p[1][1] - p[0][1]) ** 2
            else -1
        )
    if b == 0:
        return (
            0
            if (q[0] - p[0][0]) ** 2 + (q[1] - p[0][1]) ** 2
            <= (p[-1][0] - p[0][0]) ** 2 + (p[-1][1] - p[0][1]) ** 2
            else -1
        )
    l, r = 1, n - 1
    while r - l > 1:
        mid = (l + r) // 2
        if cross(p[0], p[mid], q) >= 0:
            l = mid
        else:
            r = mid
    z = cross(p[l], p[(l + 1) % n], q)
    return -1 if z < 0 else (0 if z == 0 else 1)


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    n, q = next(it), next(it)
    h = hull([(next(it), next(it)) for _ in range(n)])
    out = []
    for _ in range(q):
        z = locate(h, (next(it), next(it)))
        out.append("OUT" if z < 0 else ("BOUNDARY" if z == 0 else "IN"))
    print("\n".join(out))


if __name__ == "__main__":
    main()
