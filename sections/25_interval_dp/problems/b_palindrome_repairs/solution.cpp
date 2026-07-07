#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;
    int n = (int)s.size();
    vector<vector<int>> dp(n, vector<int>(n, 0));
    for (int len = 2; len <= n; len++) {
        for (int l = 0; l + len <= n; l++) {
            int r = l + len - 1;
            if (s[l] == s[r]) {
                dp[l][r] = (l + 1 <= r - 1 ? dp[l + 1][r - 1] : 0);
            } else {
                dp[l][r] = 1 + min(dp[l + 1][r], dp[l][r - 1]);
            }
        }
    }
    cout << dp[0][n - 1] << '\n';
    return 0;
}

