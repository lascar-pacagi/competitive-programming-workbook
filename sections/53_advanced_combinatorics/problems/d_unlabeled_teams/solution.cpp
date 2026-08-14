#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1'000'000'007LL;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;
    vector<long long> dp(k + 1, 0);
    dp[0] = 1;
    for (int people = 1; people <= n; people++) {
        for (int teams = min(people, k); teams >= 1; teams--) {
            dp[teams] = (dp[teams - 1] + teams * dp[teams]) % MOD;
        }
        dp[0] = 0;
    }
    cout << dp[k] << '\n';
    return 0;
}
