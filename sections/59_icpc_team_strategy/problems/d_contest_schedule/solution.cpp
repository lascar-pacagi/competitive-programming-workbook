#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long limit;
    if (!(cin >> n >> limit)) return 0;
    vector<long long> durations(n);
    for (long long& duration : durations) cin >> duration;
    sort(durations.begin(), durations.end());

    long long elapsed = 0;
    long long penalty = 0;
    int solved = 0;
    for (long long duration : durations) {
        if (elapsed + duration > limit) break;
        elapsed += duration;
        penalty += elapsed;
        solved++;
    }
    cout << solved << ' ' << penalty << '\n';
    return 0;
}
