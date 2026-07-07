#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<vector<long long>> profit(n, vector<long long>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) cin >> profit[i][j];
    }

    int total = 1 << n;
    const long long NEG = -(1LL << 60);
    vector<long long> dp(total, NEG);
    dp[0] = 0;

    for (int mask = 0; mask < total; mask++) {
        int worker = __builtin_popcount((unsigned)mask);
        if (worker == n || dp[mask] == NEG) continue;
        for (int job = 0; job < n; job++) {
            if ((mask & (1 << job)) == 0) {
                int nxt = mask | (1 << job);
                dp[nxt] = max(dp[nxt], dp[mask] + profit[worker][job]);
            }
        }
    }

    cout << dp[total - 1] << '\n';
    return 0;
}
