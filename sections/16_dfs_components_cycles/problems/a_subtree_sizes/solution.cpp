#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<vector<int>> adj(n);
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        --u;
        --v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<int> parent(n, -1), order;
    vector<int> st = {0};
    parent[0] = 0;
    while (!st.empty()) {
        int u = st.back();
        st.pop_back();
        order.push_back(u);
        for (int v : adj[u]) {
            if (v == parent[u]) continue;
            parent[v] = u;
            st.push_back(v);
        }
    }

    vector<int> subtree(n, 1);
    for (int i = (int)order.size() - 1; i >= 0; i--) {
        int u = order[i];
        if (u != 0) subtree[parent[u]] += subtree[u];
    }

    for (int i = 0; i < n; i++) {
        if (i) cout << ' ';
        cout << subtree[i];
    }
    cout << '\n';
    return 0;
}

