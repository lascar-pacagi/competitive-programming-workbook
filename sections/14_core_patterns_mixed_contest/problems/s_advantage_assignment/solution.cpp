#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<long long> a(n), b(n);
    for (long long &value : a) cin >> value;
    for (long long &value : b) cin >> value;
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    int wins = 0, target = 0;
    for (long long value : a) {
        if (value > b[target]) {
            ++wins;
            ++target;
            if (target == n) break;
        }
    }
    cout << wins << '\n';
}
