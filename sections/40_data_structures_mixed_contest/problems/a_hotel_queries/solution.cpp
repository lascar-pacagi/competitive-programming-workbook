#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    if (!(cin >> n >> q)) return 0;
    int size = 1;
    while (size < n) size <<= 1;
    vector<long long> seg(2 * size, 0);
    for (int i = 0; i < n; i++) cin >> seg[size + i];
    for (int i = size - 1; i >= 1; i--)
        seg[i] = max(seg[2 * i], seg[2 * i + 1]);
    for (int qi = 0; qi < q; qi++) {
        long long x;
        cin >> x;
        int ans = 0;
        if (seg[1] >= x) {
            int v = 1;
            while (v < size) {
                if (seg[2 * v] >= x) v *= 2;
                else v = 2 * v + 1;
            }
            ans = v - size + 1;
            seg[v] -= x;
            for (v >>= 1; v; v >>= 1)
                seg[v] = max(seg[2 * v], seg[2 * v + 1]);
        }
        if (qi) cout << ' ';
        cout << ans;
    }
    cout << '\n';
    return 0;
}
