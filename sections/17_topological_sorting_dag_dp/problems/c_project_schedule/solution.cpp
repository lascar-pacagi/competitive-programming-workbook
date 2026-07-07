#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<long long> duration(n);
    for (long long &x : duration) cin >> x;
    vector<vector<int>> adj(n);
    vector<int> indeg(n, 0);
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        --a;
        --b;
        adj[a].push_back(b);
        indeg[b]++;
    }

    vector<long long> earliest_start(n, 0), finish = duration;
    queue<int> q;
    for (int i = 0; i < n; i++) {
        if (indeg[i] == 0) q.push(i);
    }

    int processed = 0;
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        processed++;
        finish[u] = earliest_start[u] + duration[u];
        for (int v : adj[u]) {
            earliest_start[v] = max(earliest_start[v], finish[u]);
            indeg[v]--;
            if (indeg[v] == 0) q.push(v);
        }
    }

    if (processed != n) {
        cout << "IMPOSSIBLE\n";
    } else {
        for (int i = 0; i < n; i++) {
            if (i) cout << ' ';
            cout << finish[i];
        }
        cout << '\n';
    }
    return 0;
}

