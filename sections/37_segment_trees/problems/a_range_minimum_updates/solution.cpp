#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    if (!(cin >> n >> q)) return 0;
    int size = 1;
    while (size < n) size <<= 1;
    const long long INF = (1LL << 60);
    vector<long long> seg(2 * size, INF);
    for (int i = 0; i < n; i++) cin >> seg[size + i];
    for (int i = size - 1; i >= 1; i--) seg[i] = min(seg[2 * i], seg[2 * i + 1]);
    while (q--) {
        int typ, x, y;
        cin >> typ >> x >> y;
        if (typ == 1) {
            int p = size + x - 1;
            seg[p] = y;
            for (p >>= 1; p; p >>= 1) seg[p] = min(seg[2 * p], seg[2 * p + 1]);
        } else {
            int l = size + x - 1, r = size + y;
            long long ans = INF;
            while (l < r) {
                if (l & 1) ans = min(ans, seg[l++]);
                if (r & 1) ans = min(ans, seg[--r]);
                l >>= 1;
                r >>= 1;
            }
            cout << ans << '\n';
        }
    }
    return 0;
}
