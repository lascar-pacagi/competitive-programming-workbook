#include <bits/stdc++.h>
using namespace std;

using int64 = long long;
using i128 = __int128_t;

int ceil_log2_for_estimate(int64 n) {
    int ans = 0;
    int64 value = 1;
    while (value < n) {
        value <<= 1;
        ++ans;
    }
    return max(1, ans);
}

bool fits(i128 cost, int64 budget) {
    return cost <= static_cast<i128>(budget);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int Q;
    cin >> Q;
    while (Q--) {
        int64 n, budget;
        cin >> n >> budget;
        int64 log_estimate = ceil_log2_for_estimate(n);

        if (fits(static_cast<i128>(n) * n * n, budget)) {
            cout << "cubic\n";
        } else if (fits(static_cast<i128>(n) * n, budget)) {
            cout << "quadratic\n";
        } else if (fits(static_cast<i128>(n) * log_estimate, budget)) {
            cout << "nlogn\n";
        } else if (fits(n, budget)) {
            cout << "linear\n";
        } else {
            cout << "none\n";
        }
    }

    return 0;
}

