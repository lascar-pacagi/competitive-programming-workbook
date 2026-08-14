#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<long long> value(n + 2, 1);
    for (int i = 1; i <= n; ++i)
        cin >> value[i];

    // dp[left][right]: best gain after removing every crystal strictly
    // between the two still-present boundary indices left and right.
    vector<vector<long long>> dp(n + 2, vector<long long>(n + 2, 0));

    for (int gap = 2; gap <= n + 1; ++gap) {
        for (int left = 0; left + gap <= n + 1; ++left) {
            int right = left + gap;
            for (int last = left + 1; last < right; ++last) {
                dp[left][right] = max(
                    dp[left][right],
                    dp[left][last] + dp[last][right]
                    + value[left] * value[last] * value[right]);
            }
        }
    }

    cout << dp[0][n + 1] << '\n';
}
