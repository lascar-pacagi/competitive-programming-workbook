#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<pair<long long, long long>> intervals(n);
    for (auto &[left, right] : intervals) cin >> left >> right;
    sort(intervals.begin(), intervals.end(),
         [](auto a, auto b) { return tie(a.second, a.first) < tie(b.second, b.first); });
    long long last = LLONG_MIN;
    int answer = 0;
    for (auto [left, right] : intervals) {
        if (last < left) {
            last = right;
            ++answer;
        }
    }
    cout << answer << '\n';
}
