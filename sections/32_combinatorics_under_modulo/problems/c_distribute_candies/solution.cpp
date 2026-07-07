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
    vector<pair<int, int>> queries(q);
    int limit = 0;
    for (auto &[n, s] : queries) {
        cin >> n >> s;
        limit = max(limit, n + s - 1);
    }
    vector<long long> fact(limit + 1, 1), invfact(limit + 1, 1);
    for (int i = 1; i <= limit; i++) fact[i] = fact[i - 1] * i % MOD;
    invfact[limit] = mod_pow(fact[limit], MOD - 2);
    for (int i = limit; i >= 1; i--) invfact[i - 1] = invfact[i] * i % MOD;
    for (auto [n, s] : queries) {
        int total = n + s - 1;
        int choose = n - 1;
        cout << fact[total] * invfact[choose] % MOD * invfact[total - choose] % MOD << '\n';
    }
    return 0;
}
