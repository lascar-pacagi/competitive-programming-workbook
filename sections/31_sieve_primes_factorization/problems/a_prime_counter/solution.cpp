#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;
    vector<bool> is_prime(n + 1, true);
    if (n >= 0) is_prime[0] = false;
    if (n >= 1) is_prime[1] = false;
    for (long long p = 2; p * p <= n; p++) {
        if (is_prime[p]) {
            for (long long x = p * p; x <= n; x += p) is_prime[x] = false;
        }
    }
    vector<int> pref(n + 1, 0);
    for (int i = 1; i <= n; i++) pref[i] = pref[i - 1] + is_prime[i];
    while (q--) {
        int l, r;
        cin >> l >> r;
        cout << pref[r] - pref[l - 1] << '\n';
    }
    return 0;
}
