import sys, math, random
from collections import deque
EPS = 1e-10

def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])

def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]

def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]

def norm(a):
    return math.hypot(a[0], a[1])

def circle2(a, b):
    c = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
    return (c, norm(sub(a, b)) / 2)

def circle3(a, b, c):
    d = 2 * cross(sub(b, a), sub(c, a))
    ux = (dot(a, a) * (b[1] - c[1]) + dot(b, b) * (c[1] - a[1]) + dot(c, c) * (a[1] - b[1])) / d
    uy = (dot(a, a) * (c[0] - b[0]) + dot(b, b) * (a[0] - c[0]) + dot(c, c) * (b[0] - a[0])) / d
    center = (ux, uy)
    return (center, norm(sub(center, a)))

def minimum_circle(points):
    p = points[:]
    random.Random(947311).shuffle(p)
    circle = ((0.0, 0.0), -1.0)

    def outside(x, c):
        return c[1] < 0 or norm(sub(x, c[0])) > c[1] + 1e-09
    for i in range(len(p)):
        if outside(p[i], circle):
            circle = (p[i], 0.0)
            for j in range(i):
                if outside(p[j], circle):
                    circle = circle2(p[i], p[j])
                    for k in range(j):
                        if outside(p[k], circle):
                            circle = circle3(p[i], p[j], p[k])
    return circle

def main():
    d = list(map(float, sys.stdin.buffer.read().split()))
    n = int(d[0])
    p = [tuple(d[1 + 2 * i:3 + 2 * i]) for i in range(n)]
    c, r = minimum_circle(p)
    print(f'{c[0]:.10f} {c[1]:.10f} {r:.10f}')
if __name__ == '__main__':
    main()
