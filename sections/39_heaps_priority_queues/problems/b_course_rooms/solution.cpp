#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<pair<int,int>> intervals(n);
    for (auto &[l, r] : intervals) cin >> l >> r;
    sort(intervals.begin(), intervals.end());
    priority_queue<int, vector<int>, greater<int>> pq;
    int ans = 0;
    for (auto [l, r] : intervals) {
        while (!pq.empty() && pq.top() <= l) pq.pop();
        pq.push(r);
        ans = max(ans, (int)pq.size());
    }
    cout << ans << '\n';
    return 0;
}
