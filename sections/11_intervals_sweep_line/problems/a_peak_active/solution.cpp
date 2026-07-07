#include <bits/stdc++.h>
using namespace std;

int solve_case(const vector<pair<long long, long long>> &intervals) {
    vector<pair<long long, int>> events;
    events.reserve(intervals.size() * 2);
    for (auto [l, r] : intervals) {
        events.push_back({l, 1});
        events.push_back({r, -1});
    }
    sort(events.begin(), events.end(), [](const auto &a, const auto &b) {
        if (a.first != b.first) return a.first < b.first;
        return a.second < b.second;
    });

    int active = 0;
    int best = 0;
    for (auto [x, delta] : events) {
        (void)x;
        active += delta;
        best = max(best, active);
    }
    return best;
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
        for (auto &[l, r] : intervals) cin >> l >> r;
        cout << solve_case(intervals) << '\n';
    }

    return 0;
}

