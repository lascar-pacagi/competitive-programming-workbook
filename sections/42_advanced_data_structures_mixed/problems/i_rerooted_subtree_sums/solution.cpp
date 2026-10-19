#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    if (!(cin >> n >> q))
        return 0;
    vector<long long> values(n), bit(n + 1);
    long long total = 0;
    for (auto &x : values) {
        cin >> x;
        total += x;
    }
    vector<vector<int>> graph(n);
    for (int i = 1; i < n; i++) {
        int u, v;
        cin >> u >> v;
        --u;
        --v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    vector<int> parent(n), depth(n), tin(n), tout(n);
    int timer = 0;
    vector<tuple<int, int, bool>> stack{{0, 0, false}};
    while (!stack.empty()) {
        auto [u, p, leaving] = stack.back();
        stack.pop_back();
        if (leaving) {
            tout[u] = timer;
            continue;
        }
        parent[u] = p;
        tin[u] = timer++;
        stack.emplace_back(u, p, true);
        for (int v : graph[u]) {
            if (v == p)
                continue;
            depth[v] = depth[u] + 1;
            stack.emplace_back(v, u, false);
        }
    }
    int log = 1;
    while ((1LL << log) <= n)
        log++;
    vector<vector<int>> up(log, parent);
    for (int k = 1; k < log; k++)
        for (int u = 0; u < n; u++)
            up[k][u] = up[k - 1][up[k - 1][u]];
    auto add = [&](int i, long long x) {
        for (i++; i <= n; i += i & -i)
            bit[i] += x;
    };
    auto prefix = [&](int i) {
        long long sum = 0;
        for (; i > 0; i -= i & -i)
            sum += bit[i];
        return sum;
    };
    for (int u = 0; u < n; u++)
        add(tin[u], values[u]);
    int root = 0;
    while (q--) {
        char op;
        int u;
        cin >> op >> u;
        --u;
        if (op == 'R')
            root = u;
        else if (op == 'U') {
            long long x;
            cin >> x;
            long long delta = x - values[u];
            values[u] = x;
            total += delta;
            add(tin[u], delta);
        } else if (u == root)
            cout << total << '\n';
        else if (!(tin[u] <= tin[root] && tin[root] < tout[u]))
            cout << prefix(tout[u]) - prefix(tin[u]) << '\n';
        else {
            int child = root, distance = depth[root] - depth[u] - 1;
            for (int k = 0; k < log; k++)
                if ((distance >> k) & 1)
                    child = up[k][child];
            cout << total - prefix(tout[child]) + prefix(tin[child])
                 << '\n';
        }
    }
}
