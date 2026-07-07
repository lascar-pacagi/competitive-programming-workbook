#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007LL;

long long mod_pow(long long a, long long b) {
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
    vector<pair<long long, int>> queries(q);
    int limit = 0;
    for (auto &[n, k] : queries) {
        cin >> n >> k;
        limit = max(limit, k);
    }
    vector<long long> fact(limit + 1, 1), invfact(limit + 1, 1);
    for (int i = 1; i <= limit; i++) fact[i] = fact[i - 1] * i % MOD;
    invfact[limit] = mod_pow(fact[limit], MOD - 2);
    for (int i = limit; i >= 1; i--) invfact[i - 1] = invfact[i] * i % MOD;
    auto C = [&](int n, int r) -> long long {
        if (r < 0 || r > n) return 0;
        return fact[n] * invfact[r] % MOD * invfact[n - r] % MOD;
    };
    for (auto [n, k] : queries) {
        long long ans = 0;
        for (int missing = 0; missing <= k; missing++) {
            long long term = C(k, missing) * mod_pow(k - missing, n) % MOD;
            if (missing % 2) ans = (ans - term + MOD) % MOD;
            else ans = (ans + term) % MOD;
        }
        cout << ans << '\n';
    }
    return 0;
}
