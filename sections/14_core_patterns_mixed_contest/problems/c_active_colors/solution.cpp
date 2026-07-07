#include <bits/stdc++.h>
using namespace std;

struct Event {
    long long x;
    int kind;
    long long color;
    int idx;
};

vector<int> solve_case(const vector<tuple<long long, long long, long long>> &intervals, const vector<long long> &queries) {
    vector<Event> events;
    events.reserve(intervals.size() * 2 + queries.size());
    for (auto [l, r, color] : intervals) {
        events.push_back({r, 0, color, -1});
        events.push_back({l, 1, color, -1});
    }
    for (int i = 0; i < (int)queries.size(); ++i) {
        events.push_back({queries[i], 2, 0, i});
    }
    sort(events.begin(), events.end(), [](const Event &a, const Event &b) {
        if (a.x != b.x) return a.x < b.x;
        return a.kind < b.kind;
    });

    unordered_map<long long, int> freq;
    int distinct = 0;
    vector<int> ans(queries.size());
    for (const Event &event : events) {
        if (event.kind == 0) {
            int count = freq[event.color] - 1;
            if (count == 0) {
                --distinct;
                freq.erase(event.color);
            } else {
                freq[event.color] = count;
            }
        } else if (event.kind == 1) {
            int count = freq[event.color];
            if (count == 0) ++distinct;
            freq[event.color] = count + 1;
        } else {
            ans[event.idx] = distinct;
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
        vector<tuple<long long, long long, long long>> intervals;
        intervals.reserve(n);
        for (int i = 0; i < n; ++i) {
            long long l, r, color;
            cin >> l >> r >> color;
            intervals.push_back({l, r, color});
        }
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

