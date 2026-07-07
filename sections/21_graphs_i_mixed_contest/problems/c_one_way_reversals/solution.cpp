#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<vector<pair<int,int>>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        --u;
        --v;
        adj[u].push_back({v, 0});
        adj[v].push_back({u, 1});
    }
    const int INF = 1e9;
    vector<int> dist(n, INF);
    deque<int> dq;
    dist[0] = 0;
    dq.push_back(0);
    while (!dq.empty()) {
        int u = dq.front();
        dq.pop_front();
        for (auto [v, w] : adj[u]) {
            int nd = dist[u] + w;
            if (nd < dist[v]) {
                dist[v] = nd;
                if (w == 0) dq.push_front(v);
                else dq.push_back(v);
            }
        }
    }
    cout << (dist[n - 1] == INF ? -1 : dist[n - 1]) << '\n';
    return 0;
}

