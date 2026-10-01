import math
import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, k = data[0], data[1]
    pts = [(data[2 + 2 * i], data[3 + 2 * i]) for i in range(n)]
    if k <= 1:
        print("%.10f" % 0.0)
        return
    # Pairwise distances and directions, computed once.
    near = []
    for i, (x, y) in enumerate(pts):
        row = []
        same = 0
        for j, (u, v) in enumerate(pts):
            if i == j:
                continue
            d = math.hypot(u - x, v - y)
            if d == 0:
                same += 1
            else:
                row.append((d, math.atan2(v - y, u - x)))
        row.sort()
        near.append((same, row))
    pi = math.pi

    def feasible(R):
        """Some closed disc of radius R holds k points?  An optimal disc can be
        moved until a point p lies on its boundary; then the centre is on the
        circle of radius R around p, and each q constrains it to an arc."""
        limit = 2 * R * (1 + 1e-12)
        for same, row in near:
            if same + 1 >= k:
                return True
            events = []
            for d, ang in row:
                if d > limit:
                    break
                w = math.acos(min(1.0, d / (2 * R)))
                s = ang - w
                e = ang + w
                if s < -pi:
                    s += 2 * pi
                    e += 2 * pi
                if e > pi:
                    events.append((s, 0))
                    events.append((pi, 1))
                    events.append((-pi, 0))
                    events.append((e - 2 * pi, 1))
                else:
                    events.append((s, 0))
                    events.append((e, 1))
            events.sort()
            cur = best = same + 1
            for _, kind in events:
                if kind == 0:
                    cur += 1
                    if cur > best:
                        best = cur
                else:
                    cur -= 1
            if best >= k:
                return True
        return False

    lo = 0.0
    hi = max(r[-1][0] if r else 0.0 for _, r in near) + 1  # beyond the diameter
    for _ in range(60):
        mid = (lo + hi) / 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid
    print("%.10f" % hi)


if __name__ == "__main__":
    main()
