#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, cap_a, cap_b;
    if (!(cin >> n >> cap_a >> cap_b)) return 0;
    vector<pair<int, long long>> items(n);
    for (auto &[w, v] : items) cin >> w >> v;

    vector<vector<long long>> dp(cap_a + 1, vector<long long>(cap_b + 1, 0));
    for (auto [weight, value] : items) {
        for (int a = cap_a; a >= 0; a--) {
            for (int b = cap_b; b >= 0; b--) {
                long long cur = dp[a][b];
                if (a + weight <= cap_a) {
                    dp[a + weight][b] = max(dp[a + weight][b], cur + value);
                }
                if (b + weight <= cap_b) {
                    dp[a][b + weight] = max(dp[a][b + weight], cur + value);
                }
            }
        }
    }

    long long answer = 0;
    for (int a = 0; a <= cap_a; a++) {
        for (int b = 0; b <= cap_b; b++) answer = max(answer, dp[a][b]);
    }
    cout << answer << '\n';
    return 0;
}
