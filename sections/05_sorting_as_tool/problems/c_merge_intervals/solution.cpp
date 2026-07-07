#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        vector<pair<int, int>> intervals(n);
        for (auto &interval : intervals) {
            cin >> interval.first >> interval.second;
        }
        sort(intervals.begin(), intervals.end());

        vector<pair<int, int>> merged;
        for (auto [l, r] : intervals) {
            if (merged.empty() || l > merged.back().second + 1) {
                merged.push_back({l, r});
            } else {
                merged.back().second = max(merged.back().second, r);
            }
        }

        cout << merged.size() << '\n';
        for (auto [l, r] : merged) {
            cout << l << ' ' << r << '\n';
        }
    }

    return 0;
}

