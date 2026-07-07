#include <bits/stdc++.h>
using namespace std;

struct Event {
    long long x;
    int kind;
    int idx;
};

vector<int> solve_case(const vector<pair<long long, long long>> &intervals, const vector<long long> &queries) {
    vector<Event> events;
    events.reserve(intervals.size() * 2 + queries.size());
    for (auto [l, r] : intervals) {
        events.push_back({l, 0, -1});
        events.push_back({r, 2, -1});
    }
    for (int i = 0; i < (int)queries.size(); ++i) {
        events.push_back({queries[i], 1, i});
    }
    sort(events.begin(), events.end(), [](const Event &a, const Event &b) {
        if (a.x != b.x) return a.x < b.x;
        return a.kind < b.kind;
    });

    int active = 0;
    vector<int> ans(queries.size());
    for (const Event &event : events) {
        if (event.kind == 0) {
            ++active;
        } else if (event.kind == 1) {
            ans[event.idx] = active;
        } else {
            --active;
        }
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int n, q;
        cin >> n >> q;
        vector<pair<long long, long long>> intervals(n);
        for (auto &[l, r] : intervals) cin >> l >> r;
        vector<long long> queries(q);
        for (long long &x : queries) cin >> x;
        vector<int> ans = solve_case(intervals, queries);
        for (int i = 0; i < q; ++i) {
            if (i) cout << ' ';
            cout << ans[i];
        }
        cout << '\n';
    }

    return 0;
}

