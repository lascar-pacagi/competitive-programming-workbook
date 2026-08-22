import sys, math, random
from collections import deque
EPS = 1e-10

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])

def mul(a, k):
    return (a[0] * k, a[1] * k)

def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]

def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]

def intersection(a, b):
    t = cross(sub(b[0], a[0]), b[1]) / cross(a[1], b[1])
    return add(a[0], mul(a[1], t))

def halfplanes(raw):
    lines = []
    for a, b in raw:
        v = sub(b, a)
        lines.append((a, v, math.atan2(v[1], v[0])))
    lines.sort(key=lambda z: z[2])
    unique = []
    for p, v, angle in lines:
        if unique and abs(cross(unique[-1][1], v)) <= EPS and (dot(unique[-1][1], v) > 0):
            if cross(unique[-1][1], sub(p, unique[-1][0])) > EPS:
                unique[-1] = (p, v, angle)
        else:
            unique.append((p, v, angle))
    dq = deque()
    points = deque()

    def inside(line, p):
        return cross(line[1], sub(p, line[0])) >= -EPS
    for line in unique:
        while points and (not inside(line, points[-1])):
            points.pop()
            dq.pop()
        while points and (not inside(line, points[0])):
            points.popleft()
            dq.popleft()
        if dq and abs(cross(dq[-1][1], line[1])) <= EPS:
            return []
        if dq:
            points.append(intersection(dq[-1], line))
        dq.append(line)
    while points and (not inside(dq[0], points[-1])):
        points.pop()
        dq.pop()
    while points and (not inside(dq[-1], points[0])):
        points.popleft()
        dq.popleft()
    if len(dq) < 3:
        return []
    points.append(intersection(dq[-1], dq[0]))
    return list(points)

def area(poly):
    return abs(sum((cross(poly[i], poly[(i + 1) % len(poly)]) for i in range(len(poly))))) / 2 if len(poly) >= 3 else 0.0

def main():
    d = list(map(float, sys.stdin.buffer.read().split()))
    n = int(d[0])
    raw = []
    for i in range(n):
        x1, y1, x2, y2 = d[1 + 4 * i:5 + 4 * i]
        raw.append(((x1, y1), (x2, y2)))
    print(f'{area(halfplanes(raw)):.10f}')
if __name__ == '__main__':
    main()
