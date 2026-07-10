#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<pair<long long, long long>> tasks(n);
    for (auto& [duration, deadline] : tasks) cin >> duration >> deadline;
    sort(tasks.begin(), tasks.end(), [](auto a, auto b) { return a.second < b.second; });

    priority_queue<long long> chosen;
    long long total = 0;
    for (auto [duration, deadline] : tasks) {
        total += duration;
        chosen.push(duration);
        if (total > deadline) {
            total -= chosen.top();
            chosen.pop();
        }
    }
    cout << chosen.size() << '\n';
}
