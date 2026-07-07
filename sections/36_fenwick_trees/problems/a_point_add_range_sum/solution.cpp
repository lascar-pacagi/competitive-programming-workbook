#include <bits/stdc++.h>
using namespace std;

struct Fenwick {
    int n;
    vector<long long> bit;
    Fenwick(int n) : n(n), bit(n + 1, 0) {}
    void add(int i, long long delta) {
        for (; i <= n; i += i & -i) bit[i] += delta;
    }
    long long sum(int i) const {
        long long res = 0;
        for (; i > 0; i -= i & -i) res += bit[i];
        return res;
    }
    long long range_sum(int l, int r) const {
        return sum(r) - sum(l - 1);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    if (!(cin >> n >> q)) return 0;
    Fenwick bit(n);
    for (int i = 1; i <= n; i++) {
        long long x;
        cin >> x;
        bit.add(i, x);
    }
    while (q--) {
        int typ;
        cin >> typ;
        if (typ == 1) {
            int i;
            long long x;
            cin >> i >> x;
            bit.add(i, x);
        } else {
            int l, r;
            cin >> l >> r;
            cout << bit.range_sum(l, r) << '\n';
        }
    }
    return 0;
}
