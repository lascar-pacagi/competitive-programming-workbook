#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<vector<int>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        --u;
        --v;
        adj[u].push_back(v);
    }

    vector<char> color(n, 0);
    for (int start = 0; start < n; start++) {
        if (color[start] != 0) continue;
        color[start] = 1;
        vector<pair<int, int>> st = {{start, 0}};
        while (!st.empty()) {
            int u = st.back().first;
            int i = st.back().second;
            if (i == (int)adj[u].size()) {
                color[u] = 2;
                st.pop_back();
                continue;
            }
            int v = adj[u][i];
            st.back().second++;
            if (color[v] == 0) {
                color[v] = 1;
                st.push_back({v, 0});
            } else if (color[v] == 1) {
                cout << "CYCLIC\n";
                return 0;
            }
        }
    }
    cout << "ACYCLIC\n";
    return 0;
}

