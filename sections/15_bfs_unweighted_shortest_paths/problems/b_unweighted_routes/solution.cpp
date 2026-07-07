#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s, q_count;
    if (!(cin >> n >> m >> s >> q_count)) return 0;
    --s;
    vector<vector<int>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        --u;
        --v;
        adj[u].push_back(v);
    }
    vector<int> queries(q_count);
    for (int &x : queries) {
        cin >> x;
        --x;
    }

    vector<int> dist(n, -1);
    queue<int> q;
    dist[s] = 0;
    q.push(s);
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v : adj[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }

    for (int i = 0; i < q_count; i++) {
        if (i) cout << ' ';
        cout << dist[queries[i]];
    }
    cout << '\n';
    return 0;
}

