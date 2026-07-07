#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        int n, m;
        cin >> n >> m;
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
        vector<int> sizes;
        for (int start = 0; start < n; start++) {
            if (seen[start]) continue;
            seen[start] = true;
            queue<int> q;
            q.push(start);
            int size = 0;
            while (!q.empty()) {
                int u = q.front();
                q.pop();
                size++;
                for (int v : adj[u]) {
                    if (!seen[v]) {
                        seen[v] = true;
                        q.push(v);
                    }
                }
            }
            sizes.push_back(size);
        }

        sort(sizes.begin(), sizes.end());
        cout << sizes.size() << '\n';
        for (int i = 0; i < (int)sizes.size(); i++) {
            if (i) cout << ' ';
            cout << sizes[i];
        }
        cout << '\n';
    }
    return 0;
}

