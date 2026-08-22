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


def normalize(p):
    if len(p) > 2 and cross(p[0], p[1], p[2]) < 0:
        p.reverse()
    at = min(range(len(p)), key=lambda i: (p[i][1], p[i][0]))
    return p[at:] + p[:at]


def minkowski(a, b):
    a = normalize(a)
    b = normalize(b)
    if len(a) < 3 or len(b) < 3:
        return hull([(x[0] + y[0], x[1] + y[1]) for x in a for y in b])
    n, m = len(a), len(b)
    i = j = 0
    r = [(a[0][0] + b[0][0], a[0][1] + b[0][1])]
    while i < n or j < m:
        ea = (
            (a[(i + 1) % n][0] - a[i][0], a[(i + 1) % n][1] - a[i][1])
            if i < n
            else (0, 0)
        )
        eb = (
            (b[(j + 1) % m][0] - b[j][0], b[(j + 1) % m][1] - b[j][1])
            if j < m
            else (0, 0)
        )
        z = cross(ea, eb) if i < n and j < m else 0
        if j == m or i < n and z > 0:
            step = ea
            i += 1
        elif i == n or z < 0:
            step = eb
            j += 1
        else:
            step = (ea[0] + eb[0], ea[1] + eb[1])
            i += 1
            j += 1
        r.append((r[-1][0] + step[0], r[-1][1] + step[1]))
    return hull(r[:-1])


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
    n, m, q = next(it), next(it), next(it)
    a = [(next(it), next(it)) for _ in range(n)]
    b = [(next(it), next(it)) for _ in range(m)]
    b = [(-x, -y) for x, y in reversed(b)]
    s = minkowski(a, b)
    print(
        "\n".join(
            "YES" if locate(s, (next(it), next(it))) >= 0 else "NO"
            for _ in range(q)
        )
    )


if __name__ == "__main__":
    main()
