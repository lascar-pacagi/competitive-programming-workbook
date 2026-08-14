#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m, k;
    cin >> n >> m >> k;
    vector<vector<int>> graph(n);
    while (m--) {
        int u, v;
        cin >> u >> v;
        --u; --v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    vector<int> distance(n, -1);
    queue<int> queue;
    while (k--) {
        int station;
        cin >> station;
        --station;
        if (distance[station] == -1) {
            distance[station] = 0;
            queue.push(station);
        }
    }
    while (!queue.empty()) {
        int u = queue.front();
        queue.pop();
        for (int v : graph[u]) if (distance[v] == -1) {
            distance[v] = distance[u] + 1;
            queue.push(v);
        }
    }
    int unreachable = 0, vertex = -1, farthest = -1;
    for (int i = 0; i < n; ++i) {
        if (distance[i] == -1) {
            ++unreachable;
        } else if (distance[i] > farthest) {
            farthest = distance[i];
            vertex = i;
        }
    }
    cout << unreachable << ' ' << vertex + 1 << ' ' << farthest << '\n';
}
