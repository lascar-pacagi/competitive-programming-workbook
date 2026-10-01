#include <bits/stdc++.h>
using namespace std;

// Let f(p) = cross(b - a, p - a) (positive = left of the line).  On a convex
// polygon f rises from its minimum vertex to its maximum vertex and falls
// back; both extremes are found by a binary search over edge directions,
// which are sorted by angle.  Two more binary searches find the edges where
// f changes sign.  The left piece is the vertex range between them plus the
// two crossing points, whose area follows from prefix shoelace sums.  The
// crossing points are exact rationals, so 128-bit integers give the area of
// even tiny pieces without cancellation error.

typedef long long ll;
typedef __int128 i128;

int n;
vector<ll> xs, ys, ex, ey;
vector<int> eh;

int half(ll x, ll y) { return (y > 0 || (y == 0 && x > 0)) ? 0 : 1; }

int firstEdgeNotBefore(ll tx, ll ty) {
    int th = half(tx, ty), lo = 0, hi = n;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        bool before = eh[mid] < th || (eh[mid] == th && ex[mid] * ty - ey[mid] * tx > 0);
        if (before) lo = mid + 1;
        else hi = mid;
    }
    return lo % n;
}

int main() {
    int q;
    scanf("%d %d", &n, &q);
    xs.resize(n);
    ys.resize(n);
    for (int i = 0; i < n; i++) scanf("%lld %lld", &xs[i], &ys[i]);
    i128 area = 0;
    for (int i = 0; i < n; i++) area += (i128)xs[i] * ys[(i + 1) % n] - (i128)xs[(i + 1) % n] * ys[i];
    if (area < 0) reverse(xs.begin(), xs.end()), reverse(ys.begin(), ys.end());
    ex.resize(n);
    ey.resize(n);
    for (int i = 0; i < n; i++) ex[i] = xs[(i + 1) % n] - xs[i], ey[i] = ys[(i + 1) % n] - ys[i];
    int best = 0;
    for (int i = 1; i < n; i++) {
        int hi_ = half(ex[i], ey[i]), hb = half(ex[best], ey[best]);
        if (hi_ < hb || (hi_ == hb && ex[best] * ey[i] - ey[best] * ex[i] < 0)) best = i;
    }
    rotate(xs.begin(), xs.begin() + best, xs.end());
    rotate(ys.begin(), ys.begin() + best, ys.end());
    rotate(ex.begin(), ex.begin() + best, ex.end());
    rotate(ey.begin(), ey.begin() + best, ey.end());
    eh.resize(n);
    for (int i = 0; i < n; i++) eh[i] = half(ex[i], ey[i]);
    vector<ll> prefix(2 * n + 1, 0);
    for (int k = 0; k < 2 * n; k++) {
        int i = k % n, j = (k + 1) % n;
        prefix[k + 1] = prefix[k] + xs[i] * ys[j] - xs[j] * ys[i];
    }
    ll total2 = prefix[n];
    string out;
    char buf[64];
    while (q--) {
        ll ax, ay, bx, by;
        scanf("%lld %lld %lld %lld", &ax, &ay, &bx, &by);
        ll dx = bx - ax, dy = by - ay;
        auto f = [&](int i) { return dx * (ys[i] - ay) - dy * (xs[i] - ax); };
        int imax = firstEdgeNotBefore(-dx, -dy), imin = firstEdgeNotBefore(dx, dy);
        if (f(imax) <= 0) {
            out += "0\n";
            continue;
        }
        if (f(imin) >= 0) {
            snprintf(buf, sizeof buf, "%.10Lf\n", (long double)total2 / 2);
            out += buf;
            continue;
        }
        int lo = 0, hi = ((imax - imin) % n + n) % n;
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (f((imin + mid) % n) <= 0) lo = mid;
            else hi = mid - 1;
        }
        int i = (imin + lo) % n;
        lo = 0, hi = ((imin - imax) % n + n) % n;
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (f((imax + mid) % n) > 0) lo = mid;
            else hi = mid - 1;
        }
        int j = (imax + lo) % n, i1 = (i + 1) % n, j1 = (j + 1) % n;
        i128 fi = f(i), fi1 = f(i1), fj = f(j), fj1 = f(j1);
        i128 d1 = fi1 - fi, d2 = fj - fj1;
        i128 X0 = xs[i] * d1 + (xs[i1] - xs[i]) * (-fi), X1 = ys[i] * d1 + (ys[i1] - ys[i]) * (-fi);
        i128 Y0 = xs[j] * d2 + (xs[j1] - xs[j]) * fj, Y1 = ys[j] * d2 + (ys[j1] - ys[j]) * fj;
        int k0 = i1, k1 = j >= i1 ? j : j + n;
        i128 inner = prefix[k1] - prefix[k0];
        i128 num = (X0 * ys[i1] - X1 * xs[i1]) * d2 + inner * d1 * d2 + (xs[j] * Y1 - ys[j] * Y0) * d1 + (Y0 * X1 - Y1 * X0);
        long double value = (long double)num / ((long double)d1 * (long double)d2 * 2);
        snprintf(buf, sizeof buf, "%.10Lf\n", value);
        out += buf;
    }
    fputs(out.c_str(), stdout);
}
