#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<vector<int>> adj(n);
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        --u; --v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    vector<int> parent(n, -1), order;
    parent[0] = 0;
    order.push_back(0);
    for (int i = 0; i < (int)order.size(); i++) {
        int u = order[i];
        for (int v : adj[u]) if (parent[v] == -1) {
            parent[v] = u;
            order.push_back(v);
        }
    }
    vector<int> free(n, 0), used(n, 0);
    for (int idx = n - 1; idx >= 0; idx--) {
        int u = order[idx];
        int base = 0;
        vector<int> children;
        for (int v : adj[u]) if (parent[v] == u) {
            children.push_back(v);
            base += max(free[v], used[v]);
        }
        free[u] = base;
        int best = base;
        for (int v : children) {
            best = max(best, base - max(free[v], used[v]) + free[v] + 1);
        }
        used[u] = best;
    }
    cout << max(free[0], used[0]) << '\n';
    return 0;
}

