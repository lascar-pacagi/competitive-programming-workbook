#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long limit;
    cin >> n >> limit;
    vector<long long> durations(n);
    for (long long &duration : durations) cin >> duration;
    sort(durations.begin(), durations.end());
    long long total = 0;
    int answer = 0;
    for (long long duration : durations) {
        if (total + duration > limit) break;
        total += duration;
        ++answer;
    }
    cout << answer << '\n';
}
