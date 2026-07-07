#include <bits/stdc++.h>
using namespace std;

struct Fenwick {
    int n;
    vector<long long> bit;
    Fenwick(int n) : n(n), bit(n + 2, 0) {}
    void add(int i, long long delta) {
        for (; i <= n; i += i & -i) bit[i] += delta;
    }
    long long sum(int i) const {
        long long res = 0;
        for (; i > 0; i -= i & -i) res += bit[i];
        return res;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    if (!(cin >> n >> q)) return 0;
    Fenwick bit(n + 1);
    long long prev = 0;
    for (int i = 1; i <= n; i++) {
        long long x;
        cin >> x;
        bit.add(i, x - prev);
        prev = x;
    }
    while (q--) {
        int typ;
        cin >> typ;
        if (typ == 1) {
            int l, r;
            long long x;
            cin >> l >> r >> x;
            bit.add(l, x);
            bit.add(r + 1, -x);
        } else {
            int i;
            cin >> i;
            cout << bit.sum(i) << '\n';
        }
    }
    return 0;
}
