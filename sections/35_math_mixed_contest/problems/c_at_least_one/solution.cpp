#include <bits/stdc++.h>
using namespace std;
const long long MOD = 1000000007LL;

long long mod_pow(long long a, long long b) {
    long long r = 1;
    while (b) {
        if (b & 1LL) r = r * a % MOD;
        a = a * a % MOD;
        b >>= 1LL;
    }
    return r;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    long long none = 1;
    for (int i = 0; i < n; i++) {
        long long p, q;
        cin >> p >> q;
        none = none * ((q - p) % MOD) % MOD * mod_pow(q, MOD - 2) % MOD;
    }
    cout << (1 - none + MOD) % MOD << '\n';
    return 0;
}
