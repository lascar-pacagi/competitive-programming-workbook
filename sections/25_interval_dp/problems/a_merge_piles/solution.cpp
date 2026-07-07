#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n), pref(n + 1, 0);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        pref[i + 1] = pref[i] + a[i];
    }
    auto total = [&](int l, int r) {
        return pref[r + 1] - pref[l];
    };
    const long long INF = (1LL << 62);
    vector<vector<long long>> dp(n, vector<long long>(n, 0));
    for (int len = 2; len <= n; len++) {
        for (int l = 0; l + len <= n; l++) {
            int r = l + len - 1;
            long long best = INF;
            long long add = total(l, r);
            for (int k = l; k < r; k++) {
                best = min(best, dp[l][k] + dp[k + 1][r] + add);
            }
            dp[l][r] = best;
        }
    }
    cout << dp[0][n - 1] << '\n';
    return 0;
}

