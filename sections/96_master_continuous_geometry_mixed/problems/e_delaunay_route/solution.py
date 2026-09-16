import sys, math, random, heapq
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

def circle3(a, b, c):
    d = 2 * cross(sub(b, a), sub(c, a))
    ux = (dot(a, a) * (b[1] - c[1]) + dot(b, b) * (c[1] - a[1]) + dot(c, c) * (a[1] - b[1])) / d
    uy = (dot(a, a) * (c[0] - b[0]) + dot(b, b) * (a[0] - c[0]) + dot(c, c) * (b[0] - a[0])) / d
    center = (ux, uy)
    return (center, norm(sub(center, a)))

def orient(a, b, c):
    return cross(sub(b, a), sub(c, a))

def in_circumcircle(a, b, c, p):
    ax = a[0] - p[0]
    ay = a[1] - p[1]
    bx = b[0] - p[0]
    by = b[1] - p[1]
    cx = c[0] - p[0]
    cy = c[1] - p[1]
    det = (ax * ax + ay * ay) * (bx * cy - by * cx) - (bx * bx + by * by) * (ax * cy - ay * cx) + (cx * cx + cy * cy) * (ax * by - ay * bx)
    return det > EPS

def delaunay(points):
    n = len(points)
    if n < 3:
        return ([], [])
    minx = min((x for x, y in points))
    maxx = max((x for x, y in points))
    miny = min((y for x, y in points))
    maxy = max((y for x, y in points))
    span = max(maxx - minx, maxy - miny, 1.0)
    cx = (minx + maxx) / 2
    cy = (miny + maxy) / 2
    p = points + [(cx - 10000 * span, cy - 8000 * span), (cx + 10000 * span, cy - 8000 * span), (cx, cy + 10000 * span)]
    tri = [(n, n + 1, n + 2)]
    for idx in range(n):
        bad = [t for t in tri if in_circumcircle(p[t[0]], p[t[1]], p[t[2]], p[idx])]
        count = {}
        direct = {}
        for t in bad:
            for e in ((t[0], t[1]), (t[1], t[2]), (t[2], t[0])):
                key = tuple(sorted(e))
                count[key] = count.get(key, 0) + 1
                direct[key] = e
        gone = set(bad)
        tri = [t for t in tri if t not in gone]
        for key, cnt in count.items():
            if cnt == 1:
                u, v = direct[key]
                if orient(p[u], p[v], p[idx]) < 0:
                    u, v = (v, u)
                tri.append((u, v, idx))
    tri = [t for t in tri if max(t) < n]
    edges = set()
    for a, b, c in tri:
        edges |= {tuple(sorted((a, b))), tuple(sorted((b, c))), tuple(sorted((c, a)))}
    return (tri, sorted(edges))

def shortest_route(points, source, sink):
    _, edges = delaunay(points)
    graph = [[] for _ in points]
    for u, v in edges:
        weight = math.dist(points[u], points[v])
        graph[u].append((v, weight))
        graph[v].append((u, weight))
    distance = [math.inf] * len(points)
    distance[source] = 0.0
    queue = [(0.0, source)]
    while queue:
        current, u = heapq.heappop(queue)
        if current != distance[u]:
            continue
        for v, weight in graph[u]:
            candidate = current + weight
            if candidate < distance[v]:
                distance[v] = candidate
                heapq.heappush(queue, (candidate, v))
    return distance[sink]

def main():
    d = list(map(float, sys.stdin.buffer.read().split()))
    n, source, sink = map(int, d[:3])
    p = [tuple(d[3 + 2 * i:5 + 2 * i]) for i in range(n)]
    print(f'{shortest_route(p, source - 1, sink - 1):.10f}')
if __name__ == '__main__':
    main()
