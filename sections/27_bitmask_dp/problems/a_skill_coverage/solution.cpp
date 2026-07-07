#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<pair<long long, int>> offers;
    for (int i = 0; i < m; i++) {
        long long cost;
        int k;
        cin >> cost >> k;
        int mask = 0;
        for (int j = 0; j < k; j++) {
            int skill;
            cin >> skill;
            mask |= 1 << (skill - 1);
        }
        offers.push_back({cost, mask});
    }

    int total = 1 << n;
    int full = total - 1;
    const long long INF = (1LL << 62);
    vector<long long> dp(total, INF);
    dp[0] = 0;

    for (auto [cost, offer] : offers) {
        vector<long long> next_dp = dp;
        for (int mask = 0; mask < total; mask++) {
            if (dp[mask] == INF) continue;
            int merged = mask | offer;
            next_dp[merged] = min(next_dp[merged], dp[mask] + cost);
        }
        dp.swap(next_dp);
    }

    cout << (dp[full] == INF ? -1 : dp[full]) << '\n';
    return 0;
}
