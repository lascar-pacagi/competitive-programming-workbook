#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;
    vector<long long> h(n);
    for (long long &x : h) cin >> x;
    const long long INF = (1LL << 62);
    vector<long long> dp(n, INF);
    dp[0] = 0;
    for (int i = 1; i < n; i++) {
        for (int j = max(0, i - k); j < i; j++) {
            dp[i] = min(dp[i], dp[j] + llabs(h[j] - h[i]));
        }
    }
    cout << dp[n - 1] << '\n';
    return 0;
}

