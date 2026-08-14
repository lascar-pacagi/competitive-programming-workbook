#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int target, k;
    if (!(cin >> target >> k)) return 0;
    vector<int> coins(k);
    for (int &coin : coins) cin >> coin;

    const int INF = target + 1;
    vector<int> dp(target + 1, INF);
    dp[0] = 0;
    for (int amount = 1; amount <= target; ++amount) {
        for (int coin : coins) {
            if (coin <= amount && dp[amount - coin] != INF) {
                dp[amount] = min(dp[amount], dp[amount - coin] + 1);
            }
        }
    }

    cout << (dp[target] == INF ? -1 : dp[target]) << '\n';
    return 0;
}
