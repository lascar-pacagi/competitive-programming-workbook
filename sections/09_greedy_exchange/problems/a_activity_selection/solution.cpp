#include <bits/stdc++.h>
using namespace std;

int solve_case(vector<pair<long long, long long>> intervals) {
    sort(intervals.begin(), intervals.end(), [](const auto &a, const auto &b) {
        if (a.second != b.second) return a.second < b.second;
        return a.first < b.first;
    });

    int count = 0;
    long long last_end = numeric_limits<long long>::min() / 4;
    for (auto [start, end] : intervals) {
        if (start >= last_end) {
            ++count;
            last_end = end;
        }
    }
    return count;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        vector<pair<long long, long long>> intervals(n);
        for (auto &[start, end] : intervals) cin >> start >> end;
        cout << solve_case(intervals) << '\n';
    }

    return 0;
}

