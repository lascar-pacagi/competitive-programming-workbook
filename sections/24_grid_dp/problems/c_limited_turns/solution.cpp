#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    const int MOD = 1000000007;
    const int RIGHT = 0, DOWN = 1;
    int n, m, K;
    if (!(cin >> n >> m >> K)) return 0;
    vector<string> grid(n);
    for (string &row : grid) cin >> row;
    if (grid[0][0] == '#' || grid[n - 1][m - 1] == '#') {
        cout << 0 << '\n';
        return 0;
    }
    if (n == 1 && m == 1) {
        cout << 1 << '\n';
        return 0;
    }
    vector dp(n, vector(m, vector(K + 1, array<int, 2>{0, 0})));
    if (m > 1 && grid[0][1] == '.') dp[0][1][0][RIGHT] = 1;
    if (n > 1 && grid[1][0] == '.') dp[1][0][0][DOWN] = 1;
    for (int r = 0; r < n; r++) {
        for (int c = 0; c < m; c++) {
            if (grid[r][c] == '#') continue;
            for (int turns = 0; turns <= K; turns++) {
                if (c > 0 && grid[r][c - 1] == '.') {
                    int val = dp[r][c][turns][RIGHT];
                    val += dp[r][c - 1][turns][RIGHT];
                    if (val >= MOD) val -= MOD;
                    if (turns) {
                        val += dp[r][c - 1][turns - 1][DOWN];
                        if (val >= MOD) val -= MOD;
                    }
                    dp[r][c][turns][RIGHT] = val;
                }
                if (r > 0 && grid[r - 1][c] == '.') {
                    int val = dp[r][c][turns][DOWN];
                    val += dp[r - 1][c][turns][DOWN];
                    if (val >= MOD) val -= MOD;
                    if (turns) {
                        val += dp[r - 1][c][turns - 1][RIGHT];
                        if (val >= MOD) val -= MOD;
                    }
                    dp[r][c][turns][DOWN] = val;
                }
            }
        }
    }
    int ans = 0;
    for (int turns = 0; turns <= K; turns++) {
        ans += dp[n - 1][m - 1][turns][RIGHT];
        if (ans >= MOD) ans -= MOD;
        ans += dp[n - 1][m - 1][turns][DOWN];
        if (ans >= MOD) ans -= MOD;
    }
    cout << ans << '\n';
    return 0;
}

