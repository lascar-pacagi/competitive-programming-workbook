import argparse
import math
import random
from pathlib import Path


def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def hull(points):
    pts = sorted(set(points))
    if len(pts) < 3:
        return pts
    lower, upper = [], []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def separated(P, Q, poly):
    """Separating-axis test: is segment PQ disjoint from the open polygon?

    Weak separation along an edge normal of the polygon or the normal of PQ."""
    axes = []
    m = len(poly)
    for i in range(m):
        ex, ey = poly[(i + 1) % m][0] - poly[i][0], poly[(i + 1) % m][1] - poly[i][1]
        axes.append((-ey, ex))
    axes.append((-(Q[1] - P[1]), Q[0] - P[0]))
    for ax, ay in axes:
        if ax == 0 and ay == 0:
            continue
        seg = [ax * P[0] + ay * P[1], ax * Q[0] + ay * Q[1]]
        pol = [ax * x + ay * y for x, y in poly]
        if max(seg) <= min(pol) or max(pol) <= min(seg):
            return True
    return False


def brute(S, T, polys):
    nodes = [S, T] + [p for poly in polys for p in poly]
    V = len(nodes)
    INF = float("inf")
    d = [[INF] * V for _ in range(V)]
    for i in range(V):
        d[i][i] = 0.0
        for j in range(V):
            if i != j and all(separated(nodes[i], nodes[j], poly) for poly in polys):
                d[i][j] = math.dist(nodes[i], nodes[j])
    for k in range(V):
        for i in range(V):
            dik = d[i][k]
            if dik == INF:
                continue
            row_k = d[k]
            row_i = d[i]
            for j in range(V):
                if dik + row_k[j] < row_i[j]:
                    row_i[j] = dik + row_k[j]
    return d[0][1]


def make_case(rng):
    cells = 4
    size = rng.choice([10, 100, 10000])
    polys = []
    free = []
    for cx in range(cells):
        for cy in range(cells):
            x0, y0 = cx * 2 * size, cy * 2 * size
            if rng.random() < 0.6:
                pts = [(rng.randint(x0 + 1, x0 + 2 * size - 1), rng.randint(y0 + 1, y0 + 2 * size - 1)) for _ in range(rng.randint(3, 6))]
                h = hull(pts)
                if len(h) >= 3:
                    if rng.random() < 0.5:
                        h.reverse()
                    polys.append(h)
                    continue
            free.append((x0 + size, y0 + size))
    if len(free) < 2:
        free += [(-size, -size), (2 * cells * size + size, 2 * cells * size + size)]
    S, T = rng.sample(free, 2)
    return S, T, polys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=25)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for i in range(args.count):
        S, T, polys = make_case(rng)
        text = f"{S[0]} {S[1]} {T[0]} {T[1]}\n{len(polys)}\n"
        for poly in polys:
            text += f"{len(poly)}\n" + "".join(f"{x} {y}\n" for x, y in poly)
        stem = args.out_dir / f"case{i:03d}"
        stem.with_suffix(".in").write_text(text)
        stem.with_suffix(".out").write_text("%.10f\n" % brute(S, T, polys))


if __name__ == "__main__":
    main()
