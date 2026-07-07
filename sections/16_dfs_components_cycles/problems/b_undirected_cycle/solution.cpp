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
        adj[v].push_back(u);
    }

    vector<char> seen(n, false);
    for (int start = 0; start < n; start++) {
        if (seen[start]) continue;
        seen[start] = true;
        vector<pair<int, int>> st = {{start, -1}};
        while (!st.empty()) {
            auto [u, parent] = st.back();
            st.pop_back();
            for (int v : adj[u]) {
                if (v == parent) continue;
                if (seen[v]) {
                    cout << "CYCLIC\n";
                    return 0;
                }
                seen[v] = true;
                st.push_back({v, u});
            }
        }
    }
    cout << "ACYCLIC\n";
    return 0;
}

