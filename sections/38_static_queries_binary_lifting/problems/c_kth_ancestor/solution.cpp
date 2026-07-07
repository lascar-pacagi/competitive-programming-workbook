#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    if (!(cin >> n >> q)) return 0;
    int LOG = 1;
    while ((1 << LOG) <= n + 5) LOG++;
    vector<vector<int>> up(LOG, vector<int>(n + 1, 0));
    for (int v = 2; v <= n; v++) cin >> up[0][v];
    for (int k = 1; k < LOG; k++) {
        for (int v = 1; v <= n; v++) up[k][v] = up[k - 1][up[k - 1][v]];
    }
    while (q--) {
        int v;
        long long dist;
        cin >> v >> dist;
        for (int k = 0; k < LOG && v; k++) {
            if (dist & (1LL << k)) v = up[k][v];
        }
        cout << (v ? v : -1) << '\n';
    }
    return 0;
}
