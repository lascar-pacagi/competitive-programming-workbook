#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<vector<long long>> cost(n, vector<long long>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) cin >> cost[i][j];
    }

    int total = 1 << n;
    int full = total - 1;
    const long long INF = (1LL << 62);
    vector<vector<long long>> dp(total, vector<long long>(n, INF));
    dp[1][0] = 0;

    for (int mask = 0; mask < total; mask++) {
        if ((mask & 1) == 0) continue;
        for (int last = 0; last < n; last++) {
            if (dp[mask][last] == INF) continue;
            for (int nxt = 0; nxt < n; nxt++) {
                if ((mask & (1 << nxt)) == 0) {
                    int new_mask = mask | (1 << nxt);
                    dp[new_mask][nxt] = min(
                        dp[new_mask][nxt],
                        dp[mask][last] + cost[last][nxt]
                    );
                }
            }
        }
    }

    long long answer = INF;
    for (int last = 0; last < n; last++) {
        answer = min(answer, dp[full][last] + cost[last][0]);
    }
    cout << answer << '\n';
    return 0;
}
