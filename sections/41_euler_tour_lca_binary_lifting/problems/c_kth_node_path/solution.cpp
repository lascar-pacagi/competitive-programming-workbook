#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    int LOG = 1;
    while ((1 << LOG) <= n + 1) LOG++;

    vector<vector<int>> up(LOG, vector<int>(n + 1));
    vector<int> depth(n + 1);

    for (int v = 2; v <= n; v++) {
        cin >> up[0][v];
        depth[v] = depth[up[0][v]] + 1;
    }
    for (int k = 1; k < LOG; k++)
        for (int v = 1; v <= n; v++)
            up[k][v] = up[k - 1][up[k - 1][v]];

    auto lift = [&](int v, int d) {
        for (int k = 0; k < LOG; k++)
            if (d & (1 << k)) v = up[k][v];
        return v;
    };

    auto lca = [&](int a, int b) {
        if (depth[a] < depth[b]) swap(a, b);
        a = lift(a, depth[a] - depth[b]);
        if (a == b) return a;
        for (int k = LOG - 1; k >= 0; k--)
            if (up[k][a] != up[k][b]) {
                a = up[k][a];
                b = up[k][b];
            }
        return up[0][a];
    };

    while (q--) {
        int u, v, k;
        cin >> u >> v >> k;
        int c = lca(u, v);
        int left = depth[u] - depth[c] + 1;
        int total = depth[u] + depth[v] - 2 * depth[c] + 1;
        if (k < 1 || k > total)
            cout << -1 << '\n';
        else if (k <= left)
            cout << lift(u, k - 1) << '\n';
        else
            cout << lift(v, total - k) << '\n';
    }
}
