#include <bits/stdc++.h>
using namespace std;

// Green's theorem: the area of the union is (1/2) * the integral of
// (x dy - y dx) along its boundary, and the boundary consists of the arcs of
// each circle not covered by another circle.  After removing duplicates and
// circles contained in others, each other circle covers one angular interval
// of circle i (law of cosines); sweep the sorted intervals and integrate the
// uncovered arcs in closed form.  O(n^2 log n).

int main() {
    int n;
    cin >> n;
    vector<array<long long, 3>> raw(n);
    for (auto& c : raw) cin >> c[0] >> c[1] >> c[2];
    sort(raw.begin(), raw.end());
    raw.erase(unique(raw.begin(), raw.end()), raw.end());
    sort(raw.begin(), raw.end(), [](const auto& a, const auto& b) { return a[2] > b[2]; });
    vector<array<long long, 3>> kept;
    for (auto& c : raw) {
        bool inside = false;
        for (auto& k : kept) {
            long long dx = c[0] - k[0], dy = c[1] - k[1], dr = k[2] - c[2];
            if (dr >= 0 && dr * dr >= dx * dx + dy * dy) {
                inside = true;
                break;
            }
        }
        if (!inside) kept.push_back(c);
    }
    const double TWO_PI = 2 * acos(-1.0);
    double total = 0;
    int m = kept.size();
    vector<pair<double, double>> events;
    for (int i = 0; i < m; i++) {
        double x = kept[i][0], y = kept[i][1], r = kept[i][2];
        events.clear();
        for (int j = 0; j < m; j++) {
            if (i == j) continue;
            long long dx = kept[j][0] - kept[i][0], dy = kept[j][1] - kept[i][1], sr = kept[i][2] + kept[j][2];
            long long d2 = dx * dx + dy * dy;
            if (d2 >= sr * sr) continue;  // disjoint or externally tangent
            double d = sqrt((double)d2), R = kept[j][2];
            double cosA = (r * r + d2 - R * R) / (2 * r * d);
            double alpha = acos(max(-1.0, min(1.0, cosA)));
            double lo = fmod(atan2((double)dy, (double)dx) - alpha + 2 * TWO_PI, TWO_PI), hi = lo + 2 * alpha;
            if (hi > TWO_PI) {
                events.push_back({lo, TWO_PI});
                events.push_back({0.0, hi - TWO_PI});
            } else {
                events.push_back({lo, hi});
            }
        }
        sort(events.begin(), events.end());
        auto arc = [&](double a, double b) {
            total += 0.5 * (r * r * (b - a) + x * r * (sin(b) - sin(a)) - y * r * (cos(b) - cos(a)));
        };
        double cur = 0;
        for (auto [lo, hi] : events) {
            if (lo > cur) arc(cur, lo);
            cur = max(cur, hi);
        }
        if (cur < TWO_PI) arc(cur, TWO_PI);
    }
    printf("%.10f\n", total);
}
