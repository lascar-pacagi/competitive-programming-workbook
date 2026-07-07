#include <bits/stdc++.h>
using namespace std;

const long long NEG = -(1LL << 60);

struct Node {
    long long sum, pref, suff, best;
};

Node leaf(long long x) { return {x, x, x, x}; }
Node merge(Node a, Node b) {
    return {
        a.sum + b.sum,
        max(a.pref, a.sum + b.pref),
        max(b.suff, b.sum + a.suff),
        max({a.best, b.best, a.suff + b.pref})
    };
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    if (!(cin >> n >> q)) return 0;
    int size = 1;
    while (size < n) size <<= 1;
    Node neutral{0, NEG, NEG, NEG};
    vector<Node> seg(2 * size, neutral);
    for (int i = 0; i < n; i++) {
        long long x;
        cin >> x;
        seg[size + i] = leaf(x);
    }
    for (int i = size - 1; i >= 1; i--) seg[i] = merge(seg[2 * i], seg[2 * i + 1]);
    while (q--) {
        int pos;
        long long val;
        cin >> pos >> val;
        int p = size + pos - 1;
        seg[p] = leaf(val);
        for (p >>= 1; p; p >>= 1) seg[p] = merge(seg[2 * p], seg[2 * p + 1]);
        cout << seg[1].best << '\n';
    }
    return 0;
}
