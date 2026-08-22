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

def norm(a):
    return math.hypot(a[0], a[1])

def intersection(a, b):
    t = cross(sub(b[0], a[0]), b[1]) / cross(a[1], b[1])
    return add(a[0], mul(a[1], t))

def halfplanes(raw, presorted=False):
    lines = []
    for a, b in raw:
        v = sub(b, a)
        lines.append((a, v, math.atan2(v[1], v[0])))
    if not presorted:
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

def shifted_polygon(poly, r):
    lines = []
    for i, p in enumerate(poly):
        q = poly[(i + 1) % len(poly)]
        v = sub(q, p)
        length = norm(v)
        shift = (-v[1] * r / length, v[0] * r / length)
        lines.append((add(p, shift), add(q, shift)))
    return halfplanes(lines, True)

def shifted_feasible(edges, r):
    dq = deque()
    points = deque()

    def inside(line, point):
        px, py, vx, vy = line
        return vx * (point[1] - py) - vy * (point[0] - px) >= -EPS

    def meet(a, b):
        ax, ay, avx, avy = a
        bx, by, bvx, bvy = b
        denominator = avx * bvy - avy * bvx
        if abs(denominator) <= EPS:
            return None
        t = ((bx - ax) * bvy - (by - ay) * bvx) / denominator
        return (ax + avx * t, ay + avy * t)
    for px, py, vx, vy, nx, ny in edges:
        line = (px + nx * r, py + ny * r, vx, vy)
        while points and (not inside(line, points[-1])):
            points.pop()
            dq.pop()
        while points and (not inside(line, points[0])):
            points.popleft()
            dq.popleft()
        if dq:
            point = meet(dq[-1], line)
            if point is None:
                return False
            points.append(point)
        dq.append(line)
    while points and (not inside(dq[0], points[-1])):
        points.pop()
        dq.pop()
    while points and (not inside(dq[-1], points[0])):
        points.popleft()
        dq.popleft()
    if len(dq) < 3:
        return False
    witness = meet(dq[-1], dq[0])
    if witness is None:
        return False
    for px, py, vx, vy, nx, ny in edges:
        if not inside((px + nx * r, py + ny * r, vx, vy), witness):
            return False
    return True

def inradius(poly):
    at = min(range(len(poly)), key=lambda i: math.atan2(poly[(i + 1) % len(poly)][1] - poly[i][1], poly[(i + 1) % len(poly)][0] - poly[i][0]))
    poly = poly[at:] + poly[:at]
    edges = []
    for i, p in enumerate(poly):
        q = poly[(i + 1) % len(poly)]
        vx, vy = (q[0] - p[0], q[1] - p[1])
        length = math.hypot(vx, vy)
        edges.append((p[0], p[1], vx, vy, -vy / length, vx / length))
    low = 0.0
    high = max(max((x for x, y in poly)) - min((x for x, y in poly)), max((y for x, y in poly)) - min((y for x, y in poly))) + 1
    for _ in range(70):
        mid = (low + high) / 2
        if shifted_feasible(edges, mid):
            low = mid
        else:
            high = mid
    return low

def main():
    d = list(map(float, sys.stdin.buffer.read().split()))
    n = int(d[0])
    p = [tuple(d[1 + 2 * i:3 + 2 * i]) for i in range(n)]
    print(f'{inradius(p):.10f}')
if __name__ == '__main__':
    main()
