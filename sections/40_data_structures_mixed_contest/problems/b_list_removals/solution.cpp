#include <bits/stdc++.h>
using namespace std;

struct Fenwick {
    int n;
    vector<int> bit;
    Fenwick(int n) : n(n), bit(n + 1, 0) {}
    void add(int i, int delta) {
        for (; i <= n; i += i & -i) bit[i] += delta;
    }
    int kth(int k) const {
        int pos = 0;
        int step = 1;
        while ((step << 1) <= n) step <<= 1;
        for (; step; step >>= 1) {
            int nxt = pos + step;
            if (nxt <= n && bit[nxt] < k) {
                pos = nxt;
                k -= bit[nxt];
            }
        }
        return pos + 1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n + 1);
    for (int i = 1; i <= n; i++) cin >> a[i];
    Fenwick bit(n);
    for (int i = 1; i <= n; i++) bit.add(i, 1);
    for (int t = 0; t < n; t++) {
        int k;
        cin >> k;
        int idx = bit.kth(k);
        if (t) cout << ' ';
        cout << a[idx];
        bit.add(idx, -1);
    }
    cout << '\n';
    return 0;
}
