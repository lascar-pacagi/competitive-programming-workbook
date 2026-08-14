#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n, q; if (!(cin >> n >> q)) return 0;
    int log = 1; while ((1 << log) <= n) ++log;
    vector<vector<int>> up(log, vector<int>(n + 1));
    vector<int> depth(n + 1); vector<long long> root_sum(n + 1);
    for (int v = 2; v <= n; ++v) { long long w; cin >> up[0][v] >> w; depth[v] = depth[up[0][v]] + 1; root_sum[v] = root_sum[up[0][v]] + w; }
    for (int k = 1; k < log; ++k) for (int v = 1; v <= n; ++v) up[k][v] = up[k-1][up[k-1][v]];
    auto lift = [&](int v, int d) { for (int k = 0; k < log; ++k) if (d & (1 << k)) v = up[k][v]; return v; };
    auto lca = [&](int a, int b) { if (depth[a] < depth[b]) swap(a, b); a = lift(a, depth[a] - depth[b]); if (a == b) return a; for (int k = log - 1; k >= 0; --k) if (up[k][a] != up[k][b]) { a = up[k][a]; b = up[k][b]; } return up[0][a]; };
    while (q--) { int u, v; cin >> u >> v; int c = lca(u, v); cout << root_sum[u] + root_sum[v] - 2 * root_sum[c] << '\n'; }
}
