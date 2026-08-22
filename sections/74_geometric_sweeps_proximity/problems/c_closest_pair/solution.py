import sys

INF = 10**50


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    points = sorted(zip(data[1::2], data[2::2]))
    n = len(points)

    def solve(p):
        n = len(p)
        if n <= 3:
            d = min(
                (
                    (p[i][0] - p[j][0]) ** 2 + (p[i][1] - p[j][1]) ** 2
                    for i in range(n)
                    for j in range(i)
                ),
                default=INF,
            )
            return d, sorted(p, key=lambda x: x[1])
        m = n // 2
        mid = p[m][0]
        dl, l = solve(p[:m])
        dr, r = solve(p[m:])
        d = min(dl, dr)
        merged = []
        i = j = 0
        while i < len(l) or j < len(r):
            if j == len(r) or i < len(l) and l[i][1] <= r[j][1]:
                merged.append(l[i])
                i += 1
            else:
                merged.append(r[j])
                j += 1
        strip = []
        for point in merged:
            if (point[0] - mid) ** 2 < d:
                for other in reversed(strip):
                    if (point[1] - other[1]) ** 2 >= d:
                        break
                    d = min(
                        d,
                        (point[0] - other[0]) ** 2
                        + (point[1] - other[1]) ** 2,
                    )
                strip.append(point)
        return d, merged

    print(solve(points)[0])


if __name__ == "__main__":
    main()
