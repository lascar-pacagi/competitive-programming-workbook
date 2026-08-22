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


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    h = hull(list(zip(data[1::2], data[2::2])))
    m = len(h)
    if m < 2:
        print(0)
        return

    def sub(a, b):
        return (a[0] - b[0], a[1] - b[1])

    def d2(a, b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

    ans = 0
    j = 1
    for i in range(m):
        ni = (i + 1) % m
        e = sub(h[ni], h[i])
        while cross(e, sub(h[(j + 1) % m], h[i])) > cross(e, sub(h[j], h[i])):
            j = (j + 1) % m
        ans = max(ans, d2(h[i], h[j]), d2(h[ni], h[j]))
    print(ans)


if __name__ == "__main__":
    main()
