#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    struct Edge { int to, color; ll cost; };
    vector<vector<Edge>> graph(n);
    while (m--) {
        int u, v;
        ll cost;
        char color;
        cin >> u >> v >> cost >> color;
        graph[u - 1].push_back({v - 1, color == 'R' ? 0 : 1, cost});
    }
    const ll INF = (1LL << 62);
    vector<array<ll, 2>> dist(n, {INF, INF});
    using State = tuple<ll, int, int>;
    priority_queue<State, vector<State>, greater<State>> heap;
    for (int color = 0; color < 2; ++color) {
        for (auto edge : graph[0]) if (edge.color == color) {
            if (edge.cost < dist[edge.to][color]) {
                dist[edge.to][color] = edge.cost;
                heap.push({edge.cost, edge.to, color});
            }
        }
    }
    if (n == 1) {
        cout << 0 << '\n';
        return 0;
    }
    while (!heap.empty()) {
        auto [cost, u, last] = heap.top();
        heap.pop();
        if (cost != dist[u][last]) continue;
        for (auto edge : graph[u]) if (edge.color != last) {
            ll next = cost + edge.cost;
            if (next < dist[edge.to][edge.color]) {
                dist[edge.to][edge.color] = next;
                heap.push({next, edge.to, edge.color});
            }
        }
    }
    ll answer = min(dist[n - 1][0], dist[n - 1][1]);
    cout << (answer == INF ? -1 : answer) << '\n';
}
