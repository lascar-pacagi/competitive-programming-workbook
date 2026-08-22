import sys, math, random
from collections import deque
EPS = 1e-10

def tangent_count(c1, c2):
    x1, y1, r1 = c1
    x2, y2, r2 = c2
    d = math.hypot(x1 - x2, y1 - y2)
    if d <= EPS:
        return -1 if abs(r1 - r2) <= EPS else 0
    ans = 0
    for z in (abs(r1 - r2), r1 + r2):
        ans += 2 if d > z + EPS else 1 if abs(d - z) <= EPS else 0
    return ans

def main():
    d = list(map(float, sys.stdin.buffer.read().split()))
    print(tangent_count(d[:3], d[3:6]))
if __name__ == '__main__':
    main()
