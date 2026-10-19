#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m, q;
    if (!(cin >> n >> m >> q))
        return 0;
    vector<tuple<int, int, int>> edges;
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        edges.emplace_back(w, u - 1, v - 1);
    }
    vector<int> dsu(n), size(n, 1);
    iota(dsu.begin(), dsu.end(), 0);
    auto find = [&](int u) {
        while (dsu[u] != u) {
            dsu[u] = dsu[dsu[u]];
            u = dsu[u];
        }
        return u;
    };
    vector<vector<pair<int, int>>> graph(n);
    sort(edges.begin(), edges.end());
    for (auto [w, u, v] : edges) {
        int a = find(u), b = find(v);
        if (a == b)
            continue;
        if (size[a] < size[b])
            swap(a, b);
        dsu[b] = a;
        size[a] += size[b];
        graph[u].emplace_back(v, w);
        graph[v].emplace_back(u, w);
    }
    vector<int> parent(n), depth(n, -1), weight(n);
    iota(parent.begin(), parent.end(), 0);
    for (int root = 0; root < n; root++) {
        if (depth[root] != -1)
            continue;
        depth[root] = 0;
        vector<int> stack{root};
        while (!stack.empty()) {
            int u = stack.back();
            stack.pop_back();
            for (auto [v, w] : graph[u]) {
                if (depth[v] != -1)
                    continue;
                depth[v] = depth[u] + 1;
                parent[v] = u;
                weight[v] = w;
                stack.push_back(v);
            }
        }
    }
    int log = 1;
    while ((1LL << log) <= n)
        log++;
    vector<vector<int>> up(log, parent), high(log, weight);
    for (int k = 1; k < log; k++) {
        for (int u = 0; u < n; u++) {
            int middle = up[k - 1][u];
            up[k][u] = up[k - 1][middle];
            high[k][u] = max(high[k - 1][u], high[k - 1][middle]);
        }
    }
    while (q--) {
        int u, v;
        cin >> u >> v;
        --u;
        --v;
        if (find(u) != find(v)) {
            cout << -1 << '\n';
            continue;
        }
        int answer = 0;
        if (depth[u] < depth[v])
            swap(u, v);
        int difference = depth[u] - depth[v];
        for (int k = 0; k < log; k++) {
            if ((difference >> k) & 1) {
                answer = max(answer, high[k][u]);
                u = up[k][u];
            }
        }
        if (u != v) {
            for (int k = log - 1; k >= 0; k--) {
                if (up[k][u] != up[k][v]) {
                    answer = max({answer, high[k][u], high[k][v]});
                    u = up[k][u];
                    v = up[k][v];
                }
            }
            answer = max({answer, high[0][u], high[0][v]});
        }
        cout << answer << '\n';
    }
}
