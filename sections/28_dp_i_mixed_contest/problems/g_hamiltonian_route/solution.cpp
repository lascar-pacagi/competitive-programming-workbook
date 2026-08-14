#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<vector<ll>> weight(n, vector<ll>(n));
    for (auto& row : weight)
        for (ll& value : row)
            cin >> value;

    const ll INF = 1LL << 62;
    const int mask_count = 1 << n;
    vector<vector<ll>> dp(mask_count, vector<ll>(n, INF));
    dp[1][0] = 0;

    for (int mask = 1; mask < mask_count; ++mask) {
        for (int u = 0; u < n; ++u) {
            if (dp[mask][u] == INF)
                continue;

            for (int v = 0; v < n; ++v) {
                if ((mask >> v & 1) || weight[u][v] < 0)
                    continue;

                int next_mask = mask | (1 << v);
                dp[next_mask][v] = min(
                    dp[next_mask][v],
                    dp[mask][u] + weight[u][v]
                );
            }
        }
    }

    ll answer = dp[mask_count - 1][n - 1];
    cout << (answer == INF ? -1 : answer) << '\n';
}
