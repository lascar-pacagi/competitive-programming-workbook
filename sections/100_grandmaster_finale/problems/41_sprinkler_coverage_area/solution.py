import math
import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    circles = sorted(set((data[1 + 3 * i], data[2 + 3 * i], data[3 + 3 * i]) for i in range(n)), key=lambda c: -c[2])
    # Drop circles inside another one (the list is sorted by decreasing radius,
    # and duplicates are already gone).
    kept = []
    for x, y, r in circles:
        inside = False
        for X, Y, R in kept:
            dx = x - X
            dy = y - Y
            if R >= r and (R - r) * (R - r) >= dx * dx + dy * dy:
                inside = True
                break
        if not inside:
            kept.append((x, y, r))
    total = 0.0
    two_pi = 2 * math.pi
    for i, (x, y, r) in enumerate(kept):
        events = []
        for j, (X, Y, R) in enumerate(kept):
            if i == j:
                continue
            dx = X - x
            dy = Y - y
            d2 = dx * dx + dy * dy
            if d2 >= (r + R) * (r + R):
                continue  # disjoint or externally tangent
            d = math.sqrt(d2)
            # The part of circle i inside circle j is the arc around the
            # direction to j with half-angle alpha (law of cosines).
            cos_a = (r * r + d2 - R * R) / (2 * r * d)
            alpha = math.acos(max(-1.0, min(1.0, cos_a)))
            mid = math.atan2(dy, dx)
            lo = mid - alpha
            hi = mid + alpha
            lo %= two_pi
            hi = lo + 2 * alpha
            if hi > two_pi:
                events.append((lo, two_pi))
                events.append((0.0, hi - two_pi))
            else:
                events.append((lo, hi))
        events.sort()
        # Uncovered arcs contribute (1/2) * integral of (x dy - y dx).
        cur = 0.0
        free = []
        for lo, hi in events:
            if lo > cur:
                free.append((cur, lo))
            if hi > cur:
                cur = hi
        if cur < two_pi:
            free.append((cur, two_pi))
        for a, b in free:
            total += 0.5 * (r * r * (b - a) + x * r * (math.sin(b) - math.sin(a)) - y * r * (math.cos(b) - math.cos(a)))
    print("%.10f" % total)


if __name__ == "__main__":
    main()
