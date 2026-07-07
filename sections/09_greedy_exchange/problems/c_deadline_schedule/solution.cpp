#include <bits/stdc++.h>
using namespace std;

int solve_case(vector<pair<long long, long long>> tasks) {
    sort(tasks.begin(), tasks.end(), [](const auto &a, const auto &b) {
        if (a.second != b.second) return a.second < b.second;
        return a.first < b.first;
    });

    long long total = 0;
    priority_queue<long long> chosen;
    for (auto [duration, deadline] : tasks) {
        total += duration;
        chosen.push(duration);
        if (total > deadline) {
            total -= chosen.top();
            chosen.pop();
        }
    }
    return (int)chosen.size();
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        vector<pair<long long, long long>> tasks(n);
        for (auto &[duration, deadline] : tasks) cin >> duration >> deadline;
        cout << solve_case(tasks) << '\n';
    }

    return 0;
}

