#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;
    vector<int> values(q);
    int mx = 1;
    for (int &x : values) {
        cin >> x;
        mx = max(mx, x);
    }
    vector<int> spf(mx + 1);
    iota(spf.begin(), spf.end(), 0);
    if (mx >= 1) spf[1] = 1;
    for (long long p = 2; p <= mx; p++) {
        if (spf[p] == p && p * p <= mx) {
            for (long long x = p * p; x <= mx; x += p) {
                if (spf[x] == x) spf[x] = p;
            }
        }
    }
    for (int x : values) {
        int ans = 1;
        while (x > 1) {
            int p = spf[x];
            int exp = 0;
            while (x % p == 0) {
                exp++;
                x /= p;
            }
            ans *= exp + 1;
        }
        cout << ans << '\n';
    }
    return 0;
}
