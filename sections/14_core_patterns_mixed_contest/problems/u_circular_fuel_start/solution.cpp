#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<long long> fuel(n), cost(n);
    for (long long &value : fuel) cin >> value;
    for (long long &value : cost) cin >> value;
    long long total = 0, tank = 0;
    int candidate = 0;
    for (int i = 0; i < n; ++i) {
        long long gain = fuel[i] - cost[i];
        total += gain;
        tank += gain;
        if (tank < 0) {
            candidate = i + 1;
            tank = 0;
        }
    }
    cout << (total < 0 ? -1 : candidate) << '\n';
}
