import sys

MOD = 1_000_000_007


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    X = data[1:1 + 2 * n:2]
    Y = data[2:2 + 2 * n:2]
    # Orient counterclockwise.
    area2 = sum(X[i] * Y[(i + 1) % n] - X[(i + 1) % n] * Y[i] for i in range(n))
    if area2 < 0:
        X.reverse()
        Y.reverse()

    def cross(a, b, c):
        return (X[b] - X[a]) * (Y[c] - Y[a]) - (Y[b] - Y[a]) * (X[c] - X[a])

    def in_cone(a, b):
        """Is the segment from vertex a towards b inside the interior angle at a?"""
        a0 = (a - 1) % n
        a1 = (a + 1) % n
        if cross(a0, a, a1) >= 0:  # convex vertex
            return cross(a, b, a0) > 0 and cross(b, a, a1) > 0
        return not (cross(a, b, a1) >= 0 and cross(b, a, a0) >= 0)

    edges = [(k, (k + 1) % n) for k in range(n)]

    def crosses_boundary(a, b):
        for c, d in edges:
            if c in (a, b) or d in (a, b):
                continue
            d1 = cross(a, b, c)
            d2 = cross(a, b, d)
            if (d1 > 0) == (d2 > 0):
                continue
            d3 = cross(c, d, a)
            d4 = cross(c, d, b)
            if (d3 > 0) != (d4 > 0):
                return True
        return False

    ok = [[False] * n for _ in range(n)]
    for i in range(n):
        ok[i][(i + 1) % n] = ok[(i + 1) % n][i] = True
        for j in range(i + 2, n):
            if i == 0 and j == n - 1:
                continue
            if in_cone(i, j) and in_cone(j, i) and not crosses_boundary(i, j):
                ok[i][j] = ok[j][i] = True
    # T[i][j]: triangulations of the sub-polygon i, i+1, ..., j closed by chord (i, j).
    T = [[0] * n for _ in range(n)]
    for i in range(n - 1):
        T[i][i + 1] = 1
    for length in range(2, n):
        for i in range(0, n - length):
            j = i + length
            if not ok[i][j]:
                continue
            Ti = T[i]
            oki = ok[i]
            total = 0
            for k in range(i + 1, j):
                if oki[k] and ok[k][j]:
                    total += Ti[k] * T[k][j]
            T[i][j] = total % MOD
    print(T[0][n - 1])


if __name__ == "__main__":
    main()
