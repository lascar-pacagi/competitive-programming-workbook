#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007LL;

long long mod_pow(long long a, long long b) {
    a %= MOD;
    if (a < 0) a += MOD;
    long long result = 1;
    while (b > 0) {
        if (b & 1LL) result = result * a % MOD;
        a = a * a % MOD;
        b >>= 1LL;
    }
    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;
    while (q--) {
        long long a, b, x, k;
        cin >> a >> b >> x >> k;
        a %= MOD;
        b %= MOD;
        x %= MOD;
        if (k == 0) {
            cout << x << '\n';
            continue;
        }
        long long ak = mod_pow(a, k);
        long long geom;
        if (a == 1) {
            geom = k % MOD;
        } else {
            geom = (ak - 1 + MOD) % MOD * mod_pow(a - 1, MOD - 2) % MOD;
        }
        cout << (ak * x + b * geom) % MOD << '\n';
    }
    return 0;
}
