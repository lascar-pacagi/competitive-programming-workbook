#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; cin >> n;
    vector<ll> d(n + 1);
    for (ll& x : d) cin >> x;
    vector<vector<ll>> dp(n, vector<ll>(n));
    for (int length = 2; length <= n; ++length) {
        for (int l = 0; l + length <= n; ++l) {
            int r = l + length - 1;
            dp[l][r] = (1LL << 62);
            for (int k = l; k < r; ++k) {
                dp[l][r] = min(dp[l][r],
                    dp[l][k] + dp[k + 1][r] + d[l] * d[k + 1] * d[r + 1]);
            }
        }
    }
    cout << dp[0][n - 1] << '\n';
}
