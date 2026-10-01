import heapq
import math
import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    sx, sy, tx, ty, k = data[:5]
    pos = 5
    polys = []
    for _ in range(k):
        m = data[pos]
        pos += 1
        poly = [(data[pos + 2 * i], data[pos + 2 * i + 1]) for i in range(m)]
        pos += 2 * m
        area2 = sum(poly[i][0] * poly[(i + 1) % m][1] - poly[(i + 1) % m][0] * poly[i][1] for i in range(m))
        if area2 < 0:
            poly.reverse()
        polys.append(poly)
    nodes = [(sx, sy), (tx, ty)]
    for poly in polys:
        nodes.extend(poly)

    def blocked(P, Q):
        """Does segment PQ meet the interior of some obstacle?

        Clip t in [0,1] with the open half-planes of each (CCW) edge; the open
        constraints t > lo, t < hi are kept as exact fractions."""
        px, py = P
        dx, dy = Q[0] - px, Q[1] - py
        for poly in polys:
            m = len(poly)
            lo_n, lo_d = -1, 1  # lower bound, as a fraction (t > lo)
            hi_n, hi_d = 2, 1   # upper bound (t < hi)
            feasible = True
            for i in range(m):
                ax, ay = poly[i]
                bx, by = poly[(i + 1) % m]
                ex, ey = bx - ax, by - ay
                c0 = ex * (py - ay) - ey * (px - ax)   # f(0)
                c1 = ex * dy - ey * dx                 # slope
                # need c0 + t * c1 > 0
                if c1 == 0:
                    if c0 <= 0:
                        feasible = False
                        break
                elif c1 > 0:   # t > -c0 / c1
                    num, den = -c0, c1
                    if num * lo_d > lo_n * den:
                        lo_n, lo_d = num, den
                else:          # t < -c0 / c1 = c0 / -c1
                    num, den = c0, -c1
                    if num * hi_d < hi_n * den:
                        hi_n, hi_d = num, den
            if not feasible:
                continue
            # nonempty: lo < hi, lo < 1, hi > 0
            if lo_n * hi_d < hi_n * lo_d and lo_n < lo_d and hi_n > 0:
                return True
        return False

    V = len(nodes)
    adj = [[] for _ in range(V)]
    for i in range(V):
        for j in range(i + 1, V):
            if not blocked(nodes[i], nodes[j]):
                w = math.hypot(nodes[i][0] - nodes[j][0], nodes[i][1] - nodes[j][1])
                adj[i].append((j, w))
                adj[j].append((i, w))
    dist = [math.inf] * V
    dist[0] = 0.0
    heap = [(0.0, 0)]
    while heap:
        d, v = heapq.heappop(heap)
        if d > dist[v]:
            continue
        if v == 1:
            break
        for w, c in adj[v]:
            nd = d + c
            if nd < dist[w]:
                dist[w] = nd
                heapq.heappush(heap, (nd, w))
    print("%.10f" % dist[1])


if __name__ == "__main__":
    main()
