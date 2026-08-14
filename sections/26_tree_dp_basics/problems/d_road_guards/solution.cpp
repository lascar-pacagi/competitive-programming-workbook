#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<long long> cost(n);
    for (long long &value : cost) cin >> value;

    vector<vector<int>> graph(n);
    for (int i = 0; i + 1 < n; ++i) {
        int u, v;
        cin >> u >> v;
        --u;
        --v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    vector<int> parent(n, -1), order = {0};
    parent[0] = 0;
    for (int index = 0; index < static_cast<int>(order.size()); ++index) {
        int u = order[index];
        for (int v : graph[u]) {
            if (parent[v] == -1) {
                parent[v] = u;
                order.push_back(v);
            }
        }
    }

    vector<long long> active = cost;
    vector<long long> inactive(n, 0);
    for (int index = n - 1; index >= 0; --index) {
        int u = order[index];
        for (int v : graph[u]) {
            if (parent[v] == u) {
                active[u] += min(active[v], inactive[v]);
                inactive[u] += active[v];
            }
        }
    }

    cout << min(active[0], inactive[0]) << '\n';
    return 0;
}
