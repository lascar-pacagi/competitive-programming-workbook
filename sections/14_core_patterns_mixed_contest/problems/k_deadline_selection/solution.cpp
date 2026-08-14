#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<pair<long long, long long>> jobs(n);
    for (auto &[duration, deadline] : jobs) cin >> duration >> deadline;
    sort(jobs.begin(), jobs.end(),
         [](auto a, auto b) { return tie(a.second, a.first) < tie(b.second, b.first); });
    priority_queue<long long> selected;
    long long total = 0;
    for (auto [duration, deadline] : jobs) {
        selected.push(duration);
        total += duration;
        if (total > deadline) {
            total -= selected.top();
            selected.pop();
        }
    }
    cout << selected.size() << '\n';
}
