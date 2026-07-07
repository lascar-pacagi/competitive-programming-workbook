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
    int h, w, r, c;
    if (!(cin >> h >> w >> r >> c)) return 0;
    int limit = h + w;
    vector<long long> fact(limit + 1, 1), invfact(limit + 1, 1);
    for (int i = 1; i <= limit; i++) fact[i] = fact[i - 1] * i % MOD;
    invfact[limit] = mod_pow(fact[limit], MOD - 2);
    for (int i = limit; i >= 1; i--) invfact[i - 1] = invfact[i] * i % MOD;
    auto C = [&](int n, int k) -> long long {
        if (k < 0 || k > n) return 0;
        return fact[n] * invfact[k] % MOD * invfact[n - k] % MOD;
    };
    long long total = C(h + w - 2, h - 1);
    long long through = C(r + c - 2, r - 1) * C(h - r + w - c, h - r) % MOD;
    cout << (total - through + MOD) % MOD << '\n';
    return 0;
}
