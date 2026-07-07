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
    vector<array<int, 3>> queries(q);
    int limit = 0;
    for (auto &cur : queries) {
        cin >> cur[0] >> cur[1] >> cur[2];
        limit = max(limit, cur[0] + cur[1]);
    }
    vector<long long> fact(limit + 1, 1), invfact(limit + 1, 1);
    for (int i = 1; i <= limit; i++) fact[i] = fact[i - 1] * i % MOD;
    invfact[limit] = mod_pow(fact[limit], MOD - 2);
    for (int i = limit; i >= 1; i--) invfact[i - 1] = invfact[i] * i % MOD;
    auto C = [&](int n, int r) -> long long {
        if (r < 0 || r > n) return 0;
        return fact[n] * invfact[r] % MOD * invfact[n - r] % MOD;
    };
    for (auto [n, s, b] : queries) {
        long long ans = 0;
        int step = b + 1;
        for (int bad = 0; bad <= n && bad * step <= s; bad++) {
            int remaining = s - bad * step;
            long long term = C(n, bad) * C(remaining + n - 1, n - 1) % MOD;
            if (bad % 2) ans = (ans - term + MOD) % MOD;
            else ans = (ans + term) % MOD;
        }
        cout << ans << '\n';
    }
    return 0;
}
