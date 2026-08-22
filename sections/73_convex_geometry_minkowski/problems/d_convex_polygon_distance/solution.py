import math
import sys


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def subtract(a, b):
    return a[0] - b[0], a[1] - b[1]


def normalize(polygon):
    start = min(range(len(polygon)), key=lambda i: (polygon[i][1], polygon[i][0]))
    return polygon[start:] + polygon[:start]


def minkowski(a, b):
    a = normalize(a)
    b = normalize(b)
    edge_a = [subtract(a[(i + 1) % len(a)], a[i]) for i in range(len(a))]
    edge_b = [subtract(b[(i + 1) % len(b)], b[i]) for i in range(len(b))]
    result = [(a[0][0] + b[0][0], a[0][1] + b[0][1])]
    i = j = 0
    while i < len(edge_a) or j < len(edge_b):
        if j == len(edge_b) or (
            i < len(edge_a) and cross(edge_a[i], edge_b[j]) > 0
        ):
            step = edge_a[i]
            i += 1
        elif i == len(edge_a) or cross(edge_a[i], edge_b[j]) < 0:
            step = edge_b[j]
            j += 1
        else:
            step = (edge_a[i][0] + edge_b[j][0], edge_a[i][1] + edge_b[j][1])
            i += 1
            j += 1
        result.append((result[-1][0] + step[0], result[-1][1] + step[1]))
    result.pop()
    return result


def segment_distance(a, b):
    dx, dy = b[0] - a[0], b[1] - a[1]
    parameter = -(a[0] * dx + a[1] * dy) / (dx * dx + dy * dy)
    parameter = min(1.0, max(0.0, parameter))
    x = a[0] + parameter * dx
    y = a[1] + parameter * dy
    return math.hypot(x, y)


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    at = 0
    n = data[at]
    at += 1
    a = [(data[at + 2 * i], data[at + 2 * i + 1]) for i in range(n)]
    at += 2 * n
    m = data[at]
    at += 1
    negative_b = [(-data[at + 2 * i], -data[at + 2 * i + 1]) for i in range(m)]
    difference = minkowski(a, negative_b)
    contains_origin = all(
        cross(
            subtract(difference[(i + 1) % len(difference)], difference[i]),
            (-difference[i][0], -difference[i][1]),
        ) >= 0
        for i in range(len(difference))
    )
    answer = 0.0 if contains_origin else min(
        segment_distance(difference[i], difference[(i + 1) % len(difference)])
        for i in range(len(difference))
    )
    print(f"{answer:.12f}")


if __name__ == "__main__":
    main()
