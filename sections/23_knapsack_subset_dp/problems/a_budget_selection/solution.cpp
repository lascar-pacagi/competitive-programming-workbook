#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, W;
    if (!(cin >> n >> W)) return 0;
    vector<long long> dp(W + 1, 0);
    for (int i = 0; i < n; i++) {
        int cost;
        long long value;
        cin >> cost >> value;
        if (cost > W) continue;
        for (int cap = W; cap >= cost; cap--) {
            dp[cap] = max(dp[cap], dp[cap - cost] + value);
        }
    }
    cout << *max_element(dp.begin(), dp.end()) << '\n';
    return 0;
}

