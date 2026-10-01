#include <bits/stdc++.h>
using namespace std;

// A shortest obstacle-avoiding path is a polyline whose bends are obstacle
// corners (shorten any other bend), so it lives in the visibility graph on
// {S, T, corners}.  Segment PQ is blocked iff some point of it is strictly
// inside an obstacle: intersect t in [0,1] with the open half-planes of the
// obstacle's counterclockwise edges, comparing the bounds as exact fractions.
// Dijkstra on the visibility graph gives the answer.

typedef long long ll;
typedef __int128 i128;
typedef pair<ll, ll> Pt;

int main() {
    ll sx, sy, tx, ty;
    int k;
    cin >> sx >> sy >> tx >> ty >> k;
    vector<vector<Pt>> polys(k);
    for (auto& poly : polys) {
        int m;
        cin >> m;
        poly.resize(m);
        for (auto& p : poly) cin >> p.first >> p.second;
        i128 area2 = 0;
        for (int i = 0; i < m; i++)
            area2 += (i128)poly[i].first * poly[(i + 1) % m].second - (i128)poly[(i + 1) % m].first * poly[i].second;
        if (area2 < 0) reverse(poly.begin(), poly.end());
    }
    vector<Pt> nodes = {{sx, sy}, {tx, ty}};
    for (auto& poly : polys) nodes.insert(nodes.end(), poly.begin(), poly.end());

    auto blocked = [&](Pt P, Pt Q) {
        ll dx = Q.first - P.first, dy = Q.second - P.second;
        for (auto& poly : polys) {
            int m = poly.size();
            i128 loN = -1, loD = 1, hiN = 2, hiD = 1;
            bool feasible = true;
            for (int i = 0; i < m && feasible; i++) {
                ll ax = poly[i].first, ay = poly[i].second;
                ll ex = poly[(i + 1) % m].first - ax, ey = poly[(i + 1) % m].second - ay;
                i128 c0 = (i128)ex * (P.second - ay) - (i128)ey * (P.first - ax);
                i128 c1 = (i128)ex * dy - (i128)ey * dx;
                if (c1 == 0) {
                    if (c0 <= 0) feasible = false;
                } else if (c1 > 0) {
                    if (-c0 * loD > loN * c1) loN = -c0, loD = c1;
                } else {
                    if (c0 * hiD < hiN * (-c1)) hiN = c0, hiD = -c1;
                }
            }
            if (feasible && loN * hiD < hiN * loD && loN < loD && hiN > 0) return true;
        }
        return false;
    };

    int V = nodes.size();
    vector<vector<pair<int, double>>> adj(V);
    for (int i = 0; i < V; i++)
        for (int j = i + 1; j < V; j++)
            if (!blocked(nodes[i], nodes[j])) {
                double w = hypot((double)(nodes[i].first - nodes[j].first), (double)(nodes[i].second - nodes[j].second));
                adj[i].push_back({j, w});
                adj[j].push_back({i, w});
            }
    vector<double> dist(V, 1e300);
    priority_queue<pair<double, int>, vector<pair<double, int>>, greater<>> pq;
    dist[0] = 0;
    pq.push({0, 0});
    while (!pq.empty()) {
        auto [d, v] = pq.top();
        pq.pop();
        if (d > dist[v]) continue;
        for (auto [w, c] : adj[v])
            if (d + c < dist[w]) {
                dist[w] = d + c;
                pq.push({dist[w], w});
            }
    }
    printf("%.10f\n", dist[1]);
}
