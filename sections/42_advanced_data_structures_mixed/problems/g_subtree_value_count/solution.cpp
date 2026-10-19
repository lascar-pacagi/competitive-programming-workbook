#include <bits/stdc++.h>
using namespace std;
using ll = long long;
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
    vector<int> vertices(n);
    iota(vertices.begin(), vertices.end(), 0);
    sort(vertices.begin(), vertices.end(), [&](int u, int v) {
        return original[u] < original[v];
    });
    vector<tuple<ll, int, int, int>> events;
    vector<int> ans(q), bit(n + 1);
    for (int i = 0; i < q; ++i) {
        int u;
        ll lo, hi;
        cin >> u >> lo >> hi;
        --u;
        events.emplace_back(hi, u, i, 1);
        events.emplace_back(lo - 1, u, i, -1);
    }
    sort(events.begin(), events.end());
    auto prefix = [&](int i) {
        int total = 0;
        for (; i; i -= i & -i)
            total += bit[i];
        return total;
    };
    int current = 0;
    for (auto [bound, u, id, sign] : events) {
        while (current < n && original[vertices[current]] <= bound) {
            for (int j = tin[vertices[current]] + 1; j <= n;
                 j += j & -j)
                ++bit[j];
            ++current;
        }
        ans[id] += sign * (prefix(tout[u]) - prefix(tin[u]));
    }
    for (int x : ans)
        cout << x << '\n';
}
