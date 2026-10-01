#include <bits/stdc++.h>
using namespace std;

// Binary search the radius R.  If some closed disc of radius R holds k points,
// it can be translated until one of them, p, lies on its boundary; the centre
// is then on the circle of radius R around p, and every other point q within
// 2R allows an arc of centre angles of half-width acos(|pq| / 2R).  An
// angular sweep finds the deepest overlap.  O(n^2 log n) per probe.

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    vector<double> x(n), y(n);
    for (int i = 0; i < n; i++) scanf("%lf %lf", &x[i], &y[i]);
    if (k <= 1) {
        printf("%.10f\n", 0.0);
        return 0;
    }
    vector<int> same(n, 0);
    vector<vector<pair<double, double>>> near(n);
    double far = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j) continue;
            double d = hypot(x[j] - x[i], y[j] - y[i]);
            if (d == 0) same[i]++;
            else near[i].push_back({d, atan2(y[j] - y[i], x[j] - x[i])});
            far = max(far, d);
        }
        sort(near[i].begin(), near[i].end());
    }
    const double PI = acos(-1.0);
    vector<pair<double, int>> events;
    auto feasible = [&](double R) {
        double limit = 2 * R * (1 + 1e-12);
        for (int i = 0; i < n; i++) {
            if (same[i] + 1 >= k) return true;
            events.clear();
            for (auto [d, ang] : near[i]) {
                if (d > limit) break;
                double w = acos(min(1.0, d / (2 * R)));
                double s = ang - w, e = ang + w;
                if (s < -PI) s += 2 * PI, e += 2 * PI;
                if (e > PI) {
                    events.push_back({s, 0});
                    events.push_back({PI, 1});
                    events.push_back({-PI, 0});
                    events.push_back({e - 2 * PI, 1});
                } else {
                    events.push_back({s, 0});
                    events.push_back({e, 1});
                }
            }
            sort(events.begin(), events.end());
            int cur = same[i] + 1, best = cur;
            for (auto [a, kind] : events) {
                if (kind == 0) best = max(best, ++cur);
                else cur--;
            }
            if (best >= k) return true;
        }
        return false;
    };
    double lo = 0, hi = far + 1;
    for (int it = 0; it < 60; it++) {
        double mid = (lo + hi) / 2;
        if (feasible(mid)) hi = mid;
        else lo = mid;
    }
    printf("%.10f\n", hi);
}
