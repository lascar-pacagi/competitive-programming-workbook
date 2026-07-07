#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int n, m;
        cin >> n >> m;
        vector<long long> diff(m + 2, 0);
        for (int i = 0; i < n; ++i) {
            int l, r;
            long long w;
            cin >> l >> r >> w;
            diff[l] += w;
            diff[r + 1] -= w;
        }
        long long cur = 0;
        long long best = LLONG_MIN;
        int best_time = 1;
        for (int time = 1; time <= m; ++time) {
            cur += diff[time];
            if (cur > best) {
                best = cur;
                best_time = time;
            }
        }
        cout << best << ' ' << best_time << '\n';
    }

    return 0;
}

