#include <bits/stdc++.h>
using namespace std;

struct Query {
    int l, r, id;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    if (!(cin >> n >> q)) return 0;
    vector<int> a(n), vals;
    for (int &x : a) {
        cin >> x;
        vals.push_back(x);
    }
    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());
    for (int &x : a) x = int(lower_bound(vals.begin(), vals.end(), x) - vals.begin());
    vector<Query> queries(q);
    for (int i = 0; i < q; i++) {
        cin >> queries[i].l >> queries[i].r;
        --queries[i].l; --queries[i].r;
        queries[i].id = i;
    }
    int block = max(1, (int)sqrt(n));
    sort(queries.begin(), queries.end(), [&](const Query& A, const Query& B) {
        int ba = A.l / block, bb = B.l / block;
        if (ba != bb) return ba < bb;
        return (ba & 1) ? A.r > B.r : A.r < B.r;
    });
    vector<int> freq(vals.size(), 0), ans(q);
    int distinct = 0, l = 0, r = -1;
    auto add = [&](int pos) {
        if (freq[a[pos]]++ == 0) distinct++;
    };
    auto remove = [&](int pos) {
        if (--freq[a[pos]] == 0) distinct--;
    };
    for (auto qu : queries) {
        while (r < qu.r) add(++r);
        while (r > qu.r) remove(r--);
        while (l < qu.l) remove(l++);
        while (l > qu.l) add(--l);
        ans[qu.id] = distinct;
    }
    for (int x : ans) cout << x << '\n';
    return 0;
}
