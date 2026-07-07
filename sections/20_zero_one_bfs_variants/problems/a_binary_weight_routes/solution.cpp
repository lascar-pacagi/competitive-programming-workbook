#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s, qn;
    if (!(cin >> n >> m >> s >> qn)) return 0;
    --s;
    vector<vector<pair<int,int>>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u - 1].push_back({v - 1, w});
    }
    vector<int> queries(qn);
    for (int &x : queries) { cin >> x; --x; }
    const int INF = 1e9;
    vector<int> dist(n, INF);
    deque<int> dq;
    dist[s] = 0;
    dq.push_back(s);
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
    for (int i = 0; i < qn; i++) {
        if (i) cout << ' ';
        cout << (dist[queries[i]] == INF ? -1 : dist[queries[i]]);
    }
    cout << '\n';
    return 0;
}

