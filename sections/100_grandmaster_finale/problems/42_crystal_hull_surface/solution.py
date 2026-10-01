import math
import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    pts = [(data[1 + 3 * i], data[2 + 3 * i], data[3 + 3 * i]) for i in range(n)]

    def orient(a, b, c, d):
        """Positive when d is on the side of plane abc that the normal
        (b - a) x (c - a) points to."""
        ax, ay, az = pts[a]
        ux, uy, uz = pts[b][0] - ax, pts[b][1] - ay, pts[b][2] - az
        vx, vy, vz = pts[c][0] - ax, pts[c][1] - ay, pts[c][2] - az
        wx, wy, wz = pts[d][0] - ax, pts[d][1] - ay, pts[d][2] - az
        return (ux * (vy * wz - vz * wy) - uy * (vx * wz - vz * wx) + uz * (vx * wy - vy * wx))

    # Initial tetrahedron: four affinely independent points.
    i0 = 0
    i1 = next(i for i in range(1, n) if pts[i] != pts[i0])
    i2 = None
    for i in range(n):
        ux = [pts[i1][k] - pts[i0][k] for k in range(3)]
        vx = [pts[i][k] - pts[i0][k] for k in range(3)]
        cr = (ux[1] * vx[2] - ux[2] * vx[1], ux[2] * vx[0] - ux[0] * vx[2], ux[0] * vx[1] - ux[1] * vx[0])
        if cr != (0, 0, 0):
            i2 = i
            break
    i3 = next(i for i in range(n) if orient(i0, i1, i2, i) != 0)
    if orient(i0, i1, i2, i3) > 0:
        i1, i2 = i2, i1  # make face (i0, i1, i2) point away from i3
    faces = {}
    edge_face = {}
    next_id = [0]

    def add_face(a, b, c):
        fid = next_id[0]
        next_id[0] += 1
        faces[fid] = (a, b, c)
        edge_face[(a, b)] = fid
        edge_face[(b, c)] = fid
        edge_face[(c, a)] = fid

    add_face(i0, i1, i2)
    add_face(i0, i3, i1)
    add_face(i1, i3, i2)
    add_face(i2, i3, i0)
    used = {i0, i1, i2, i3}
    for p in range(n):
        if p in used:
            continue
        visible = [fid for fid, (a, b, c) in faces.items() if orient(a, b, c, p) > 0]
        if not visible:
            continue  # inside (or on) the current hull
        vis = set(visible)
        horizon = []
        for fid in visible:
            a, b, c = faces[fid]
            for u, v in ((a, b), (b, c), (c, a)):
                if edge_face.get((v, u)) not in vis:
                    horizon.append((u, v))
        for fid in visible:
            a, b, c = faces.pop(fid)
            for u, v in ((a, b), (b, c), (c, a)):
                if edge_face.get((u, v)) == fid:
                    del edge_face[(u, v)]
        for u, v in horizon:
            add_face(u, v, p)
    area = 0.0
    for a, b, c in faces.values():
        ux, uy, uz = (pts[b][k] - pts[a][k] for k in range(3))
        vx, vy, vz = (pts[c][k] - pts[a][k] for k in range(3))
        cx, cy, cz = uy * vz - uz * vy, uz * vx - ux * vz, ux * vy - uy * vx
        area += math.sqrt(cx * cx + cy * cy + cz * cz) / 2
    print("%.10f" % area)


if __name__ == "__main__":
    main()
