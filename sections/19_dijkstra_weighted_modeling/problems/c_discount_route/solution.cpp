#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<vector<pair<int,long long>>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v; long long w;
        cin >> u >> v >> w;
        adj[u - 1].push_back({v - 1, w});
    }
    const long long INF = (1LL << 62);
    vector<array<long long,2>> dist(n, {INF, INF});
    using State = tuple<long long,int,int>;
    priority_queue<State, vector<State>, greater<State>> pq;
    dist[0][0] = 0;
    pq.push({0, 0, 0});
    while (!pq.empty()) {
        auto [d, u, used] = pq.top(); pq.pop();
        if (d != dist[u][used]) continue;
        for (auto [v, w] : adj[u]) {
            long long nd = d + w;
            if (nd < dist[v][used]) {
                dist[v][used] = nd;
                pq.push({nd, v, used});
            }
            if (!used) {
                nd = d + w / 2;
                if (nd < dist[v][1]) {
                    dist[v][1] = nd;
                    pq.push({nd, v, 1});
                }
            }
        }
    }
    long long ans = min(dist[n - 1][0], dist[n - 1][1]);
    cout << (ans == INF ? -1 : ans) << '\n';
    return 0;
}

