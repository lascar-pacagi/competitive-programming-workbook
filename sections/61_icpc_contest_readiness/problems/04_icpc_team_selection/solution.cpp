#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        int n;
        cin >> n;
        vector<pair<long long, long long>> intervals(n);
        for (auto &[left, right] : intervals) cin >> left >> right;
        sort(intervals.begin(), intervals.end(), [](const auto &a, const auto &b) {
            if (a.second != b.second) return a.second < b.second;
            return a.first < b.first;
        });

        long long last_day = LLONG_MIN;
        int answer = 0;
        for (auto [left, right] : intervals) {
            if (last_day < left) {
                ++answer;
                last_day = right;
            }
        }
        cout << answer << '\n';
    }
    return 0;
}
