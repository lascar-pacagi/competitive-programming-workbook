#include <bits/stdc++.h>
using namespace std;
using ll = long long;
class SegmentTree {
    int n;
    vector<ll> tree;

    void build(int node, int left, int right, const vector<ll> &a) {
        if (right - left == 1) {
            tree[node] = a[left];
            return;
        }
        int mid = (left + right) / 2;
        build(2 * node, left, mid, a);
        build(2 * node + 1, mid, right, a);
        tree[node] = max(tree[2 * node], tree[2 * node + 1]);
    }

    void assign(int node, int left, int right, int i, ll x) {
        if (right - left == 1) {
            tree[node] = x;
            return;
        }
        int mid = (left + right) / 2;
        if (i < mid)
            assign(2 * node, left, mid, i, x);
        else
            assign(2 * node + 1, mid, right, i, x);
        tree[node] = max(tree[2 * node], tree[2 * node + 1]);
    }

    ll query(int node, int left, int right, int l, int r) const {
        if (r <= left || right <= l)
            return LLONG_MIN;
        if (l <= left && right <= r)
            return tree[node];
        int mid = (left + right) / 2;
        return max(query(2 * node, left, mid, l, r),
                   query(2 * node + 1, mid, right, l, r));
    }

  public:
    explicit SegmentTree(const vector<ll> &a)
        : n(a.size()), tree(4 * a.size()) {
        build(1, 0, n, a);
    }

    void assign(int i, ll x) {
        assign(1, 0, n, i, x);
    }

    ll query(int l, int r) const {
        return query(1, 0, n, l, r);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    if (!(cin >> n >> q))
        return 0;
    vector<ll> original(n);
    for (auto &x : original)
        cin >> x;
    vector<vector<int>> g(n);
    for (int i = 1, u, v; i < n; ++i) {
        cin >> u >> v;
        --u;
        --v;
        g[u].push_back(v);
        g[v].push_back(u);
    }
    vector<int> tin(n), tout(n), order;
    vector<tuple<int, int, bool>> stack{{0, -1, false}};
    while (!stack.empty()) {
        auto [u, p, leaving] = stack.back();
        stack.pop_back();
        if (leaving) {
            tout[u] = order.size();
            continue;
        }
        tin[u] = order.size();
        order.push_back(u);
        stack.emplace_back(u, p, true);
        for (auto it = g[u].rbegin(); it != g[u].rend(); ++it)
            if (*it != p)
                stack.emplace_back(*it, u, false);
    }
    vector<ll> flattened(n);
    for (int i = 0; i < n; ++i)
        flattened[i] = original[order[i]];
    SegmentTree tree(flattened);
    while (q--) {
        char op;
        int u;
        cin >> op >> u;
        --u;
        if (op == 'Q')
            cout << tree.query(tin[u], tout[u]) << '\n';
        else {
            ll x;
            cin >> x;
            tree.assign(tin[u], x);
        }
    }
}
