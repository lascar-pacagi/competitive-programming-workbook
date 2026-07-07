#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    const long long MOD = 1000000007LL;
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
    vector<long long> white(n, 1), black(n, 1);
    for (int idx = n - 1; idx >= 0; idx--) {
        int u = order[idx];
        for (int v : adj[u]) if (parent[v] == u) {
            white[u] = white[u] * ((white[v] + black[v]) % MOD) % MOD;
            black[u] = black[u] * white[v] % MOD;
        }
    }
    cout << (white[0] + black[0]) % MOD << '\n';
    return 0;
}

