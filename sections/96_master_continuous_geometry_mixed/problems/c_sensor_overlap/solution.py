import sys, math, random
from collections import deque
EPS = 1e-10

def overlap(c1, c2):
    x1, y1, r1 = c1
    x2, y2, r2 = c2
    d = math.hypot(x1 - x2, y1 - y2)
    if d >= r1 + r2:
        return 0.0
    if d <= abs(r1 - r2):
        return math.pi * min(r1, r2) ** 2
    a = math.acos(max(-1, min(1, (d * d + r1 * r1 - r2 * r2) / (2 * d * r1))))
    b = math.acos(max(-1, min(1, (d * d + r2 * r2 - r1 * r1) / (2 * d * r2))))
    return r1 * r1 * a + r2 * r2 * b - d * r1 * math.sin(a)

def main():
    d = list(map(float, sys.stdin.buffer.read().split()))
    print(f'{overlap(d[:3], d[3:6]):.10f}')
if __name__ == '__main__':
    main()
