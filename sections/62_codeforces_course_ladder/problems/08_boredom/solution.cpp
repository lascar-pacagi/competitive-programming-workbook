#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int t; if (!(cin >> t)) return 0;
    while (t--) {
        int n; long long goal; cin >> n >> goal;
        vector<long long> time(n); for (auto& x : time) cin >> x;
        long long lo = 0, hi = *min_element(time.begin(), time.end()) * goal;
        while (lo < hi) {
            long long mid = lo + (hi - lo) / 2, made = 0;
            for (long long x : time) { made += mid / x; if (made >= goal) break; }
            if (made >= goal) hi = mid; else lo = mid + 1;
        }
        cout << lo << '\n';
    }
}
