#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int n;
        long long limit;
        cin >> n >> limit;
        vector<long long> values(n);
        for (long long &value : values) {
            cin >> value;
        }

        long long best = 0;
        for (int mask = 0; mask < (1 << n); ++mask) {
            long long total = 0;
            for (int i = 0; i < n; ++i) {
                if (mask & (1 << i)) {
                    total += values[i];
                }
            }
            if (total <= limit) {
                best = max(best, total);
            }
        }
        cout << best << '\n';
    }

    return 0;
}

