#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<vector<pair<int, long long>>> graph(n);
    for (int i = 0; i < m; ++i) {
        int u, v;
        long long w;
        cin >> u >> v >> w;
        graph[u - 1].push_back({v - 1, w});
    }

    const long long INF = (1LL << 62);
    vector<array<long long, 2>> dist(n, {INF, INF});
    using State = tuple<long long, int, int>;
    priority_queue<State, vector<State>, greater<State>> pq;
    dist[0][0] = 0;
    pq.push({0, 0, 0});

    while (!pq.empty()) {
        auto [cost, u, parity] = pq.top();
        pq.pop();
        if (cost != dist[u][parity]) continue;
        for (auto [v, weight] : graph[u]) {
            int next_parity = parity ^ 1;
            long long next_cost = cost + weight;
            if (next_cost < dist[v][next_parity]) {
                dist[v][next_parity] = next_cost;
                pq.push({next_cost, v, next_parity});
            }
        }
    }

    cout << (dist[n - 1][0] == INF ? -1 : dist[n - 1][0]) << '\n';
    return 0;
}
