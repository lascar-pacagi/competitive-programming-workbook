#include <bits/stdc++.h>
using namespace std;

long long solve_case(const vector<pair<long long, long long>> &intervals) {
    vector<pair<long long, int>> events;
    events.reserve(intervals.size() * 2);
    for (auto [l, r] : intervals) {
        events.push_back({l, 1});
        events.push_back({r, -1});
    }
    sort(events.begin(), events.end());

    long long active = 0;
    long long prev = events[0].first;
    long long total = 0;
    int i = 0;
    while (i < (int)events.size()) {
        long long x = events[i].first;
        if (active > 0) {
            total += x - prev;
        }
        while (i < (int)events.size() && events[i].first == x) {
            active += events[i].second;
            ++i;
        }
        prev = x;
    }
    return total;
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

