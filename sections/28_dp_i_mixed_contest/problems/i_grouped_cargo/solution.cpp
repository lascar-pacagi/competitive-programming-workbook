#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int groups, capacity;
    cin >> groups >> capacity;
    vector<long long> dp(capacity + 1, 0);

    for (int group = 0; group < groups; ++group) {
        int count;
        cin >> count;
        vector<pair<int, long long>> items(count);
        for (auto& [weight, value] : items)
            cin >> weight >> value;

        vector<long long> next = dp;
        for (auto [weight, value] : items)
            for (int used = 0; used + weight <= capacity; ++used)
                next[used + weight] = max(next[used + weight],
                                          dp[used] + value);
        dp.swap(next);
    }

    cout << *max_element(dp.begin(), dp.end()) << '\n';
}
