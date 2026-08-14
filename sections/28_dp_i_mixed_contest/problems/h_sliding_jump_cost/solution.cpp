#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    cin >> n >> k;
    vector<long long> cost(n), dp(n);
    for (long long& value : cost)
        cin >> value;

    deque<int> candidates;
    dp[0] = cost[0];
    candidates.push_back(0);

    for (int i = 1; i < n; ++i) {
        while (candidates.front() < i - k)
            candidates.pop_front();

        dp[i] = cost[i] + dp[candidates.front()];

        while (!candidates.empty() && dp[candidates.back()] >= dp[i])
            candidates.pop_back();
        candidates.push_back(i);
    }

    cout << dp[n - 1] << '\n';
}
