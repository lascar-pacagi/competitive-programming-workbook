#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<pair<long long, long long>> tasks;
    tasks.reserve(n);
    for (int i = 0; i < n; i++) {
        long long duration, deadline;
        cin >> duration >> deadline;
        tasks.push_back({deadline, duration});
    }
    sort(tasks.begin(), tasks.end());

    priority_queue<long long> kept;
    long long total = 0;
    for (auto [deadline, duration] : tasks) {
        kept.push(duration);
        total += duration;
        if (total > deadline) {
            total -= kept.top();
            kept.pop();
        }
    }
    cout << kept.size() << '\n';
    return 0;
}
