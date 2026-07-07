#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    const long long MOD = 1000000007LL;
    int n, b;
    if (!(cin >> n >> b)) return 0;
    vector<char> broken(n + 1, false);
    for (int i = 0; i < b; i++) {
        int x;
        cin >> x;
        broken[x] = true;
    }
    vector<long long> dp(n + 1, 0);
    dp[0] = 1;
    for (int i = 1; i <= n; i++) {
        if (broken[i]) continue;
        dp[i] = dp[i - 1];
        if (i >= 2) dp[i] = (dp[i] + dp[i - 2]) % MOD;
    }
    cout << dp[n] % MOD << '\n';
    return 0;
}

