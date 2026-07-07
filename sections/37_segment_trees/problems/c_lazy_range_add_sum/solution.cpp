#include <bits/stdc++.h>
using namespace std;

struct SegTree {
    int n;
    vector<long long> seg, lazy;
    SegTree(const vector<long long>& a) {
        n = 1;
        while (n < (int)a.size()) n <<= 1;
        seg.assign(2 * n, 0);
        lazy.assign(2 * n, 0);
        for (int i = 0; i < (int)a.size(); i++) seg[n + i] = a[i];
        for (int i = n - 1; i >= 1; i--) seg[i] = seg[2 * i] + seg[2 * i + 1];
    }
    void apply(int v, int len, long long x) {
        seg[v] += x * len;
        lazy[v] += x;
    }
    void push(int v, int len) {
        if (lazy[v] && v < n) {
            int half = len / 2;
            apply(2 * v, half, lazy[v]);
            apply(2 * v + 1, half, lazy[v]);
            lazy[v] = 0;
        }
    }
    void add(int v, int tl, int tr, int l, int r, long long x) {
        if (l <= tl && tr <= r) {
            apply(v, tr - tl + 1, x);
            return;
        }
        push(v, tr - tl + 1);
        int tm = (tl + tr) / 2;
        if (l <= tm) add(2 * v, tl, tm, l, r, x);
        if (tm < r) add(2 * v + 1, tm + 1, tr, l, r, x);
        seg[v] = seg[2 * v] + seg[2 * v + 1];
    }
    long long query(int v, int tl, int tr, int l, int r) {
        if (l <= tl && tr <= r) return seg[v];
        push(v, tr - tl + 1);
        int tm = (tl + tr) / 2;
        long long ans = 0;
        if (l <= tm) ans += query(2 * v, tl, tm, l, r);
        if (tm < r) ans += query(2 * v + 1, tm + 1, tr, l, r);
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    if (!(cin >> n >> q)) return 0;
    vector<long long> a(n);
    for (long long &x : a) cin >> x;
    SegTree st(a);
    while (q--) {
        int typ, l, r;
        cin >> typ >> l >> r;
        if (typ == 1) {
            long long x;
            cin >> x;
            st.add(1, 1, st.n, l, r, x);
        } else {
            cout << st.query(1, 1, st.n, l, r) << '\n';
        }
    }
    return 0;
}
