#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<ll> alarm(n);
    for (ll& value : alarm) cin >> value;
    vector<vector<pair<int, ll>>> adj(n);
    for (int i = 1; i < n; ++i) {
        int u, v;
        ll delay;
        cin >> u >> v >> delay;
        --u; --v;
        adj[u].push_back({v, delay});
        adj[v].push_back({u, delay});
    }
    vector<int> parent(n, -1), order{0};
    for (int i = 0; i < n; ++i) {
        int u = order[i];
        for (auto [v, delay] : adj[u]) {
            if (v != parent[u]) {
                parent[v] = u;
                order.push_back(v);
            }
        }
    }
    vector<ll> down = alarm, up(n, -1), answer(n);
    for (int i = n - 1; i >= 0; --i) {
        int u = order[i];
        for (auto [v, delay] : adj[u])
            if (parent[v] == u) down[u] = max(down[u], down[v] + delay);
    }
    for (int u : order) {
        answer[u] = max(down[u], up[u]);
        ll best = -1, second = -1;
        int best_child = -1;
        for (auto [v, delay] : adj[u]) {
            if (parent[v] != u) continue;
            ll candidate = down[v] + delay;
            if (candidate > best) {
                second = best;
                best = candidate;
                best_child = v;
            } else if (candidate > second) {
                second = candidate;
            }
        }
        for (auto [v, delay] : adj[u]) {
            if (parent[v] == u) {
                ll other = v == best_child ? second : best;
                up[v] = delay + max({alarm[u], up[u], other});
            }
        }
    }
    for (int u = 0; u < n; ++u)
        cout << answer[u] << (u + 1 == n ? '\n' : ' ');
}
