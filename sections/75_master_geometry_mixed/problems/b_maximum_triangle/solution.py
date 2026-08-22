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
    h = hull(list(zip(data[1::2], data[2::2])))
    m = len(h)
    ans = 0
    for i in range(m):
        k = i + 2
        for j in range(i + 1, m):
            k = max(k, j + 1)
            if k >= m:
                break
            while k + 1 < m and abs(cross(h[i], h[j], h[k + 1])) > abs(
                cross(h[i], h[j], h[k])
            ):
                k += 1
            ans = max(ans, abs(cross(h[i], h[j], h[k])))
    print(ans)


if __name__ == "__main__":
    main()
