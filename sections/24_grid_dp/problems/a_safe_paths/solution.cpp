#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    const long long MOD = 1000000007LL;
    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<string> grid(n);
    for (string &row : grid) cin >> row;
    vector<vector<long long>> dp(n, vector<long long>(m, 0));
    if (grid[0][0] == '.') dp[0][0] = 1;
    for (int r = 0; r < n; r++) {
        for (int c = 0; c < m; c++) {
            if (grid[r][c] == '#') {
                dp[r][c] = 0;
                continue;
            }
            if (r) dp[r][c] = (dp[r][c] + dp[r - 1][c]) % MOD;
            if (c) dp[r][c] = (dp[r][c] + dp[r][c - 1]) % MOD;
        }
    }
    cout << dp[n - 1][m - 1] << '\n';
    return 0;
}

