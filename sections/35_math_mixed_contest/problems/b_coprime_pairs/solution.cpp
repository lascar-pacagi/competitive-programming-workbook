#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<int> a(n);
    int mx = 1;
    for (int &x : a) {
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
    vector<int> seen(mx + 1, 0);
    long long answer = 0;
    for (int idx = 0; idx < n; idx++) {
        int x = a[idx];
        vector<int> factors;
        while (x > 1) {
            int p = spf[x];
            factors.push_back(p);
            while (x % p == 0) x /= p;
        }
        long long share = 0;
        int m = factors.size();
        for (int mask = 1; mask < (1 << m); mask++) {
            int prod = 1, bits = 0;
            for (int i = 0; i < m; i++) if (mask & (1 << i)) {
                prod *= factors[i];
                bits++;
            }
            if (bits % 2) share += seen[prod];
            else share -= seen[prod];
        }
        answer += idx - share;
        for (int mask = 1; mask < (1 << m); mask++) {
            int prod = 1;
            for (int i = 0; i < m; i++) if (mask & (1 << i)) prod *= factors[i];
            seen[prod]++;
        }
    }
    cout << answer << '\n';
    return 0;
}
