#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<vector<long long>> value(n, vector<long long>(m));
    for (auto &row : value) {
        for (long long &x : row) cin >> x;
    }

    const long long NEG = -(1LL << 62);
    vector<vector<long long>> dp(n, vector<long long>(n, NEG));
    dp[0][0] = value[0][0];
    for (int step = 0; step < n + m - 2; step++) {
        vector<vector<long long>> next(n, vector<long long>(n, NEG));
        for (int r1 = 0; r1 < n; r1++) {
            int c1 = step - r1;
            if (c1 < 0 || c1 >= m) continue;
            for (int r2 = 0; r2 < n; r2++) {
                int c2 = step - r2;
                if (c2 < 0 || c2 >= m || dp[r1][r2] == NEG) continue;
                for (int down1 = 0; down1 <= 1; down1++) {
                    for (int down2 = 0; down2 <= 1; down2++) {
                        int nr1 = r1 + down1, nr2 = r2 + down2;
                        int nc1 = c1 + 1 - down1, nc2 = c2 + 1 - down2;
                        if (nr1 >= n || nr2 >= n || nc1 >= m || nc2 >= m) continue;
                        long long gain = value[nr1][nc1];
                        if (nr1 != nr2 || nc1 != nc2) gain += value[nr2][nc2];
                        next[nr1][nr2] = max(next[nr1][nr2], dp[r1][r2] + gain);
                    }
                }
            }
        }
        dp.swap(next);
    }
    cout << dp[n - 1][n - 1] << '\n';
    return 0;
}
