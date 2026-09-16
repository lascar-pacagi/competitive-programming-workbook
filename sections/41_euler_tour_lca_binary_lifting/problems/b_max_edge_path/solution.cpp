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
    vector<vector<int>> mx(LOG, vector<int>(n + 1));
    vector<int> depth(n + 1);

    for (int v = 2; v <= n; v++) {
        int p, w;
        cin >> p >> w;
        up[0][v] = p;
        mx[0][v] = w;
        depth[v] = depth[p] + 1;
    }
    for (int k = 1; k < LOG; k++)
        for (int v = 1; v <= n; v++) {
            int mid = up[k - 1][v];
            up[k][v] = up[k - 1][mid];
            mx[k][v] = max(mx[k - 1][v], mx[k - 1][mid]);
        }

    // Raises v by d edges and returns the heaviest edge crossed.
    auto lift = [&](int &v, int d) {
        int best = 0;
        for (int k = 0; k < LOG; k++)
            if (d & (1 << k)) {
                best = max(best, mx[k][v]);
                v = up[k][v];
            }
        return best;
    };

    while (q--) {
        int a, b;
        cin >> a >> b;
        if (depth[a] < depth[b]) swap(a, b);
        int ans = lift(a, depth[a] - depth[b]);
        if (a != b) {
            for (int k = LOG - 1; k >= 0; k--)
                if (up[k][a] != up[k][b]) {
                    ans = max({ans, mx[k][a], mx[k][b]});
                    a = up[k][a];
                    b = up[k][b];
                }
            ans = max({ans, mx[0][a], mx[0][b]});
        }
        cout << ans << '\n';
    }
}
