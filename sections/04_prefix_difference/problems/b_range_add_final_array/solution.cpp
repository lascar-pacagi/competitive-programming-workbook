#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int n, q;
        cin >> n >> q;
        vector<long long> diff(n + 2, 0);
        while (q--) {
            int l, r;
            long long x;
            cin >> l >> r >> x;
            diff[l] += x;
            diff[r + 1] -= x;
        }
        long long cur = 0;
        for (int i = 1; i <= n; ++i) {
            cur += diff[i];
            if (i > 1) cout << ' ';
            cout << cur;
        }
        cout << '\n';
    }

    return 0;
}

