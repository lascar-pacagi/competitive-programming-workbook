#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<pair<int, int>> events(n);
    for (auto &[start, finish] : events) cin >> start >> finish;
    sort(events.begin(), events.end());
    priority_queue<int, vector<int>, greater<int>> finishes;
    int index = 0, answer = 0;
    long long day = 0;
    while (index < n || !finishes.empty()) {
        if (finishes.empty()) day = max(day, (long long)events[index].first);
        while (index < n && events[index].first <= day) {
            finishes.push(events[index].second);
            ++index;
        }
        while (!finishes.empty() && finishes.top() < day) finishes.pop();
        if (!finishes.empty()) {
            finishes.pop();
            ++answer;
            ++day;
        }
    }
    cout << answer << '\n';
}
