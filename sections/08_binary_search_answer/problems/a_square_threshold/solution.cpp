#include <bits/stdc++.h>
using namespace std;

using int64 = long long;
using i128 = __int128_t;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int64 n;
        cin >> n;
        int64 lo = 0;
        int64 hi = 1'000'000'000LL;
        while (lo < hi) {
            int64 mid = lo + (hi - lo) / 2;
            if ((i128)mid * mid >= n) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        cout << lo << '\n';
    }

    return 0;
}

