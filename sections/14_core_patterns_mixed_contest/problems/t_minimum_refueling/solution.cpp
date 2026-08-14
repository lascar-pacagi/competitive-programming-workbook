#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long destination, reachable;
    int n;
    cin >> destination >> reachable >> n;
    vector<pair<long long, long long>> stations(n);
    for (auto &[position, fuel] : stations) cin >> position >> fuel;
    sort(stations.begin(), stations.end());
    priority_queue<long long> available;
    int index = 0, stops = 0;
    while (reachable < destination) {
        while (index < n && stations[index].first <= reachable) {
            available.push(stations[index].second);
            ++index;
        }
        if (available.empty()) {
            cout << -1 << '\n';
            return 0;
        }
        reachable += available.top();
        available.pop();
        ++stops;
    }
    cout << stops << '\n';
}
