#include <bits/stdc++.h>
using namespace std;

// Incremental 3D convex hull.  Faces are stored counterclockwise as seen from
// outside, so a point sees a face exactly when it lies strictly on the
// outward side (exact 128-bit orientation tests).  Adding a point removes its
// visible faces and connects the horizon -- edges between a visible and an
// invisible face -- to the point.  The surface area is the sum of triangle
// areas; the statement guarantees that hull faces are triangles.

typedef long long ll;
typedef __int128 i128;

int n;
vector<array<ll, 3>> pts;

i128 orient(int a, int b, int c, int d) {
    i128 ux = pts[b][0] - pts[a][0], uy = pts[b][1] - pts[a][1], uz = pts[b][2] - pts[a][2];
    i128 vx = pts[c][0] - pts[a][0], vy = pts[c][1] - pts[a][1], vz = pts[c][2] - pts[a][2];
    i128 wx = pts[d][0] - pts[a][0], wy = pts[d][1] - pts[a][1], wz = pts[d][2] - pts[a][2];
    return ux * (vy * wz - vz * wy) - uy * (vx * wz - vz * wx) + uz * (vx * wy - vy * wx);
}

int main() {
    scanf("%d", &n);
    pts.resize(n);
    for (auto& p : pts) scanf("%lld %lld %lld", &p[0], &p[1], &p[2]);
    int i0 = 0, i1 = -1, i2 = -1, i3 = -1;
    for (int i = 1; i < n && i1 < 0; i++)
        if (pts[i] != pts[i0]) i1 = i;
    for (int i = 0; i < n && i2 < 0; i++) {
        i128 ux = pts[i1][0] - pts[i0][0], uy = pts[i1][1] - pts[i0][1], uz = pts[i1][2] - pts[i0][2];
        i128 vx = pts[i][0] - pts[i0][0], vy = pts[i][1] - pts[i0][1], vz = pts[i][2] - pts[i0][2];
        if (uy * vz - uz * vy != 0 || uz * vx - ux * vz != 0 || ux * vy - uy * vx != 0) i2 = i;
    }
    for (int i = 0; i < n && i3 < 0; i++)
        if (orient(i0, i1, i2, i) != 0) i3 = i;
    if (orient(i0, i1, i2, i3) > 0) swap(i1, i2);  // outward normal away from i3

    vector<array<int, 3>> faces;
    vector<char> alive;
    map<pair<int, int>, int> edgeFace;
    auto addFace = [&](int a, int b, int c) {
        int id = faces.size();
        faces.push_back({a, b, c});
        alive.push_back(1);
        edgeFace[{a, b}] = id;
        edgeFace[{b, c}] = id;
        edgeFace[{c, a}] = id;
    };
    addFace(i0, i1, i2);
    addFace(i0, i3, i1);
    addFace(i1, i3, i2);
    addFace(i2, i3, i0);
    vector<int> live = {0, 1, 2, 3};
    vector<char> isVisible;
    for (int p = 0; p < n; p++) {
        if (p == i0 || p == i1 || p == i2 || p == i3) continue;
        vector<int> visible;
        isVisible.assign(faces.size(), 0);
        for (int id : live)
            if (orient(faces[id][0], faces[id][1], faces[id][2], p) > 0) {
                visible.push_back(id);
                isVisible[id] = 1;
            }
        if (visible.empty()) continue;
        vector<pair<int, int>> horizon;
        for (int id : visible) {
            auto [a, b, c] = faces[id];
            for (auto [u, v] : {pair(a, b), pair(b, c), pair(c, a)}) {
                int other = edgeFace[{v, u}];
                if (!isVisible[other]) horizon.push_back({u, v});
            }
        }
        for (int id : visible) {
            alive[id] = 0;
            auto [a, b, c] = faces[id];
            for (auto e : {pair(a, b), pair(b, c), pair(c, a)}) {
                auto it = edgeFace.find(e);
                if (it != edgeFace.end() && it->second == id) edgeFace.erase(it);
            }
        }
        for (auto [u, v] : horizon) addFace(u, v, p);
        vector<int> next;
        for (int id : live)
            if (alive[id]) next.push_back(id);
        for (int id = (int)faces.size() - (int)horizon.size(); id < (int)faces.size(); id++) next.push_back(id);
        live.swap(next);
    }
    double area = 0;
    for (int id : live) {
        auto [a, b, c] = faces[id];
        double ux = pts[b][0] - pts[a][0], uy = pts[b][1] - pts[a][1], uz = pts[b][2] - pts[a][2];
        double vx = pts[c][0] - pts[a][0], vy = pts[c][1] - pts[a][1], vz = pts[c][2] - pts[a][2];
        double cx = uy * vz - uz * vy, cy = uz * vx - ux * vz, cz = ux * vy - uy * vx;
        area += sqrt(cx * cx + cy * cy + cz * cz) / 2;
    }
    printf("%.10f\n", area);
}
