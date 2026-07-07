#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<long long> h(n);
    for (long long &x : h) cin >> x;
    vector<vector<int>> adj(n);
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        --u; --v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    vector<int> parent(n, -1), order;
    order.push_back(0);
    parent[0] = 0;
    for (int i = 0; i < (int)order.size(); i++) {
        int u = order[i];
        for (int v : adj[u]) if (parent[v] == -1) {
            parent[v] = u;
            order.push_back(v);
        }
    }
    vector<long long> take = h, skip(n, 0);
    for (int idx = n - 1; idx >= 0; idx--) {
        int u = order[idx];
        for (int v : adj[u]) if (parent[v] == u) {
            take[u] += skip[v];
            skip[u] += max(take[v], skip[v]);
        }
    }
    cout << max(take[0], skip[0]) << '\n';
    return 0;
}

