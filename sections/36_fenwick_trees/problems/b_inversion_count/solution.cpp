#include <bits/stdc++.h>
using namespace std;

struct Fenwick {
    int n;
    vector<int> bit;
    Fenwick(int n) : n(n), bit(n + 1, 0) {}
    void add(int i, int delta) {
        for (; i <= n; i += i & -i) bit[i] += delta;
    }
    int sum(int i) const {
        int res = 0;
        for (; i > 0; i -= i & -i) res += bit[i];
        return res;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n), vals;
    for (long long &x : a) {
        cin >> x;
        vals.push_back(x);
    }
    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());
    Fenwick bit((int)vals.size());
    long long inv = 0;
    for (int i = 0; i < n; i++) {
        auto position = lower_bound(vals.begin(), vals.end(), a[i]);
        int rank = int(position - vals.begin()) + 1;
        inv += i - bit.sum(rank);
        bit.add(rank, 1);
    }
    cout << inv << '\n';
    return 0;
}
