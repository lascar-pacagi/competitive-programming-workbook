#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, qn;
    if (!(cin >> n >> m >> qn)) return 0;
    vector<long long> duration(n);
    for (long long &x : duration) cin >> x;
    vector<vector<int>> adj(n);
    vector<int> indeg(n, 0);
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        adj[a - 1].push_back(b - 1);
        indeg[b - 1]++;
    }
    vector<int> queries(qn);
    for (int &x : queries) {
        cin >> x;
        --x;
    }
    vector<long long> start(n, 0), finish = duration;
    queue<int> q;
    for (int i = 0; i < n; i++) if (indeg[i] == 0) q.push(i);
    int processed = 0;
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        processed++;
        finish[u] = start[u] + duration[u];
        for (int v : adj[u]) {
            start[v] = max(start[v], finish[u]);
            indeg[v]--;
            if (indeg[v] == 0) q.push(v);
        }
    }
    if (processed != n) {
        cout << "IMPOSSIBLE\n";
    } else {
        for (int i = 0; i < qn; i++) {
            if (i) cout << ' ';
            cout << finish[queries[i]];
        }
        cout << '\n';
    }
    return 0;
}

