#include <bits/stdc++.h>
using namespace std;

long long solve_case(const vector<long long> &a) {
    long long cost = 0;
    long long need = a[0];
    for (int i = 1; i < (int)a.size(); ++i) {
        if (a[i] < need) {
            cost += need - a[i];
        } else {
            need = a[i];
        }
    }
    return cost;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        vector<long long> a(n);
        for (long long &x : a) cin >> x;
        cout << solve_case(a) << '\n';
    }

    return 0;
}

